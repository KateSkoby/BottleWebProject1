import unittest
import myform

class Test_test_T_mail(unittest.TestCase):
    def test_A(self):
        list_mail_true = ["m1@mail.ru", "m1.@gmail.com", "1m@mail.bk.com", "katesko@yandex.ru", "pelbek1999@mail.com", ".1."]

        for x in list_mail_true:
            self.assertTrue(myform.isCorrectEmail(x))

if __name__ == '__main__':
    unittest.main()
