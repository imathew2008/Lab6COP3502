
#Isabelle Mathew

print('hello world')
def menu():
    #print menu
    print(f'Menu\n-------------\n1. Encode\n2. Decode\n3. Quit')

def encode(password):
    #create empty string for encoded password
    newPassword = ''
    #iterate through password
    for char in password:
        #take last digit +3 and add to newPassword
        new_digit = (int(char) + 3) % 10
        newPassword += str(new_digit)

    print("Your password has been encoded and stored!")
    return newPassword

#main
if __name__ == "__main__":
    #initialize empty passwords
    storedPassword = ""
    encodedPassword = ""
    #program loop
    while True:
        #print menu and take menu selection
        menu()
        print("Please enter an option: ", end = '')
        pick = int(input())

        #if user selected 1 ask for and encode password
        if pick == 1:
            print("Please enter your password to encode: ", end = '')
            storedPassword = input()
            encodedPassword = encode(storedPassword)

        #if pick == 2:
            #decode

        #if user selected 3 terminate program
        if pick == 3:
            exit()