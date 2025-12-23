from flask import Flask, render_template, jsonify, request
from ai_questions import ai_soru_uret

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

# JS buraya istek atıyor
@app.route("/soru")
def soru():
    zorluk = request.args.get("zorluk", "orta")
    return jsonify(ai_soru_uret(zorluk))

if __name__ == "__main__":
    app.run(debug=True)
