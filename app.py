from flask import Flask, request, jsonify
from flask import *  
from flask_cors import CORS
import tensorflow as tf
import pickle
from tensorflow.keras.preprocessing.sequence import pad_sequences


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

cors = CORS(app, resources={r"*": {"origins": "*"}})

model = tf.keras.models.load_model("results/ClassificationModel2.h5", custom_objects={'f1_metric': None})
pickleFile = open("results/tokenizer.pkl", 'rb')
tokenizer = pickle.load(pickleFile)



@app.route('/',  methods = ['GET', 'POST'])
def IsFake():
    name = request.args.get('name')
    X = tokenizer.texts_to_sequences([name])
    X = pad_sequences(X, maxlen=30, padding='post')
    result = model.predict(X)[0][0]
    if result <= 0.373775:
        response_body = {
        "Prediction": "Normal",
        "confidence":  str(1 - result)

    }
    else:
        response_body = {
        "Prediction": "Fake",
        "confidence": str(result) 
    }

    print(result)
    
    return jsonify(response_body)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)