let dogruCevap = "";

async function yeniSoru() {
    const soruEl = document.getElementById("soru");
    const siklarDiv = document.getElementById("siklar");
    const sonucEl = document.getElementById("sonuc");

    // Loading durumu
    soruEl.innerText = "🤖 Yapay zeka düşünüyor...";
    siklarDiv.innerHTML = "";
    sonucEl.innerText = "";

    try {
        const response = await fetch("/soru");

        if (!response.ok) {
            throw new Error("Sunucu cevap vermedi");
        }

        const data = await response.json();

        // Backend güvenli fallback döndürüyor ama yine de kontrol
        if (!data || !data.soru || !data.siklar || !data.dogru) {
            throw new Error("Eksik veri geldi");
        }

        soruEl.innerText = data.soru;
        dogruCevap = data.dogru;

        data.siklar.forEach(secenek => {
            const label = document.createElement("label");
            label.className = "secenek";

            label.innerHTML = `
                <input type="radio" name="cevap">
                <span>${secenek}</span>
            `;

            label.onclick = () => cevapKontrol(secenek, label);
            siklarDiv.appendChild(label);
        });

    } catch (error) {
        console.error("JS HATASI:", error);
        soruEl.innerText = "⚠️ Soru üretilemedi";
        sonucEl.innerText = "Tekrar dene.";
        sonucEl.style.color = "#ff6b6b";
    }
}

function cevapKontrol(secenek, label) {
    const sonucEl = document.getElementById("sonuc");

    // Tüm şıkları kilitle
    document.querySelectorAll(".secenek").forEach(el => {
        el.style.pointerEvents = "none";
    });

    if (secenek === dogruCevap) {
        label.classList.add("dogru");
        sonucEl.innerText = "✅ Doğru!";
        sonucEl.style.color = "#00ffcc";
    } else {
        label.classList.add("yanlis");
        sonucEl.innerText = `❌ Yanlış! Doğru cevap: ${dogruCevap}`;
        sonucEl.style.color = "#ff6b6b";

        // Doğru cevabı vurgula
        document.querySelectorAll(".secenek").forEach(el => {
            if (el.innerText.trim() === dogruCevap) {
                el.classList.add("dogru");
            }
        });
    }
}

// Sayfa açılır açılmaz otomatik soru getir
window.addEventListener("load", yeniSoru);
