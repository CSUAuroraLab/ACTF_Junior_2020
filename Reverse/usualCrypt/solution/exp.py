import base64
#flag = 'flag{bAse64_h2s_a_Surprise}'
enflag = 'zMXHz3TIgnxLxJhFAdtZn2fFk3lYCrtPC2l9' #'ZmxhZ3tiONXlXJhfaQFzN2FfK3LycRTpc2L9'
input_s = ''
dic = 'ABCDEFQRSTUVWXYPGHIJKLMNOZabcdefghijklmnopqrstuvwxyz0123456789+/'
sdic = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

tab = str.maketrans(dic,sdic)

enflag_l = list(enflag)
for i in range(len(enflag)):
  if enflag[i].isupper():
    enflag_l[i] = chr(ord(enflag[i])+32)
  if enflag[i].islower():
    enflag_l[i] = chr(ord(enflag[i])-32)
print(enflag_l)
enflag = str(enflag_l)

input_s = base64.b64decode(enflag.translate(tab).encode("utf-8"))
print(input_s)
