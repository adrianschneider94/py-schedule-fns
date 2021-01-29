from datetime import datetime

from schedule_fns import ctx, generate_id


class Schedule(object):
    def __init__(self, js_schedule_id: str):
        self.js_schedule_id = js_schedule_id

    def __call__(self, start_date: datetime):
        id = generate_id()
        ctx.eval(f"let {id} = {self.js_schedule_id}({start_date.timestamp() * 1000})")

        def generator():
            done = False
            while not done:
                result = ctx.eval(f"{id}.next()")
                value = result['value']
                done = result['done']
                yield value

        return generator()


def createSchedule(name: str):
    class NewSchedule(Schedule):
        def __init__(self, *args):
            id = generate_id()
            args = tuple(map(lambda arg: arg.timestamp() * 1000, args))
            ctx.eval(f"let {id} = scheduleFns.{name}{args}")
            super().__init__(id)

    return NewSchedule


Mondays = createSchedule('Mondays')
Tuesdays = createSchedule('Tuesdays')
Wednesdays = createSchedule('Wednesdays')
Thursdays = createSchedule('Thursdays')
Fridays = createSchedule('Fridays')
Saturdays = createSchedule('Saturdays')
DailySchedule = createSchedule("DailySchedule")
RegularSchedule = createSchedule('RegularSchedule')
ScheduleFromIntervals = createSchedule('ScheduleFromIntervals')
Weekends = createSchedule('Weekends')
WorkingDays = createSchedule('WorkingDays')
Holidays = createSchedule('Holidays')
From = createSchedule('From')
Until = createSchedule('Until')
