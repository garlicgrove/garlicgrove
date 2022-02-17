def helloWorld():
    print(f"Hello world!")

def helloSomeone(name):
    print(f"Hello {name}!")

def add(a, b):
    return a + b

def main():
    helloWorld()
    helloSomeone("Bobby")

    fruits = ["apple", "banana", "carrot"]
    print()
    for fruit in fruits:
        helloSomeone(fruit)

    sum = add(1, 2)
    print()
    print(f"sum is {sum}")

if __name__ == '__main__':
    main()