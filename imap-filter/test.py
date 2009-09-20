
import getpass
import imaplib
import email

login = "josterhouse@gmail.com"
passwd = getpass.getpass()
server = "imap.gmail.com"
folder = "INBOX"

mailbox = imaplib.IMAP4(server)
mailbox.login(login,passwd)
mailbox.select(folder)

def get_header(num, msg_parts="(BODY.PEEK[HEADER])"):
    type,data = mailbox.fetch(num, msg_parts)
    message = email.message_from_string(data[0][1])
    return message
def get_message(num, msg_parts="(RFC822)"):
    type,data = mailbox.fetch(num, msg_parts)
    message = email.message_from_string(data[0][1])
    return message


