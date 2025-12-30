YAPILACAKALR-
Algoritma nedir? 
Günlük hayattan örnekler bul
Problem cözme adımları anla,planla,uygula,kontrol et
Pseudocode(sözde kod) nedir? bir problemi pseudocode ile yaz
Akış diyagrafı cizerek bir algoritmayi gorselleştir


BÖLÜM 1
Algoritma=belirli bir problemi çözmek ve ya belirli bir amaca ulasmak için tasarlanan yol.
örnek = Yemek yaparken o yemegin tarifde ki adımları aslıda bir algoritmadır.
              Çay nasıl demlenir?
adım1=:başla
adım2:çaydanlıga su koy
adım3:çaydanlıgı ocaga koy
adım4:ocagı yak
adım5:suyun kaynamasını bekle
adım6:demlenmesini bekle
adım7:su kaynadı ise demliğe çay koy,kaynamadı ise 6. adımna git
adım8:çayı servis et 

BÖLÜM 2
ANLA: problemin sınırlarını belirle
PLANLA: mantıksal straleji kur
UYGULA: çözümü inşaa et
KONTROL ET: hataları bul ve iyileştir

Suyun Halini Bulan Program
1ADIM:ANLA
Verilen bir sicaklik derecesini göre suyun Katı, Sıvı veya Gaz olduğunu söylememiz gerekiyor.

2ADIM:PLANLA
Sıcaklık değerini (derece cinsinden) al.
Eğer derece <= 0 ise sonuç "Katı".
Değilse, Eğer derece < 100 ise sonuç "Sıvı".
Değilse (yani 100 ve üstü ise) sonuç "Gaz".

3ADIM:UYGULA

#include <stdio.h>

int main() {
 
    float derece;

    // Kullanıcıdan veri alalım
    printf("Sıcaklık değerini giriniz: ");
    scanf("%f", &derece);

    // Algoritmayı kontrol yapılarıyla uygulayalım
    if (derece <= 0) {
        printf("Su şu an KATI (Buz) halindedir.\n");
    } 
    else if (derece > 0 && derece < 100) {
        printf("Su şu an SIVI halindedir.\n");
    } 
    else {
        printf("Su şu an GAZ (Buhar) halindedir.\n");
    }

    return 0;
}
4ADIM: KONTROL ET
Test 1: derece = -5 girildi. Çıktı: Katı. (Doğru)
Test 2: derece = 25 girildi. Çıktı: Sıvı. (Doğru)
Test 3: derece = 150 girildi. Çıktı: Gaz. (Doğru)

BÖLÜM3:
Pseudocode(sözde kod) nedir? 
Ayrıntılı ve okunabilir bir açıklamadır,kolayca anlaşılması için dogal sözdizimi kurallarına uygun yazılır.
Kodun mantıgı gercek bir programlama diline çevirmek için bir plan görevi görür.
Dilden bağımsızdır,hataları azaltır,iletişimi kolaylaştır.
  
NASIL YAZILIR?
Her zaman ilk kelimeyi büyük harfle yazın.
Satır başına yalnızca bir açıklama yapın.
Hiyerarşiyi göstermek, okunabilirliği artırmak için girintili yapılar kullanın.
Çok satırlı bölümleri her zaman END anahtar sözcüklerinden (ENDIF, ENDWHILE, vb.) herhangi birini kullanarak bitirin.
İfadelerinizi programlama dilinden bağımsız tutun.
İfadeleri basit, öz ve okunabilir tutun.


BAŞLA
Kullanıcıdan "limit" bilgisini al "
Toplam" değerini 0 olarak belirle "sayac" değerini 1 olarak belirle
WHILE "sayac" <= "limit" 
OLDUĞU SÜRECE "toplam" = "toplam" + "sayac" VE "sayac" = "sayac" + 1
ENDWHILE  "1'den " + "limit" + " değerine kadar olan sayıların toplamı: " + "toplam"
BİTİR


C PROGRAM DİLİNDE BÖYLE YAZILIR:
int main() {
    // Veri Tanımlama
    int limit, toplam = 0, sayac = 1;

    // 1. Adım: Anla (Kullanıcıdan veri al)
    printf("Hangi sayiya kadar toplamak istiyorsunuz?: ");
    scanf("%d", &limit);

    // 2. ve 3. Adım: Planla & Uygula (Döngü Yapısı)
    // Sözde koddaki WHILE yapısını kuruyoruz
    while (sayac <= limit) {
        toplam = toplam + sayac; // Sepete sayıyı ekle
        sayac = sayac + 1;       // Bir sonraki sayıya geç
    }

    // 4. Adım: Kontrol Et (Sonucu Yazdır)
    printf("1'den %d sayisina kadar olan toplam: %d\n", limit, toplam);

    return 0;
}

BÖLÜM4:
BOZUK LAMBANIN TESPİTİNİ SAGLAYAN AKIŞ ŞEMASI

OVAL:BAŞLA
OK AŞAĞI İNER :LAMBA ÇALISIYOR MU?
EŞKENAR DÖRTGEN:FİŞ TAKILI MI?
DİKTORGEN:HAYIR /FİŞİ TAK
AŞAĞI DEVAM ET: EVET
EŞKENAR DÖRTGEN:AMPUL PATLAK MI?
DİKTORGEN:EVET /AMPÜLÜ DEĞİŞTİR
AŞAGI DEVAM ET: HAYIR
DİKTORGEN:YENİ LAMBA AL/TAMİRE GÖTÜR
OVAL : BİTİR


int main() {
    int fis_takili, ampul_patlak;
    printf("Lamba Ariza Tespit Sistemi\n");
    printf("Lamba fisi takili mi? Evet icin 1, Hayir icin 0: ");
    scanf("%d", &fis_takili);

    if (fis_takili == 0) {
        printf("COZUM: Fisi takiniz.\n");
    } 
    else {
        printf("Ampul patlamis mi? Evet icin 1, Hayir icin 0: ");
        scanf("%d", &ampul_patlak);

        if (ampul_patlak == 1) {
            printf("COZUM: Ampulu degistiriniz.\n");
        } 
        else {
            printf("COZUM: Lambayi tamire goturun veya yeni bir lamba alin.\n");
        }
    }

    return 0;
}










