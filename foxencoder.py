table = [' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',"0","1","2","3","4","5","6","7","8","9","!","@","#","$","%","^","&","*","","đĢ","âšī¸","đ","đ¤","đ","â­","â ī¸","đ","đ","đ¤Ą","âī¸","đĄ","đ§Š","đļ","đĻ","đģ","đž","đŽ","đ¤Ž","đĒ","â","đ ","đ","đŗī¸âđ"]

def encodestr(stri):
 pwrd = ""
 for x in range(0, len(stri), 1):
  char = stri[x:x + 1]
  foundch = False
  if char in table:
   if table.index(char):
    char = table[(table.index(char) + ((x + 1 * 3) % 5)) % len(table)]
  pwrd = pwrd+char
 return pwrd

def decodestr(stri):
 pwrd = ""
 for x in range(0, len(stri), 1):
  char = stri[x:x + 1]
  foundch = False
  if char in table:
   if table.index(char):
    char = table[(table.index(char) - ((x + 1 * 3) % 5)) % len(table)]
  pwrd = pwrd+char
 return pwrd