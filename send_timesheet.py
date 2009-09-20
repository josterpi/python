
# From http://docs.python.org/lib/node162.html

import smtplib
import mimetypes
from email import encoders
from email.message import Message
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

COMMASPACE = ', '

outer = MIMEMultipart()
outer['Subject'] = 'Timesheet'
outer['To'] = 'You <you@example.com>'
outer['From'] = 'Me <me@example.com>'

outer.preamble = 'You will not see this in a MIME-aware mail reader.\n'

ctype, encoding = mimetypes.guess_type(path)
if ctype is None or encoding is not None:
    ctype = 'application/octet-stream'

maintype, subtype = ctype.split('/', 1)

fp = open(path, 'rb')
msg = MIMEBase(maintype, subtype)
msg.set_payload(fp.read())
fp.close()
encoders.encode_base64(msg)

msg.add_header('Content-Displosition', 'attachment', filename=filename)
outer.attach(msg)

composed = outer.as_string()

s = smtplib.SMTP()
s.connect()
s.sendmail(sender, recipients, composed)
sl.close()
