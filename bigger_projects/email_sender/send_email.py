import smtplib
import ssl
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import Any 

import credentials


def create_image_attachment(path: str) -> MIMEImage:
    """Create an image attachment from a file path. Needs some preprocessing."""
    raise NotImplementedError("This function is not implemented yet.")


def send_email(to_email: str, subject: str, body: str, image: str | None = None):
    host: str = 'smtp-mail.outlook.com'
    port: int = 587
    
    context = ssl.create_default_context() # Validates host name and certificates
    
    with smtplib.SMTP(host, port) as server:
        print('Logging in')
        server.ehlo() # Greet server
        server.starttls(context=context)
        server.login(credentials.EMAIL_ADDRESS, credentials.EMAIL_PASSWORD)
        
        # Prepare the email
        print('Attempting to send the email')
        msg = MIMEMultipart()
        msg['From'] = credentials.EMAIL_ADDRESS
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        
        if image: 
            file: MIMEImage = create_image_attachment(image)
            msg.attach(file)
            
        server.sendmail(from_addr=credentials.EMAIL_ADDRESS,
                        to_addrs=to_email,
                        msg=msg.as_string())
        
        # Success!
        print('Sent!')
        
if __name__ == '__main__':
    send_email(to_email='...')
        
