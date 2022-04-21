#!/usr/bin/env python3
# Created by: Hunter Connolly
# Created on: April 20, 2022
# This program asks the user to enter a whole number
# it then calculates the factorial of that number

def main():

    # Get the user input as a string
    user_input_string = input("Enter a whole number: ")
    print("")

    try:
        # get the user number
        user_input = int(user_input_string)
        
        if user_input <= -1:
            print("That is negative")
        elif user_input == 0:
            print("0! is 1")
        else:
            # initialize loop counter and the answer
            loop_counter = 0
            factorial_answer = 1
            # calculate the factorial
            while True:
                loop_counter = loop_counter + 1
                factorial_answer = factorial_answer * loop_counter
                print("Tracking {} times through loop".format(loop_counter))
                if loop_counter >= user_input:
                    break

        print("")
        print("{}! = {}".format(user_input, factorial_answer))

    except Exception:
        print("That is not a number!!")


if __name__ == "__main__":
    main()
