
# variables are something that stores a value!
# use the assignment operator = (equals sign)
def main():
    # bool - is a boolean ex: True, False
    b = True
    print(f"Varible b = {b} and is type {type(b)}")
    # int - which is an integer number (no decimals) ex: -1, 0, 1, 2, 3 ....
    i = 1
    print(f"Varible i = {i} and is type {type(i)}")
    # float - which is a real number (is a decimal number) ex: 1.0, 3.14
    f = 1.0
    print(f"Varible f = {f} and is type {type(f)}")
    # str - which is a word (or "string" of characters)
    s = "lollypop"
    print(f"Varible s = {s} and is type {type(s)}")
    # list - a collection of values
    l = [1, 2.0, "a"]
    print(f"Varible l = {l} and is type {type(l)}")

    x = 2
    y = 3
    z = x + y
    print(f"x + y = z is {x} + {y} = {z}")

if __name__ == '__main__':
    main()