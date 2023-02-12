def user_number():
    while True:
        try:
            number = int(input('enter [1...10]:'))
            print('Good')
        except:
            print('Enter valid')
        else:
            if 0 >= number or number > 10:
                print('Wrong!')
                continue
            print(f'You enter {number}')
            return number

user_number()