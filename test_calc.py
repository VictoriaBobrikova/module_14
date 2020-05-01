import unittest
from calc import calc_me

class CalcTest(unittest.TestCase):
    def test_add(self):
        "Сложение"
        self.assertEqual(calc_me(1, 2,"+"), 3)
        
    def test_sub(self):
        "Вычитание"
        self.assertEqual(calc_me(4, 2,"-"), 2)
        
    def test_mul(self):
        "Умножение"
        self.assertEqual(calc_me(12345679, 8,"*"), 98765432)
        
    def test_div(self):
        "Деление"
        self.assertEqual(calc_me(111111111, 9,"/"), 12345679)

    def test_degree1(self):
        "Возведение в степень значком ^"
        self.assertEqual(calc_me(4, 2,"^"), 16)

    def test_degree2(self):
        "Возведение в степень значком **"
        self.assertEqual(calc_me(4, 2,"**"), 16)


    def test_div_neg(self):
        "Негативный, деление на ноль"
        self.assertEqual(calc_me(12, 0, "/"), 'ERROR: Divide by zero!')


    def test_symb_numb1(self):
        "Ввод символа в переменную Число1"
        self.assertEqual(calc_me("q", 2,"+"), 'ERROR: now it is not supported')

    def test_symb_numb2(self):
        "Ввод символа в переменную Число2"
        self.assertEqual(calc_me(2, "q", "+"), 'ERROR: now it is not supported')

    def test_symb_numb12(self):
        "Ввод символов в обе переменные Число1 и Число2"
        self.assertEqual(calc_me("q","w","+"), 'ERROR: now it is not supported')


    def test_none_numb1(self):
        "Запуск без переменной Число1"
        self.assertEqual(calc_me(None, 2,'+'), 'ERROR: send me Number1')

    def test_none_numb2(self):
        "Запуск без переменной Число2"
        self.assertEqual(calc_me(2, None,'+'), 'ERROR: send me Number2')

    # в документации отсуствует такой случай,надо добавить или и без него хорошо?
    def test_none_numb12(self):
        "Запуск без обеих переменных Число1 и Число2"
        self.assertEqual(calc_me(None, None,'+'), 'ERROR: send me Number1 and Number2')

    # при запуске калькулятора из sublime он выводит такую ошибку, но тест почему-то считает
    def test_none(self):
        "Расчёт больших чисел"
        self.assertEqual(calc_me(3, 1000,'^'), 'Overflow error: Result is too large')

    

if __name__ == '__main__':
    unittest.main(verbosity=2)