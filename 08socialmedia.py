# Social Media Message Sharing:

# Suppose each person shares a message with 3 new people every round. Write a python program to
# estimate the number of people reached in each round.

initial_people = int(input("Enter the initial number of people: "))
number_of_rounds = int(input("Enter the number of rounds: "))

total_people = initial_people * (3 ** number_of_rounds)
print(f"The total number of people reached after {number_of_rounds} rounds is {total_people}")