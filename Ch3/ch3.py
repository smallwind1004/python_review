########################
#ch3_5 bin
x3_5 = 0b00001001
print(x3_5)
y3_5 = 13
print(bin(y3_5))
'''======output======'''
# 9
# 0b1101

########################
#ch3_6 oct
x3_6 = 0o57
print(x3_6)
y3_6 = 64
print(oct(y3_6))
'''======output======'''
# 47
# 0o100

########################
#ch3_7 hex
x3_7 = 0x5d
print(x3_7)
y3_7 = 255
print(hex(y3_7))
'''======output======'''
# 73
# 0xff

########################
#ch3_10 math func
x3_9 = -10.25
y3_9 = 2
print('abs: ', abs(x3_9))
print('pow: ', pow(x3_9, y3_9))
print('round: ', round(x3_9))
print('round n: ', round(x3_9, y3_9))
'''======output======'''
# abs: 10.25
# pow: 100.0625
# round: -10
# round n: -10.25

########################
#3_ex complex
x_ex = 6+9j
print(x_ex.real)
print(x_ex.imag)
'''======output======'''
# 6.0
# 9.0

########################
# ch3_22 the 'r'string
str_3_22_1 = 'hello\nworld'
str_3_22_2 = r'hello\nworld'
print(str_3_22_1)
print(str_3_22_2)
'''======output======'''
# hello
# world
# hello\nworld

########################
#ch3_ASCII
x3_char = 'a'
y3_ascii = 49
print(ord(x3_char))
print(chr(y3_ascii))
'''======output======'''
# 97
# 1

########################
#ch3_23 unicode
x3_24 = '亞'
print(hex(ord(x3_24)))
'''======output======'''
# 0x4e9e

########################
#ch3_byte***
str_eng = 'abc'
str_eng_byte = str_eng.encode('utf-8')
print('str_eng_byte -->')
print('type: ', type(str_eng_byte))
print('len : ', len(str_eng_byte))
print('=> ', str_eng_byte)
str_ch = '劉宇翔'
str_ch_byte = str_ch.encode('utf-8')
print('str_ch_byte -->')
print('type: ', type(str_ch_byte))
print('len : ', len(str_ch_byte))
print('=> ', str_ch_byte)

print('utf-8 decode -->')
print(str_ch_byte.decode('utf-8'))
'''======output======'''
# str_eng_byte -->
# type:  <class 'bytes'>
# len :  3
# =>  b'abc'
# str_ch_byte -->
# type:  <class 'bytes'>
# len :  9
# =>  b'\xe5\x8a\x89\xe5\xae\x87\xe7\xbf\x94'
# utf-8 decode -->
# 劉宇翔

########################
########################
#project 3-7-1
dist = 384400 # earth to moon
speed = 1225 # 1Mach
tot = dist // speed
print('total hours:', tot)
print('total:', tot // 24, 'days and', tot % 24, 'hour(s)')
'''======output======'''
# total hours: 313
# total: 13 days and 1 hour(s)

########################
# ch3_25
dist = 384400
speed = 1225
tot = dist // speed
days, mins = divmod(tot, 24)
print('total time...')
print(days, 'day', mins, 'min')

########################
########################
#project 3-7-2
dot1x, dot1y = 1, 8
dot2x, dot2y = 3, 10
line_dist = ((dot1x - dot2x) ** 2 + (dot1y - dot2y) ** 2) ** 0.5
print('two dot dist. is...')
print(line_dist)
'''======output======'''
# two dot dist. is...
# 2.8284271247461903

########################
########################
# CH3 practice
# Q1.
'''
a = 10, b = 18, c = 5
'''
a = 10
b = 18
c = 5
print('(a)=>', a + b - c)
print('(b)=>', 2 * a + 3 - c)
print('(c)=>', b * c + 20 / b)
print('(d)=>', a % c * b + 10)
print('(e)=>', a ** c - a * b * c)

# Q4.
'''
earth to moon 384400km, jet speed 250km/min
how long to arrival ? day ? hour ? mmin
'''
dist = 384400
speed = 250
total_min = (384400 // 250)
tot_min = total_min % 60
tot_hour = (total_min // 60) % 24
tot_day = (total_min // 60) // 24
print('total times...')
print('test', total_min)
print(tot_day, 'day', tot_hour, 'hour', tot_min, 'min')

# Q5.
'''
name unicode in 10
'''
name1 = '劉'
name2 = '宇'
name3 = '翔'
print('10=>', ord(name1), ord(name2), ord(name3))

# Q6.
'''
name unicode in 16
'''
print('16=>', hex(ord(name1)), hex(ord(name2)), hex(ord(name3)))

# Q7.
'''
unicode to byte with str "Python 王者歸來"
'''
string = 'Python 王者歸來'
string_byte = string.encode('utf-8')
print('byte data...')
print(string_byte)
