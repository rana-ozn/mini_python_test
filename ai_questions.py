import os, json
from dotenv import load_dotenv
from google import genai

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

def ai_soru_uret(zorluk="orta"):
    seviye = {
        "kolay": "kolay seviye",
        "orta": "orta seviye",
        "zor": "zor seviye"
    }.get(zorluk, "orta seviye")

    if not API_KEY:
        return {
            "soru": "Python'da list comprehension ne işe yarar?",
            "siklar": [
                "Listeyi sıralar",
                "Tek satırda liste üretir",
                "Dosya okur",
                "Hata ayıklar",
                "Class oluşturur"
            ],
            "dogru": "Tek satırda liste üretir",
            "aciklama": "List comprehension, Python'da kısa ve okunabilir şekilde liste üretmeyi sağlar."
        }

    try:
        client = genai.Client(api_key=API_KEY)

        prompt = (
            f"{seviye} bir Python veya JavaScript sorusu üret. "
            "Kod içerebilir. "
            "5 şık olsun. "
            "Yanlış cevap için kısa açıklama ekle. "
            "SADECE şu JSON formatında cevap ver:\n"
            "{"
            "\"soru\": \"...\", "
            "\"siklar\": [\"A\",\"B\",\"C\",\"D\",\"E\"], "
            "\"dogru\": \"...\", "
            "\"aciklama\": \"Neden bu cevap doğru?\""
            "}"
        )

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        text = response.text.replace("```json", "").replace("```", "").strip()
        return json.loads(text)

    except Exception:
        return {
            "soru": "Python'da dictionary hangi parantez ile tanımlanır?",
            "siklar": ["()", "[]", "{}", "<>", "||"],
            "dogru": "{}",
            "aciklama": "Dictionary veri tipi süslü parantez {} ile tanımlanır."
        }
