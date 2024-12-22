from flask import Flask, request, jsonify
import numpy as np

app = Flask(__name__)

@app.route('/')
def home():
    return "Witaj! Użyj endpointu /predict, aby wysłać dane do predykcji.", 200

def predict(data):
    prediction = np.sum(data)
    return {"prediction": int(prediction)}


@app.route('/predict', methods=['POST'])
def predict_endpoint():
    try:
        data = request.get_json()
        values = data.get("values", [])
        print(f"Otrzymane dane: {values}")

        result = predict(values)
        print(f"Wynik predykcji: {result}")

        return jsonify(result)
    except Exception as e:
        print(f"Błąd: {e}")
        return jsonify({"error": str(e)}), 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
