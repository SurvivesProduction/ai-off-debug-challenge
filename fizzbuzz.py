"""
FizzBuzz — the exact challenge from Survives Production's
"I Turned Off AI And Timed My Own Debugging" (AI Critical Thinking, Episode 1).

Prompt (verbatim, as given on camera):
Print the numbers 1 to 100, but for multiples of 3 print "Fizz", multiples
of 5 print "Buzz", and multiples of both print "FizzBuzz".

Try it yourself before you look at this: set a 3-minute timer, no AI
assistant, and see how it goes.
"""


def fizzbuzz(n: int = 100) -> None:
    for i in range(1, n + 1):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


if __name__ == "__main__":
    fizzbuzz()
