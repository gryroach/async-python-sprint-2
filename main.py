import time

from scheduler import Scheduler
from job import Job


sh = Scheduler()


def s(a, b):
    time.sleep(4)
    return a + b


def d(x, y):
    return x - y


# j1 = Job(s, '11-12-2022 15:10:00')
j2 = Job(d, [7, 6], start_at='11-12-2022 15:10:00')
j3 = Job(s, [5, 3], max_working_time=3, tries=3, dependencies=[j2],
         start_at='11-12-2022 15:10:00')
j4 = Job(d, [10, 3], start_at='12-10-2022 15:10:00')
j5 = Job(s, [10, 10])

sh.schedule(j2)
sh.schedule(j3)
sh.schedule(j4)
sh.schedule(j5)
sh.run()