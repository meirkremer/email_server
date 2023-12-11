from flask import Flask, render_template, request
from flask_mail import Mail, Message
from config import conf

app = Flask(__name__)

# Configure Flask-Mail settings
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = conf['sender_email']
app.config['MAIL_PASSWORD'] = conf['password']

mail = Mail(app)


@app.route('/send_email', methods=['POST'])
def send_email():
    if request.method == 'POST':
        to_address = request.form.get('to_address')
        subject = request.form.get('subject')
        body = request.form.get('body')
        print(to_address, subject, body)

        # Create a Message object
        message = Message(subject=subject,
                          recipients=to_address.split(', '),
                          body=body)

        # Send the email
        mail.send(message)

        return 'Email sent successfully'


@app.route('/receive-email', methods=['POST'])
def receive_email():
    data = request.get_data(as_text=True)
    print(f"Received Pub/Sub message: {data}")
    # Implement your notification handling logic here
    # This could include sending system notifications, emails, etc.
    return 'OK', 200


if __name__ == '__main__':
    app.run()
