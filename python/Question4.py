# Python Exam Question 4
import random

#This code creates a basic list of 10 random numbers 
def get_randomList(length, min_value, max_value):
    return [random.randint(min_value, max_value) for _ in range(length)]

#This code is used to use substitute on the basic list (get_randomList function)
def substitute(lst):
    for i in range(len(lst)):
        if lst[i] % 5 == 0:
            lst[i] = lst[i] ** 2

def main():
    # This code prints a list with 10 random numbers between 1 and 50
    random_list = get_randomList(10, 1, 50)
    
    print("Before substitution, the list is:", random_list)
    
    # This code is used to perform substitution on random_list
    substitute(random_list)
    
    print("After substitution, the list is:", random_list)

if __name__ == "__main__":
    main()
