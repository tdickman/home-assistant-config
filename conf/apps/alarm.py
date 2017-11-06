import datetime
import appdaemon.appapi as appapi


class Alarm(appapi.AppDaemon):
    def initialize(self):
        self.complete_callbacks = []

        for schedule in self.args['schedule']:
            time = self.parse_time(schedule['time'])
            time = (datetime.datetime.combine(datetime.datetime.today(), time) - datetime.timedelta(seconds=self.args['transition_seconds'])).time()
            self.log('{} at {} starting at {}'.format(schedule['days'], schedule['time'], time))
            self.run_daily(self.check_alarm, time, days=schedule['days'])

    def check_alarm(self, kwargs):
        days = kwargs['days']
        current_day = self.datetime().strftime('%A').lower()
        if current_day in days:
            self.log('Starting alarm')
            self.start_wakeup()

    def start_wakeup(self):
        # Fade in lights for 20 minutes
        self.turn_on(self.args['lights'],
                     transition=self.args['transition_seconds'],
                     brightness=self.args['brightness'],
                     color_temp=self.args['color_temp']
                     )
        handler = self.run_in(self.complete_wakeup, self.args['transition_seconds'])
        self.complete_callbacks.append(handler)

        # Cancel complete callback if we see motion in the bathroom
        # handler = self.listen_event(self.complete_wakeup, 'motion', entity_id='binary_sensor.motion_sensor_158d00012dae15')
        # self.complete_callbacks.append(handler)
        self.log('wakeup running')

    def complete_wakeup(self, *arg):
        self.log('Completing wakeup process.')
        while len(self.complete_callbacks) > 0:
            self.cancel_timer(self.complete_callbacks.pop())
        self.select_option('input_select.house_mode', 'awake')
        self.turn_on('group.bathroom')
