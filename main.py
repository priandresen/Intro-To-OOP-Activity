from school_schedule.student import Student
from school_schedule.high_school_student import HighSchoolStudent
from school_schedule.middle_school_student import MiddleSchoolStudent

from school_schedule.comparison import get_student_with_more_classes

# first instance
samara = Student( "Samara", "junior", [ "Pre-Calc", "English III", "World History", "Gym", "Chemistry", "Music Composition" ] )

samara.add_class("Painting")  # => [ "Pre-Calc", "English III", "World History", "Gym", "Chemistry", "Music Composition", "Painting" ]

samara.get_num_classes()  # => 7

samara.summary()  # => "Samara is a junior enrolled in 7 classes"

# second instance
claire = Student( "Claire", "freshman", [ "Algebra", "Writing", "Contemporary World Issues", "Gym", "Earth Science" ] )

claire.add_class("Painting")  # => [ "Algebra", "Writing", "Contemporary World Issues", "Gym", "Earth Science", "Painting" ]

claire.get_num_classes()  # => 6

claire.summary()  # => "Claire is a freshman enrolled in 6 classes"

# function
print(get_student_with_more_classes(claire, samara)) # => samara


quinn = Student(
                "Quinn", 
                "junior", 
                [
                    "Pre-Calc", 
                    "English III", 
                    "World History", 
                    "Gym", 
                    "Chemistry", 
                    "Music Composition"
                ]
            )

quinn.add_class("Painting")

# second instance
claire = HighSchoolStudent(
                "Claire", 
                "freshmen", 
                [
                    "Algebra", 
                    "Writing", 
                    "Contemporary Issues", 
                    "Gym", 
                    "Earth Science", 
                    "Painting"
                ],
                has_parking_privileges=True,
                clubs=["Algorithms Club"]
            )
# third instance

mikelle = MiddleSchoolStudent(
                "Mikelle", 
                "sophomore", 
                [
                    "Algebra", 
                    "Python", 
                    "Logic 101", 
                ],
                gets_transportation=True
            )

students = [quinn, claire, mikelle]
for student in students:
    print(student.summary())
