import math


def toplama(a,b):
    sonuc=a+b
    print(sonuc)
    return sonuc
    pass
def cikarma(a,b):
    sonuc=a-b
    print(sonuc)
    return sonuc
    pass
def carpma(a,b):
    sonuc=a*b
    print(sonuc)
    return sonuc
    pass
def bolme(a,b):
    sonuc=a/b
    print(sonuc)
    return sonuc
    pass
def tersCevir(yazi):
    cevirilmisYazi=list(reversed(yazi))
    print(cevirilmisYazi)
    return cevirilmisYazi
    pass
def faktoriyel(a):
    return math.factorial(a)
    pass
class Kullanicilar():
    def kullanicilar(self,k_adi,k_username,k_passwrd,k_gorev):
        self.k_adi = k_adi
        self.k_username = k_username
        self.k_passwrd = k_passwrd
        self.k_gorev = k_gorev
        bilgi = [k_adi,k_username,k_passwrd,k_gorev]
        print(bilgi)
        return bilgi
        pass


toplama(5,6)
cikarma(10,6)
carpma(4,6)
bolme(30,10)
tersCevir("Ramazan")
sinif = Kullanicilar()
sinif.kullanicilar("Ramazan","ramo","passwrd","ogrenci")
