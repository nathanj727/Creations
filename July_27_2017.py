# If and while one in the same

spam = 0
if spam < 5:
    print("Hello World.")
    spam = + 1

spam = 0
while spam < 5:
    print("Hello,world!")
    spam = spam + 1

spam = 5
if spam < 5:
    print("Hi World!")
    spam = + 1
else:
    print("What??")


while True:
    print('Please tell me your name.(*lowercase*only*)')
    name = input(">")
    if name.islower():
        print(f"Your name is lowercase:{name}")
        break
    else:
        print(f"Please try again.")
        continue
