ilkSayi=int(input("hesaplanmasi istenilen ilk sayiyi giriniz: "))
ikinciSayi=int(input("ikinci sayiyi giriniz: "))
 
islem=input("""islem belirleyiniz:
(toplama: 1,cikarma: 2,carpma: 3, bolme:3  )\n
            """ )
if islem =="1":
    print("toplama islemi sonucu:"+str(ilkSayi+ikinciSayi))

if islem =="2":
    print("cikarma islemi sonucu:"+str(ilkSayi-ikinciSayi))

if islem =="3":
    print("carpma islemi sonucu:"+str(ilkSayi*ikinciSayi))
print()
if islem =="4":
    print("bolme islemi sonucu:"+str(ilkSayi/ikinciSayi))