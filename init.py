# Entry point for the system
import patient, prescription, helper, appointment_schedule, receptionist
import healthcare_professionals

# Global variables
patients = []
doctors = []
prescription_list = []
patient_num = 1

app_schedule1 = appointment_schedule.Appointment_Schedule()

#Create 2 doctors to populate the list
doc1 = healthcare_professionals.Doctor("Dr. Watson", "221B", app_schedule1)
doctors.append({'val': 1, 'doc': doc1})
doc2 = healthcare_professionals.Doctor("Dr. Strange", "222A", app_schedule1)
doctors.append({'val': 2, 'doc': doc2})

#Populate a few patients
user1 = patient.Patient("Sherlock", "221B Baker Street", "0827493518", doc1)
patients.append({'val': 1, 'patient': user1})
user2 = patient.Patient("Sinbad", "The Sky", "998877665", doc2)
patients.append({'val': 2, 'patient': user2})

#Populate a few prescriptions for patient 1
med1 = prescription.Prescription("Panado", user1, 4, 10.5, doc1)
user1.prescription_list.append({'val': 1, 'med': med1})
med2 = prescription.Prescription("Corenza", user1, 2, 12.5, doc1)
user1.prescription_list.append({'val': 2, 'med': med2})
med3 = prescription.Prescription("ACC", user1, 4, 12.5, doc1)
user1.prescription_list.append({'val': 3, 'med': med3})

#Populate a prescription for patient 2
med3 = prescription.Prescription("Panado", user2, 10, 10.5, doc2)
user2.prescription_list.append({'val': 1, 'med': med3})

#Populate a receptionist
reception = receptionist.Receptionist("Haley", "123456")

print('''
Welcome to the Doctor's Office
______________________________''')

def main_menu():
  """The entry point to the system"""
  print('''
Please enter your role and hit ENTER:

1: Register New Patient
2: Existing Patient Login
3: Healthcare Professional Login

''')
  
  user = helper.check_input_int()

  # 1: Register New Patient
  if user == 1:

    name = str(raw_input("Please enter your name: ")) # WHY ARE WE in PYTHON 2?? Have to use raw_input instead of input...
    address = str(raw_input("Please enter your address: "))
    phone = str(raw_input("Please enter your phone number: "))

    print("Please choose your doctor which wish to be registered with. ")
    for doc in doctors:
      print("{}: {}").format(doc.get('val'), doc.get('doc').name)
    doctor = helper.check_input_int()
    selected_doctor = ''
    for i in doctors:
      if doctor == i.get('val'):
        #if doctor <= len(doctors):
        selected_doctor = i.get('doc')
        print("Selected doc: {}").format(i.get('doc').name)
        if len(selected_doctor.print_patients(patients)) <= 500: # Check if doctor has less than 500 patients registered with him/her
          new_patient = patient.Patient(name,address,phone,selected_doctor)
          patients.append({'val': len(patients) + 1, 'patient': new_patient})
          print("New patient: {}").format(patients[len(patients)-1].get('patient').name)
          helper.line_end()
          main_menu()
        else:
          print("Sorry, this doctor has no more capacity for patients, please select a different doctor")
          main_menu()
    helper.line_end()
    print("Invalid input")
    main_menu()




# 2: Login Existing Patient

  elif user == 2:
    print("Please select your name from the list: ")
    for p in patients:
      print("{}: {}").format(p.get('val'), p.get('patient').name)
    print("")
    choice = helper.check_input_int()
    if choice <= len(patients):
      for pat in patients:
        if choice == pat.get('val'):
          active_patient = pat.get('patient')
          helper.line_end()
          #print(active_patient)
          patient_options(active_patient)
    else:
      print("")
      print("Invalid entry, please try again. Just enter the number associated to the patient name.")
      main_menu()

# 3: Doctor Login

  elif user == 3:
    helper.line_end()
    print("Please select your name from the list: ")
    for doc in doctors:
      print("{}: {}").format(doc.get('val'),doc.get('doc').name)
    print("")
    choice = helper.check_input_int()
    if choice > 0 & choice <= len(doctors):
      for d in doctors:
        if choice == d.get('val'):
          active_doctor = d.get('doc')
          helper.line_end()
          print("Welcome {}").format(active_doctor.name)
          helper.line_end()
          doctor_options(active_doctor)
      main_menu()
    else:
      print("")
      print("Invalid entry, please try again. Just enter the number associated to your name.")
      main_menu()

  else:
    print("")
    print("Invalid input. Please try again")
    main_menu()


def patient_options(patient):
  print('''
Please select an option:

1. View active prescriptions
2. Make an appointment
3. Cancel appointment
4. Exit
  ''')
  prescription_choice = helper.check_input_int()
  helper.line_end()
  if prescription_choice == 1:
    if patient.prescription_list:
      for i in patient.prescription_list:
        print("{}: {} - Repeat prescriptions left: {}").format(i.get('val'), i.get('med').type, i.get('med').quantity)
      option = helper.check_input_int()
      if option <= len(patient.prescription_list):
        for j in patient.prescription_list:
          if option == j.get('val'):
            if j.get('med').quantity != 0:
              j.get('med').quantity -= 1
              print("{} ordered").format(j.get('med').type)
              print("")
              print("You have {} repeats of {} left").format(j.get('med').quantity, j.get('med').type)
              print("")
              helper.line_end()
              patient_options(patient)
            elif j.get('med').quantity == 0:
              print("No more {} left, please see your doctor. {}").format(j.get('med').type, patient.doctor)
              patient_options(patient)
      else:
        print("")
        print("Invalid number entered")
        helper.line_end()
        patient_options(patient)
    else:
      print("You have no active prescriptions")
      helper.line_end()
      patient_options(patient)
  
  #Make an appointment
  elif prescription_choice == 2:
    available = patient.doctor.app_schedule.check_available_appointments()
    for i in available:
      print("{}: {}").format(i.get('val'), i.get('time'))
    timeslot = helper.check_input_int()
    helper.line_end()
    for j in available:
      if timeslot == j.get('val'):
        patient.request_appointment(j, reception)
        print("Your appointment time is booked for {}").format(j.get('time'))
        patient_options(patient)
    print("")
    print("Invalid input")
    patient_options(patient)
  
  # Cancel appointment
  elif prescription_choice == 3:
    appointments = patient.doctor.app_schedule.return_appointments_by_name(patient.name)
    if appointments:
      print('You have appointment/s for: ')
      for i in appointments:
        print("{}: {}").format(i.get('val'), i.get('time'))
      print("Enter the number for the appointment you wish to cancel")
      chosen = helper.check_input_int()
      for i in appointments:
        if chosen == i.get('val'):
          reception.cancel_appointment(patient.doctor, i)
          helper.line_end()
          print("Appointment cancelled")
          helper.line_end()
          patient_options(patient)
      print("Invalid option")
      patient_options(patient)
    else:
      print("You have no appointments booked currently")
      helper.line_end()
      patient_options(patient)
      
      

  # Exit
  elif prescription_choice == 4:
    main_menu()
  
  else: 
    print("")
    print("Invalid option, please try again")
    helper.line_end()
    patient_options(patient)


def doctor_options(doctor):
  print('''
Please select an option:

1. View schedule
2. Issue Prescription
3. Exit
  ''')
  doctor_choice = helper.check_input_int()
  helper.line_end()

# View Schedule
  if doctor_choice == 1:
    doctor.app_schedule.view_schedule()
    helper.line_end()
    doctor_options(doctor)

# Issue a prescription
  elif doctor_choice == 2:
    print("Please select your patient you want to issue a prescription for: ")
    patient_list = []
    for p in patients:
      patient_list.append(p)
    list_patients = doctor.print_patients(patient_list)
    for pat in list_patients:
      print("{}: {}").format(pat.get('val'), pat.get('patient').name)
    choice = helper.check_input_int()
    helper.line_end()
    for i in list_patients:
      if choice == int(i.get('val')):
        doctor.issue_prescription(i.get('patient'))
        doctor_options(doctor)

    print("")
    print("Invalid option, please try again")
    helper.line_end()
    doctor_options(doctor)

  elif doctor_choice == 3:
    main_menu()

  else:
    print("")
    print("Invalid option")
    main_menu()      

main_menu()
  
