import unittest
from modulo.aritimetica import sub

class SubTest(unittest.TestCase):
    def setUpClass(cls) -> None:
        return super.setUpClass()

    def setUp(self) -> None:
        self.valor1 = 50
        self.valor2 = 40


    def test_sub_positivos(self):
        s = sub(self.valor1, self.valor2)
        self.assertEqual(s, 10)
        print(s)

