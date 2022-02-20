import patient, prescription, helper

class Healthcare_professionals():
  """Create instance of a new Healtcare Professional. Parent class, can be either Doctor or Nurse"""
  def __init__(self, name, emp_nr, app_schedule):
    self._name = name
    self._emp_nr = emp_nr
    self.app_schedule = app_schedule

  @property
  def emp_nr(self):
    return self._emp_nr

  @property
  def name(self):
    return self._name

  def __str__(self):
    return "{}".format(self.name)

class Doctor(Healthcare_professionals):
  def __init__(self, name, emp_nr, app_schedule):
    Healthcare_professionals.__init__(self, name, emp_nr, app_schedule)

  def issue_prescription(self, patient):
    """Only doctors can issue prescriptions. Method creates new instance of Prescription class and assigns it to patient argument"""
    doctor = self.name
    patient = patient
    prescription_type = raw_input("Please enter your prescription type: ")
    print("Please enter the prescription quantity - ") # Would have loved to use end='' here, but we still working in python 2 sadly.
    quantity = helper.check_input_int()
    print("Please enter the dosage amount (ml) - ")
    dosage = helper.check_input_float()
    doctor = self.name
    new_prescription = prescription.Prescription(prescription_type, patient, quantity, dosage, self.name)
    prescription_val = len(patient.prescription_list) + 1
    prescription_dict = {'val': prescription_val, 'med': new_prescription}
    patient.prescription_list.append(prescription_dict)
    return

  def print_patients(self, patients):
    """Returns a list of patients that the doctor is currently registered with"""
    my_patients = []
    for p in patients:
      if str(p.get('patient').doctor) == str(self.name):
        my_patients.append(p)
    return my_patients
  

class Nurse(Healthcare_professionals):
  def __init__(self):
    super().__init__()