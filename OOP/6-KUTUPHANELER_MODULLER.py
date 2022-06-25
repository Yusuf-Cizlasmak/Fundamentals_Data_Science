import numpy
import matplotlib.pyplot as matplot

maasListesi= numpy.random.normal(4000,500,1000) #burada 4000 lira civarında tane random değeri 500 aralıkla  1000 tane rasgele değer oluştur. 
ortalama =numpy.mean(maasListesi) #ya da maasl listesinin ortalama değerini dee alabiliriz.

#print(maasListesi)
print(ortalama)

#peki bunun görüntüsü görebilir miyiz sorusunun cevabı evettir o da matplotlib ile

matplot.hist(maasListesi,50) #maaşları çizdir diyom 50 tane histogram yapsan yeterli diyorum.
matplot.show()