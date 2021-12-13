import os

NUMBER_OF_FIBONACCI_ELEMENTS = 50


def prompt_greeting_message() -> None:
    os.system('toilet -f smblock --filter border:gay "My container is online!"')


def fibonacci(n: int) -> None:
    print(f'Printing the first {n} Fibonacci numbers:')

    previous = 0
    current = 1
    for i in range(n):
        print(f'The #{i + 1} fibonacci number is: {previous}')
        tmp = previous + current
        current = previous
        previous = tmp


def main() -> None:
    prompt_greeting_message()
    fibonacci(NUMBER_OF_FIBONACCI_ELEMENTS)


if __name__ == '__main__':
    main()
