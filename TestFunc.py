import MainFunc
import unittest

class test_case(unittest.TestCase):

    def test_toplama(self):
        self.assertEqual(MainFunc.toplama(5,6),11)
        pass
    def test_cikarma(self):
        self.assertEqual(MainFunc.cikarma(10,6),4)
        pass
    def test_bolme(self):
        self.assertEqual(MainFunc.bolme(15,3),5)

        pass
    def test_carpma(self):
        self.assertEqual(MainFunc.carpma(5,6),30)
        print("Doğru")
        pass
    def test_tersCevir(self):
        self.assertTrue(MainFunc.tersCevir("Yazılım_Kalite"),"etilaK_mılızay")
        pass
    def test_Kullanici(self):
        self.assertTrue(MainFunc.sinif.kullanicilar("Ramazan","ramo","passwrd","ogrenci"), ["Ramazan","ramo","passwrd","ogrenci"])
        pass
