import servo_motor_manage

force_level = {0: 20, 1: 70, 2:74}
pre_index = 0

def add_force_level(index):
    global pre_index
    if index != pre_index:
        pre_index = index
        servo_motor_manage.add_force(force_level[index])

add_force_level(1)

if __name__ == "__main__":
    try:
        while True:
            flag = input("Input resistance level(0-2):")
            servo_motor_manage.add_force(force_level[int(flag)])
    except KeyboardInterrupt:
        print ("Quit..")
