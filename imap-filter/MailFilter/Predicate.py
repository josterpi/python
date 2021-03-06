
import re

class Predicate:
    def __init__(self, predicate, object):
        self.PREDICATES = {'contains' : self.contains,
                           'doesn\'t contain' : self.notContains,
                           'is' : self.isMatcher,
                           'isn\'t' : self.isnt,
                           'begins with' : self.beginsWith,
                           'ends with' : self.endsWith}
        self.predicate = predicate
        self.object = object
        if predicate in self.PREDICATES:
            self.matcher_init = self.PREDICATES[predicate](object, True)
        else:
            raise KeyError(predicate)

    def getRegEx(self, predicate, object):
        if predicate in self.PREDICATES:
            return self.PREDICATES[predicate](object)

    def match(self, s):
        return self.PREDICATES[self.predicate](s)

    def contains(self, object, init=False):
        if init:
            return re.compile(object)
        if self.matcher_init.search(object) is not None:
            return True
        else:
            return False
    def notContains(self, object, init=False):
        if init:
            return re.compile(object)
        if self.matcher_init.search(object) is None:
            return True
        else:
            return False
    def isMatcher(self, object, init=False):
        if init:
            return re.compile(object)
        if self.matcher_init.match(object) is not None:
            return True
        else:
            return False
    def isnt(self, object, init=False):
        if init:
            return re.compile(object)
        if self.matcher_init.match(object) is None:
            return True
        else:
            return False
    def beginsWith(self, object, init=False):
        if init:
            return re.compile('^' + object)
        if self.matcher_init.search(object) is not None:
            return True
        else:
            return False
    def endsWith(self, object, init=False):
        if init:
            return re.compile(object + '$')
        if self.matcher_init.search(object) is not None:
            return True
        else:
            return False
