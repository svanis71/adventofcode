import re

print('***********************')
print('Day 5')
print('***********************')


def removeChars(indata, start):
    copy = [indata[:start]]
    l = len(indata)
    for i in range(start, len(indata)):
        if abs(ord(indata[i]) - ord(indata[i + 1 if (i + 1) < l else i])) != 32:
            co
            py.append(indata[i])
        else:
            copy.append(indata[i + 2:])
            return True, ''.join(copy), 0 if i == 0 else i - 1
    return False, ''.join(copy), 0


with open('day5/in.txt') as f:
    content = f.readlines()[0]
indata = content

(didReplace, data, nextpos) = removeChars(indata, 0)
while didReplace:
    (didReplace, data, nextpos) = removeChars(data, nextpos)
print('Part 1:', len(data))

letters = r'[Aa],[Bb],[Cc],[Dd],[Ee],[Ff],[Gg],[Hh],[Ii],[Jj],[Kk],[Ll],[Mm],[Nn],[Oo],[Pp],[Qq],[Rr],[Ss],[Tt],[Uu],[Vv],[Ww],[Xx],[Yy],[Zz]'
result = []
for letter in letters.split(','):
    (didReplace, data, nextpos) = removeChars(re.sub(letter, '', content), 0)
    while didReplace:
        (didReplace, data, nextpos) = removeChars(data, nextpos)
    result.append(len(data))
print('Part 2:', min(result))
