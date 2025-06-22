# 1st  task ////

# for i in range(1,51):
    
#   if i % 3 == 0 and i % 5 == 0:
#     print(f'FizzBuzz',i)
#   elif i % 3 == 0:
#     print(f'fizz',i) 
#   elif i % 5 == 0:
#     print(f'buzz',i)
#   else:
#     print(i)     

# 2nd task       /////////

# palindrome = 'madam'

# istrue = True

# while istrue:
#   input_palindrome = input('Enter your name ')

#   if palindrome == input_palindrome:
#     print('palindrome')
#   else:
#     print('not palindrome')  


istrue = True

while istrue:
    input_palindrome = input("Enter a word (or type 'exit' to quit): ").strip()

    if input_palindrome.lower() == "exit":
        break

    if input_palindrome == input_palindrome[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")


