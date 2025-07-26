

from Doctor import Doctor
from Patient import Patient
from Common import Person
import calendar
from matplotlib import pyplot as plt


class Admin(Person):
    """A class that deals with the Admin operations"""
    def __init__(self, username, password, address = ''):
        """
        Args:
            username (string): Username
            password (string): Password
            address (string, optional): Address Defaults to ''
        """

        self.__username = username
        self.__password = password
        self.__address =  address





    def view(self,a_list):
        """
        print a list
        Args:
            a_list (list): a list of printables
        """
        for index, item in enumerate(a_list):
            print(f'{index+1:3}|{item}')


    def login(self) :
        """
        A method that deals with the login
        Raises:
            Exception: returned when the username and the password ...
                    ... don`t match the data registered
        Returns:
            string: the username
        """

        print("-----Login-----")
        #Get the details of the admin

        username = input('Enter the username: ')
        password = input('Enter the password: ')

        try:
            if username == self.__username and password == self.__password:
                return True
        except:
            print('Invalid username or password. Try Again.')



    def find_index(self,index,doctors):
        
            # check that the doctor id exists          
        if index in range(0,len(doctors)):
            return True

        # if the id is not in the list of doctors
        else:
            return False
        
            
    def get_doctor_details(self) :
        """
        Get the details needed to add a doctor
        Returns:
            first name, surname and ...
                            ... the speciality of the doctor in that order.
        """
        #ToDo2
        # self.view()
        first_name = input("Enter the first name: ")
        surname = input("Enter the surname of the doctor: ")
        speciality = input("Enter the speciality of the doctor: ")

        return first_name, surname, speciality



    def doctor_management(self, doctors):
        """
        A method that deals with registering, viewing, updating, deleting doctors
        Args:
            doctors (list<Doctor>): the list of all the doctors names
        """

        print("-----Doctor Management-----")

        # menu
        print('Choose the operation:')
        print(' 1 - Register')
        print(' 2 - View')
        print(' 3 - Update')
        print(' 4 - Delete')

        #ToDo3
        # pass
        op = input("Enter the choice: ")

        # register
        if op == '1':
            print("-----Register-----")

            # get the doctor details
            print('Enter the doctor\'s details:')
            #ToDo4
            # pass
            while True:

                first_name, surname, speciality = self.get_doctor_details()

                # check if the name is already registered
                name_exists = False
                for doctor in doctors:
                    if first_name == doctor.get_first_name() and surname == doctor.get_surname():
                        print('Name already exists.')
                        name_exists = True
                        # save time and end the loop
                        break
                        # add the doctor ...
                                                             # ... to the list of doctors
                if not name_exists:
                    doctors.append(Doctor(first_name, surname, speciality))
                    print('Doctor registered.')
                    break


        # View
        elif op == '2':
            print("-----List of Doctors-----")
            print('ID |          Full Name           |  Speciality   ')
            self.view(doctors)



        # Update
        elif op == '3':
            while True:
                print("-----Update Doctor`s Details-----")
                print('ID |          Full name           |  Speciality')
                self.view(doctors)
                try:
                    index = int(input('Enter the ID of the doctor: ')) - 1
                    doctor_index = self.find_index(index,doctors)
                    if doctor_index != False:
                        break
                    else:
                        print("Doctor not found")

                    
                        # doctor_index is the ID mines one (-1)
                        

                except ValueError: # the entered id could not be changed into an int
                    print('The ID entered is incorrect')

            # menu
            print('Choose the field to be updated:')
            print(' 1 First name')
            print(' 2 Surname')
            print(' 3 Speciality')

            try:
                op = int(input('Enter the field to choice: ')) # make the user input lowercase

                if op == 1:
                    first_name = input("Enter the first name: ")
                    doctors[index].set_first_name(first_name)
                    print("Doctor's first name updated")
                elif op == 2:
                    surname = input("Enter the surname: ")
                    doctors[index].set_surname(surname)
                    print("Doctor's surname updated")
                elif op == 3:
                    speciality = input("Enter the speciality: ")
                    doctors[index].set_speciality(speciality)
                    print("Doctor's speciality updated")
                else:
                    print("Invalid choice")

            except ValueError:
                print("Please enter proper input")
                
            

        # Delete
        elif op == '4':
            print("-----Delete Doctor-----")
            print('ID |          Full Name           |  Speciality')
            self.view(doctors)

            try:
                doctor_index = int(input('Enter the ID of the doctor to be deleted: ')) - 1
                doctor_idx = self.find_index(doctor_index,doctors)
                if doctor_idx != False:
                    del doctors[doctor_index]
                    print("Doctor deleted")
                else:
                    print('The id entered is incorrect')
                    

            except ValueError:
                print("The id entered was not found")


        # if the id is not in the list of patients
        else:
            print('Invalid operation choosen. Check your spelling!')


    def view_patient(self, patients):
        """
        print a list of patients
        Args:
            patients (list<Patients>): list of all the active patients
        """
        print("-----View Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode | Symptoms ')
        self.view(patients)



    def assign_doctor_to_patient(self, patients, doctors):
        """
        Allow the admin to assign a doctor to a patient
        Args:
            patients (list<Patients>): the list of all the active patients
            doctors (list<Doctor>): the list of all the doctors
        """
        print("-----Assign Doctor to Patient-----")

        print("-----Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        self.view(patients)

        patient_index = input('Please enter the patient ID: ')

        try:
            # patient_index is the patient ID mines one (-1)
            patient_index = int(patient_index) -1

            # check if the id is not in the list of patients
            if patient_index not in range(len(patients)):
                print('The id entered was not found.')
                return # stop the procedures

        except ValueError: # the entered id could not be changed into an int
            print('The id entered is incorrect')
            return # stop the procedures

        
        print('Select the doctor that fits these symptoms:')
        s_imp = patients[patient_index].print_symptoms().split(", ") # print the patient symptoms
        for i in s_imp:
            print(i)

        print("-----Doctors-----")
        print('--------------------------------------------------')
        print('ID |          Full Name           |  Speciality   ')
        self.view(doctors)
        doctor_index = input('Please enter the doctor ID: ')

        try:
            # doctor_index is the patient ID mines one (-1)
            doctor_index = int(doctor_index) - 1

            # check if the id is in the list of doctors
            if self.find_index(doctor_index,doctors)!=False:
                    
                # link the patients to the doctor and vice versa
                #ToDo11 

                if patients[patient_index].get_doctor() != 'None':
                    print('The doctor is already assigned to this patient')
                else:
                    patients[patient_index].link(doctors[doctor_index].full_name())
                    doctors[doctor_index].add_patient(patients[patient_index])
                    print('The patient is now assigned to the doctor.')
                    self.view_patient(patients)

            # if the id is not in the list of doctors
            else:
                print('The id entered was not found.')

        except ValueError: # the entered id could not be changed into int type
            print('The id entered is incorrect')



    def discharge(self, patients, discharge_patients):
        """
        Allow the admin to discharge a patient when treatment is done
        Args:
            patients (list<Patients>): the list of all the active patients
            discharge_patients (list<Patients>): the list of all the non-active patients
        """


        # self.view(patients)
        print("-----Discharge Patient-----")

        try:
            if not patients:
                print("No patients left to discharge.")

            else:
                patient_index = input('Please enter the patient ID: ')
                patient_index = int(patient_index) - 1
                if patient_index >= 0 and patient_index <= len(patients):
                    discharge_patients.append(patients[patient_index])
                    print(f'The patient {patients[patient_index].full_name()} has been discharged.')
                    del patients[patient_index]
                    print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
                    self.view(patients)

                else:
                    print("Patient ID not found")

        except ValueError:
            print("Enter the valid input")

          
                


    def view_discharge(self, discharged_patients):
        """
        Prints the list of all discharged patients
        Args:
            discharge_patients (list<Patients>): the list of all the non-active patients
        """

        print("-----Discharged Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        
        # self.view_patient()
        self.view(discharged_patients)


    def update_admin_details(self):
        """
        Allows the user to update and change username, password and address
        """

        print('Choose the field to be updated')
        print('1- Username')
        print('2- Password')
        print('3- Address')


        try:
            op = int(input('Input the data you want to update: '))

            if op == 1:
                username = input("Enter the new username: ")
                # self.set_admin_username(username)
                self.__username = username

            elif op == 2:
                password = input('Enter the new password: ')
                # validate the password
                if password == input("Enter the new password again: "):
                    self.__password = password
                else:
                    print('Passwords do not match')
                    print('Try again')

            elif op == 3:
                #ToDo15
                address = input("Enter the new address: ")
                self.__address = address

            else:
                print("Enter the correct input.")

            self.view_admin_details()

        except ValueError:
            print("Invalid input.")



    def view_patient_doctor_assignment(self, patients):
        print("-----Doctor-Patient Assignments-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode | Symptoms ')
        self.view(patients)


    def doctor_list(self, doctors):
        print("-----Doctors List-----")
        print('ID |          Full Name           |  Speciality   ')
        self.view(doctors)


    def view_admin_details(self):
        print("-----Admin Details-----")
        print(f"Username: {self.__username}")
        print(f"Password: {self.__password}")
        print(f"Address: {self.__address}")


    def add_patient(self, patients, filename):
        first_name = input("Enter first name: ")
        surname = input("Enter last name: ")
        full_name = f"{first_name} {surname}"
        age = input("Enter age: ")
        mobile = input("Enter mobile: ")
        postcode = input("Enter postcode: ")
        patients.append(Patient(first_name, surname, age, mobile, postcode, symptoms=''))
        print(f"Patient {full_name} added successfully")
        self.write_patients_to_file(patients, filename)


    def write_patients_to_file(self, patients, filename):
        with open(filename, 'w') as f:
            f.write('ID            Full Name                  Doctor`s Full Name        Age      Mobile       Postcode ')
            f.write("\n" + "-" * 111)
            for index, patient in enumerate(patients):
                f.write(f"\n\n\n{index+1} {str(patient)}")
                # f.write("\n" + "-"*30 + "\n")  # Add a separator between each patient record


    def load_patient_from_file(self, filename):
        try:
            temp_lst = []
            with open(filename, 'r') as g:
                lines = g.readlines()
                lines = lines[4:]
                for line in lines:
                    line = line.strip()
                    if line:
                        temp_lst.append(line)

            print('ID            Full Name                  Doctor`s Full Name      Age      Mobile       Postcode      Symptoms ')
            print("-" * 96)
            for i in temp_lst:
                print(i)

        except FileNotFoundError:
            print(f"Error: The file was not found.")



    def add_symptons(self, patients):
        self.view_patient(patients)
        index = int(input("Enter the index of patient: "))
        index -= 1

        if 0 <= index < len(patients):
            sym = input("Enter the symptoms(sepearated with commase): ")
            patients[index].add_symptoms(sym)
            print("Symptoms added successfully.")
        else:
            print("Invalid index")

    
    def relocating_patients(self, patients, doctors):
        print("-----Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode | Symptoms ')
        self.view(patients)
        p_idx = int(input("Enter the id of the patient whom you want to relocate: ")) - 1
        print("-----Doctors-----")
        print('ID |          Full name           |  Speciality')
        self.view(doctors)
        d_idx = int(input("Enter the id of the doctor: ")) - 1
        print(f"{patients[p_idx].full_name()} is relocated to {doctors[d_idx].full_name()}")
        patients[p_idx].link(doctors[d_idx].full_name())


    def filtering_surnames(self, patients):
        print("-----Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode | Symptoms ')
        self.view(patients)

        self.T_surname = input("Enter the surname: ").capitalize()
        print((f"-----{self.T_surname}-----"))
        for i in patients:
            if self.T_surname in i.get_surname().capitalize():
                print(i.full_name())





    def management_report(self, patients, doctors):
        print("-----Management Report-----")
        print("1- Total number of doctors")
        print("2- Total number of patients per doctor")
        print("3- Total number of appointments per month per doctor")
        print("4- Total number of patients based on illness type")

        op = input("Enter the choice: ")

        if op == '1':
            num_doctors = len(doctors)

            fig_size = (6, 4)  

            print(f"Total number of doctors: {num_doctors}")
            # plt.figure(figsize=fig_size)
            plt.bar(['Doctors'], [num_doctors], color= 'orange')  

            plt.title('Total Number of Doctors', fontsize=14, fontweight='bold')
            plt.xlabel('Doctors', fontsize=12)
            plt.ylabel('Count', fontsize=12)

            plt.show()

        elif op == '2':
            patients_per_doctor = len(patients) / len(doctors)

            result = f"{patients_per_doctor:.2f}"  # Formatting the result to 2 decimal places
            print(f"Total number of patients per doctor: {result}")

            plt.figure(figsize=(6, 4))
            plt.bar(['Patients per Doctor'], [patients_per_doctor], color='purple')
            plt.title('Total Number of Patients per Doctor')
            plt.xlabel('Doctors')
            plt.ylabel('Average Patients per Doctor')

            plt.show()

        elif op == '3':

            count = {}  # Store total appointments per month for the selected doctor
            print("-----Doctors-----")
            print('ID |          Full name           |  Speciality')
            self.view(doctors)  # Display doctors list

            DR_index = int(input("Enter the index of the doctor: ")) -1 

            if 0 <= DR_index < len(doctors):  
                doctor = doctors[DR_index] 
                Dr_name = doctor.full_name()   

                # Initialize all 12 months with 0 appointments
                count = {calendar.month_name[i]: 0 for i in range(1, 13)}

                for appointment in doctor.get_appointments():
                    if appointment["doctor"] == Dr_name:  
                        month_num = int(appointment["date"].split("-")[1])  
                        month_name = calendar.month_name[month_num]   
                        count[month_name] += 1      # For increasing the No. of appointment of that month

                print(f"\nAppointments for Dr. {Dr_name}:")
                for month, total in count.items():
                    print(f"{month}: {total} appointments")
                    

                empty_months = [month for month, total in count.items() if total == 0]
                if empty_months:
                    print("\nMonths with NO appointments:")
                    print(", ".join(empty_months))
                else:
                    print("\nDoctor has appointments in all months.")

                plt.figure(figsize=(8, 6))

                # Removing months with zero appointments from the chart
                non_empty_months = [month for month, total in count.items() if total > 0]
                non_empty_values = [total for total in count.values() if total > 0]
 
                plt.pie(non_empty_values, labels=non_empty_months, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
                plt.title(f'Appointment Distribution for Dr. {Dr_name}')
                plt.show()

        elif op == '4':
            symptom_counts = {}     
            for patient in patients:
                symptoms_str = patient.print_symptoms()  # Returns a string of symptoms or "None"
                if symptoms_str != "None":
                    # Split the symptoms if there are multiple and count each one
                    symptom_list = [sym.strip() for sym in symptoms_str.split(",")]
                    for sym in symptom_list:
                        symptom_counts[sym] = symptom_counts.get(sym, 0) + 1

            print("\nTotal number of patients based on the illness type:")
            for symptom, count_value in symptom_counts.items():
                print(f"{symptom}: {count_value} patients")

            # Pie Chart for Illness Type Distribution (All Types)
            plt.figure(figsize=(8, 6))
            illnesses = list(symptom_counts.keys())
            patient_counts = list(symptom_counts.values())
            plt.pie(patient_counts, labels=illnesses, autopct='%1.1f%%',)

            plt.title('Patient Based on Illness Type')
            plt.show()
        
        else:
            print("\nInvalid option. Please choose a valid option from the menu.\n")

