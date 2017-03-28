'''
python program to implement message flow from tyop layer to bottom later of the OSI model

Author: Victor Mimo


Seven layers of the OSI model are
- Application
- Presentation
- Session
- Transport
- Network
- Data Link
- Physical

confirm if the arbitrary bit stream should be inputted by user
confirm how the ASCII representation would change is not done through string but normal var

Questions

- where do the header bits go/ are they arbitraty
- what layer does IP/port number go - IP goes in network?
- 64 characters with ASCII representation - what does this actually mean do 10 random generated
- does the input stream imply user input or?

'''
import sys


sampleInput = 'avs' # change to make an std input
sampleISize = sys.getsizeof(sampleInput)*8 # returns the memory size in bytes, changed to bits
print 'sample input size',sampleISize

def applicationLayer(buffer, size):
    header = 'aaaa'
    output = buffer + header
    sizeOutput = sys.getsizeof(output)*8
    sizeHeaderandSize = size + sys.getsizeof(header)*8
    sizeHeader = sys.getsizeof(header)*8

    print 'header size', sizeHeader
    print 'size of output when adding buffer and header first is', sizeOutput
    print 'size of output when adding size of input plus size of header is', sizeHeaderandSize
    print  output

    return {'output':output,'size':size}

def presentationLayer(buffer, size):
    header = 'bbbb'
    output = buffer + header
    size = sys.getsizeof(output) * 8
    print output

    return {'output':output,'size':size}

def sessionLayer(buffer, size):
    header = 'cccc'
    output = buffer + header
    size = sys.getsizeof(output) * 8
    print output

    return {'output':output,'size':size}

def transportLayer(buffer, size):
    header = 'dddd'
    output = buffer + header
    size = sys.getsizeof(output) * 8
    print output

    return {'output':output,'size':size}

def networkLayer(buffer, size): #contains IP and port, careful with IP 244.14.23 the 244 is 1 byte not char by char, same with port and bytecount
    header = 'eeee'
    output = buffer + header
    size = sys.getsizeof(output) * 8
    print output

    return {'output':output,'size':size}

def dataLinkLayer(buffer, size): # need to do framing technique thats bytecount, header becomes the count of the buffer message
    header = 'ffff'
    output = buffer + header
    size = sys.getsizeof(output) * 8
    print output

    return {'output':output,'size':size}

def physicalLayer(buffer, size):
    header = 'gggg'
    output = buffer + header
    size = sys.getsizeof(output) * 8
    result = ''.join(format(ord(x), 'b') for x in output) # this is wrong
    #format to separate headers from original message
    print result

    return {'output':output,'size':size}


a = applicationLayer(sampleInput ,sampleISize)
b = presentationLayer(a['output'],a['size'])
c = sessionLayer(b['output'],b['size'])
d = transportLayer(c['output'],c['size'])
e = networkLayer(d['output'],d['size'])
f = dataLinkLayer(e['output'],e['size'])
g = physicalLayer(f['output'],f['size'])

a = ('a', 'b', 'c')
s = '-'
b = 'victor'
print s.join(b)  #join joins b's elements through s

#print g

