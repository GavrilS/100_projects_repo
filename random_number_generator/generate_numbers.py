from random import randrange

START_RANGE = 0
END_RANGE = 10
NUM_COUNT = 1


def main():
    flag = True
    while flag:
        details = input("What's the range you want to use:")


def show_instructions():
    pass


def dissect_input(user_input):
    details_array = user_input.split(',')
    range_details = details_array[0].strip()
    if '-' in range_details:
        range_details = range_details.split('-')
        START_RANGE = int(range_details[0])
        END_RANGE = int(range_details[1])
    else:
        END_RANGE = int(range_details)
    
    if len(details_array) > 1:
        NUM_COUNT = int(details_array[1])
    
    return START_RANGE, END_RANGE, NUM_COUNT


def check_for_exit(user_input):
    if 'exit' in user_input.lower():
        print('Thank you for using the application!')
        return False
    else:
        return True


def verify_input(user_input):
    pass


def reset_defaults():
    START_RANGE = 0
    END_RANGE = 10
    NUM_COUNT = 1



if __name__=='__main__':
    main()
