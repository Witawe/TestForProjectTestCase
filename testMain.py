import unittest
from unittest.mock import patch
from io import StringIO
from datetime import date
from addstudent import addstud
from addspec import addspec
from addgroup import addgroup
from addsubject import addsubject
from addexam import addexam
from addexampoint import addexampoint

class TestMain(unittest.TestCase):

    ##Student##

    stud = ['Луковцев Алексей Владимирович', '185775']

    @patch('builtins.input', side_effect=stud)
    @patch('sys.stdout', new_callable=StringIO)
    def test_1(self, mock_output, mock_input):
        addstud(['', 'add', 'stud'])
        self.assertEqual(mock_output.getvalue(),
                         'Student(fio=\'Луковцев Алексей Владимирович\', code=185775)\nСтудент успешно добавлен\n')

    def test_2(self):
        stud = ['', '']
        with patch('builtins.input', side_effect=stud):
            with self.assertRaises(Exception):
                addstud(['', 'add', 'stud'])

    ##Specialization##

    spec = ['Фундаментальная информатика и информационные технологии']

    @patch('builtins.input', side_effect=spec)
    @patch('sys.stdout', new_callable=StringIO)
    def test_3(self, mock_output, mock_input):
        addspec(['', 'add', 'spec'])
        self.assertEqual(mock_output.getvalue(),
                         'Specialization(name=\'Фундаментальная информатика и информационные технологии\')'
                         '\nСпециализация успешно добавлена\n')

    def test_4(self):
        spec = ['']
        with patch('builtins.input', side_effect=spec):
            with self.assertRaises(Exception):
                addspec(['', 'add', 'spec'])

    ##Group##

    group = ['М-ФИИТ-21', '2021', 'Фундаментальная информатика и информационные технологии']

    @patch('builtins.input', side_effect=group)
    @patch('sys.stdout', new_callable=StringIO)
    def test_5(self, mock_output, mock_input):
        addgroup(['', 'add', 'group'])
        self.assertEqual(mock_output.getvalue(),
                         'Group(name=\'М-ФИИТ-21\', year=2021, specialization=Specialization(name=\''
                         'Фундаментальная информатика и информационные технологии\'))\nГруппа успешно добавлена\n')

    def test_6(self):
        group = ['']
        with patch('builtins.input', side_effect=group):
            with self.assertRaises(Exception):
                addgroup(['', 'add', 'group'])

    ##Subject##

    subj = ['Б1.О.07', 'Машинное обучение', '2', '288', 'Фундаментальная информатика и информационные технологии']

    @patch('builtins.input', side_effect=subj)
    @patch('sys.stdout', new_callable=StringIO)
    def test_7(self, mock_output, mock_input):
        addsubject(['', 'add', 'subj'])
        self.assertEqual(mock_output.getvalue(),
                         'Subject(code=\'Б1.О.07\', name=\'Машинное обучение\', semestr=2, hours=288, '
                         'specialization=Specialization(name=\'Фундаментальная информатика и информационные технологии\'))\nПредмет успешно добавлен\n')

    def test_8(self):
        subj = ['']
        with patch('builtins.input', side_effect=subj):
            with self.assertRaises(Exception):
                addsubject(['', 'add', 'subj'])

    ##Exam##

    exam = ['Б1.О.07', 'Машинное обучение', '2', '288', 'Фундаментальная информатика и информационные технологии', '1/1/2021', '2021-2022', 'Эверстов Владимир Васильевич']

    @patch('builtins.input', side_effect=exam)
    @patch('sys.stdout', new_callable=StringIO)
    def test_9(self, mock_output, mock_input):
        addexam(['', 'add', 'exam'])
        self.assertEqual(mock_output.getvalue(),
                         'Exam(subject=Subject(code=\'Б1.О.07\', name=\'Машинное обучение\', semestr=2, hours=288, '
                         'specialization=Specialization(name=\'Фундаментальная информатика и информационные технологии\')), '
                         'examDate=datetime.date(2021, 1, 1), group=None, year=\'2021-2022\', lecturer_fio=\'Эверстов Владимир Васильевич\')\nЭкзамен успешно добавлен\n')

    def test_10(self):
        exam = ['']
        with patch('builtins.input', side_effect=exam):
            with self.assertRaises(Exception):
                addexam(['', 'add', 'exam'])

    ##ExamPoint##

    exam_point = ['Луковцев Алексей Владимирович', '185775', '59.9', '25.4',
                  '1/1/2021', 'Б-ФИИТ-21', 'Б1.О.07', 'Машинное обучение', '2', '288',
                  'Фундаментальная информатика и информационные технологии']

    @patch('builtins.input', side_effect=exam_point)
    @patch('sys.stdout', new_callable=StringIO)
    def test_11(self, mock_output, mock_input):
        addexampoint(['', 'add', 'exampoint'])
        self.assertEqual(mock_output.getvalue(),
                         'ExamPoints(student=Student(fio=\'Луковцев Алексей Владимирович\', code=185775), '
                         'inPoints=59.9, examPoints=25.4, exDate=datetime.date(2021, 1, 1), '
                         'groupName=\'Б-ФИИТ-21\', subject=Subject(code=\'Б1.О.07\', name=\'Машинное обучение\', '
                         'semestr=2, hours=288, specialization=Specialization'
                         '(name=\'Фундаментальная информатика и информационные технологии\')))\nРезультат успешно добавлен\n')

    def test_12(self):
        exam_point = ['']
        with patch('builtins.input', side_effect=exam_point):
            with self.assertRaises(Exception):
                addexam(['', 'add', 'exampoint'])

if __name__ == '__main__':
    unittest.main()