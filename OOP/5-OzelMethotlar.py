class Meyve():
    def __init__(self,isim,kalori):
        self.isim= isim
        self.kalori= kalori
    def __str__(self):
        return f"{self.isim} şu kadar kaloriye sahiptir :{self.kalori}" #(3)
 #f"" formatting anlamına geliyor bu da farklı bir yazış şekli aklında bulunsun.
muz= Meyve("Muz",150)
#init  tam olarak bu işe yarıyor.
muz.kalori #yazsam çıkar ama print(muz) yazınca hata alıcam. başka methotlarda var tıpkı __init__ gibi (3)'ü yaptıktan sonra bakalım ne çıkacak ?
print(muz)