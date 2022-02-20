# Script used in isolation - all test scenarios built here and tested - once it passes, implemented in the code

print('''
Run tests - 
1: Test Setup
2: Test Patient Class
3: Test dict calling
4: Test input type
''')

answer = input("Enter test nr  ")

# Test 1: testing
if answer == 1:
  print("Test 1 successfull") 
  

# Test 2: Create Patient instance
elif answer == 2:

  class Patient:
    def __init__(self, name, address, phone):
      self.name = name
      self.address = address
      self.phone = phone
    
    def __str__(self):
      #return f"{self.name}" - THIS IS NOT WORKING...apparently we are using Python 2 and not 3 which do not support f strings.
      return "{} is living at {} with number {}".format(self.name, self.address, self.phone)

  person = Patient("Max", "123 Abc Street", "0123456789")
  print(person)

# Test 3: Call person from dict val
elif answer == 3:

  doctors = []

  class Doctor:
    def __init__(self, name, emp_nr):
      self.name = name
      self.emp_nr = emp_nr

  doc1 = Doctor("Dr. Watson", "221B")
  doctors.append({'val': 1, 'doc': doc1})
  doc2 = Doctor("Dr. Strange", "222A")
  doctors.append({'val': 2, 'doc': doc2})

  for i in doctors:
    print("{}: {}").format(i.get('val'), i.get('doc').name)

# Test 4: Check input values
elif answer == 4:

  def check_input_int(input):
    while True:
      try:
        val = int(raw_input("Please enter a number: "))
        return val
      except ValueError:
        print("Not a Number")
        continue
      else:
        break

  val = raw_input("Enter an int value: ")
  int_val = check_input_int(val)
  print("Done! {}").format(int_val)



