def main():
    MENU = """C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            def celsius_to_fahrenheit():
                celsius = float(input("Celsius: "))
                fahrenheit = celsius * 9.0 / 5 + 32
                return fahrenheit
            fahrenheit = celsius_to_fahrenheit()
            print("Result: {:.2f} F".format(fahrenheit))
        elif choice == "F":
            def fahrenheit_to_celsius()
            fahrenheit = float(input("Fahrenheit:"))
            #celsius = 5 / 9 * (fahrenheit - 32)
            #print("Result: {:.2f} C".format(celsius))
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")

main()