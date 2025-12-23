let dogruCevap = "";
let aciklamaText = "";
let zorluk = "orta";

function goLevel() {
    document.getElementById("welcome").classList.add("hidden");
    document.getElementById("level").classList.remove("hidden");
}

function setLevel(l) {
    zorluk = l;
    document.getElementById("level").classList.add("hidden");
    document.getElementById("quiz").classList.remove("hidden");
    yeniSoru();
}

async function yeniSoru() {
    const soru = document.getElementById("soru");
    const siklar = document.getElementById("siklar");
    const sonuc = document.getElementById("sonuc");
    const aciklama = document.getElementById("aciklama");

    soru.innerText = "🤖 Yapay zeka düşünüyor...";
    siklar.innerHTML = "";
    sonuc.innerText = "";
    aciklama.innerText = "";

    const res = await fetch(`/soru?zorluk=${zorluk}&t=${Date.now()}`);
    const data = await res.json();

    dogruCevap = data.dogru.trim().toLowerCase();
    aciklamaText = data.aciklama;

    soru.innerText = data.soru;

    data.siklar.forEach(secenek => {
        const d = document.createElement("div");
        d.className = "secenek";
        d.innerText = secenek;
        d.onclick = () => kontrol(secenek, d);
        siklar.appendChild(d);
    });
}

function kontrol(secenek, el) {
    const secenekler = document.querySelectorAll(".secenek");
    secenekler.forEach(s => s.style.pointerEvents = "none");

    const secenekTemiz = secenek.trim().toLowerCase();

    if (secenekTemiz === dogruCevap) {
        el.classList.add("dogru");
        document.getElementById("sonuc").innerText = "✅ Doğru!";
    } else {
        el.classList.add("yanlis");
        document.getElementById("sonuc").innerText = "❌ Yanlış!";
        document.getElementById("aciklama").innerText = aciklamaText;

        secenekler.forEach(s => {
            if (s.innerText.trim().toLowerCase() === dogruCevap) {
                s.classList.add("dogru");
            }
        });
    }
}
