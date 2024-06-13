import random

START_RANGE = 0
END_RANGE = 10
NUM_COUNT = 1


def main():
    flag = True
    while flag:
        details = input("What's the range you want to use:")

        if check_for_exit(details):
            break

        start, end, num_count, value_error = dissect_input(details)

        if value_error:
            print(value_error)
            continue

        get_numbers(start, end, num_count)

        reset_defaults()


def show_instructions():
    pass


def get_numbers(start, end, num_count):
    tracker = 0
    while tracker < num_count:
        print(random.randint(start, end), end=' ')
        tracker += 1
    print(end='\n')


def dissect_input(user_input):
    global START_RANGE, END_RANGE, NUM_COUNT
    value_error = None
    print(f"Start - {START_RANGE}, End - {END_RANGE}, Count - {NUM_COUNT} in dissect input")
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

    if START_RANGE > END_RANGE:
        value_error = 'The start of the random range cannot be bigger than the end! Please put correct ranges!'
    
    return START_RANGE, END_RANGE, NUM_COUNT, value_error


def check_for_exit(user_input):
    if 'exit' in user_input.lower():
        print('Thank you for using the application!')
        return True
    else:
        return False


def verify_input(user_input):
    pass


def reset_defaults():
    global START_RANGE, END_RANGE, NUM_COUNT
    print(f"Start - {START_RANGE}, End - {END_RANGE}, Count - {NUM_COUNT} in reset defaults")
    START_RANGE = 0
    END_RANGE = 10
    NUM_COUNT = 1



if __name__=='__main__':
    main()
