from xml.dom.minidom import parse

dom = parse("dane.xml")
name = dom.getElementsByTagName('name')
kod = dom.getElementsByTagName('kod')
url = dom.getElementsByTagName('url')
psw = dom.getElementsByTagName('passwd')

print(" ".join(t.nodeValue for t in name[0].childNodes if t.nodeType == t.TEXT_NODE))
print(" ".join(t.nodeValue for t in url[0].childNodes if t.nodeType == t.TEXT_NODE))
print(" ".join(t.nodeValue for t in kod[0].childNodes if t.nodeType == t.TEXT_NODE))
print(" ".join(t.nodeValue for t in url[1].childNodes if t.nodeType == t.TEXT_NODE))
print(" ".join(t.nodeValue for t in kod[1].childNodes if t.nodeType == t.TEXT_NODE))
print(" ".join(t.nodeValue for t in psw[0].childNodes if t.nodeType == t.TEXT_NODE))
