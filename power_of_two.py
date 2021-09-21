def ispoweroftwo(n):
    b = 0
    if n <= 0:
        return False
    while n > 1:
        b = int(n % 2)
        if b != 0:
            return False
        n = n / 2
    return True


def main():
    print(ispoweroftwo(1))
    print(ispoweroftwo(16))
    print(ispoweroftwo(3))
    print(ispoweroftwo(4))
    print(ispoweroftwo(5))
    print(ispoweroftwo(0))
    print(ispoweroftwo(-16))


if __name__ == "__main__":
    main()
