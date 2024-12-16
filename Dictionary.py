class CourseDictionary:
    def __init__(self):
        self.room_number_dictionary = {
            "CSC101": "3004",
            "CSC102": "4501",
            "CSC103": "6755",
            "NET110": "1244",
            "COM241": "1411",
            }

        self.instructor_dictionary = {
            "CSC101": "Haynes",
            "CSC102": "Alvarado",
            "CSC103": "Rich",
            "NET110": "Burke",
            "COM241": "Lee",
            }

        self.meeting_time_dictionary = {
            "CSC101": "8:00 a.m.",
            "CSC102": "9:00 a.m.",
            "CSC103": "10:00 a.m.",
            "NET110": "11:00 a.m.",
            "COM241": "1:00 p.m.",
            }

    def print_course_information(self, course_number):        
        if course_number not in self.room_number_dictionary or course_number not in self.instructor_dictionary or course_number not in self.meeting_time_dictionary:
            print('{: ^100}'.format(f"Course Number: {course_number} information is missing from our records."))
            print('{: ^100}'.format("__________"))
            return
            
        print('{: ^100}'.format(f"Course Number: {course_number}"))
        print('{: ^100}'.format(f"Course Room: {self.room_number_dictionary[course_number]}"))
        print('{: ^100}'.format(f"Course Instructor: {self.instructor_dictionary[course_number]}"))
        print('{: ^100}'.format(f"Course Meeting Time: {self.meeting_time_dictionary[course_number]}"))
        print('{: ^100}'.format("__________"))



# Initialize the course dictionary.
course_dictionary = CourseDictionary()

while(True):
    course_number = input("Enter the course number you want information for? \n")
    course_dictionary.print_course_information(course_number)
    choice = input("Enter Y to continue Or anything else to Quit.\n")
    if choice != 'Y':
        break;
            
