"""
Tip Calculator
Instructions
If the bill was $150.00, split between 5 people, with 12% tip.

Each person should pay (150.00 / 5) * 1.12 = 33.6

Format the result to 2 decimal places = 33.60

Thus everyone's share of the total bill is $30.00 plus a $3.60 tip.

Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

Example Input
Welcome to the tip calculator!
What was the total bill? $124.56
How much tip would you like to give? 10, 12, or 15? 12
How many people to split the bill? 7
Example Output
Each person should pay: $19.93
Hint"""


def simple_version():
    total_bill_amount = float(input("What was the total bill? "))
    tip_percentage = float(
        input("How much tip would you like to give? 10%, 12%, 15%").replace("%", "")
    )
    number_of_people = float(input("How many people will be splitting the bill?"))
    total_with_tip = total_bill_amount * (1 + tip_percentage / 100)
    split_amount = total_with_tip / number_of_people
    print(f"Each person should pay: ${split_amount:.2f}")


class TipCalculator:
    """## TipCalculator

    Takes the total Bill amount, number of people, and the tip percentage desired to be left and returns the price due per person
    """

    def __init__(self) -> None:
        self.greeting()
        self.total_bill_amount = self.get_total_bill()
        self.number_of_people = self.get_number_of_people()
        self.tip_percentage = self.get_tip_percentage()

    def greeting(self) -> None:
        print("Welcome to the tip calculator!")

    def get_total_bill(self) -> float:
        total_bill_amount = float(input("What was the total bill? "))
        return total_bill_amount

    def get_tip_percentage(self) -> float:
        tip_percentage = input("How much tip would you like to give? 10%, 12%, 15% ")
        tip_percentage = float(tip_percentage.replace("%", ""))
        return tip_percentage

    def get_number_of_people(self) -> float:
        number_of_people = float(input("How many people will be splitting the bill? "))
        return number_of_people

    def calculate_amount_per_person(
        self,
    ) -> str:
        self.tip_percentage: float
        total_with_tip = self.total_bill_amount * (1 + self.tip_percentage / 100)
        split_amount = total_with_tip / self.number_of_people
        return f"Each person should pay: ${split_amount:.2f}"


if __name__ == "__main__":
    #  main()
    # simple_version()
    my_calc = TipCalculator()
    print(my_calc.calculate_amount_per_person())
