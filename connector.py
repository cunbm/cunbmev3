import socket

if socket.gethostname() == 'ev3dev':
    import ev3dev.ev3 as ev3
else:
    import rpyc
    conn = rpyc.classic.connect('192.168.137.3')
    ev3 = conn.modules['ev3dev.ev3']