from flask import Flask, render_template

app = Flask(__name__)

# Sorular: [Soru metni, [Seçenekler], Doğru cevap]
sorular = [
    ["Python'da değişken tanımlamak için hangi sembol kullanılır?", ["=", "==", ":"], "="],
    ["Hangisi Python listesine örnektir?", ["[1,2,3]", "{1,2,3}", "(1,2,3)"], "[1,2,3]"],
    ["Python yorum satırı nasıl yazılır?", ["// yorum", "# yorum", "/* yorum */"], "# yorum"],
    ["Python'da fonksiyon tanımlamak için hangi anahtar kelime kullanılır?", ["def", "function", "fun"], "def"],
    ["Python 3'te bir yazıyı ekrana yazdırmak için hangi fonksiyon kullanılır?", ["echo()", "print()", "write()"], "print()"]
]

@app.route('/', methods=['GET', 'POST'])
def home():
    # Puanlama frontend'de JS ile yapılacak
    return render_template('index.html', sorular=sorular)

if __name__ == '__main__':
    app.run(debug=True)

