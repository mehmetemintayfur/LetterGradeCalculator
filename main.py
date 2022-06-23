f = open("notlar.txt","a")
f.write("Mehmet Emin Tayfur,80,85\n")
f.write("Samil Yusa Demir,70,80\n")
f.write("Yagizcan Sahin,50,65\n")
f.write("Metehan Tufan,60,80\n")
f.write("Cengizhan Kose,55,75\n")
f.write("Omer Faruk Yardimci,65,55\n")
f.close()
def harfnotuhesapla(satir):
 ayir = satir.split(",")
 isim = ayir[0]
 not1 = int(ayir[1])
 not2 = int(ayir[2])

 ortalama = (not1*0.4)+(not2*0.6)

 if(ortalama>=80):
     harfnotu = "AA"
 elif(ortalama>=75):
     harfnotu = "BA"
 elif(ortalama>=70):
     harfnotu = "BB"
 elif(ortalama>=65):
     harfnotu = "CB"
 elif(ortalama>=60):
     harfnotu = "CC"
 elif(ortalama>=55):
     harfnotu = "DC"
 elif(ortalama>=50):
     harfnotu = "DD"
 else:
     harfnotu = "FF"


 return isim + "-> " + harfnotu


with open("notlar.txt","r") as f:
 ogrlistesi = []
 for i in f :
   ogrlistesi.append(harfnotuhesapla(i))

with open("notlar.txt","a") as f2:
    for j in ogrlistesi:
        f2.write(j)
