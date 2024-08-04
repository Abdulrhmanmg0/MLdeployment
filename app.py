from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)
model = joblib.load('model.joblib')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    features = [
        data['Clump'],
        data['UnifSize'],
        data['UnifShape'],
        data['MargAdh'],
        data['SingEpiSize'],
        data['BareNuc'],
        data['BlandChrom'],
        data['NormNucl'],
        data['Mit']
    ]
    prediction = model.predict([features])[0]
    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(debug=True)
