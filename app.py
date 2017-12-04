from flask import Flask,request,Response,render_template
from flask_mail import Mail, Message

app =Flask(__name__)
mail=Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
#app.config['MAIL_PORT'] = 465
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'connectedcontaineralerts@gmail.com'
app.config['MAIL_PASSWORD'] = 'email1234'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route("/sendMail")
def sendMail():
    dict = {'firstName':'Amit','lastName':'Yadav','bodyContent':'breach','location':'Mumbai','signature':'capgemini.com'}
    msg = Message('Hello', sender = 'connectedcontaineralerts@gmail.com', recipients = ['kotharinimit8@gmail.com','nimit.kothari08@gmail.com'])
    #msg.body = "Hello Flask message sent from Flask-Mail"
    msg.html = render_template('email.hmtl',result=dict)
    mail.send(msg)
    return "Sent"

if __name__ == '__main__':
   app.run(debug = True)