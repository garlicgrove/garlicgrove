
def main():
    b = False
    print()
    print("---")
    if (b):
        # if the statement is true, we do this
        print(f"it's true!")
    else:
        # otherwise (else), we do this
        print(f"rip, it's false")

    i = 15
    print()
    print("---")
    if (i < 10):
        print(f"i it's small")
    else:
        print(f"i it's big")

    # elif - means "else if"
    j = 15
    print()
    print("---")
    if (j < 10):
        print(f"j it's small")
    elif (j < 20):
        print(f"j it's medium")
    else:
        print(f"j it's big")

    k = 25
    print()
    print("---")
    if (k < 10):
        print(f"k it's small")
    elif (k < 20):
        print(f"k it's medium")
    elif (k < 30):
        print(f"k it's medium-big")
    else:
        print(f"it's big")

    # this is why elif is important
    m = 9
    print()
    print("---")
    if (m < 10):
        print(f"m small")
    if (m < 20):
        print(f"m medium")
    if (m < 30):
        print(f"m medium-big")

if __name__ == '__main__':
    main()