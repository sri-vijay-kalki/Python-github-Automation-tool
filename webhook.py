#!/usr/bin/env python3  
from flask import Flask, request
from flask_mail import Mail, Message
import json
import urllib.parse

app = Flask(__name__)  

# Configuration for Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False  # Explicitly setting MAIL_USE_SSL to False
app.config['MAIL_USERNAME'] = 'psvkyear2023@gmail.com'
app.config['MAIL_PASSWORD'] = 'skmo tnxn dckl bgnn'  

mail = Mail(app)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = get_data_from_request(request)
    print(data)  
    if 'message' not in data:
        send_mail(data)
    else:
        print(data['message'])
    return "Hello, world!"

def get_data_from_request(request):
    form_data = request.form
        
    # Access the 'payload' field from the form data
    payload = form_data.get('payload')
    
    if payload:
        # Decode the URL-encoded payload 
        # using this process because the request is of content type application/x-www-form-urlencoded
        decoded_payload = urllib.parse.unquote(payload)
        
        try:
            # Try to parse the decoded payload as JSON
            payload_dict = json.loads(decoded_payload)
            
            # Print the received data
            print("Received data:", payload_dict)
            return payload_dict
        except json.JSONDecodeError:
            return {"message": "Error decoding payload"}
    else:
        return {"message": "No valid payload"}

def send_mail(data): 
    try:
        # Extracting information from the payload with default values
        ref = data.get('ref', 'No ref information')
        # print(f"Ref: {ref}")  # Debug print

        pusher = data.get('pusher', {})
        pusher_name = pusher.get('name', 'No pusher name')
        pusher_email = pusher.get('email', 'No pusher email')
        # print(f"Pusher: {pusher_name} ({pusher_email})")  # Debug print

        head_commit = data.get('head_commit', {})
        commit_message = head_commit.get('message', 'No commit message')
        # print(f"Commit Message: {commit_message}")  # Debug print

        author = head_commit.get('author', {})
        author_name = author.get('name', 'No author name')
        author_email = author.get('email', 'No author email')
        author_username = author.get('username', 'No author username')
        # print(f"Author: {author_name} ({author_email}) - @{author_username}")  # Debug print

        compare_url = data.get('compare', 'No compare URL')
        # print(f"Compare URL: {compare_url}")  # Debug print

        # Constructing the email body
        email_body = (
            f'Commit made to the repository:\n'
            f'Ref: {ref}\n'
            f'Pusher: {pusher_name} ({pusher_email})\n'
            f'Commit Message: {commit_message}\n'
            f'Compare URL: {compare_url}\n'
            f'Commit Author: {author_name} ({author_email}) - @{author_username}\n'
            f'This is a test email sent from a Flask application!'
        )
        # print(f"Email Body: {email_body}")  # Debug print

        msg = Message('Message from your GitHub Monitoring Tool',
                      sender='no-reply-github-monitoring@gmail.com',
                      recipients=['psvkyear2023@gmail.com'])
        msg.body = email_body
        mail.send(msg)
        print('Email sent successfully!')
    except Exception as e:
        print(f'Failed to send email: {e}')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
