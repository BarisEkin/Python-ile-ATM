class Musteri:
    def __init__(self,ad,soyad,kartsifre,hesapbakiye,kredikartborc,sonodeme):
        self.ad=ad
        self.soyad=soyad
        self.kartsifre=kartsifre
        self.hesapbakiye=hesapbakiye
        self.kredikartborc=kredikartborc
        self.sonodeme=sonodeme

BaranHesap=Musteri("Baran","Ok","1591",7500,2850,"21.09.2024")
MuratHesap=Musteri("Murat","Yilmaz","3573",9650,4000,"1.06.2023")
TakılanKart=BaranHesap


class ATM:
    def __init__(self,atmad):
        self.atmad=atmad
        self.giriskontrol()
        self.dongu=True

    def giriskontrol(self):
        Hak=2
        for i in range(0,3):
            Sifre=input("Lütfen 4 Haneli Şifrenizi Giriniz:")
            if Sifre==TakılanKart.kartsifre:
                self.program()
            elif Sifre!=TakılanKart.kartsifre and Hak!=0:
                print("Şifrenizi Yanlış Girdiniz. Kalan Hakkınız {}".format(Hak))
                Hak-=1
            elif Sifre!=TakılanKart.kartsifre and Hak==0:
                print("Şifrenizi 3 Defa Yanlış Girdiğiniz İçin Kartınız Bloke Olmuştur.Lütfen En Yakın Şubemize Başvurunuz.")
                exit()
    def program(self):
        secim=self.menu()

        if secim==1:
            self.bakiye()
        if secim==2:
            self.kredikartborc()
        if secim==3:
            self.paracekme()
        if secim==4:
            self.parayatırma()
        if secim==5:
            self.cıkıs()   

    def menu(self):
        secim=int(input("******Merhabalar, {}'a Hoşgeldiniz Sayın {} {}.\n\nLütfen Yapmak İstediğiniz İşlemi Seçiniz.\n\n[1] Bakiye Sorgulama\n[2] Kredi Kart Borç Sorgulama\n[3] Para Çekme\n[4] Para Yatırma\n[5] Kart İade\n\nSeçim: ".format(self.atmad,TakılanKart.ad,TakılanKart.soyad)))
        while secim<1 or secim>5:
            print("\n\nLütfen 1 ve 5 Arasında Geçerli Bir Değer Giriniz...\nAna Menüye Dönülüyor...")  
            self.program()
        return secim
    
    def bakiye(self):
        print("Hesap Bakiyeniz: {} TL'dir.".format(TakılanKart.hesapbakiye))
        self.dongu=False
        self.menudon()

    def kredikartborc(self):
        print("Kredi Kartı Borcunuz {} Son Ödeme Tarihli {} TL'dir. ".format(TakılanKart.sonodeme,TakılanKart.kredikartborc))
        self.dongu=False
        self.menudon()
    
    def paracekme(self):
        miktar1=int(input("Lütfen Çekmek İstediğiniz Miktarı Giriniz:"))
        YeniMiktar=TakılanKart.hesapbakiye-miktar1
        if TakılanKart.hesapbakiye<miktar1:
            print("Hesabınızda Yeterli Bakiye Bulunmamaktadır.")
            self.menudon()
        else:
            print("Lütfen Paranızı Alınız.Hesabınızda Kalan Tutar {} TL'dir.".format(YeniMiktar))
            self.menudon()
    
    def parayatırma(self):
        miktar2=int(input("Lütfen Yatırmak İstediğiniz Tutarı Giriniz:"))
        YeniMiktar2=TakılanKart.hesapbakiye+miktar2
        print("Paranız Başarıyla Yatırılmıştır.Yeni Bakiyeniz {} TL'dir.".format(YeniMiktar2))
        self.menudon()

    def cıkıs(self):
        print("Sayın {} {} Bankamızı Tercih Ettiğiniz İçin Teşekkür Eder, İyi Günler Dileriz.".format(TakılanKart.ad,TakılanKart.soyad))
        self.dongu=False
        exit()

    def menudon(self):
        x=int(input("Ana Menüye Dönmek İçin Lütfen 1 e Basınız.Kart İade İçin 2 ye Basınız."))
        if x==1:
            self.program()
        elif x==2:
            self.cıkıs()

Banka=ATM("XBank")
while Banka.dongu:
    Banka.program()








                
        
    

    

        
