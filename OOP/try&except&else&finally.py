#şimdi konudanda anlaşacağı üzere hataları ele alıcaz.Ana başlığımız try&except &else &finally

def toplama(numara1,numara2):
    return numara1+numara2

x=int(input("İlk numarayı giriniz"))
y=int(input("İkinci numarayı giriniz"))
toplama(x,y)

while True:
    try:
        benimInt=int(input("Numaranızı giriniz :"))
    except:
        print("lütfen adam akıllı bir numara giriniz") #eğer except girmeseydik sistemin çökmesi gerekiyordu ve biz bunu except ile önledik.
        continue
    else:
        print("Teşekkürler")
        break
    finally:                            # ne olursa olsun sonunda print'ini yazdıracak olan finally fonksiyonu.
        print("finally çağrıldı.")