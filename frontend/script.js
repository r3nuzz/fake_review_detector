let fakeCount = 0;
let genuineCount = 0;
let chart;

function updateChart(label) {

    if (label === "Fake") {
        fakeCount++;
    } else {
        genuineCount++;
    }

    const ctx = document.getElementById('reviewChart').getContext('2d');

    if (chart) chart.destroy();

    chart = new Chart(ctx, {
        type: 'pie',
        data: {
            labels: ['Fake', 'Genuine'],
            datasets: [{
                data: [fakeCount, genuineCount],
                backgroundColor: ['#ff4d4d', '#4CAF50']
            }]
        }
    });
}

async function analyze() {

    const review = document.getElementById("review").value;

    const res = await fetch("http://127.0.0.1:5000/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ review })
    });

    const data = await res.json();

    if (data.error) {
        alert(data.error);
        return;
    }

    document.getElementById("result").innerHTML =
        "Result: " + data.label;

    document.getElementById("confidence").innerHTML =
        "Confidence: " + (data.confidence * 100).toFixed(2) + "%";

    document.getElementById("progressBar").style.width =
        (data.confidence * 100) + "%";

    updateChart(data.label);
}