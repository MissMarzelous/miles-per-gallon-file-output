# PROGRAMMER:   Marlena Fabrick
# PROGRAM NAME: Miles Per Gallon Calculator — Functions with File Output
# DATE WRITTEN: 11/11/2020
# UPDATED:      2026 — MULTIPLE BUG FIXES: wrong variable names in writeResults()
#                      (gals/miles → gal/mls), outFile.write() called with no args,
#                      writeResults() called with no arguments. All fixed.
#                      Renamed variables to snake_case, removed unused toFixed().
#
# PURPOSE: Calculate the miles per gallon for a vehicle using functions,
#          and write the results to a user-named external output file.
#          Demonstrates file I/O combined with modular function design.
#
# FUNCTIONS:
#   checkFloatDataType(data_type) — validates positive float input
#   calcMPG(miles, gals)          — calculates and returns MPG
#   writeResults(mls, gal, mpg, out_file) — writes formatted report to file

# ============================================================
# Create an external file to store output
# Ask user for the desired output file name
file_name = input("Enter a name for the output file (without extension):\n")
out_file = open(file_name + ".txt", "w")  # Open file in write mode

# ============================================================
# Declare Variables in alpha order
# Initialize / declare variables
gallons_used = 0.0
miles_per_gallon = 0.0
miles_driven = 0.0

# ============================================================
# FUNCTION DEFINITIONS

# Function to validate data type and check for negative/zero values
def checkFloatDataType(data_type):  # formal parameter to hold/store input
    while True:
        try:
            data_type = float(input())
        except ValueError:
            print("Wrong data type entered — please enter a positive numeric value.\n")
            continue
        else:
            if data_type <= 0:
                print("Negative value or zero entered — re-enter a positive numeric value.\n")
                continue
            else:
                break  # Valid input received, exit loop
    return data_type
    # end checkFloatDataType function

# Function to calculate miles per gallon
def calcMPG(miles, gals):
    mpg = miles / gals  # Divide miles driven by gallons used
    return mpg
    # end calcMPG function

# Function to write the formatted MPG report to the output file
def writeResults(mls, gal, mpg, out_file):
    # Output Operations — write results to the external file
    out_file.write("=" * 65 + "\n")
    out_file.write("CAR MILEAGE INFORMATION\n")
    out_file.write("=" * 65 + "\n")
    out_file.write("Miles Driven     = " + format(mls, "10,.2f") + "\n")  # Fixed: was using undefined 'miles'
    out_file.write("Gallons Used     = " + format(gal, "10,.2f") + "\n")  # Fixed: was using undefined 'gals'
    out_file.write("Miles Per Gallon = " + format(mpg, "10,.2f") + "\n")
    out_file.write("=" * 65 + "\n")
    out_file.write("\n")  # Fixed: was outFile.write() with no arguments
    # END writeResults function

# ============================================================
# INPUT OPERATIONS

# Collect miles driven — call function to validate data type
print("How many miles were driven using your vehicle?")
miles_driven = checkFloatDataType(miles_driven)

# Collect gallons used — call function to validate data type
print("How many gallons were used by the vehicle?")
gallons_used = checkFloatDataType(gallons_used)

# ============================================================
# CALCULATE MILES PER GALLON — call calcMPG function
miles_per_gallon = calcMPG(miles_driven, gallons_used)

# ============================================================
# OUTPUT — call writeResults, passing all required values and the file handle
writeResults(miles_driven, gallons_used, miles_per_gallon, out_file)  # Fixed: was called with no arguments

# Close the output file once writing is complete
out_file.close()
print(f"Results written to {file_name}.txt")

# END PROGRAM
