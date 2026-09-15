#Prompt: I’m writing a Python program to help my friend
# track the amount of energy drinks he drinks in a week.
# Keep the code simple and easy to use for most people.
# You should be able to input how many energy drinks they drank on which
# specific day of the week, and the output should tell them possible health
# effects that amount of caffeine could cause. It should also have text
# at the end recommending the number of energy drinks a person should
# drink in a week. Please return Python code with comments explaining each step.

# Define the days of the week
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Define the average caffeine content in an energy drink (in mg)
average_caffeine_per_drink = 80

# Initialize a dictionary to store the number of energy drinks consumed each day
energy_drinks_consumed = {day: 0 for day in days_of_week}

# Function to get user input for the number of energy drinks consumed each day
def get_energy_drink_input():
    for day in days_of_week:
        while True:
            try:
                drinks = int(input(f"How many energy drinks did you drink on {day}? "))
                if drinks < 0:
                    print("Please enter a non-negative number.")
                else:
                    energy_drinks_consumed[day] = drinks
                    break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

# Function to calculate the total caffeine intake for the week
def calculate_total_caffeine(energy_drinks):
    total_drinks = sum(energy_drinks.values())
    total_caffeine = total_drinks * average_caffeine_per_drink
    return total_caffeine

# Function to provide feedback on potential health effects based on total caffeine intake
def provide_feedback(total_caffeine):
    if total_caffeine <= 400:
        print("Your caffeine intake is within a safe range.")
    elif total_caffeine <= 600:
        print("Your caffeine intake is moderate. Be cautious as higher amounts can cause side effects like jitteriness and insomnia.")
    else:
        print("Your caffeine intake is high. Excessive caffeine can lead to serious health issues such as increased heart rate, anxiety, and sleep disturbances.")

# Function to recommend the number of energy drinks to consume in a week
def provide_recommendation(total_caffeine):
    if total_caffeine <= 400:
        print("It's recommended to keep your weekly energy drink consumption to 5 or fewer drinks.")
    elif total_caffeine <= 600:
        print("It's recommended to reduce your weekly energy drink consumption to 3 or fewer drinks.")
    else:
        print("It's strongly recommended to limit your weekly energy drink consumption to 2 or fewer drinks.")

# Main function to run the program
def main():
    print("Welcome to the Energy Drink Tracker!")
    get_energy_drink_input()
    total_caffeine = calculate_total_caffeine(energy_drinks_consumed)
    print(f"\nTotal caffeine intake for the week: {total_caffeine} mg")
    provide_feedback(total_caffeine)
    provide_recommendation(total_caffeine)

# Run the main function
if __name__ == "__main__":
    main()
