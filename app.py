from flask import Flask, render_template, request
import pickle, os
from utils.fertilizer import fertilizer_recommendation
from utils.disease import predict_disease

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

crop_model = pickle.load(open("models/crop_model.pkl", "rb"))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict_crop', methods=['POST'])
def predict_crop():
    values = [float(x) for x in request.form.values()]
    prediction = crop_model.predict([values])[0]
    return render_template('result.html', result=prediction)

@app.route('/predict_fertilizer', methods=['POST'])
def predict_fertilizer():
    N,P,K = int(request.form['N']), int(request.form['P']), int(request.form['K'])
    return render_template('result.html', result=fertilizer_recommendation(N,P,K))

@app.route('/predict_disease', methods=['POST'])
def predict_disease_route():
    file = request.files['image']
    path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(path)
    return render_template('result.html', result=predict_disease(path))

if __name__=='__main__':
    app.run(debug=True)
