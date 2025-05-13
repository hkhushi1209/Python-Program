def check_light_clothes_weather(temperature_celsius):
  """Checks if the given temperature is suitable for wearing light clothes.

  Args:
    temperature_celsius: The temperature in Celsius.

  Returns:
    A string indicating whether it's suitable for light clothes.
  """
  if temperature_celsius > 20:
    return "It's warm enough for light clothes!"
  elif temperature_celsius > 15:
    return "Light clothes might be okay, but consider a light layer."
  else:
    return "It's a bit cool for just light clothes. Consider something warmer."

def get_temperature_input():
  """Gets the temperature input from the user."""
  while True:
    try:
      temperature_str = input("Enter the current temperature in Celsius: ")
      temperature = float(temperature_str)
      return temperature
    except ValueError:
      print("Invalid input. Please enter a numerical temperature.")

if __name__ == "__main__":
  print("Welcome to the Light Clothes Weather Checker!")
  current_temperature = get_temperature_input()
  recommendation = check_light_clothes_weather(current_temperature)
  print(recommendation)
  print("Stay comfortable!")