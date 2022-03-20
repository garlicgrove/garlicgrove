def main():
    # range is creating a list of numbers 0 - 9
    # the loop will assign the value to i each iteration of the loop
    print(f"for loop")
    for i in range(10):
        print(f"i is {i}")

    fruits = ["apple", "banana", "carrot"]
    print()
    for fruit in fruits:
        print(f"the fruit is {fruit}")

    print()
    print(f"while loop")
    j = 0
    while j < 5:
        print(f"j is {i}")
        i += 1

if __name__ == '__main__':
    main()