# lib/app.py
def filter_moringa_names(names):
    moringa_students = ("Alice", "David", "Eve")
    moringa_students_list = (name for name in names if name in moringa_students)
    return moringa_students_list

names_list = ("Alice", "Eve", "John", "David", "Jane")

moringa_students_list = filter_moringa_names(names_list)
print("Moringa School Students:", moringa_students_list)
