from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def calculate_expenses(contributions, total_amount):
    num_people = len(contributions)
    equal_share = total_amount / num_people
    balances = {person: amount - equal_share for person, amount in contributions.items()}
    creditors = [(p, b) for p, b in balances.items() if b > 0]
    debtors = [(p, -b) for p, b in balances.items() if b < 0]
    transactions = []
    i, j = 0, 0

    while i < len(debtors) and j < len(creditors):
        debtor, debt_amount = debtors[i]
        creditor, credit_amount = creditors[j]
        settled_amount = min(debt_amount, credit_amount)
        transactions.append(f"{debtor} pays {settled_amount:.2f} to {creditor}")
        debtors[i] = (debtor, debt_amount - settled_amount)
        creditors[j] = (creditor, credit_amount - settled_amount)
        if debtors[i][1] == 0:
            i += 1
        if creditors[j][1] == 0:
            j += 1

    return transactions

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.json
    total_amount = float(data["total_amount"])
    contributions = {entry["name"]: float(entry["amount"]) for entry in data["contributors"]}
    transactions = calculate_expenses(contributions, total_amount)
    return jsonify({"transactions": transactions})

if __name__ == "__main__":
    app.run(debug=True)
