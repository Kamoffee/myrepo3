# number_to_shift = int(input("Please enter a number of places to shift:"))
# text = input("Please enter a sentence: ")
# alpha = "abcdefghijklmnopqrstuvwxyz"
# new_alpha = list(alpha)
# text_low = text.lower()
# new_list = []

# for letters in text_low:
#     # Check if the letters are in the alphabet
#     if letters in alpha:
#         index = alpha.index(letters)
#     # Apply the shift of input
#         new_index = (index + number_to_shift) %  26
#         new_letters = new_alpha[new_index]
#         new_list.append(new_letters)
#     else:
#         # keep non - characters from the sentence
#         new_list.append(letters)

# new_text = ''.join(new_list)
# print(new_text)

## another aproach by what open sap wanted before

# # asking for user input
# number_to_shift = input("Please enter the number of places to shift: ")
# text = input("Please enter a sentence: ")

# # check if input number integer.
# if not number_to_shift.isdecimal():
#     print("Error")
#     exit()

# number_to_shift = int(number_to_shift)

# # check that the user input a number between 1 and 25
# if not 0 <= number_to_shift <= 25:
#     print("error")
#     exit()

# text_low = text.lower()
# alpha = "abcdefghijklmnopqrstuvwxyz"
# new_alpha = {}
# other_alpha = {}
# #create a dictionary
# for index, value in enumerate(alpha):
#     new_alpha[value] = index

# #find the index for encrypted sentence
# encrypted_text = ''
# for letter in text_low:
#     #check if letter is found in the alphabet:
#     if letter in alpha:
#         index = new_alpha[letter]
#         new_index = (index + number_to_shift) % 26
#         new_letter = alpha[new_index]
#         encrypted_text += alpha[new_index]
#     else:
#         # add the non-characters in the text
#         encrypted_text += letter

# # print the encrypted text
# print("Encrypted text:", encrypted_text)

### what opensap wants with error
number_to_shift = input("Please enter the number of places to shift: ")
# check if input number is decimal.
if not number_to_shift.isdecimal():
    print("Error")
else:
    number_to_shift = int(number_to_shift) % 26
    # check that the user input a number between 1 and 25
    if not 0 <= number_to_shift <= 25:
        print("Error: The shift value must be between 0 and 25.")


text = input("Please enter a sentence: ")
text_low = text.lower()
alpha = "abcdefghijklmnopqrstuvwxyz"
new_text = ""

for letter in text_low:
    if letter.isalpha():
        index = alpha.find(letter.lower())
        if index != -1:
            new_index = (index + number_to_shift) % 26  # Applying the shift of input
            new_letter = alpha[new_index]
        # Preserve the case of the original letter
            if letter.isupper():
                new_letter = new_letter.upper()
            new_text += new_letter
        else:
        # keep non -alphabetic characters unchanged
            new_text += letter
    else:
        new_text += letter


print("The encrypted sentence is:", new_text)
