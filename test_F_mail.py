import unittest
import myform

class Test_test_F_mail(unittest.TestCase):
    def test_A(self):
        list_mail_false = ["", "1", "a", "m1@", "@mail", "@", ".", ".ru", ".com", ".1", "1.", "a.", ".a", "m1@mail", "m1@mail.", "m1@mail@", "@m1@mail.ru"]

        for x in list_mail_false:
            self.assertFalse(myform.isCorrectEmail(x))

if __name__ == '__main__':
    unittest.main()
