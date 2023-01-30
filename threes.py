def func(usr_in):
    print(usr_in * '*')

def func2(usr_in):
    i = 0
    while i <= usr_in:
        func(i)
        i += 1

def func3(usr_in):
    for i in range(usr_in):
        func(i+1)

def main():
    func(3)
    func2(3)
    func3(3)

if __name__ == "__main__":
    main()