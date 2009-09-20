
import imaplib

TRASH = "INBOX.Trash"

class Action:
    def __init__(self, mailbox, action, value=None):
        ACTIONS = {'Move to folder' : self.moveToFolder,
                   'Copy to folder' : self.copyToFolder,
                   'Change priority' : self.changePriority,
                   'Label' : self.label,
                   'JunkScore' : self.junkScore,
                   'Mark read' : self.markRead,
                   'Mark flagged' : self.markFlagged,
                   'Delete' : self.delete}
        if isinstance(mailbox,imaplib.IMAP4):
            self.mailbox = mailbox
        else:
            raise TypeError('Mailbox must be of type imaplib.IMAP4')
        if action in ACTIONS:
            self.action = action
        else:
            raise KeyError('\'action\' must be in ' + str(ACTIONS.keys()))
        self.value = value
        self.perform = ACTIONS[action]

    def moveToFolder(self, mailId, mailbox=None, value=None):
        if mailbox is None:
            mailbox = self.mailbox
        if value is None:
            value = self.value
        mailbox.copy(mailId, value)
        mailbox.store(mailId, '+FLAGS.SILENT', '\\Deleted')
        
    def copyToFolder(self, mailId, mailbox=None, value=None):
        if mailbox is None:
            mailbox = self.mailbox
        if value is None:
            value = self.value
        mailbox.copy(mailId, value)
        
    def changePriority(self, mailId, mailbox=None, value=None):
        if mailbox is None:
            mailbox = self.mailbox
        if value is None:
            value = self.value

    def label(self, mailId, mailbox=None, value=None):
        if mailbox is None:
            mailbox = self.mailbox
        if value is None:
            value = self.value
        LABELS = {1:'($Label1)', 2:'($Label2)', 3:'($Label3)', 4:'($Label4)', 5:'($Label5)'}
        mailbox.store(mailId, '+FLAGS.SILENT', LABELS[value])

    def junkScore(self, mailId, mailbox=None, value=None):
        if mailbox is None:
            mailbox = self.mailbox
        if value is None:
            value = self.value
        if value == 100:
            mailbox.store(mailId, '+FLAGS.SILENT', '(Junk)')
        else:
            mailbox.store(mailId, '+FLAGS.SILENT', '(NonJunk)')

    def markRead(self, mailId, mailbox=None):
        if mailbox is None:
            mailbox = self.mailbox
        mailbox.store(mailId, '+FLAGS.SILENT', '\\Seen')

    def markFlagged(self, mailId, mailbox=None):
        if mailbox is None:
            mailbox = self.mailbox
        mailbox.store(mailId, '+FLAGS.SILENT', '\\Flagged')

    def delete(self, mailId, mailbox=None):
        if mailbox is None:
            mailbox = self.mailbox
        # Actually, move to Trash. Error check of course
        mailbox.copy(mailId, TRASH)
        mailbox.store(mailId, '+FLAGS.SILENT', '\\Deleted')
