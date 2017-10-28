import appdaemon.appapi as appapi


class MotionLights(appapi.AppDaemon):
    def initialize(self):
        self.log('Motion lights initialized for {}'.format(self.args['sensor']))
        self.handle = None
        # assert_args(['sensor', 'lights', 'delay'])
        self.listen_event(self.motion, 'motion', entity_id=self.args['sensor'])

    def motion(self, event, data, kwargs):
        self.log('Event: {}, data: {}'.format(event, data))
        self.log('Motion detected: turning {} on'.format(self.args['lights']))
        if 'brightness' in self.args and 'color_temp' in self.args:
            self.turn_on(self.args['lights'], brightness=self.args['brightness'], color_temp=self.args['color_temp'])
        else:
            self.turn_on(self.args['lights'])
        self.cancel_timer(self.handle)
        self.handle = self.run_in(self.lights_off, self.args['stay_on_for'])

    def lights_off(self, kwawgs):
        self.turn_off(self.args['lights'])
