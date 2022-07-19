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


def greeting() -> None:
    print("Welcome to the tip calculator!")


def get_total_bill() -> float:
    total_bill_amount = float(input("What was the total bill? "))
    return total_bill_amount


def get_tip_percentage() -> float:
    tip_percentage = input("How much tip would you like to give? 10%, 12%, 15%")
    tip_percentage = float(tip_percentage.replace("%", ""))
    return tip_percentage


def get_number_of_people() -> float:
    number_of_people = float(input("How many people will be splitting the bill?"))
    return number_of_people


def calculate_tip(
    total_bill_amount: float, number_of_people: float, tip_percentage: float
) -> str:
    total_with_tip = total_bill_amount * (1 + tip_percentage / 100)
    split_amount = total_with_tip / number_of_people
    return f"Each person should pay: ${split_amount:.2f}"


def main():
    bill = get_total_bill()
    tip = get_tip_percentage()
    people = get_number_of_people()
    tip = calculate_tip(bill, people, tip)

    print(tip)


if __name__ == "__main__":
    #  main()
    simple_version()
