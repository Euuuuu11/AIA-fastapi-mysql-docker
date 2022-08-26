from app.models.grade import Grade

class GradeService(object):
    def __init__(self) -> None:
        self.grade = 0
    
    def set_grade(self, name, korean, english, math):
        grade = Grade(name, korean, english, math)
        avg = grade.set_avg()
        if avg >= 90 :
            grade = 'A'
        elif avg >= 80 :
            grade = 'B'
        elif avg >= 70 :
            grade = 'C'
        elif avg >= 60 :
            grade = 'D'
        elif avg >= 50 :
            grade = 'E'
        else :
            grade = 'F'
        self.grade = 0
    
    def get_grade(self, name, korean, english, math):
        self.set_grade(self, name, korean, english, math)
        return self.grade
        name, korean, english, math