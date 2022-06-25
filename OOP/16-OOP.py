#obje odaklı programlama.

benimListem= list()

type(benimListem)

#ilk önce iki tane önemli kelime başlayabiliriz : instance & attribute 
# instance : o sınıfın örneği diyebiliyoruz.
# sınıfın içerisinde özellikleri attribute oluyor.

superKahramanAdı= "Superman"
superKahramanYasi= 30                   #işte bunlar bizim attribute'larımız classlar için.
superKahramanMeslegi= "Gazeteci"

class SuperKahraman():
    OzelGuc= "Gorunmezlik" #illa bir attribute'u 
    def __init__(self,isimInput,yasInput,meslekInput):
        print("init cağrıldı.")                     #def __init__ bizim özel methodumuz self(kendş) demek
        self.isim = isimInput
        self.yas= yasInput
        self.meslek= meslekInput

        
        
superman= SuperKahraman("Superman",30,"Gazeteci") #şimdi self'den sonra yazdığım attribute'lere karşılık gelenleri yazıcam.

#hatta ben bunları değiştirebilirim bile:

superman.isim= "Clark Kent" 
superman.OzelGuc
print(superman.isim)
print(superman.OzelGuc)