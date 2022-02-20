#Appointment Schedule

class Appointment_Schedule:
  """Each doctor has an instance of this class, to manage their appointments"""
  def __init__(self):
    #Pre-populated the list with some available/not available times (Both doctors happen to have the same populated schedule for this excercise)
    self.appointment_list = [
      {'val': 1, 'time': "09:00", 'available': False, 'patient': 'Tom'}, 
      {'val': 2, 'time': "09:30", 'available': True, 'patient': ''},
      {'val': 3, 'time': "10:00", 'available': False, 'patient': 'John'},
      {'val': 4, 'time': "10:30", 'available': False, 'patient': 'Martin'},
      {'val': 5, 'time': "11:00", 'available': True, 'patient': ''},
      {'val': 6, 'time': "11:30", 'available': True, 'patient': ''},
      {'val': 7, 'time': "12:00", 'available': True, 'patient': ''},
      {'val': 8, 'time': "12:30", 'available': False, 'patient': 'Joah'},
      {'val': 9, 'time': "13:00", 'available': False, 'patient': 'Ester'},
      {'val': 10, 'time': "13:30", 'available': True, 'patient': ''},
      {'val': 11, 'time': "14:00", 'available': False, 'patient': 'Sanri'},
      {'val': 12, 'time': "14:30", 'available': False, 'patient': 'Someone'},
      {'val': 13, 'time': "15:00", 'available': True, 'patient': ''},
    ]

  def check_available_appointments(self):
    """Iterate through the appointment_list, and return the available timeslots"""
    slots_available = []
    print("The available times are: ")
    for i in self.appointment_list:
      if i.get('available') == True:
        slots_available.append(i)
    return slots_available

  def return_appointments_by_name(self, patient):
    """Function returns the appointments for patients in arguments"""
    appointments = []
    for i in self.appointment_list:
      if i.get('patient') == patient:
        appointments.append(i)
    return appointments

  def add_appointment(self, patient, timeslot):
    """Function adds a new appointment to the appointment_list for the patient in arguments"""
    for i in self.appointment_list:
      if timeslot.get('val') == i.get('val'):
        i.update({'available': False, 'patient': patient})
    

  def cancel_appointment(self, appointment):
    """Function cancels an appointment made - called by a patient"""
    for i in self.appointment_list:
      if appointment.get('val') == i.get('val'):
        i.update({'available': True, 'patient': ''})

  def view_schedule(self):
    """Function returns a list of ALL appointments"""
    for i in self.appointment_list:
      if i.get('available') == True:
        print("{}: ________________ ").format(i.get('time'))
      else:
        print("{}: {}").format(i.get('time'), i.get('patient'))
