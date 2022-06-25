from msvcrt import LK_RLCK
import pandas as pd
import numpy as np

data=np.random.randn(4,3)# burada rastgele veriler oluşturduk.

dataFrame=pd.DataFrame(data)
print(dataFrame) #Çok boyutlu veri yapımızı da oluşturduk. Colonlar ve indexleri oluşturduk.
yeniDataFrame=pd.DataFrame(data,index=["Atil","Zeynep","Atlas","Mehmet"],columns=["Maas","Yas","Calisma Saati"]) #2.parametrelerim index verdiğimiz gibi..
print(yeniDataFrame)
#az önce yaptığımız uygulamalarımızı yeniden yapılandırmak için aşağıdaki fonksiyonu kullanıcaz.
yeniDataFrame.reset_index()
#belki yanda yazan isimleri komple değiştirmek istiyoruz.
yeniIndeksListesi=["Ati","Zey","Atl","Meh"]
yeniDataFrame["Yeni Indeks"]=yeniIndeksListesi #buraya colomns olarak yazdık.
print(yeniDataFrame.set_index("Yeni Indeks")) #hangisine yapmak istiyorsam onu yazıyoruz.


#%%
yeniDataFrame.set_index("Yeni Indeks",inplace=True) #inplace=True yani bu fonksiyonu kullanırken yeniDataFrame'i değiştirmeyecek.
print(yeniDataFrame)


# %%
yeniDataFrame
# %%
yeniDataFrame.loc["Ati"]
# %%
# Peki multi-indexler nasıl anlarız?