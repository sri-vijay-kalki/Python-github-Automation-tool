# GitHub Webhook Email Notification Tool

## Overview

This project consists of a Flask web application that listens for GitHub webhook events and sends email notifications about commits made to a repository. Additionally, it includes a PowerShell script to automate committing and pushing changes to a GitHub repository for testing purposes.

## Features

- Flask web application to handle GitHub webhook events.
- Sends email notifications with commit details.
- PowerShell script to automate commit and push operations for testing.

## Requirements

- Python 3.x
- Flask
- Flask-Mail
- PowerShell
- Git

## Installation

### Flask Web Application

1. **Clone the repository:**

   ```sh
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
2. **Install the required packages:**
    
    ```sh
    Copy code
    pip install Flask Flask-Mail

3. **Set up your email configuration**
    
    ```sh
    Open the webhook.py file and configure the following settings with your email credentials:
    app.config['MAIL_USERNAME'] = 'your-email@gmail.com'
    app.config['MAIL_PASSWORD'] = 'your-email-password'

4. **To test the functionality**
    open powershell in current directory run executeSampleTest.ps1