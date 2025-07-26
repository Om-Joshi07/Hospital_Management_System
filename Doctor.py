

from Common import Person

class Doctor(Person):
    """A class that deals with the Doctor operations"""

    def __init__(self, first_name, surname, speciality):
        """
        Args:
            first_name (string): First name
            surname (string): Surname
            speciality (string): Doctor`s speciality
        """
        super().__init__(first_name, surname)
        self.__speciality = speciality
        self.__patients = []
        self.__appointments = [
            {"doctor": "Jone Smith" ,"date": "2024-01-15"},
            {"doctor": "John Smith" ,"date": "2024-01-28"},
            {"doctor": "John Smith" ,"date": "2024-02-15"},
            {"doctor": "Jone Carlos" ,"date": "2024-03-15"},
            {"doctor": "John Smith" ,"date": "2024-04-15"},
            {"doctor": "John Smith" ,"date": "2024-05-15"},
            {"doctor": "Jone Smith" ,"date": "2024-06-28"},
            {"doctor": "Jone Carlos" ,"date": "2024-07-7"},
            {"doctor": "John Smith" ,"date": "2024-07-9"},
            {"doctor": "Jone Carlos" ,"date": "2024-07-11"},
            {"doctor": "Jone Smith" ,"date": "2024-07-17"},
            {"doctor": "John Smith" ,"date": "2024-07-28"},
            {"doctor": "Jone Smith" ,"date": "2024-08-15"},
            {"doctor": "Jone Smith" ,"date": "2024-09-28"},
            {"doctor": "Jone Carlos" ,"date": "2024-10-15"},
            {"doctor": "Jone Carlos" ,"date": "2024-11-28"},
            {"doctor": "Jone Smith" ,"date": "2024-12-15"}
        ]

    
    def full_name(self) :
        return f"{self.get_first_name()} {self.get_surname()}"

    def get_speciality(self) :
        return self.__speciality

    def set_speciality(self, new_speciality):
        self.__speciality = new_speciality
        return self.__speciality
    
    def add_patient(self, patient):
        self.__patients.append(patient)

    def get_appoinment_count(self):
        return len(self.__appointments)
    
    def get_appointments(self):
        return self.__appointments

    def __str__(self) :
        return f'{self.full_name():^30}|{self.get_speciality():^15}'
