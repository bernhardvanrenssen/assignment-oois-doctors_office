import prescription, receptionist
#import init

patient_list = []

class Patient:
  """Create a new instance of a patient"""
  def __init__(self, name, address, phone, doctor):
    self._name = name
    self.address = address
    self.phone = phone
    self._doctor = doctor
    self.prescription_list = []

  @property
  def doctor(self):
    return self._doctor

  @property
  def name(self):
    return self._name

  def request_prescription(self):
    """Return list of prescriptions registered under this user instance"""

    prescription_type = input("""
Please list the type of prescription:
1: See active prescriptions
2: Repeat prescription
""")
    if prescription_type == 1:

      return
    elif prescription_type == 2:
      if self.prescription_list:
        print("Your current active prescriptions are: ")
        for x in self.prescription_list:
          print(x.patient)
      else:
        print("You do not have any active prescriptions")
        self.request_prescription()

  def request_appointment(self, timeslot, reception):
    reception.make_appointment(self.name, self.doctor, timeslot)
