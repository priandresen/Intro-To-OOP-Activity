# add your get_student_with_more_classes function here!
def get_student_with_more_classes(student_1, student_2):
    num_1 = student_1.get_num_classes()
    num_2 = student_2.get_num_classes()

    if num_1 > num_2:
        return student_1.name
    
    return student_2.name