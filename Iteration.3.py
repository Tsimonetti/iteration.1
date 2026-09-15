#I’m writing a Python program to help my friend track the amount of
# energy drinks he drinks in a year. Keep the code simple and easy to
# use for most people. You should be able to input how many energy
# drinks they drank on which specific months of the year, and the output
# should tell them possible health effects that amount of caffeine could
# cause as well as other unhealthy ingredients and their effects. Then it
# should graph the results on a chart where the x-axis is the months and
# the y-axis is the amount of energy drinks. It should also have text at
# the end recommending the number of energy drinks a person should drink
# in a year. Please return Python code with comments explaining each step.

import matplotlib.pyplot as plt

# Define the months of the year
months_of_year = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

# Define the average caffeine content in an energy drink (in mg)
average_caffeine_per_drink = 80

# Define other unhealthy ingredients and their effects
unhealthy_ingredients = {
    "Sugar": "Excessive sugar can lead to weight gain, diabetes, and tooth decay.",
    "Taurine": "High levels of taurine can cause heart problems and increased blood pressure.",
    "Ginseng": "Overconsumption of ginseng can cause insomnia, headaches, and digestive issues.",
    "Guarana": "Guarana contains caffeine and can cause similar side effects, including jitteriness and anxiety."
}

# Initialize a dictionary to store the number of energy drinks consumed each month
energy_drinks_consumed = {month: 0 for month in months_of_year}


# Function to get user input for the number of energy drinks consumed each month
def get_energy_drink_input():
    for month in months_of_year:
        while True:
            try:
                drinks = int(input(f"How many energy drinks did you drink in {month}? "))
                if drinks < 0:
                    print("Please enter a non-negative number.")
                else:
                    energy_drinks_consumed[month] = drinks
                    break
            except ValueError:
                print("Invalid input. Please enter a valid number.")


# Function to calculate the total caffeine intake for the year
def calculate_total_caffeine(energy_drinks):
    total_drinks = sum(energy_drinks.values())
    total_caffeine = total_drinks * average_caffeine_per_drink
    return total_caffeine


# Function to provide feedback on potential health effects based on total caffeine intake
def provide_feedback(total_caffeine):
    if total_caffeine <= 400 * 52:  # 400 mg per day * 52 weeks
        print("Your caffeine intake is within a safe range for the year.")
    elif total_caffeine <= 600 * 52:  # 600 mg per day * 52 weeks
        print(
            "Your caffeine intake is moderate. Be cautious as higher amounts can cause side effects like jitteriness and insomnia.")
    else:
        print(
            "Your caffeine intake is high. Excessive caffeine can lead to serious health issues such as increased heart rate, anxiety, and sleep disturbances.")


# Function to provide feedback on other unhealthy ingredients
def provide_unhealthy_ingredient_feedback(total_drinks):
    if total_drinks <= 208:  # 4 drinks per week * 52 weeks
        print("Your consumption of other unhealthy ingredients is within a safe range for the year.")
    elif total_drinks <= 312:  # 6 drinks per week * 52 weeks
        print(
            "Your consumption of other unhealthy ingredients is moderate. Be cautious as higher amounts can cause various health issues.")
    else:
        print(
            "Your consumption of other unhealthy ingredients is high. Excessive intake can lead to serious health issues such as heart problems, weight gain, and digestive issues.")
    for ingredient, effect in unhealthy_ingredients.items():
        print(f"Effect of {ingredient}: {effect}")


# Function to recommend the number of energy drinks to consume in a year
def provide_recommendation(total_drinks):
    if total_drinks <= 208:
        print("It's recommended to keep your yearly energy drink consumption to 208 or fewer drinks.")
    elif total_drinks <= 312:
        print("It's recommended to reduce your yearly energy drink consumption to 156 or fewer drinks.")
    else:
        print("It's strongly recommended to limit your yearly energy drink consumption to 104 or fewer drinks.")


# Function to plot the energy drink consumption
def plot_energy_drink_consumption(energy_drinks):
    months = list(energy_drinks.keys())
    drinks = list(energy_drinks.values())

    plt.figure(figsize=(10, 6))
    plt.bar(months, drinks, color='blue')
    plt.xlabel('Month')
    plt.ylabel('Number of Energy Drinks')
    plt.title('Energy Drink Consumption Over the Year')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


# Main function to run the program
def main():
    print("Welcome to the Energy Drink Tracker!")
    get_energy_drink_input()
    total_drinks = sum(energy_drinks_consumed.values())
    total_caffeine = calculate_total_caffeine(energy_drinks_consumed)
    print(f"\nTotal number of energy drinks consumed for the year: {total_drinks}")
    print(f"Total caffeine intake for the year: {total_caffeine} mg")
    provide_feedback(total_caffeine)
    provide_unhealthy_ingredient_feedback(total_drinks)
    provide_recommendation(total_drinks)
    plot_energy_drink_consumption(energy_drinks_consumed)


# Run the main function
if __name__ == "__main__":
    main()