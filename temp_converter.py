def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)


def main():
    print("Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Celsius to Kelvin")
    print("3. Fahrenheit to Celsius")
    print("4. Fahrenheit to Kelvin")
    print("5. Kelvin to Celsius")
    print("6. Kelvin to Fahrenheit")

    choice = input("Choose an option (1-6): ")
    value = float(input("Enter the temperature value: "))

    if choice == "1":
        result = celsius_to_fahrenheit(value)
        print(f"{value}°C = {result:.2f}°F")
    elif choice == "2":
        result = celsius_to_kelvin(value)
        print(f"{value}°C = {result:.2f}K")
    elif choice == "3":
        result = fahrenheit_to_celsius(value)
        print(f"{value}°F = {result:.2f}°C")
    elif choice == "4":
        result = fahrenheit_to_kelvin(value)
        print(f"{value}°F = {result:.2f}K")
    elif choice == "5":
        result = kelvin_to_celsius(value)
        print(f"{value}K = {result:.2f}°C")
    elif choice == "6":
        result = kelvin_to_fahrenheit(value)
        print(f"{value}K = {result:.2f}°F")
    else:
        print("Invalid choice. Please run the program again.")


if __name__ == "__main__":
    main()