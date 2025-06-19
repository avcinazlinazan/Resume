from models import ResumeStructured
import openai
import os
import json
import re

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_structured_resume(text: str) -> ResumeStructured:
    
    prompt = f"""
Aşağıdaki özgeçmiş metnini oku ve bana şu alanlarda yapılandırılmış SADECE GEÇERLİ BİR JSON döndür:
- title (ünvan)
- summary (kısa özet)
- experiences (her biri: company ve summary)
- skills (teknik beceriler)
- soft_skills (kişisel beceriler)
- certificates (varsa sertifikalar)
- languages (konuşulan diller)
Açıklama ekleme, sadece geçerli bir JSON döndür.

Metin:
{text}
"""
    client = openai.OpenAI(api_key=openai.api_key)
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "Sen bir insan kaynakları asistanısın."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2,
        max_tokens=1024
    )
    content = response.choices[0].message.content
    print("OpenAI yanıtı:", content)

    # Kod bloğu işaretlerini ve baştaki 'json' kelimesini temizle
    content = re.sub(r"^```json\\s*|^```|```$", "", content.strip(), flags=re.MULTILINE | re.IGNORECASE).strip()
    content = re.sub(r"^json\\s*", "", content, flags=re.IGNORECASE).strip()
    # Sadece ilk JSON objesini ayıkla
    match = re.search(r'({.*})', content, re.DOTALL)
    if match:
        json_str = match.group(1)
    else:
        raise ValueError(f"Yanıtta JSON bulunamadı: {content}")
    try:
        data = json.loads(json_str)
    except Exception as e:
        print("JSON parse hatası:", e)
        raise ValueError(f"OpenAI'dan geçerli bir JSON gelmedi: {json_str}")
    return ResumeStructured(**data)