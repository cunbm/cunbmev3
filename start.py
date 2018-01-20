from connector import ev3

m = ev3.LargeMotor()
m.run_timed(time_sp=3000, speed_sp=500)
