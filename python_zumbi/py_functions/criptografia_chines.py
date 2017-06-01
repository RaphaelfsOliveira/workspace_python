msg = 'raphael'

def cript(msg):
    s = ''
    for c in msg:
    	s += chr(ord(c) + 30000)
    return s


def dcript(msg):
	s = ''
	for c in msg:
		s += chr(ord(c) - 30000)
	return s

print(msg)

msg = cript(msg)

print(msg)

msg = dcript(msg)

print(msg)