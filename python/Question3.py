# Python Exam Question 3


# Class that models an email message.
class Message:
    def __init__(self, sender, recipient):
        self.sender = sender
        self.recipient = recipient
        self.message_body = ""
        
    
    def get_sender(self):
        return self.sender


    def get_recipient(self):
        return self.recipient

    def append_msg(self, text):
        # appends a line of text to the message body
        self.message_body += text + "\n"
        
    # adds whole message to the message body    
    def add_message_manually(self):
        print("Enter your message (Enter 'done' on a new line to finish): ")
        while True:
            line = input()
            if line.lower() == 'done':
                break
            self.append_msg(line)
    
    # Returns message as tring
    def __str__(self):
        body_with_sender = self.message_body + f"\nBest regards,\n{self.sender}\n"
        return f"From: {self.sender}\nTo: {self.recipient}\n\n{body_with_sender}"


# Example
# Main function to create and send messages for users

def main():
    while True:
        try:
            # Prompt the user to have to enter sender's name as string
            sender_name = input("Enter sender's name: ")
            if not sender_name.strip():
                raise ValueError("Sender's name cannot be empty.")
                
            # promt the user for recipient's name
            recipient_name = input("Enter recipient's name: ")
            if not recipient_name.strip():
                raise ValueError("Recipient's name cannot be empty.")
            
            # Creating instance of class Message
            message = Message(sender_name, recipient_name)
            
            # Allow's user to add message manually
            message.add_message_manually()
            
            
            # Composed message
            print("\nYour Message:")
            print(message)
            
            # Notifies user of sent message
            print("Message sent")
            break
            
        except ValueError:
            print("Error: Please try typing in string")
        
        except KeyboardInterrupt:
            print("\nUser terminated the input.")
            return
            
    
# Calling main to execute example program      
main()
