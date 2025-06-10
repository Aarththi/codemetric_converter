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
