# from connector import ev3
from listener import listener
#
# m = ev3.LargeMotor()
# m.run_timed(time_sp=3000, speed_sp=1000)
print(listener.listen(3))