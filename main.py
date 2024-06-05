y_box_position = 0
x_box_position = 0
box_height_default = 65
speed = 0
screen_width = 320
screen_hight = 240

width_center = screen_width / 2
hight_center = screen_hight / 2

free_gap_x = 30
free_gap_y = 10
speed = 35

def MoveRight():
    maqueenPlusV2.control_motor(maqueenPlusV2.MyEnumMotor.LEFT_MOTOR,
        maqueenPlusV2.MyEnumDir.FORWARD,
        speed)
    maqueenPlusV2.control_motor_stop(maqueenPlusV2.MyEnumMotor.RIGHT_MOTOR)

def MoveLeft():
    maqueenPlusV2.control_motor(maqueenPlusV2.MyEnumMotor.RIGHT_MOTOR,
        maqueenPlusV2.MyEnumDir.FORWARD,
        speed)
    maqueenPlusV2.control_motor_stop(maqueenPlusV2.MyEnumMotor.LEFT_MOTOR)

def MoveBackward():
    maqueenPlusV2.control_motor(maqueenPlusV2.MyEnumMotor.ALL_MOTOR,
        maqueenPlusV2.MyEnumDir.BACKWARD,
        speed)

def MoveForward():
    maqueenPlusV2.control_motor(maqueenPlusV2.MyEnumMotor.ALL_MOTOR,
        maqueenPlusV2.MyEnumDir.FORWARD,
        speed)

def Stop():
    maqueenPlusV2.control_motor_stop(maqueenPlusV2.MyEnumMotor.ALL_MOTOR)
def on_forever():
    huskylens.request()

    x_box_position = huskylens.reade_box(1, Content1.X_CENTER)
    box_height = huskylens.reade_box(1, Content1.HEIGHT)

    if x_box_position > width_center + free_gap_x:
        MoveRight()
    elif width_center - free_gap_x > x_box_position and x_box_position > -1:
        MoveLeft()
    elif box_height > box_height_default + free_gap_y:
            MoveBackward()
    elif box_height < box_height_default - free_gap_y and box_height > -1:
            MoveForward()
    else:
        Stop()

maqueenPlusV2.i2c_init()
huskylens.init_i2c()
huskylens.init_mode(protocolAlgorithm.ALGORITHM_OBJECT_TRACKING)

basic.forever(on_forever)

