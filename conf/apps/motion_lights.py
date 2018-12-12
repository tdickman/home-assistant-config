import appdaemon.plugins.hass.hassapi as hass


class MotionLights(hass.Hass):
    def initialize(self):
        self.log('Motion lights initialized for {}'.format(self.args['sensor']))
        self.handle = None
        # assert_args(['sensor', 'lights', 'delay'])
        self.listen_state(self.motion, entity=self.args['sensor'], new='on')

    def motion(self, entity, attribute, old, new, kwargs):
        self.log('Motion detected: turning {} on'.format(self.args['lights']))
        if 'brightness' in self.args and 'color_temp' in self.args:
            self.turn_on(self.args['lights'], brightness=self.args['brightness'], color_temp=self.args['color_temp'])
        else:
            self.turn_on(self.args['lights'])
        self.cancel_timer(self.handle)
        self.handle = self.run_in(self.lights_off, self.args['stay_on_for'])

    def lights_off(self, kwawgs):
        bathroom_humidity = float(self.get_state('sensor.humidity_158d00011003cd'))
        hallway_humidity = float(self.get_state('sensor.hallway_thermostat_humidity'))
        self.log('Bathroom humidity {}, hallway humidity {}'.format(bathroom_humidity, hallway_humidity))
        # Renew timer if humidity is high in bathroom
        if self.args['sensor'] == 'binary_sensor.motion_sensor_158d00012dae15' and bathroom_humidity > (hallway_humidity + 20):
            self.log('High bathroom humidity, keeping lights on')
            self.handle = self.run_in(self.lights_off, self.args['stay_on_for'])
        else:
            self.turn_off(self.args['lights'])
