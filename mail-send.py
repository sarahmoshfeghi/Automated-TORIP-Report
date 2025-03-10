
import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_mail(to_addr, Cc, subject):
    with open("/pathtothefile/ip-block.csv", "r") as f:
        if len(f.readlines()) == 0:
            return
    fromaddr = 'test@test.com'
    toaddrs = to_addr
    msg = MIMEMultipart('alternative')
    msg['From'] = fromaddr
    msg['To'] = toaddrs
    msg['Subject'] = subject
    msg['Cc'] = Cc
    text = 'IPBLOCK'
    html = """\
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link href="https://db.onlinewebfonts.com/c/b1dd60ece4e2e12eebf05e575f87225c?family=SG+Kara+Light" rel="stylesheet">
        <style>
            @import url(https://db.onlinewebfonts.com/c/b1dd60ece4e2e12eebf05e575f87225c?family=SG+Kara+Light);
            @font-face {
            font-family: "SG Kara Light";
            src: url("https://db.onlinewebfonts.com/t/b1dd60ece4e2e12eebf05e575f87225c.eot");
            src: url("https://db.onlinewebfonts.com/t/b1dd60ece4e2e12eebf05e575f87225c.eot?#iefix")format("embedded-opentype"),
            url("https://db.onlinewebfonts.com/t/b1dd60ece4e2e12eebf05e575f87225c.woff2")format("woff2"),
            url("https://db.onlinewebfonts.com/t/b1dd60ece4e2e12eebf05e575f87225c.woff")format("woff"),
            url("https://db.onlinewebfonts.com/t/b1dd60ece4e2e12eebf05e575f87225c.ttf")format("truetype"),
            url("https://db.onlinewebfonts.com/t/b1dd60ece4e2e12eebf05e575f87225c.svg#SG Kara Light")format("svg");
            }
            body{
                direction:rtl
            }
            h3{
                font-family: "SG Kara Light";
            }
            p{
                font-family: "SG Kara Light";
            }
            .vuln{
                direction:ltr;
                font-family: "SG Kara Light";
            }

        </style>
    </head>
    <body>
        <br>
        <p class="vuln">https://feodotracker.abuse.ch/downloads/ipblocklist_recommended.txt</br>
https://rules.emergingthreats.net/fwrules/emerging-Block-IPs.txt</br>
https://www.dan.me.uk/torlist/?full
</p>
    </body>
    </html>
    """
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')
    msg.attach(part1)
    msg.attach(part2)
    files = [
        r'/pathtothefile/ip-block.csv']
    for f in files:
        with open(f, "rb") as fil:
            part = MIMEApplication(
                fil.read(),
                Name=basename(f)
            )
            part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
            msg.attach(part)
    server = smtplib.SMTP('mail.abramad.com', 25)
    server.starttls()
    server.sendmail(fromaddr, msg['To'].split(","), msg.as_string())
    server.quit()
