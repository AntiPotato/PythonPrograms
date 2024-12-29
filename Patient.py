
# Patient class to hold patient data.
class Patient:
    
    # Parameterized constructor to create a patient.
    def __init__(self, firstName: str, lastName: str, dob: str):
        self.firstName = firstName
        self.lastName = lastName
        self.dob = dob

    # Less than comparison override to help with sorting patient object.
    def __lt__(self, other):
        
        # First compare last names.
        if self.lastName < other.lastName:
            return True
        if self.lastName > other.lastName:
            return False

        # Then compare first names.
        if self.firstName < other.firstName:
            return True
        if self.firstName > other.firstName:
            return False

        # Then compare dob.
        return self.dob < other.dob

    # to String override to help print patient object.
    def __str__(self):
        return f'Patient with name: {self.lastName},{self.firstName} and dob: {self.dob}'


# Sorter class to hold sorting methods.
class Sorter:

    # Parameterized constructor to create a sorter object to help with sorting.
    def __init__(self, patients):
        self.patients = patients

    # Internal function to help with swapping two patients.
    def __swap__(self, first_index, second_index):
        patient = self.patients[first_index]
        self.patients[first_index] = self.patients[second_index]
        self.patients[second_index] = patient

    # Internal merge function to help merge two sections of patients by start, end indexes.
    def __merge__(self, first_start, first_end, second_start, second_end):
        result_list = []

        i = first_start
        j = second_start

        # Compare both the lists from left to right until there any one of the list runs out.
        while i <= first_end and j <= second_end:
            if self.patients[i] < self.patients[j]:
                result_list.append(self.patients[i])
                i = i + 1
            else:
                result_list.append(self.patients[j])
                j = j + 1

        # Copy the remaining of the first list if that did not run out.      
        while i <= first_end:
            result_list.append(self.patients[i])
            i = i + 1

        # Copy the remaining of the second list if that did not run out. 
        while j <= second_end:
            result_list.append(self.patients[j])
            j = j + 1

        return result_list
                

    # Internal merge sort function to help with sorting patients within the left and right indexes.
    def __merge_sort__(self, left, right):
        if left >= right:
            return

        # Find mid.
        mid = int((left + right) / 2)

        # Sort left side.
        self.__merge_sort__(left, mid)

        # Sort right side.
        self.__merge_sort__(mid + 1, right)

        # Merge the sorted sections.
        result_list = self.__merge__(left, mid, mid + 1, right)

        # Copy the sorted list into the section of the patients that was sent for sorting.
        for i in range(left, right + 1):
            self.patients[i] = result_list.pop(0)


    # Merge sort function to help with merge sort.
    def merge_sort(self):
        print("\nPatients before merge sort:\n")
        self.print_patients()
        
        self.__merge_sort__(left = 0, right = len(self.patients) - 1)

        print("\nPatients after merge sort:\n")
        self.print_patients()
        

    # Bubble sort function.
    def bubble_sort(self):
        print("\nPatients before bubble sort:\n")
        self.print_patients()

        # Iterate all elemets but the last.
        for i in range(len(self.patients) - 1):

            # Iterate all elements right to the index i.
            for j in range(i+1, len(self.patients)):
                
                # Compare patients and swap if needed.
                if self.patients[j] < self.patients[i]:
                    self.__swap__(i, j)
                    
        print("\nPatients after bubble sort:\n")
        self.print_patients()

    # Function to help print patients.
    def print_patients(self):
        for patient in self.patients:
            print(patient)

# Take a patients list.
patients = []
choice = 'Y'

# Prompt user to enter patient data.
while(choice != 'N'):
    patient = Patient(input("Enter patient last name: "), input("Enter patient first name: "), input("Enter patient date of birth: "))
    patients.append(patient)
    choice = input("Enter N to stop entering more patients or anything else to continue: ")

merge_sorter = Sorter(patients.copy())
bubble_sorter = Sorter(patients.copy())
merge_sorter.merge_sort()
bubble_sorter.bubble_sort()



        
