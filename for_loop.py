#For Loop
#is used for iterating over a sequence
#so we can execute something for each item in list


calulation_to_units=24
name_of_units='hours'

def days_to_units(n):
    return(f"{n} days are {n * calulation_to_units} {name_of_units}")


def validate_user_execute():
    try:
        #user_input_number=int(user_input)
        user_input_number=int(input_days )
        if user_input_number > 0:
            calculated_value=days_to_units(user_input_number)
            print(calculated_value)
        elif user_input_number == "":  #it's not working 
             #user_input_number =""
        # if not user_input_number:
                print("you must enter number don't leave blank")

        elif user_input_number == 0:
             print("you should not enter zero")
        else:
             print("you should not enter negative numbers")
            
    except ValueError:
         print("your input number is not valid")


# user_input= ""   # 1)assign and empty string to user_input

# while user_input != "exit" :  #2)conditions gets executed   #5)second loop:check if exits was typed in             
            
#   user_input=input("Hey user, please enter a number i will do  conversion\n") #3)user is promted for its input
#   validate_user_execute() #4)function is called and input is validated and executed
# #after 5) it again goes the same process 4,5

user_input= ""

while user_input != "exit" :
     user_input=input("Hey user, please enter a number i will do  conversion\n")
     for input_days in user_input.split(","): #convet string to list
      validate_user_execute()

