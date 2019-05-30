import servo_motor_manage

force_level = {0: 20, 1: 65, 2:75}

if __name__ == "__main__":
    try:
        while True:
            flag = input("Input resistance level(0-2):")
            servo_motor_manage.add_force(force_level[int(flag)])
    except KeyboardInterrupt:
        print ("Quit..")
