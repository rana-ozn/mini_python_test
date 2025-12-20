import os
import json
from dotenv import load_dotenv
from google import genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

def ai_soru_uret():
    # API key yoksa bile sistem çalışsın
    if not API_KEY:
        print("❌ GEMINI_API_KEY yok, fallback soru dönülüyor")
        return {
            "soru": "Python'da list comprehension ne işe yarar?",
            "siklar": [
                "Listeyi sıralar",
                "Tek satırda liste üretir",
                "Dosya okur",
                "Hata ayıklar",
                "Class oluşturur"
            ],
            "dogru": "Tek satırda liste üretir"
        }

    try:
        client = genai.Client(api_key=API_KEY)

        prompt = (
            "Orta seviye bir yazılım sorusu üret. "
            "Python veya JavaScript olabilir. "
            "5 şık olsun. "
            "SADECE şu formatta JSON döndür: "
            "{"
            "\"soru\": \"...\", "
            "\"siklar\": [\"A\",\"B\",\"C\",\"D\",\"E\"], "
            "\"dogru\": \"...\""
            "}"
        )

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        text = response.text.strip()
        text = text.replace("```json", "").replace("```", "").strip()

        return json.loads(text)

    except Exception as e:
        print("❌ Gemini hata:", e)
        return {
            "soru": "Python'da dictionary hangi parantez ile tanımlanır?",
            "siklar": ["()", "[]", "{}", "<>", "||"],
            "dogru": "{}"
        }
