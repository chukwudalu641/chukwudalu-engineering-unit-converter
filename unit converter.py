# CTE123 Mini Project: Engineering Unit Converter
# Student Name: ONYEJIMBE CHUKWUDALU KAOBIMDI
# Department: ND1 Mechatronics Engineering, YabaTech

def convert_units():
    print("==================================================")
    print("         ENGINEERING UNIT CONVERTER              ")
    print("==================================================")
    
    while True:
        print("\nChoose a conversion option:")
        print("1. Millimeters to Inches (mm -> in)")
        print("2. Celsius to Fahrenheit (°C -> °F)")
        print("3. Kilograms to Pounds (kg -> lb)")
        print("4. Kilometers/hour to Meters/second (km/h -> m/s)")
        print("5. MPa to PSI [Custom Twist: Material Stress]")
        print("6. Exit")
        
        choice = input("\nEnter choice (1-6): ").strip()
        
        if choice == '6':
            print("Exiting program. Engineering unit converter closed.")
            break
            
        if choice not in ['1', '2', '3', '4', '5']:
            print("❌ Invalid selection! Please pick a number from 1 to 6.")
            continue
            
        # Error handling for non-numerical input
        try:
            val = float(input("Enter value to convert: "))
        except ValueError:
            print("❌ Error: Invalid input! Please enter a numerical value.")
            continue

        # Performing conversion logic
        if choice == '1':
            if val < 0:
                print("⚠️ Warning: Length measurement cannot be negative.")
                continue
            res = val / 25.4
            print(f"👉 Result: {val} mm = {res:.4f} inches")

        elif choice == '2':
            if val < -273.15:
                print("⚠️ Warning: Temperature below absolute zero (-273.15 °C) is physically impossible.")
                continue
            res = (val * 9/5) + 32
            print(f"👉 Result: {val} °C = {res:.2f} °F")

        elif choice == '3':
            if val < 0:
                print("⚠️ Warning: Mass cannot be negative.")
                continue
            res = val * 2.20462
            print(f"👉 Result: {val} kg = {res:.4f} lbs")

        elif choice == '4':
            if val < 0:
                print("⚠️ Warning: Speed/velocity cannot be negative here.")
                continue
            res = val / 3.6
            print(f"👉 Result: {val} km/h = {res:.2f} m/s")

        elif choice == '5':
            if val < 0:
                print("⚠️ Warning: Tensile stress/pressure magnitude cannot be negative.")
                continue
            res = val * 145.038
            print("--------------------------------------------------")
            print(f"👉 [My Twist] Material Stress Conversion:")
            print(f"   {val} MPa = {res:.2f} PSI (Pounds per Square Inch)")
            print("--------------------------------------------------")

if __name__ == "__main__":
    convert_units()