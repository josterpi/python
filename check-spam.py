#!/usr/bin/python -O

EMAIL = "jeremy@josterpi.com"
PASSWD = ""
SERVER = "mail.jrcorps.com"
FOLDER = "INBOX.junk"

import imaplib
import string
import email
import re
import getpass

class Mailbox:
	def __init__(self, email=EMAIL, passwd=PASSWD, server=SERVER, folder=FOLDER):
		self.email = email
		self.passwd = passwd
		self.server = server
		self.folder = folder
		self.mbsize = 0
		self.mailbox = None

	def open(self):
		self.mailbox = imaplib.IMAP4(self.server)
		type, data = self.mailbox.login(self.email,self.passwd)
		if type != 'OK':
			print "Login Failed"
		type, self.mbsize = self.mailbox.select(self.folder)
		self.mbsize = int(self.mbsize[0])
		if type != 'OK':
			print "Select %s failed" % self.folder

	def close(self):
		self.mailbox.logout()
	
	def get_origin_ip(self,message):
		"""
		1) Go last to first
		2) header must start with "from"
		3) must have an ip address
		4) ip address can't be a private address: localhost or 10.*
		"""
		received_headers = message.get_all("Received")
		received_headers.reverse()
		ip_addr_re = re.compile("(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})")
		for ip_str in received_headers:
			if ip_str.startswith("from"):
				ip_addr = ip_addr_re.search(ip_str)
				if (ip_addr is not None) and (ip_addr.group() != '127.0.0.1') and (not ip_addr.group().startswith('10.')):
					return ip_addr.group()

	def get_origin_ips(self, callback=None):
		ips = {}
		for i in range(1,self.mbsize-1):
			message = self.get_message(i)
			if callback:
				message = callback(message)
			orig_ip = self.get_origin_ip(message)
			ips[orig_ip] = ips.get(orig_ip,0) + 1
		return ips

	def get_message(self, num, msg_parts="(RFC822)"):
		type,data = self.mailbox.fetch(num, msg_parts)
		message = email.message_from_string(data[0][1])
		return message

def process_spam_headers(message):
	if message.get("X-Spam-Flag"):
		# We want the second payload
		# then, take the string, delete the line between the attachement
		# headers and the original headers, then parse it back into email.
		message = email.message_from_string(message.get_payload(1).as_string().replace("\n\n","\n",1))
	return message
	
def main():
	PASSWD = getpass.getpass()
	junk = Mailbox(EMAIL, PASSWD, SERVER, FOLDER)
	junk.open()
	ips = junk.get_origin_ips(process_spam_headers)
	for a,b in ips.iteritems():
		print "%s\t%d" % (a,b)

if __name__ == '__main__':
	main()


