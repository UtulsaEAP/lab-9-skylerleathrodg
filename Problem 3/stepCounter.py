def feet_to_steps(user_feet):
    steps_per_foot = 1 / 2.5
    return int(user_feet * steps_per_foot)

if __name__ == '__main__':
   user_feet = float(input("Enter the number of feet walked: "))
   steps = feet_to_steps(user_feet)
    
   print(f"Number of steps: {steps}")
   feet_to_steps(5280)