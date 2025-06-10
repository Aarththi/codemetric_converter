# codemetric_converter
Task 4 – Create a Unit Converter
Goal:
Build a console-based Python program that converts units like temperature, distance, and weight, using clean design patterns and user-friendly interaction.
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def kilometers_to_miles(km):
    return km * 0.621371

def miles_to_kilometers(miles):
    return miles / 0.621371

def kilograms_to_pounds(kg):
    return kg * 2.20462

def pounds_to_kilograms(lb):
    return lb / 2.20462

conversions = {
    "1": ("Celsius to Fahrenheit", celsius_to_fahrenheit, "°C", "°F"),
    "2": ("Fahrenheit to Celsius", fahrenheit_to_celsius, "°F", "°C"),
    "3": ("Kilometers to Miles", kilometers_to_miles, "km", "miles"),
    "4": ("Miles to Kilometers", miles_to_kilometers, "miles", "km"),
    "5": ("Kilograms to Pounds", kilograms_to_pounds, "kg", "lb"),
    "6": ("Pounds to Kilograms", pounds_to_kilograms, "lb", "kg"),
}

def show_menu():
    print("\n--- Unit Converter ---")
    for key in sorted(conversions):
        print(f"{key}. {conversions[key][0]}")
    print("7. Exit")

def get_valid_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid number. Please enter a valid numeric value.")

def main():
    while True:
        show_menu()
        choice = input("Choose a conversion option (1-7): ").strip()
        if choice in conversions:
            label, func, from_unit, to_unit = conversions[choice]
            value = get_valid_number(f"Enter value in {from_unit}: ")
            result = func(value)
            print(f"{value:.2f} {from_unit} = {result:.2f} {to_unit}")
        elif choice == "7":
            print("Exiting Unit Converter. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
 Detailed Explanation
1. Conversion Functions
Each function handles a specific unit conversion:

celsius_to_fahrenheit(c)

kilometers_to_miles(km)

And so on.

This separation ensures clarity and reusability.

2. Structured Conversion Mapping
The conversions dictionary maps each option number to:

A descriptive label

Reference to the conversion function

Input and output units

This structure allows for scalable and maintainable addition of new conversions.

3. Menu Interface
show_menu() displays options dynamically using the conversions dictionary.

Users choose options by entering numbers (1–7).

4. Input Validation
get_valid_number() continuously prompts until the user enters a valid floating-point number.

5. Main Loop
Runs indefinitely, handling:

Valid conversions (1–6): Performs and prints the result.

Option 7: Exits the loop.

Invalid selections: Prompts the user to choose again.

6. Entry-Point Guard
The if __name__ == "__main__": condition ensures main() only runs when the script is executed directly—not when imported 
discuss.python.org
+2
youtube.com
+2
levelup.gitconnected.com
+2
labex.io
+7
stackoverflow.com
+7
youtube.com
+7
dev.to
+1
discuss.python.org
+1
youtube.com
dev.to
+4
datacamp.com
+4
builtin.com
+4
.

 Example Run
pgsql
Copy
Edit
--- Unit Converter ---
1. Celsius to Fahrenheit
2. Fahrenheit to Celsius
3. Kilometers to Miles
4. Miles to Kilometers
5. Kilograms to Pounds
6. Pounds to Kilograms
7. Exit
Choose a conversion option (1-7): 3
Enter value in km: 5
5.00 km = 3.11 miles

--- Unit Converter ---
Choose a conversion option (1-7): 1
Enter value in °C: 25
25.00 °C = 77.00 °F

--- Unit Converter ---
Choose a conversion option (1-7): 7
Exiting Unit Converter. Goodbye!
 What You Learn
Modular conversion functions make code clean and reusable.

Dictionary-driven menus simplify adding new conversions.

Loop and input validation ensure robust user interaction.

Formatted output via f‑strings clearly shows units.

__name__ == "__main__" keeps code clean when the module is imported elsewhere 
blog.pythonlibrary.org
