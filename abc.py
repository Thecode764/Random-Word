import random
def start():
    text = str(input("Enter Text:"))
    answer = random.choice(text)
    answeruser = input("Enter Choice From Your Text:")
    if answeruser == answer:
        print("True")
    else:
        print("False")
    while answeruser != "end":
        text = str(input("Enter Text:"))
        answer = random.choice(text)
        answeruser = input("Enter Choice From Your Text:")
        if answeruser == answer:
            print("True")
        else:
            print("False")
start()