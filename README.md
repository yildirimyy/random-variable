# RASTGELE DEGİSKENLER
**Probability Density Function - Probability Mass Function**

* Rastgele Değişkenler: Rastgele deney ile  çalışırken, deneyin çıktılarının ölçümü ya da sayısal özellikleri ile ilgilenir. 
Örneğin;
    * Bir sınıftaki öğrencilerin boyları ya da kiloları
    * Doktor sırası bekleyen hastaların bekleme süreleri
    * 1 saat içerisinde bir mağazaya giren kişi sayısı 
* Rastgele Değişkenler büyük harfler ile gösterilir. 
* Rastgele Değişkenler **"AYRIK"** ve **"SÜREKLİ"** olmak üzere **iki gruba** ayrılır. 

**1) AYRIK:** Sonucu tam sayıdır. 
--> Para atma deneyinde art arda yapılan 5 atışta tura gelme sayısı
--> 1 saat içerisinde bir mağazaya giren kişi sayısı 

**2) SÜREKLİ:** Sonucu sürekli aralıktadır. 
--> Bir sınıftaki öğrencilerin boyları ya da kiloları
--> Atılan topun çıkabildiği yükseklik

![](https://raw.githubusercontent.com/yildirimyy/random-variable/master/Screen/1.png) 

**Probability Density Function (Olasılık Yoğunluk Fonksiyonu):**
 
Sürekli  bir rasgele değişkenin alabileceği değerlerin sayısı sonsuz, bu değerleri alma olasılıklarının  toplamı  ise  1’dir. Grafiksel olarak da sonuç elde edilebilir. Grafiğin altında kalan alan 1'e eşit olacaktır ve sürekli değerler üzerinden işlem yapıldığı için integral alınarak sonuç bulunur.

![](https://raw.githubusercontent.com/yildirimyy/random-variable/master/Screen/2.png) 

![](https://raw.githubusercontent.com/yildirimyy/random-variable/master/Screen/4.png) 

![](https://raw.githubusercontent.com/yildirimyy/random-variable/master/Screen/5.png) 



**Probability Mass Function (Olasılık Kütle Fonksiyonu):**

Olasılık kütle fonksiyonu bir değişkenin olasılığının aynı belli bir değere eşit olduğunu belirten bir fonksiyondur.


**SORU: İki hilesiz zarın atılması olayında X; atılan iki zardaki sayıların toplamını gösteren rastgele değişkeni olsun. X’in olasılık fonksiyonun bulunuz**

***Aşağıdaki olasılık değerlerini, olasılık fonksiyonu kullanarak elde ediniz***
 
**a) Toplamın 7 veya 11 olması** 
**b) Toplamın 8’den büyük olması**
**c) Toplamın 3 den büyük fakat 9 dan küçük olması**


**ÇÖZÜM:**

```
X rastgele değişkenin alacağı değerler 2,3,...,12 olduğundan X rastgele değişkeni kesikli rastgele değişkendir. Olasılık fonksiyonun değerleri:
```
![](https://raw.githubusercontent.com/yildirimyy/random-variable/master/Screen/6.png) 

![](https://raw.githubusercontent.com/yildirimyy/random-variable/master/Screen/7.png) 

**a)** A-> toplamların 7 olması  ve B-> toplamların 11 olması ise;
![](https://raw.githubusercontent.com/yildirimyy/random-variable/master/Screen/8.png) 

**b)**
![](https://raw.githubusercontent.com/yildirimyy/random-variable/master/Screen/9.png) 

**c)**
![](https://raw.githubusercontent.com/yildirimyy/random-variable/master/Screen/10.png) 

**SORU: 1 ile 9 arasında 30 adet rastgele oluşturulacak sayıların olasılık kütle fonksiyonu**

**ÇÖZÜM:**

1 ile 9 arasında random üretilen sayıların hangi olasılıkla geleceklerinin bulunabilmesi için öncelikle belli bir sayıdan dizi boyunca kaç adet geldiğinin bulunması gerekmektedir.

![](https://raw.githubusercontent.com/yildirimyy/random-variable/master/Screen/11.png) 

![](https://raw.githubusercontent.com/yildirimyy/random-variable/master/Screen/12.png) 

Herbir sayıdan dizide kaç adet geldiği bulunduktan sonra hangi olasılıkla geleceği de bulunabilir.

![](https://raw.githubusercontent.com/yildirimyy/random-variable/master/Screen/13.png) 

![](https://raw.githubusercontent.com/yildirimyy/random-variable/master/Screen/14.png) 

```
Kaynaklar:
http://muhserv.atauni.edu.tr/makine/ikaymaz/istatistik/lecture_notes/DERS_5_ANAKUTLE_DAGILIMLARI_I_2015_IKaymaz.pdf
http://www.baskent.edu.tr/~iserdem/dersler/258/Bolum3_1.pdf
http://www.yildiz.edu.tr/~tastan/teaching/appendixB.pdf
