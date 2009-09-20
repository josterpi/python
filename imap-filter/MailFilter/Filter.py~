
AND = True
OR = False

class Filter:
    def __init__(self, conditions, actions, andOr=AND, name=None, mailbox=None):
        self.name = name
        self.andOr = andOr
        self.conditions = conditions # tuple of conditions
        self.actions = actions # tuple of actions to perform
        self.mailbox = mailbox

    def filter(self, email, mailId, mailbox=None):
        if mailbox is None:
            if self.mailbox is None:
                raise Exception("No mailbox specified")
            else: 
                mailbox = self.mailbox
        if self.andOr is OR:
            for c in self.conditions: # OR
                if c.match(email):
                    for a in self.actions:
                        a.perform(mailId, mailbox)
                    return
        else:
            matches = [c.match(email) for c in self.conditions]
            if sum(matches) == len(matches): # All matches matched
                for a in self.actions:
                    a.perform(mailId, mailbox)

