
EMAIL = "jeremy@josterpi.com"
PASSWD = ""
SERVER = "mail.jrcorps.com"
FOLDER = "INBOX.sent-mail"

import imaplib
import string
import email
import re
import getpass

PASSWD = getpass.getpass()

mb = imaplib.IMAP4(SERVER)
print "Logging in..."
print mb.login(EMAIL,PASSWD)
print "selecting %s..." % FOLDER
print mb.select(FOLDER)
print "Fetching message..."
print mb.fetch(1, "(RFC822)")
print "Logging out..."
print mb.logout()

