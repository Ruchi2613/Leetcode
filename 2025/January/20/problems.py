def getSubarrayBeauty(nums, k, x):
    res = []
    l, r = 0, 0
    negatives = []

    for r in range(len(nums)):
        if nums[r] < 0:
            negatives.append(nums[r])

        if r - l + 1 > k:
            if nums[l] < 0:
                negatives.remove(nums[l])
            l += 1

        if r - l + 1 == k:
            if len(negatives) >= x:
                sorted_negatives = sorted(negatives)
                smallest_element = sorted_negatives[x - 1]
                res.append(smallest_element)
            else:
                res.append(0)

    return res


print(getSubarrayBeauty(nums=[-3, 1, 2, -3, 0, -3], k=2, x=1))

# video: word replacement proj

def replace_word():

    str = "hi Ruchi,Bipin and Amit"

    word_to_replace = input("Enter the word to replace: ")
    word_replacement = input("Enter the word replacement: ")
    str_list = str.split()

    for i in range(len(str_list)):
        if str_list[i] == word_to_replace:
            str_list[i] = word_replacement
        else:
            continue
    updated_sent = " ".join(str_list)
    return updated_sent
print(replace_word())


#Baic calculator:

def add(a,b):
    answer = a+b
    print(str(a) + "+" + str(b) + "=" + str(answer))

def sub(a,b):
    answer = a-b
    print(str(a) + "-" + str(b) + "=" + str(answer))

def mul(a,b):
    answer = a*b
    print(str(a) + "*" + str(b) + "=" + str(answer))

def div(a,b):
    answer = a/b
    print(str(a) + "/" + str(b) + "=" + str(answer))

def cal():

    while True:
        print("A. Addition")
        print("B. Subtraction")
        print("C. Multiply")
        print("D. Division")
        print("E. Exit")

        input_user = input("input your choice:")

        if input_user == 'a' or input_user == 'A':
            print("Addition")

            a = int(input("input first number: "))
            b = int(input("input second number: "))
            add(a,b)

        elif input_user == 'b' or input_user == 'B':
            print("Subtraction")

            a = int(input("input first number: "))
            b = int(input("input second number: "))
            sub(a, b)

        elif input_user == 'c' or input_user == 'C':
            print("Multiply")

            a = int(input("input first number: "))
            b = int(input("input second number: "))
            mul(a, b)

        elif input_user == 'd' or input_user == 'D':
            print("Division")

            a = int(input("input first number: "))
            b = int(input("input second number: "))
            div(a, b)

        elif input_user == 'e' or input_user == 'E':
            quit()

cal()

# Quiz Application
def quiz_application():
    print("Welcome to the Quiz Application!")
    print("Answer the following questions:\n")

    question = {
        "What is the capital of France?": "Paris",
        "What is 5 + 7?": "12",
        "What is the color of the sky on a clear day?": "Blue",
        "Who wrote 'Romeo and Juliet'?": "Shakespeare",
        "What is the boiling point of water (in Celsius)?": "100",
    }
    total_question = len(question)
    score = 0

    for ques, answer in question.items():
        print(ques)
        user_input = input("Answer the question?")

        if user_input.lower() == answer.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is:{answer}\n")

    print(f"Quiz completed! Your score: {score}/{total_question}")

    if score == total_question:
        print("Excellent! You got all the answers right!")

    elif score >= total_question / 2:
        print("Good job! You got more than half correct.")
    else:
        print("Better luck next time!")


quiz_application()

'''QR Generator'''

import qrcode

def generate_qr_code():
    url = input("Enter the website URL: ").strip()

    # Generate QR code
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR code (1 = smallest)
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,  #Size of each box in the QR code grid
        border=4,  #Thickness of the border (minimum is 4)
    )
    qr.add_data(url)
    qr.make(fit=True)

    # Create the QR code image
    img = qr.make_image(fill_color="black", back_color="white")

    file_name = "myportfolio.png"
    img.save(file_name)

    print(f"QR code generated and saved as {file_name}.")

generate_qr_code()

# Password generate
import random
import string


def generate_password():
    length = int(input("How long do you need the password to be? "))
    all_characters = string.ascii_letters + string.digits + string.punctuation

    password = ""

    for x in range(length):
        password += random.choice(all_characters)

    print(f"Your generated password is: {password}")


generate_password()









