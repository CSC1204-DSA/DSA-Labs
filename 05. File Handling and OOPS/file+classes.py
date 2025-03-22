# Define a Student class to manage basic student information and course enrollment
class Student:
    def __init__(self, first, last, courses=None):
        """
        Initialize a new Student instance.

        Parameters:
            first (str): Student's first name.
            last (str): Student's last name.
            courses (list, optional): List of courses the student is enrolled in.
                                      Defaults to an empty list if not provided.
        """
        self.first_name = first
        self.last_name = last
        # If no course list is provided, initialize an empty list
        if courses is None:
            self.courses = []
        else:
            self.courses = courses

    def add_course(self, course):
        """
        Add a course to the student's course list if not already enrolled.

        Parameters:
            course (str): The course name to be added.
        """
        if course not in self.courses:
            self.courses.append(course)
        else:
            # Inform the user if the course is already in the course list
            print(f"{self.first_name} is already enrolled in the {course} course")

    def remove_course(self, course):
        """
        Remove a course from the student's course list if it exists.

        Parameters:
            course (str): The course name to be removed.
        """
        if course in self.courses:
            self.courses.remove(course)
        else:
            # Inform the user if the course is not found in the list
            print(f"{course} not found")

    def find_in_file(self, filename):
        """
        Check if the student's record exists in a file.

        The file is expected to have records in the format:
            "first,last:course1,course2,..."

        Parameters:
            filename (str): Path to the file containing student records.

        Returns:
            bool: True if the student record is found, otherwise False.
        """
        with open(filename) as f:
            for line in f:
                # Prepare the record from each line in the file
                first_name, last_name, course_details = Student.prep_record(line.strip())
                # Create a temporary Student object from the file record
                student_read_in = Student(first_name, last_name, course_details)
                # Compare the current student with the one from the file using __eq__
                if self == student_read_in:
                    return True
            return False

    def add_to_file(self, filename):
        """
        Add the student's record to the file if it does not already exist.

        Parameters:
            filename (str): Path to the file where student records are stored.

        Returns:
            str: A message indicating whether the record was added or already exists.
        """
        if self.find_in_file(filename):
            return "Record already exists"
        else:
            # Prepare a string record for the student in the required format
            record_to_add = Student.prep_to_write(self.first_name, self.last_name, self.courses)
            with open(filename, "a+") as to_write:
                # Write the record with a newline at the end
                to_write.write(record_to_add + "\n")
            return "Record added"

    @staticmethod
    def prep_record(line):
        """
        Parse a line from the file to extract student data.

        Parameters:
            line (str): A record string in the format "first,last:course1,course2,...".

        Returns:
            tuple: A tuple containing first name, last name, and a list of courses.
        """
        # Split the line into name and course details using ':' as the separator
        line = line.split(":")
        # Extract first and last name from the name section (separated by a comma)
        first_name, last_name = line[0].split(",")
        # Get the list of courses; strip any extra whitespace and split by commas
        course_details = line[1].rstrip().split(",")
        return first_name, last_name, course_details

    @staticmethod
    def prep_to_write(first_name, last_name, courses):
        """
        Prepare a formatted string for writing a student's record to a file.

        Parameters:
            first_name (str): Student's first name.
            last_name (str): Student's last name.
            courses (list): List of courses.

        Returns:
            str: A string formatted as "first,last:course1,course2,..."
        """
        # Concatenate first and last name separated by a comma
        full_name = first_name + ',' + last_name
        # Join the courses into a single string separated by commas
        courses = ",".join(courses)
        return full_name + ':' + courses

    def __eq__(self, other):
        """
        Check if two Student instances are equal based on first and last names.

        Parameters:
            other (Student): Another student instance to compare with.

        Returns:
            bool: True if both have the same first and last name, else False.
        """
        return self.first_name == other.first_name and self.last_name == other.last_name

    def __len__(self):
        """
        Return the number of courses the student is enrolled in.

        Returns:
            int: The count of courses.
        """
        return len(self.courses)

    def __repr__(self):
        """
        Return the official string representation of the Student instance.

        This representation is useful for debugging.

        Returns:
            str: A string that represents the student object.
        """
        return f"Student('{self.first_name}','{self.last_name}',{self.courses})"

    def __str__(self):
        """
        Return a user-friendly string representation of the student.

        Returns:
            str: Formatted details of the student including capitalized names and courses.
        """
        # Capitalize the first and last name and each course for display
        return (
            f"First name: {self.first_name.capitalize()}\n"
            f"Last name: {self.last_name.capitalize()}\n"
            f"Courses: {', '.join(map(str.capitalize, self.courses))}"
        )


# Define a StudentAthlete class that inherits from Student and adds a sport attribute
class StudentAthlete(Student):
    def __init__(self, first, last, courses=None, sport=None):
        """
        Initialize a new StudentAthlete instance.

        Parameters:
            first (str): Athlete's first name.
            last (str): Athlete's last name.
            courses (list, optional): List of courses the athlete is enrolled in.
                                      Defaults to an empty list if not provided.
            sport (str, optional): The sport the athlete participates in.
        """
        # Initialize the base Student attributes
        super().__init__(first, last, courses)
        # Add the sport attribute for the athlete
        self.sport = sport


# Example usage:

# Create a list of courses
courses = ["python", "ruby", "javascript"]

# Create a StudentAthlete instance with the given name, courses, and sport
jane = StudentAthlete("jane", "doe", courses, "hockey")

# Print the sport associated with the student athlete
print(jane.sport)

# Check if 'jane' is an instance of the Student class (True because StudentAthlete inherits from Student)
print(isinstance(jane, Student))
