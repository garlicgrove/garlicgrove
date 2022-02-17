
from tkinter import Variable


def helloWorld():
    print("Hello World!")

def variables():
    val = input("Enter something: ")
    print(f"value is {val} of type {type(val)}")

def ifStatement():
    val = int(input("Enter a number: "))
    if (val % 2 == 0):
        print(f"{val} is even")
    else:
        print(f"{val} is odd")

def loops():
    val = int(input("Enter a number: "))
    for i in range(val):
        print(f"looped {i + 1} time(s)")

def main():
    choice = ""
    while choice != "exit":
        choice = str(input("What do you want to do? ")).lower()
        if choice == "helloworld":
            helloWorld()
        elif choice == "variables":
            variables()
        elif choice == "if_statement" or choice == "ifstatement":
            ifStatement()
        elif choice == "loops":
            loops()

if __name__ == '__main__':
    main()
