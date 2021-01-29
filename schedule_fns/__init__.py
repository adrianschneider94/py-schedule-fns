from dataclasses import dataclass
from uuid import uuid4

from py_mini_racer import py_mini_racer

ctx = py_mini_racer.MiniRacer()
with open("../../schedule-fns/lib/schedule-fns.min.js", encoding="utf-8") as f:
    schedule_fns_src = f.read()

ctx.eval(schedule_fns_src)


def generate_id():
    return '_' + str(uuid4()).replace('-', '')


@dataclass
class Duration:
    years: int = 0
    months: int = 0
    weeks: int = 0
    days: int = 0
    hours: int = 0
    minutes: int = 0
    seconds: int = 0
