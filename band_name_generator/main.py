import random

def main():
    city = input('What is the name of your city?\n')
    pet = input('What is the name of your pet?\n')
    drink = input('What is the name of your favourite drink?\n')
    destination = input('What is the name of your favourite vacation destination?\n')

    name_options = [city, pet, drink, destination]
    
    first_name_choice = random.randint(1, 4) - 1
    second_name_choice = random.randint(1, 4) - 1
    if first_name_choice == second_name_choice:
        if second_name_choice + 1 < len(name_options):
            second_name_choice += 1
        else:
            second_name_choice -= 1
    
    band_name = name_options[first_name_choice] + ' ' + name_options[second_name_choice]
    print('The name of your band could be ' + band_name)



if __name__=='__main__':
    main()
