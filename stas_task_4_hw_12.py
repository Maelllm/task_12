class Students:

    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age

    def favorite_lesson(self, value):
        self.favorite_lesson = value

    def student_local(self):  # Add attributes and custom method to local scope of our new method
        age = self.age
        name = self.name
        favorite_lesson = self.favorite_lesson
        l = locals()
        return l


student_1 = Students(name='Alex', age=21)
student_1.favorite_lesson('math')
print(student_1.student_local())
