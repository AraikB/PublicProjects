
#Day 1 - Project BAND GENERATOR 
#1 Create A Greeting for your program 
#2 Ask the User for a City they grew up in
#3 Ask the User for a name of a pet 
#4 Combine the name of their pet and city and then show them the band name 
#5 Make sure the cursor shows on a new li  

def greeting() -> None:  
    print("Welcome to the Band Name Generator!\n")

def get_city() -> str :
    """ ## get_city 
    Prompts the user for the name of the city they grew up in and returns as str 
    
    ## Returns: 
    :   - city (str) : The name of the city
    """ 
    city = input("Whicy city did you grow up in? \n")
    return city

def get_pet() -> str: 
    """## get_pet 
    Prompts the user for the name of their pet they grew up with and returns as str 
    
    ## Returns: 
    :   - city (str) : The name of the city
    """
    pet = input("What's the name of a pet\n")
    return pet 

def functional_main() -> None: 
    greeting()
    city = get_city()
    pet = get_pet()
    print(f"Your band name could be: {city} {pet}")


def simple_main() -> None: 
    print("Welcome to the Band Name Generator.")
    street = input("What's name of the city you grew up in?\n")
    pet = input("What's your pet's name?\n")
    print("Your band name could be " + street + " " + pet)

if __name__ == '__main__': 
    simple_main()