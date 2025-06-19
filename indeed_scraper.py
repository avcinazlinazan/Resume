import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import random

def scrape_indeed_jobs(url):
    # Kullanıcı ajanı ekleyerek gerçek bir tarayıcı gibi davranıyoruz
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        # Sayfayı çek
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # HTTP hatalarını kontrol et
        
        # BeautifulSoup ile HTML'i parse et
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # İş ilanlarını bul
        job_cards = soup.find_all('div', class_='job_seen_beacon')
        
        jobs_data = []
        
        for job in job_cards:
            try:
                # İş başlığı
                title = job.find('h2', class_='jobTitle').text.strip()
                
                # Şirket adı
                company = job.find('span', class_='companyName').text.strip()
                
                # Lokasyon
                location = job.find('div', class_='companyLocation').text.strip()
                
                # Maaş bilgisi (varsa)
                salary = job.find('div', class_='salary-snippet')
                salary = salary.text.strip() if salary else "Belirtilmemiş"
                
                # İş tanımı
                description = job.find('div', class_='job-snippet')
                description = description.text.strip() if description else "Belirtilmemiş"
                
                # Veriyi listeye ekle
                jobs_data.append({
                    'İş Başlığı': title,
                    'Şirket': company,
                    'Lokasyon': location,
                    'Maaş': salary,
                    'Açıklama': description
                })
                
            except Exception as e:
                print(f"İş ilanı işlenirken hata oluştu: {e}")
                continue
        
        # DataFrame oluştur
        df = pd.DataFrame(jobs_data)
        
        # Excel dosyasına kaydet
        df.to_excel('indeed_jobs.xlsx', index=False)
        print(f"Toplam {len(jobs_data)} iş ilanı başarıyla kaydedildi.")
        
        return df
        
    except Exception as e:
        print(f"Hata oluştu: {e}")
        return None

if __name__ == "__main__":
    url = "https://tr.indeed.com/jobs?q=data+scientist&l=&from=searchOnHP&from=gnav-util-jobsearch--indeedmobile&vjk=c740f4dcd975f8dd"
    jobs_df = scrape_indeed_jobs(url) 