from main import Student, Specialization, Subject, Group, Exam, ExamPoints
from classes.getSubject import getSubject
from datetime import date
import unittest

class TestClasses(unittest.TestCase):
    def test_class_student(self):
        student = Student("Луковцев Алексей Владимирович", 185775)
        self.assertEqual("Луковцев Алексей Владимирович", student.fio)
        self.assertEqual(185775, student.code)

    def test_class_specialization(self):
        spec = Specialization("ФИИТ")
        self.assertEqual("ФИИТ", spec.name)

    def test_class_subject(self):
        subject = Subject("Б1.В.02", "Методы тестирования и верификации программных продуктов", 2, 108, Specialization)
        self.assertEqual("Б1.В.02", subject.code)
        self.assertEqual("Методы тестирования и верификации программных продуктов", subject.name)
        self.assertEqual(2, subject.semestr)
        self.assertEqual(108, subject.hours)
        self.assertEqual(Specialization, subject.specialization)

    def test_class_group(self):
        specialization = "ФИИТ"
        group = Group("М-ФИИТ-21", 2021, specialization)
        self.assertEqual("М-ФИИТ-21", group.name)
        self.assertEqual(2021, group.year)
        self.assertEqual(specialization, group.specialization)

    def test_class_exam(self):
        specialization = "ФИИТ"
        data = date(2021, 1, 1)
        sbj = Subject("Б1.В.02", "Методы тестирования и верификации программных продуктов", 2, 108, specialization)
        exam = Exam(sbj, data, 2021, "Эверстов Владимир Васильевич")
        self.assertEqual(sbj, exam.subject)
        self.assertEqual(data, exam.examDate)
        self.assertEqual(2021, exam.year)
        self.assertEqual("Эверстов Владимир Васильевич", exam.lecturer_fio)

    def test_class_exampoints(self):
        exampoints = ExamPoints(Student, 59.9, 30)
        self.assertEqual(Student, exampoints.student)
        self.assertEqual(59.9, exampoints.inPoints)
        self.assertEqual(30, exampoints.examPoints)

    def test_class_getsubject(self):
        g_subject = getSubject("../data/2семестр.xlsx", "Межкультурная коммуникация в профессиональной деятельности")
        self.assertEqual("Б1.О.02", g_subject.code)
        self.assertEqual("Межкультурная коммуникация в профессиональной деятельности", g_subject.name)
        self.assertEqual(2, g_subject.semestr)
        self.assertEqual(72, g_subject.hours)
        self.assertEqual("ФИИТ", g_subject.specialization.name)

if __name__ == '__main__':
    unittest.main()