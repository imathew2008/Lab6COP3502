#first comment
print('hello world')
def menu():
    print(f'Menu\n-------------\n1. Encode\n2. Decode\n3. Quit')

def encode(password):
    newpassword = ''
    for char in password:
        new_digit = (int(char) + 3) % 10
        newpassword += str(new_digit)

    print("Your password has been encoded and stored!")
    return newpassword


if __name__ == "__main__":
    storedPassword = "999999"
    encodedPassword = ''
    while True:
        menu()
        print("Please enter an option: ", end = '')
        pick = int(input())

        if pick == 1:
            print("Please enter your password to encode: ", end = '')
            storedPassword = input()
            encodedPassword = encode(storedPassword)

        #if pick == 2:
            #decode

        if pick == 3:
            exit()