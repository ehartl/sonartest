from flask import Flask, request, jsonify

app = Flask(__name__)

users = {}

class User:
    def __init__(self, name):
        self.name = name
        self.owes = {}
        self.owed_by = {}
        self.balance = 0.0

    def to_dict(self):
        return {
            "name": self.name,
            "owes": self.owes,
            "owed_by": self.owed_by,
            "balance": self.balance
        }

def update_balance(user):
    total_owed = sum(user.owes.values())
    total_owed_by = sum(user.owed_by.values())
    user.balance = total_owed_by - total_owed

@app.route('/users', methods=['GET'])
def get_users():
    requested_users = request.json.get('users', None)
    if requested_users:
        result = [users[name].to_dict() for name in sorted(requested_users)]
    else:
        result = [user.to_dict() for user in sorted(users.values(), key=lambda x: x.name)]
    return jsonify({"users": result})

@app.route('/add', methods=['POST'])
def add_user():
    name = request.json['user']
    if name in users:
        return jsonify({"error": "User already exists"}), 400
    users[name] = User(name)
    return jsonify(users[name].to_dict())

@app.route('/iou', methods=['POST'])
def create_iou():
    lender_name = request.json['lender']
    borrower_name = request.json['borrower']
    amount = request.json['amount']

    if lender_name not in users or borrower_name not in users:
        return jsonify({"error": "User not found"}), 400

    lender = users[lender_name]
    borrower = users[borrower_name]

    borrower.owes[lender_name] = borrower.owes.get(lender_name, 0) + amount
    lender.owed_by[borrower_name] = lender.owed_by.get(borrower_name, 0) + amount

    update_balance(borrower)
    update_balance(lender)

    result = sorted([lender.to_dict(), borrower.to_dict()], key=lambda x: x['name'])
    return jsonify({"users": result})

if __name__ == '__main__':
    app.run(debug=True)