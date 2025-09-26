strip = False

def on_forever():
    global strip
    if maqueen.ultrasonic() < 30 and maqueen.ultrasonic() != "-1":
        strip = Math.random_boolean()
        if strip == True:
            maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 255)
            maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 0)
            basic.pause(800)
        if strip == False:
            maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 0)
            maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 255)
            basic.pause(800)
    else:
        maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CW, 255)
basic.forever(on_forever)
