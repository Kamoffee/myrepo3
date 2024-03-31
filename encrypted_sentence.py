# add your code here
# Define the caesar function
def caesar (sentence):
    encrypted_sentence = "" 
    encryption_key = 5
    alpha = "abcdefghijklmnopqrstuvwxyz"

    #Checking if the letter
    for letter in sentence.lower():
        # Check if the letters are in the alphabet
        if letter in alpha:
            index = alpha.find(letter)
            # Apply the shift of input
            new_index = (index + encryption_key) % 26
            # Adding the new index to the sentence
            encrypted_sentence += alpha[new_index]
        else:
         # keep non - characters from the sentence
            encrypted_sentence += letter

    return encrypted_sentence


# Creating a main function to coordinate caesar function
def main():
    # Asking for user input in our caesar variables
    text_low = input("Please enter a sentence: ")
    cypher = caesar(text_low)
    # Sentence that is going to be printed when the function will be called
    print("The encrypted sentence is: " + cypher)

# Calling the main function
main()

## another aproach 

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



# # Define a function
# def caesar (number_to_shift, text_low): 
#     # Checking to see if the user input is decimal and in range
#     if not number_to_shift.isdecimal() or not (0 <= int(number_to_shift) <= 25) :
#         print("You need to enter a number between 0 and 25!") 
#     else:
#         # set our variables
#         number_to_shift = int(number_to_shift)
#         alpha = "abcdefghijklmnopqrstuvwxyz"
#         new_alpha = list(alpha)
#         new_list = []

#         for letters in text_low.lower():
#             # Check if the letters are in the alphabet
#             if letters in alpha:
#                 index = alpha.find(letters.lower())
#             # Apply the shift of input
#                 new_index = (index + number_to_shift) %  26
#                 new_letters = new_alpha[new_index]
#                 new_list.append(new_letters)
#             else:
#                 # keep non - characters from the sentence
#                 new_list.append(letters)

#         new_text = ''.join(new_list)
#         return new_text

# # Creating a main function to coordinate caesar function
# def main():
#     # Asking for user input in our caesar variables
#     number_to_shift = input("Please enter a number of places to shift:") 
#     text_low = input("Please enter a sentence: ")
#     cypher = caesar(number_to_shift, text_low)
#     print(cypher)


main()

## another aproach 

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


