def fizz_buzz(num):
    for n in range(1, num + 1):
        if n % 3 == 0 and n % 5 == 0:
            print(f"{n} FizzBuzz")
        elif n % 3 == 0:
            print(f"{n} Fizz")
        elif n % 5 == 0:
            print(f"{n} Buzz")

def main():
    fizz_buzz(50)

main()

