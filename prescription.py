import patient

class Prescription:
  """Create instance of a new prescription"""
  def __init__(self, type, patient, quantity, dosage, doctor=None):
    self.type = type
    self.patient = patient
    self.doctor = doctor 
    self.quantity = quantity
    self.dosage = dosage

    #print("New prescription logged: {}").format(self.type)

