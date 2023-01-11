from weakref import WeakKeyDictionary

class Homework:
    def __init__(self):
        self._grade = 0

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self,value):
        if not(0<=value<=100):
            raise ValueError('ocena musi być wartością z zakresu 0 - 100')
        self._grade = value

gal = Homework()
gal.grade = 95
assert gal.grade == 95

class Exam:
    def __init__(self):
        self._writing_grade = 0
        self._math_grade = 0

    @staticmethod
    def _check_grade(value):
        if not (0 <= value <= 100):
            raise ValueError('ocena musi być wartością z zakresu 0 - 100')

    @property
    def writing_grade(self):
        return self._writing_grade

    @writing_grade.setter
    def writing_grade(self,value):
        self._check_grade(value)
        self._writing_grade = value

    @property
    def math_grade(self):
        return self._math_grade

    @math_grade.setter
    def math_grade(self, value):
        self._check_grade(value)
        self._math_grade = value


st = Exam()
st.writing_grade = 67
st.math_grade = 54

assert st.writing_grade == 67
assert st.math_grade == 54

class Grade:
    def __init__(self):
        self._value = 0

    def __get__(self,instance,instance_type):
        return self._value

    def __set__(self, instance, value):
        if not (0 <= value <= 100):
            raise ValueError('ocena musi być wartością z zakresu 0 - 100')
        self._value = value

class Exam:
    math_grade = Grade()
    writing_grade = Grade()
    science_grade = Grade()

f_exam = Exam()

f_exam.writing_grade = 82
f_exam.math_grade = 99
f_exam.science_grade = 76
print(f'recenzja: {f_exam.writing_grade}')
print(f'obliczenia: {f_exam.math_grade}')
print(f'analiza naukowa: {f_exam.science_grade}')

s_exam = Exam()

s_exam.math_grade = 22
print(f'pierwszy egzamin - obliczenia: {f_exam.math_grade}')
print(f'drugi egzamin - obliczenia: {s_exam.math_grade}')


class NewGrade:
    def __init__(self):
        self._values = WeakKeyDictionary()

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return  self._values.get(instance,0)

    def __set__(self, instance, value):
        if not (0 <= value <= 100):
            raise ValueError('ocena musi być wartością z zakresu 0 - 100')
        self._values[instance] = value


class Exam:
    math_grade = NewGrade()
    writing_grade = NewGrade()
    science_grade = NewGrade()


f_exam = Exam()

f_exam.writing_grade = 82
f_exam.math_grade = 99
f_exam.science_grade = 76
print(f'recenzja: {f_exam.writing_grade}')
print(f'obliczenia: {f_exam.math_grade}')
print(f'analiza naukowa: {f_exam.science_grade}')

s_exam = Exam()

s_exam.math_grade = 22
print(f'pierwszy egzamin - obliczenia: {f_exam.math_grade}')
print(f'drugi egzamin - obliczenia: {s_exam.math_grade}')
