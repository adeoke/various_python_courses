"""
We shall investigate into parallel programming:
taking a task and splitting it into multiple components and then
handing each component to be worked on by a separate core (note that on mac
its 2 logical cores per physical core).
Parallel programing is useful when the task is CPU intensive, that is,
cpu intensive, so most of the time is spent solving the problem rather than
reading to or writing to a device.
Useful for:
search algorithms,
string operations
graphics processing
number crunching algorithms
to name a few.

Then asynchronous programming:
When the task is spent predomininently reading to or writing from a device then
I/O.
Such tasks include:
database reads and writes,
web service calls,
copying and downloading data

***Distributed programming is not included here.*****
"""


