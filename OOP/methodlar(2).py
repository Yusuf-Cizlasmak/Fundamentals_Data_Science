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
    def ornekMethod(self):
        #print("ben süper Kahramanım") # burada eğer aşagıda çalıştırmaya çalıştırırsak hata alırız çünkü def'inda illa bir self istiyor..
        print(f"Ben super kahramanım ve meslegim{self.meslek}")
        
superman=SuperKahraman("Superman",30,"Gazeteci") #şimdi self'den sonra yazdığım attribute'lere karşılık gelenleri yazıcam.

#hatta ben bunları değiştirebilirim bile:

superman.isim= "Clark Kent" 
print(superman.isim)
print(superman.OzelGuc)
superman.ornekMethod() #Ben super kahramanım ve meslegimGazeteci olarak çıktı verecektir.