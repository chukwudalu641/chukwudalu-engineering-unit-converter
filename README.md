# Engineering Unit Converter

## What it does
This Python program serves as an interactive unit converter for common engineering measurements. It converts between millimeters and inches, Celsius and Fahrenheit, kilograms and pounds, and km/h to m/s, using continuous loop execution and defensive error handling.

## How to run it
Install Python 3, then run:
`python unit_converter.py`

## Sample output
ENGINEERING UNIT CONVERTER
Choose a conversion option:

Millimeters to Inches (mm -> in)

Celsius to Fahrenheit (°C -> °F)

Kilograms to Pounds (kg -> lb)

Kilometers/hour to Meters/second (km/h -> m/s)

MPa to PSI [Custom Twist: Material Stress]

Exit

Enter choice (1-6): 5
Enter value to convert: 250
👉 [My Twist] Material Stress Conversion:
250.0 MPa = 36259.50 PSI (Pounds per Square Inch)

## My own twist
I added a material stress and pressure conversion feature (Megapascals to PSI). This allows mechatronics students and engineers to convert tensile strength values from metric system specifications (MPa) to imperial pressure units (PSI).

## What I learned
I learned how to write defensive input validation using `try-except` blocks to prevent string input crashes, and how to use conditional loops to continuously run an engineering menu until the user explicitly quits.

## Author
ONYEJIMBE CHUKWUDALU KAOBIMDI, ND1 Mechatronics Engineering, YabaTech.
