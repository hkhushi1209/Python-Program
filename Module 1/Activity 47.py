import math

def calculate_circumference(radius):
  """
  Calculates the circumference of a circle given its radius.

  Args:
    radius: The radius of the circle (a non-negative number).

  Returns:
    The circumference of the circle.
    Returns None if the radius is negative.
  """
  if radius < 0:
    print("Error: Radius cannot be negative.")
    return None
  else:
    circumference = 2 * math.pi * radius
    return circumference

# Example usage:
if __name__ == "__main__":
  # Get input from the user
  try:
    user_radius = float(input("Enter the radius of the circle: "))

    # Call the function to calculate circumference
    circ = calculate_circumference(user_radius)

    # Display the result
    if circ is not None:
      print(f"The circumference of a circle with radius {user_radius} is: {circ:.2f}")
  except ValueError:
    print("Invalid input. Please enter a number for the radius.")