# El Hareketleriyle Fare Kontrolü ve Yazı Görüntüleme Projesi  

Bu proje, bilgisayar kamerası aracılığıyla yapılan el hareketleriyle fare işlevlerini kontrol etmeyi (sağ tık, sol tık ve hareket ettirme işlevlerini) ve yazı görüntülemeyi amaçlamaktadır. Makine öğrenmesi tekniklerini kullanarak, el hareketlerini tanıyan ve kullanıcı etkileşimini sağlayan bir sistem sunar.

![Image](https://github.com/user-attachments/assets/22cae9c1-3a04-4b5f-a255-7e716b7ef66c)
![Image](https://github.com/user-attachments/assets/52cbefcc-b8ed-4a37-8604-5db50561b06b)
![Image](https://github.com/user-attachments/assets/599856bb-02c9-44d3-b079-b88a02874279)

## Özellikler  

- **El Hareketleriyle Yazı Yazma**: Kullanıcı, tanımlanmış el hareketlerini kullanarak yazı yazabilir.  
- **Makine Öğrenmesi**: Kullanıcı hareketleri kaydedilir ve bu verilerle bir makine öğrenmesi modeli eğitilir.
- - **Fare Kontrolü**: Sol elin işaret parmağı ile fare imlecini hareket ettirme, sağ elin baş parmak ve işaret parmağını birleştirerek sol tıklama, baş parmak ve orta parmağını birleştirerek sağ tıklama işlevlerini gerçekleştirme.

## Gereksinimler  

Bu projeyi çalıştırabilmek için aşağıdaki yazılımlara ihtiyacınız olacak:  

- Python 3.x  
- TensorFlow
- OpenCV (Görüntü işleme için)  
- Mediapipe (El hareketlerini tanımak için)  
- NumPy  
- Matplotlib (Opsiyonel, görselleştirme için)  

## Kurulum  

### Adım 1: Proje Dosyalarının İndirilmesi
Bu repoyu kendi bilgisayarınıza klonlayın veya indirin: 

  ```bash
git clone [https://github.com/kullaniciadi/proje-adi.git](https://github.com/EnesSenerr/El-Hareketleriyle-Fare-Kontrolu-ve-Yazi-Goruntuleme-Projesi-.git)
cd El-Hareketleriyle-Fare-Kontrolu-ve-Yazi-Goruntuleme-Projesi
```

### Adım 2: Python ve Bağımlılıkların Kurulumu

Python 3.x sürümlerinden birisini yükleyin ve bir IDE seçip dosyaları açın.

Gerekli kütüphaneleri yüklemek için aşağıdaki komutu çalıştırın:

```bash
pip install tensorflow opencv-python mediapipe numpy matplotlib
```

### Adım 3: Projenin Çalıştırılması

Proje, "main.py" dosyasının çalıştırılmasıyla başlar:

```bash
python main.py
```

Proje çalışmaya başladığında kamera otomatik olarak açılacaktır. Kamera üzerinden:

- Fare kontrol işlevlerini kullanabilirsiniz.
- Sol elinizin beş parmağını açık tutarak tahmin moduna geçebilirsiniz.


### Model Kullanımı ve Eğitimi

## Önceden Eğitilmiş Modelin Kullanımı

Proje ile birlikte gelen "knn_model3.pkl" dosyası önceden eğitilmiş bir modeldir. Bu modeli kullanarak, el hareketlerine dayalı tahminlerde bulunabilir ve işaret dillerini tanımlayabilirsiniz.

## Kendi Modelinizi Eğitmek

### 1. Veri Toplama:

- Veriseti_olusturma.py dosyasını çalıştırarak veri toplayabilirsiniz.
- current_label değişkenine hangi harf veya kelimeyi eğitmek istediğinizi girin.
- Kaydı başlatmak için S tuşuna basın, bitirmek için tekrar S tuşuna basın.
- Kaydı sonlandırmak için Q tuşunu kullanın.

### 2. Veri Setlerinin Birleştirilmesi:

- Topladığınız tüm verileri Veriseti_birlestirme.py dosyasını kullanarak birleştirebilirsiniz.


### 3. Model Eğitimi:

- Birleştirilmiş veri setini kullanarak Model_egitimi.py dosyası ile yeni bir model oluşturabilirsiniz.
- Bu projede KNN (K-Nearest Neighbors) algoritması kullanılmıştır.

### Not:

Tüm işlemleri sonlandırmak için Q tuşunu kullanabilirsiniz.
