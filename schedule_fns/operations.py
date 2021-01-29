import dataclasses
from typing import List

from schedule_fns import Duration, ctx, generate_id
from schedule_fns.schedules import Schedule


def intersect_schedules(*schedules: List[Schedule]):
    id = generate_id()
    ids = list(map(lambda schedule: schedule.js_schedule_id, schedules))
    ctx.eval(f"let {id} = scheduleFns.intersectSchedules({', '.join(ids)})")
    return Schedule(js_schedule_id=id)


def invert_schedules(schedule: Schedule):
    id = generate_id()
    ctx.eval(f"let {id} = scheduleFns.invertSchedule({schedule.js_schedule_id})")
    return Schedule(js_schedule_id=id)


def join_schedules(*schedules: List[Schedule]):
    id = generate_id()
    ids = list(map(lambda schedule: schedule.js_schedule_id, schedules))
    ctx.eval(f"let {id} = scheduleFns.joinSchedules({', '.join(ids)})")
    return Schedule(js_schedule_id=id)


def shift_schedule(schedule: Schedule, duration: Duration):
    id = generate_id()
    expr = f"let {id} = scheduleFns.shiftSchedule({schedule.js_schedule_id}, " \
           f"{dataclasses.asdict(duration)})"
    print(expr)
    ctx.eval(expr)
    return Schedule(js_schedule_id=id)


def subtract_schedules(left_schedule: Schedule, right_schedule: Schedule):
    id = generate_id()
    ctx.eval(
        f"let {id} = scheduleFns.subtractSchedules({left_schedule.js_schedule_id}, {right_schedule.js_schedule_id})")
    return Schedule(js_schedule_id=id)


def symmetric_difference_of_schedules(left_schedule: Schedule, right_schedule: Schedule):
    id = generate_id()
    ctx.eval(
        f"let {id} = scheduleFns.symmetricDifferenceOfSchedules({left_schedule.js_schedule_id}, {right_schedule.js_schedule_id})")
    return Schedule(js_schedule_id=id)
