from flask import Flask, render_template, Response,redirect,request,url_for
import load_model

app = Flask(__name__)

accuracy = load_model.accuracy_score
list1=[]
@app.route('/')
def index():
    return render_template("index(2).html")

@app.route('/Home',methods=['POST','GET'])
def Home():
    if request.method=='POST':
        user = request.form['username']
        list1.append(user)
        return redirect(url_for("Home2"))

@app.route('/Home2')
def Home2():
    return render_template("index.html")

@app.route('/heart')
def heart():
    return render_template('index_heart.html')
@app.route('/diabetes')
def diabetes():
    return render_template('index_diabetes.html')

@app.route('/diab_symptoms')
def diab_symptoms():
    return render_template("diabetes_symptoms.html")

@app.route('/result_diab/<int:ans>')
def result_diab(ans):
    result_dia=""
    if ans==0:
        result_dia="We are glad to inform you that you don't show any signs of diabates.."
    else:
        result_dia = "We are sorry to inform you that you show signs of diabates."
    return render_template('diabetes_result.html', answer=result_dia)

@app.route('/heart_symptoms')
def heart_symptoms():
    return render_template("heart_symptoms.html")

@app.route('/result_heart/<int:ans>')

def result_heart(ans):

    return  render_template('heart_result.html', answer=ans)



@app.route('/submit',methods = ['POST','GET'])
def submits():
    list=[]
    if request.method=='POST':
        preg = int(request.form['preg'])
        list.append(preg)
        gluco = int(request.form['glucose'])
        list.append(gluco)
        B_P = int(request.form['bp'])
        list.append(B_P)
        STL = int(request.form['stl'])
        list.append(STL)
        I_L = int(request.form['il'])
        list.append(I_L)
        BMI = float(request.form['bmi'])
        list.append(BMI)
        DPFV = float(request.form['dpfv'])
        list.append(DPFV)
        Age = int(request.form["age"])
        list.append(Age)
        res = load_model.diab_prediction(list)
    return redirect(url_for("result_diab", ans=res))

@app.route('/submit_heart',methods = ['POST','GET'])
def submit_heart():
    list=[]
    age = int(request.form['age'])
    list.append(age)
    sex = int(request.form["options"])
    list.append(sex)
    cp = int(request.form['chestpain'])
    list.append(cp)
    rbp = int(request.form['rbp'])
    list.append(rbp)
    sc = int(request.form['sc'])
    list.append(sc)
    fbs = int(request.form['fbs'])
    list.append(fbs)
    rer = int(request.form['rer'])
    list.append(rer)
    mhr = int(request.form['mhr'])
    list.append(mhr)
    eia = int(request.form['eia'])
    list.append(eia)
    std = float(request.form['std'])
    list.append(std)
    slope = int(request.form['slope'])
    list.append(slope)
    mv = int(request.form['mv'])
    list.append(mv)
    thal = int(request.form['thal'])
    list.append(thal)
    model = load_model.heart_prediction(list)
    final_ans = model[0]
    return redirect(url_for("result_heart", ans=final_ans))


if __name__ == "__main__":
    app.run(debug=True)
