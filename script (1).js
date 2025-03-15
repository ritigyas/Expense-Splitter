let contributors = [];

function addPerson() {
    const container = document.getElementById("contributors");
    const div = document.createElement("div");
    div.innerHTML = `<input type="text" placeholder="Name"> <input type="number" placeholder="Amount">`;
    container.appendChild(div);
    contributors.push(div);
}

function calculateExpenses() {
    let totalAmount = parseFloat(document.getElementById("totalAmount").value);
    let data = { total_amount: totalAmount, contributors: [] };

    contributors.forEach(div => {
        let inputs = div.getElementsByTagName("input");
        let name = inputs[0].value;
        let amount = parseFloat(inputs[1].value);
        if (name && !isNaN(amount)) {
            data.contributors.push({ name: name, amount: amount });
        }
    });

    fetch("/calculate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("result").innerHTML = data.transactions.join("<br>");
    })
    .catch(error => console.error("Error:", error));
}
