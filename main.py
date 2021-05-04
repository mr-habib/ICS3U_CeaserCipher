# Lastname, Firstname
# mm/dd/yyyy
# Description of your code

def ceaser_cipher_encode(message, shift):
    # Code goes here
    pass

def main():
    message = input("Enter the message you wish to encode\n")
    shift = int("Enter the shift amount: ")
  
    new_message = ceaser_cipher_encode(message, shift)
    print(f"Decoded message: {new_message}")
  
  
  
if __name__ == '__main__':
    main()
