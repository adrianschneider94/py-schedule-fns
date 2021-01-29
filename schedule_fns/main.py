from datetime import datetime, timedelta

from schedule_fns import Duration
from schedule_fns.operations import intersect_schedules, shift_schedule
from schedules import Mondays, Until

if __name__ == '__main__':
    schedule = Mondays()
    schedule2 = Until(datetime.now() + timedelta(weeks=5))
    res = intersect_schedules(schedule, schedule2)
    res2 = shift_schedule(res, Duration(days=3))
    i = 0
    for x in res2(datetime.now()):
        print(x)
        i += 1
        if i > 50:
            break
