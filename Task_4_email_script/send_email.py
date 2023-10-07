import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

"""
Please Change "recipient_email" in the end of the code where function is called.
"""

html_table = """
<!DOCTYPE html>
<html>
<head>
<style>
table {
  font-family: Arial, sans-serif;
  border-collapse: collapse;
  width: 50%;
}

th, td {
  border: 1px solid #dddddd;
  text-align: left;
  padding: 8px;
}

tr:nth-child(even) {
  background-color: #f2f2f2;
}
</style>
</head>
<body>

<h2>Sample HTML Table</h2>

<table>
  <tr>
    <th>Name</th>
    <th>Age</th>
    <th>City</th>
  </tr>
  <tr>
    <td>Arth Patel</td>
    <td>24</td>
    <td>Vadodara</td>
  </tr>
  <tr>
    <td>Akash Rana</td>
    <td>31</td>
    <td>Pune</td>
  </tr>
  <tr>
    <td>Hirva Sing</td>
    <td>35</td>
    <td>Mumbai</td>
  </tr>
</table>

</body>
</html>
"""


def send_now(recipient_email):
    sender_email = "arthpatelbooks@gmail.com"
    sender_password = "vnbg ehbo zxjs bprq"

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = recipient_email
    message["Subject"] = "Sample HTML Table"

    message.attach(MIMEText(html_table, "html"))

    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()

    print('Processing.....')
    server.login(sender_email, sender_password)

    server.sendmail(sender_email, recipient_email, message.as_string())

    server.quit()

    print("Email with HTML table sent successfully.")


if __name__ == '__main__':
    # Please change recipient_email
    send_now(recipient_email="arthpatel.ce@gmail.com")
