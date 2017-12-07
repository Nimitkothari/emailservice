from flask import Flask,request,Response,render_template
from flask_mail import Mail, Message
import os

app =Flask(__name__,template_folder='/home/vcap/templates')
port = int(os.getenv("PORT", 3000))
mail=Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
#app.config['MAIL_PORT'] = 465
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = ''
app.config['MAIL_PASSWORD'] = ''
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)
@app.route("/sendMail/",methods=['GET'])
def sendMail():
    try:
        dict = {'firstName':'Amit','lastName':'Yadav','bodyContent':'breach','location':'Mumbai','signature':'capgemini.com'}
        msg = Message('Hello', sender = 'connectedcontaineralerts@gmail.com', recipients = ['nimit.kothari08@gmail.com'],cc=['kotharinimit8@gmail.com'],bcc=['kotharinimit8@outlook.com'])
        msg.body = "Hello Flask message sent from Flask-Mail"
        print("entering rendering template")
        print('pwd',os.getcwd())
        #msg.html = render_template('index.html',result=dict)
        print('befor sending msg')
        mail.send(msg)
        return 'sent'
    except Exception as e:
        print(e)

if __name__ == '__main__':
    #app.run(host='0.0.0.0',port=port)
    app.run(port=port)
