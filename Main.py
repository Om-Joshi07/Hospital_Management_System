

# Imports
from Admin import Admin
from Doctor import Doctor
from Patient import Patient

def main():
    """
    the main function to be ran when the program runs
    """

    # Initialising the actors
    admin = Admin('admin','123','B1 1AB') # username is 'admin', password is '123'
    doctors = [Doctor('John','Smith','Internal Med.'), Doctor('Jone','Smith','Pediatrics'), Doctor('Jone','Carlos','Cardiology')]
    patients = [Patient('Sara','Smith', 20, '07012345678','B1 234', ['Fever', 'Cough'] ), Patient('Mike','Jones', 37,'07555551234','L2 2AB', ['Ache', 'Acne']), Patient('Daivd','Smith', 15, '07123456789','C1 ABC', ['Pox', 'Stones'])]
    discharged_patients = []

    # keep trying to login tell the login details are correct
    while True:
        if admin.login():
            running = True # allow the program to run
            break
        else:
            print('Incorrect username or password.')

    while running:
        # print the menu
        print('\nChoose the operation:')
        print(' 1- Register/View/Update/Delete Doctor')
        print(' 2- View/Discharge Patients')                # Added View in 2
        print(' 3- View discharged Patient')
        print(' 4- Assign Doctor to a Patient')
        print(' 5- Update Admin detais')
        print(' 6- View Patient-Doctor Assigned List')
        print(' 7- View Doctors list')        
        print(" 8- Store in File")
        print(" 9- Add Patient")
        print(" 10- Load Patient")
        print(" 11- Add Symptoms")
        print(" 12- Relocating Patients")
        print(" 13- View Patinet by Surname")
        print(" 14- Management Report")
        print(' 15- Quit')

        # get the option
        op = input('Option: ')

        if op == '1':
            # 1- Register/view/update/delete doctor
          
          admin.doctor_management(doctors)

        elif op == '2':
            # 2- View or discharge patients
            admin.view_patient(patients) 

            while True:
                try:
                    op = input('Do you want to discharge a patient(Y/N):').lower()
                    
                    if op == 'yes' or op == 'y':
                        admin.discharge(patients, discharged_patients)
                    
                    elif op == 'no' or op == 'n':
                        break

                    # unexpected entry
                    else:
                        print('Please answer by yes or no.')

                except ValueError:
                    print("The input is invalid")
        
        elif op == '3':
            # 3 - view discharged patients
            admin.view_discharge(discharged_patients)

        elif op == '4':
            # 4- Assign doctor to a patient
            admin.assign_doctor_to_patient(patients, doctors)

        elif op == '5':
            # 5- Update admin detais
            admin.update_admin_details()

        elif op == '6':
            admin.view_patient_doctor_assignment(patients)

        elif op == '7':
            admin.doctor_list(doctors)


        elif op == '8':
            admin.write_patients_to_file(patients, 'Patient.txt')

        elif op == '9':
            admin.add_patient(patients, 'Patient.txt' )

        elif op == '10':
            admin.load_patient_from_file('Patient.txt')

        elif op == '11':
            admin.add_symptons(patients)

        elif op == '12':
            admin.relocating_patients(patients, doctors)

        elif op == '13':
            admin.filtering_surnames(patients)

        elif op == '14':
            admin.management_report(patients, doctors)


        elif op == '15':
            # 6 - Quit
            break

        else:
            # the user did not enter an option that exists in the menu
            print('Invalid option. Try again')


if __name__ == '__main__':
    main()


