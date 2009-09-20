
from Predicate import Predicate
import email

class Condition:
    def __init__(self, subject, predicate, object):
        SUBJECTS = {'Subject' : self.subject,
                    'Sender' : self.sender,
                    'To' : self.to,
                    'Cc' : self.cc,
                    'To or cc' : self.toOrCc,
                    'X-Spam-Flag' : self.xSpamFlag,
                    'Reply-To' : self.replyTo}
        if subject in SUBJECTS:
            self.match = SUBJECTS[subject]
        else:
            raise KeyError(subject)
        self.predicate = Predicate(predicate,object)
        self.object = object
        
    def subject(self, email):
        return self.predicate.match(email.get('Subject'))
    def sender(self, email):
        return self.predicate.match(email.get('From'))
    def to(self, email):
        return self.predicate.match(email.get('To'))
    def cc(self, email):
        return self.predicate.match(email.get('Cc'))
    def toOrCc(self, email):
        return self.to(email) or self.cc(email)
    def xSpamFlag(self, email):
        return self.predicate.match(email.get('X-Spam-Flag'))
    def replyTo(self, email):
        return self.predicate.match(email.get('Reply-To'))
