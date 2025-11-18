# Python Exam Queston 5

class NumberCategorizer:
    def __init__(self):
        # Initialize lists to store positive, zero and negative numbers
        self.positive_numbers = []
        self.zeros = []
        self.negative_numbers = []
    
    # Function to add the integars into their list
    def add_numbers(self, num):
        # Checks what the number is, and appends to its appropriate list
        if num > 0:
            self.positive_numbers.append(num)
        elif num == 0:
            self.zeros.append(num)
        else:
            self.negative_numbers.append(num)
            
    # Function to print the numbers in one line       
    def print_numbers(self):
        all_numbers = self.positive_numbers + self.zeros + self.negative_numbers
        print("The numbers were:")
        print(" ".join(map(str, all_numbers)))
        
# Main function where the program initializes
def main():
    # Creating instance of the class
    categorizer = NumberCategorizer()
    
    try:
        while True:
            user_input = input("Enter an integer (blank to quit, 'q' to quit immediately): ").strip()
            
            # if the users enters blank, they have option to continue or quit
            if user_input == "":
                confirm = input("Are you sure you want to quit? (y/n): ").strip().lower()
                if confirm == 'y':
                    break
                else:
                    continue
            # Immidiate quit if entering 'q'  
            if user_input.lower() == 'q':
                break
            
            
            try:  
                # Convert user input to an integer
                num = int(user_input)
                
            except ValueError:
                print("Invalid input! Please enter an integer.")
                continue
            
            except OverflowError:
                print("The number entered is too large.")
                continue
            
            # Adding the integer to the categorizer
            categorizer.add_numbers(num)
    
    except KeyboardInterrupt:
        # Handle keyboard interruptions
        print("\n\nProgram interrupted by user.")
        return
    
    finally:
        # Printing the categorized numbers
        categorizer.print_numbers()
        print("Thank you for using the program!")
        
main()