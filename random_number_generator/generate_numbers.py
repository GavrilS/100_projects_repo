from random import randrange

START_RANGE = 0


def main():
    flag = True
    while flag:
        details = input("What's the range you want to use:")
        details_array = details.split(',')
        range_details = details_array[0].strip()
        if '-' in range_details:
            range_details = range_details.split('-')
            START_RANGE = range_details[0]
            end_range = range_details[1]
        else:
            end_range = range_details



if __name__=='__main__':
    main()
