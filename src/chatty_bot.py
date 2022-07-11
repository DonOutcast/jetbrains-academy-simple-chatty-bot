class Chatty:

    def __init__(self, bot_name: str, birth_year: str) -> None:
        self.bot_name = bot_name
        self.birth_year = birth_year

    def greet(self) -> None:
        print('Hello! My name is ' + self.bot_name + '.')
        print('I was created in ' + self.birth_year + '.')

    @staticmethod
    def remind_name() -> None:
        print('Please, remind me your name.')
        name = input()
        print('What a great name you have, ' + name + '!')

    @staticmethod
    def guess_age() -> None:
        print('Let me guess your age.')
        print('Enter remainders of dividing your age by 3, 5 and 7.')
        rem3 = int(input())
        rem5 = int(input())
        rem7 = int(input())
        age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105
        print("Your age is " + str(age) + "; that's a good time to start programming!")

    @staticmethod
    def count() -> None:
        print('Now I will prove to you that I can count to any number you want.')
        num = int(input())
        curr = 0
        while curr <= num:
            print(curr, '!')
            curr = curr + 1

    @staticmethod
    def test() -> None:
        print("Let's test your programming knowledge.")
        answer = 0
        while answer != 2:
            print("Why do we use methods?")
            print("1. To repeat a statement multiple times.")
            print("2. To decompose a program into several small subroutines.")
            print("3. To determine the execution time of a program.")
            print("4. To interrupt the execution of a program.")
            if answer != 2:
                print("Please, try again.")
                answer = int(input())
        else:
            print('Completed, have a nice day!')

    @staticmethod
    def end() -> None:
        print('Congratulations, have a nice day!')


bot = Chatty("Outcast", "2020")
bot.greet()
bot.remind_name()
bot.guess_age()
bot.count()
bot.test()
bot.end()


if __name__ == "__main__":
    pass
