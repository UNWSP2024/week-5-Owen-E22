# Program #1: Kilometer Converter
# Write a program that asks the user to enter a distance in kilometers, 
# then converts that distance to miles.  The conversion formula is as follows:  
# Miles = kilometers x 0.6214.   
# The conversion must be done as a function with input and output.


def kilometer_conversion(kilometers):

    miles = kilometers * 0.6214
    print(kilometers,f'is equal to {miles:.2f} miles')

    # Return the variable to the calling function
    return miles

kilometer_conversion(float(input('Enter distance in Kilometers: ')))

    # Call kilometer_conversion
    
    # Display the miles
