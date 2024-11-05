def kilo_to_pounds(kilos):
    # This statement intentionally has an error. 
    pounds = kilos * 2.20462
    return (pounds)

# Main part of the program starts here. Do not remove the line below.
if __name__ == '__main__':
    kilos = float(input())
    
    pounds = kilo_to_pounds(kilos)
    print(f'{pounds:.3f} lbs')