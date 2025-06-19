
### 3. Docker ile Çalıştırma

```sh
docker compose build --no-cache
docker compose up
```

### 4. Uygulamayı Kullanma

- API dokümantasyonu: [http://localhost:8000/docs](http://localhost:8000/docs)
- Web arayüzü: [http://localhost:8000/](http://localhost:8000/)

### 5. API Kullanımı

#### Özgeçmiş Yükleme (Swagger veya Web Arayüzü ile)

- `/parse_resume` endpointine dosya yükleyin.
- Sonuç yapılandırılmış JSON olarak döner.

#### Örnek JSON Yanıtı

```json
{
  "title": "Data Scientist",
  "summary": "10+ yıl tecrübeli veri bilimci...",
  "experiences": [
    {
      "company": "ABC Inc",
      "summary": "Makine öğrenmesi projeleri geliştirdi..."
    }
  ],
  "skills": ["Python", "Machine Learning"],
  "soft_skills": ["Problem-Solving"],
  "certificates": ["Google Certified Professional Data Engineer"],
  "languages": ["English", "Turkish"]
}
```

## Geliştirici Notları

- OpenAI API anahtarınızı kimseyle paylaşmayın.
- Proje tamamen Docker ile izole çalışır, ek sanal ortama gerek yoktur.
- Tesseract ve textract gibi bağımlılıklar Dockerfile ile otomatik kurulur.

## Katkı ve Lisans

- Pull request ve katkılara açıktır.
- [MIT License](LICENSE)

---

## Docker ve Proje Mimarisi

```mermaid
graph TD
    A[Web Arayüzü (HTML/CSS/JS)] -->|Dosya Yükle| B(FastAPI REST API)
    B -->|Metin Çıkar| C[extractor.py]
    B -->|OpenAI ile Özet| D[openai_structurer.py]
    D -->|Yapılandırılmış JSON| B
    B -->|Yanıt| A
    subgraph Docker
        B
        C
        D
    end
```

---

## Hızlı Başlangıç

```sh
git clone https://github.com/kullanici_adiniz/proje-adi.git
cd proje-adi
# .env dosyasını oluşturun ve OpenAI API anahtarınızı ekleyin
docker compose build --no-cache
docker compose up
```

---

## İletişim

Her türlü soru ve öneri için issue açabilirsiniz.