from flask import Flask, render_template, jsonify
from ai_questions import ai_soru_uret

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

# ⚠️ DİKKAT: JS BURAYA İSTEK ATIYOR
@app.route("/soru")
def soru():
    soru = ai_soru_uret()
    return jsonify(soru)

if __name__ == "__main__":
    app.run(debug=True)
