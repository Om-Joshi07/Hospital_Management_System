

from Common import Person


class Patient(Person):
    """Patient class"""

    def __init__(self, first_name, surname, age, mobile, postcode, symptoms):
        """
        Args:
            first_name (string): First name
            surname (string): Surname
            age (int): Age
            mobile (string): the mobile number
            address (string): address
        """
        super().__init__(first_name, surname)
        self.__age = age
        self.__mobile = mobile
        self.__postcode = postcode
        self.__symptoms = []


        self.__doctor = 'None'


    def full_name(self) :
        """full name is first_name and surname"""
        return f"{self.get_first_name()} {self.get_surname()}"

    def get_doctor(self) :
        return self.__doctor
    
    def get_age(self):
        return self.__age
    
    def get_mobile(self):
        return self.__mobile
    
    def get_postcode(self):
        return self.__postcode

    def link(self, doctor):
        """Args: doctor(string): the doctor full name"""
        self.__doctor = doctor

    def add_symptoms(self, symptom):
        if symptom:
            return self.__symptoms.append(symptom)
        return "None"

    def print_symptoms(self):
        """prints all the symptoms"""
        return ", ".join(self.__symptoms) if self.__symptoms else "None"

    def __str__(self):
        return f'{self.full_name():^30}|{self.__doctor:^30}|{self.__age:^5}|{self.__mobile:^15}|{self.__postcode:^10}|{self.print_symptoms():^10}'



