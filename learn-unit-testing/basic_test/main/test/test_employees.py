import unittest
from ..main.employee import Employee

class TestEmployee(unittest.TestCase):
    def test_email(self):
        emp_1 = Employee('Aan', 'Aldi', 5000)
        emp_2 = Employee('siapa', 'saja', 3000)

        self.assertEqual(emp_1.email,'Aan.Aldi@email.com')
        self.assertEqual(emp_2.email,'siapa.saja@email.com')

        emp_1.first = 'Ana'
        emp_2.first = 'ayo'

        self.assertEqual(emp_1.email, 'Ana.Aldi@email.com')
        self.assertEqual(emp_2.email, 'ayo.saja@email.com')

if __name__=="__main__":
    unittest.main()