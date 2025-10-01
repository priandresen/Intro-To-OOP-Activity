from school_schedule.student import Student

def test_student_initialization():

    #Arrange
    name = "Mikelle"
    grade = "freshman"
    classes = ["Math", "Python", "Photography"]

    #Act

    student = Student(name, grade, classes)

    #Assert

    assert student.name == name
    assert student.grade == grade
    assert student.classes == classes

def test_add_class_adds_to_classes_list(): 
    # Arrange
    student = Student("Mikelle","freshman",["Math", "Python", "Photography"])


    #Act
    result = student.add_class("Spelling")

    #Assert
    assert student.classes == result
    assert len(student.classes) == 4
    assert "Spelling" in student.classes

def test_get_num_classes_returns_correct_num_of_classes():
    #Arrange
    student = Student("Mikelle","freshman",["Math", "Python", "Photography"])

    #Act
    result = student.get_num_classes()

    #Assert
    assert result == 3

def test_display_classes_displays_corrects_classes():
    #Arrange
    student = Student("Mikelle","freshman",["Math", "Python", "Photography"])

    #Act
    result = student.display_classes()

    #Assert
    assert result == "Math, Python, Photography"

