#yeni bir class açmakta fayda var defaultDegerlere bakmak icin

class Kopek():
    YilCarpani=7
    def __init__(self,yas=5):  #ben burada yas=5'te yapabiliyorum aslında hatta altta parantezin içine 3 yazsam dahi overwrite'layıp tekrar değer atabiliyorum. 
        self.yas = yas
    def insanYasiniHesapla(self):
        return self.yas*self.YilCarpani  #ben burada self.YilCarpani yerine Kopek.YilCarpanı da diyebilirdim aslında.
benimKopek=Kopek()


img=benimKopek.insanYasiniHesapla()
print(img)
#peki kopekYasi ile insan yasını hesaplayan bir uygulama yapsak.(1'cisi yukarıda yapılmıştır şimdi 2. yolu denicez.)
#class Kopek():
    
    #def __init__(self,yas=5):  #ben burada yas=5'te yapabiliyorum aslında hatta altta parantezin içine 3 yazsam dahi overwrite'layıp tekrar değer atabiliyorum. 
        #self.yas = yas
        #self.insanYasinaCevrilmisAttribute= yas *7
    #def insanYasiniHesapla(self):
        #return self.yas*self.YilCarpani  #ben burada self.YilCarpani yerine Kopek.YilCarpanı da diyebilirdim aslında.


#insanYasi= benimKopek.insanYasinaCevrilmisAttribute()
#print(insanYasi)

 #sen self. kullan yine..