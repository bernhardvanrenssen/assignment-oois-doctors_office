import appointment_schedule

class Receptionist:
  """Class to create instance of a new receptionist"""
  def __init__(self, name, emp_nr):
    self.name = name
    self.emp_nr = emp_nr
  
  def make_appointment(self, patient, doctor, timeslot):
    """Appointments are made through receptionists - function called to make a new appointment for a doctor & patient instance"""
    doctor.app_schedule.add_appointment(patient, timeslot)

  def cancel_appointment(self, doctor, appointment):
    """Function cancels an appointment made"""
    doctor.app_schedule.cancel_appointment(appointment)