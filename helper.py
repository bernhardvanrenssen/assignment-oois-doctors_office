# Script with helper functions here


def check_input_int():
  """Function to check whether input is integer"""
  while True:
    try:
      val = int(raw_input("Please enter a number: "))
      return val
    except ValueError:
      print("Not a valid Number")
      continue
    else:
      break

def check_input_float():
  """Function to check whether input is float """
  while True:
    try:
      val = float(raw_input("Please enter a decimal number, separated by a dot : "))
      return val
    except ValueError:
      print("Not a valid Number")
      continue
    else:
      break

def line_end():
  """Used to space after certain code blocks"""
  print("_________________________________")
  print("")
  return