from flask import Flask,render_template,request
import numpy as np
import pickle
model=pickle.load(open('new_model.pkl','rb'))

app=Flask(__name__)
@app.route('/')
def loan():
    print('API created')

    return render_template('index.html')



@app.route('/prediction',methods=['POST'])
def fun():
    l=['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed',
       'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount',
       'Loan_Amount_Term', 'Credit_History', 'Semiurban', 'Urban']
    print('prediction API created')
    Gender=float(request.form.get(l[0]))
    Married=float(request.form.get(l[1]))
    Dependents=float(request.form.get(l[2]))
    Education=float(request.form.get(l[3]))
    Self_Employed=float(request.form.get(l[4]))
    ApplicantIncome=float(request.form.get(l[5]))
    CoapplicantIncome=float(request.form.get(l[6]))
    LoanAmount=float(request.form.get(l[7]))
    Loan_Amount_Term=float(request.form.get(l[8]))
    Credit_History=float(request.form.get(l[9]))
    Semiurban=float(request.form.get(l[10]))
    Urban=float(request.form.get(l[11]))

    result=model.predict(np.array([[Gender, Married, Dependents,Education,Self_Employed,ApplicantIncome, CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Semiurban,Urban]]))
    if result[0]==1:
        result='Approved'
    else:
        result='Decline'
    print(f'{result=}')
    return render_template('result.html',pred=result)

    

if __name__=='__main__':
    app.run()

