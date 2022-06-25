class Hayvan():
    def __init__(self):
        print("hayvan sınfı init çağrıldı.")
    def method1(self):
        print("hayvan sınıfı method1 çağrıldı.")
    def method2(self):
        print("hayvan sınıfı method2 ")

benimHayvanım= Hayvan()

method11= benimHayvanım.method1()
method22= benimHayvanım.method2() #aptal gibi bunların yanına fonksiyon işareti koymayı unutma Yusuf :)

print(method11)
print(method22)
#artık ben bu  başka bir class içinde de kullanabilirim aslında. yani
class Kedi(Hayvan):
    def __init__(self):
        Hayvan.__init__(self)
        print("kedi sınıf init çağrıldı.")
    def miyavla(self):
        print("meeeeeeeeeeow")
    def method1(self):
        print("kedi sınıfından çağrılan method 1 ") #(4)
benimKedi= Kedi()

#vurucu kısım şu aslında ben 
benimKedi.method1()  #bişey çağrıyabiliyorum ben bunu kedi class'ında yazmama rağmen.

benimKedi.miyavla() #bunu bile çağırabiliyorum hem.

#mesela şey diyelim ilk yazdığımız class'ta 500 def var. ama ben yine method 1 çağırmak istiyorumm (4)
benimKedi.method1()
benimHayvanım.method1()
#işte biz bu duruma override diyoruz bildiğin üstüne yazma


#POLYMORPHIM
class Elma():
    def __init__(self,isim):
        self.isim=isim
    def bilgiVer(self):
        return self.isim + " 100 kaloridir."

class Muz():
    def __init__(self,isim):
        self.isim=isim

    def bilgiVer(self):
        return self.isim + " 150 kaloridir."

elma= Elma("elma") #benden bi isim isteyecek ya o yüzden içini doldurdum
elma.bilgiVer()

muz= Muz("muz")

muz.bilgiVer()

#peki bu polymorpshism nerede ortaya çıkıyor.
meyveListesi= [elma,muz] #bak bunlar string değil he. unutma bunları.

for meyve in meyveListesi:
    print(meyve.bilgiVer()) #print olarak bize iki çıktığı da vericek. ancak sadece bu durumu for loop'da düşünmemek gerek bence.   
    #bi fonksiyonda da bunu yapabiliriz.

def bilgiAl(meyve):
    print(meyve.bilgiVer())

bilgiAl(muz)
bilgiAl(elma) #aynı şekilde çıktıyı veriyor.