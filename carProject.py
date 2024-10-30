car_started = False
car_stopped = False
while True:
    input_option = input('>')
    if input_option.upper() == 'START':
        if car_started:
            print("Sorry, You've already started the car")
        else:
            car_started = True
            print('Car started...Ready to go!')
    elif input_option.upper() == 'STOP':
        if car_stopped:
            print("Sorry, You've already stopped the car")
        else:
            car_stopped = True
            print('Car stopped')
    elif input_option.upper() == 'HELP':
        print("""
start - to start the car
stop - to stop the car
quit - to quit
        """)
    elif input_option.upper() == 'QUIT':
        break
    else:
        print("Sorry, I don't understand that")