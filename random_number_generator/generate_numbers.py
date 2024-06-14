import random

START_RANGE = 0
END_RANGE = 10
NUM_COUNT = 1


def main():
    show_instructions()
    flag = True
    while flag:
        details = input("What's the range you want to use:")

        if check_for_exit(details):
            break

        start, end, num_count, value_error = dissect_input(details)

        if value_error:
            print(value_error)
            show_instructions()
            continue

        get_numbers(start, end, num_count)

        reset_defaults()


def show_instructions():
    instructions = "This program is generating random numbers in the user specified range. \n" \
        "If the user does not provide a range when prompted, the defaults will be used.\n" \
        "Defaults: Start range number - 0; End range number - 10; Number of randomly generated numbers - 1.\n" \
        "The format of the range you can specify is START_NUMBER-END_NUMBER,NUMBER_COUNT_TO_GENERATE.\n" \
        "Example: What's the range you want to use: 10-100,5 will generate 5 random numbers between 10 and 100.\n" \
        "You can skip the start number and the number count parameters and the default values will be used.\n" \
        "Type 'exit' to stop the program."

    print('-------------------')
    print('Instructions:')
    print(instructions)
    print('-------------------')


def get_numbers(start, end, num_count):
    tracker = 0
    while tracker < num_count:
        print(random.randint(start, end), end=' ')
        tracker += 1
    print(end='\n')


def dissect_input(user_input):
    global START_RANGE, END_RANGE, NUM_COUNT
    value_error = None
    try:
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
    except Exception as e:
        return START_RANGE, END_RANGE, NUM_COUNT, str(e)


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
