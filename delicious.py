
from datetime import datetime, timedelta
from time import sleep
import urllib2
from urllib import urlencode
import libxml2
from xml.dom.minidom import parse

API = "https://api.del.icio.us/v1/"
AUTH_REALM = "del.icio.us API"
AUTH_URL = "api.del.icio.us"


class Delicious:
    def __init__(self, user, passwd):
        auth_handler = urllib2.HTTPBasicAuthHandler()
        auth_handler.add_password(AUTH_REALM, AUTH_URL, user, passwd)
        opener = urllib2.build_opener(auth_handler)
        opener.addheaders = [('User-agent', 'josterpi-del.icio.us')]
        urllib2.install_opener(opener)
        self.last_call = datetime.now() - timedelta(minutes=1)

    def _call(self, call, **args):
        # Returns file-like object
        # TODO: Handle HTTP error codes: 503, 401, 404
        request = "%s%s?%s" % (API, call, urlencode(args))
        # Throttle: 1 call/sec
        if (datetime.now() - self.last_call) < timedelta(seconds=1):
            sleep(1.2)
        reply = self.parse_reply(urllib2.urlopen(request))
        self.last_call = datetime.now()
        return reply

    def _call_factory(self, call):
        def _caller(**args):
            return self._call(call, **args)
        return _caller

    def parse_reply(self, xml):
        dom = parse(xml)
        name = dom.documentElement.nodeName
        print name
        if name == 'posts':
            klass = Post
        elif name == 'tags':
            klass = Tag
        else:
            klass = Element
        return [klass(element) for element in dom.getElementsByTagName(name[:-1])]
    def __getattr__(self, name):
        if name != '':
            return self._call_factory('/'.join(name.split('_')))

class Element(object):
    supported_attribs = ()
    def __init__(self, element):
        try:
            if element.nodeName != self.__class__.__name__.lower():
                raise Exception
        except:
            raise Exception("not an element")
        for attrib in self.supported_attribs:
            if element.hasAttribute(attrib):
                attrib_value = self.process_attribs(attrib, element.getAttribute(attrib))
                setattr(self, attrib, attrib_value)
    def process_attribs(self, attrib, attrib_value):
        return attrib_value
    def __repr__(self):
        return "<%s: %s>" % (self.__class__.__name__, getattr(self, self.supported_attribs[0]))

class Post(Element):
    supported_attribs = ('href', 'description',  'hash', 'tag', 'time')
    def process_attribs(self, attrib, attrib_value):
        if attrib not in ('tag', ):
            return attrib_value
        # process specials
        if attrib == 'tag':
            return attrib_value.split(' ')
        #elif attrib == 'time':
        #    return strptime(attrib_value, '%Y-%m-%dT%H:%M:%SZ')

class Tag(Element):
    supported_attribs = ('tag', 'count')
