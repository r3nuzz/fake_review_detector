function loadAnimation(file) {
    document.getElementById("animation").innerHTML = "";
    lottie.loadAnimation({
        container: document.getElementById("animation"),
        renderer: "svg",
        loop: true,
        autoplay: true,
        path: `animations/${file}`
    });
}

async function analyze() {
    const review = document.getElementById("review").value;

    loadAnimation("scan.json");

    const res = await fetch("http://127.0.0.1:5000/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ review })
    });

    const data = await res.json();

    if (data.label === "Fake") {
        loadAnimation("danger.json");
    } else {
        loadAnimation("success.json");
    }

    document.getElementById("result").innerHTML = `Result: ${data.label}`;
    document.getElementById("confidence").innerHTML =
        `Confidence: ${(data.confidence * 100).toFixed(2)}%`;
}