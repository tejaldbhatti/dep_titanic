from flask import Flask, render_template , request 
import pickle

app = Flask(__name__)

#load the model
LR_model = pickle.load(open('titanic_train.pkl','rb'))

@app.route('/')
def hello():
    return render_template('form.html')



@app.route('/submit', methods = ['POST'])
def form_data():
    Pclass = request.form.get('Pclass')
    Age = request.form.get('Age')
    SibSp = request.form.get('SibSp')
    Parch = request.form.get('Parch')
    Fare = request.form.get('Fare')
    Sex_female = request.form.get('Sex_female')
    Sex_male = request.form.get('Sex_male')
    Embarked_C = request.form.get('Embarked_C')
    Embarked_Q = request.form.get('Embarked_Q')
    Embarked_S = request.form.get('Embarked_S')
    Embarked_s = request.form.get('Embarked_s')
    Title_Miss = request.form.get('Title_Miss')
    Title_Mr = request.form.get('Title_Mr')
    Title_Mrs = request.form.get('Title_Mrs')
    Title_Others = request.form.get('Title_Others')

    val_prediction = LR_model.predict([[Pclass,Age,SibSp,Parch,Fare,Sex_female,Sex_male,Embarked_C,Embarked_Q,Embarked_S,Embarked_s,Title_Miss,Title_Mr,Title_Mrs,Title_Others]])
    if val_prediction == 0:
        out = "Not Survived"
    else:
        out = 'Survived'


    return render_template('predict.html', data = f'person is {out}')

if __name__ == '__main__':
    app.run(app.run(host='0.0.0.0', port=8080))

