# Create your classes here
class Student:
    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address

class Question:
    def __init__(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer
    def ask_and_evaluate(self):
        answer = input(self.question)
        if answer == self.correct_answer:
            return True
        else:
            return False


class Exam:
    
    def __init__(self, name):
        self.name = name
        self.questions=[]

    def add_question(self, question):
        self.questions.append(question)

    def administer(self):
        score = 0
        total = 0
        for q in self.questions:
            if q.ask_and_evaluate():
                score += 1 
            total += 1
        return score / total

class StudentExam:
    def __init__(self, student, exam):
        self.student = student
        self.exam =  exam
        self.score = 0
    def take_test(self):
        result = self.exam.administer()
        print(result)
        self.score = result

class Quiz(Exam):
    def administer(self):
        score = super().administer()
        if score >= 0.5:
            return 1
        else:
            return 0
        
class StudentQuiz(StudentExam):
    pass
        
def example():
    quiz = Quiz("quiz")
    set_q = Question(
        'What is the method for adding an element to a set?',
        '.add()')
    quiz.add_question(set_q)
    pwd_q = Question(
        'What does pwd stand for?',
        'print working directory')
    quiz.add_question(pwd_q)
    list_q = Question(
        'Python lists are mutable, iterable, and what?',
        'ordered')
    quiz.add_question(list_q)
    student = Student("Ella", "Lee", "San Francisco")
    student_quiz = StudentQuiz(student, quiz)
    student_quiz.take_test()

example()

        

