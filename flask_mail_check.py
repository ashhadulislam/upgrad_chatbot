from threading import Thread
from flask import Flask
from flask_mail import Mail, Message
from email_config import Config
gmail_credentials = Config()
app = Flask(__name__)


mail_settings = {
         "MAIL_SERVER": 'smtp.gmail.com',
         "MAIL_PORT": 465,
         "MAIL_USE_TLS": False,
         "MAIL_USE_SSL": True,
         "MAIL_USERNAME": gmail_credentials[0],
         "MAIL_PASSWORD": gmail_credentials[1]
     }

app.config.update(mail_settings)
mail = Mail(app)


def send_async_email(app, recipient, response):
     with app.app_context():
          if '<mailto' in recipient:
            recipient = recipient.split("|",1)[1]
            recipient = recipient.split(">",1)[0]
          print(recipient)
          msg = Message(subject="Restaurant Details", sender=gmail_credentials[0], recipients=[recipient])
          msg.html =u'<h2>Foodie has found few restaurants for you:</h2>'
          restaurant_names = response['restaurant_name'].values
          restaurant_photo = response['restaurant_photo'].values
          restaurant_location = response['restaurant_address'].values
          restaurant_url = response['restaurant_url'].values
          restaurant_budget = response['budget_for2people'].values
          restaurant_rating = response['restaurant_rating'].values
          for i in range(len(restaurant_names)):
               name = restaurant_names[i]
               location = restaurant_location[i]
               image = restaurant_photo[i]
               url = restaurant_url[i]
               budget = restaurant_budget[i]
               rating = restaurant_rating[i]
                    #msg.body +="This is final test"
               msg.html += u'<h3>{name} (Rating: {rating})</h3>'.format(name = name, rating = rating)
               msg.html += u'<h4>Address: {locality}</h4>'.format(locality = location)
               msg.html += u'<h4>Average Budget for 2 people: Rs{budget}</h4>'.format(budget = budget)
               msg.html += u'<div dir="ltr">''<a href={url}><img height = "325", width = "450", src={image}></a><br></div>'.format(url = url, image = image)

          mail.send(msg)

def send_email(recipient, response):
     thr = Thread(target=send_async_email, args=[app, recipient,response])
     thr.start()