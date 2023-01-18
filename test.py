import os
import re

path = "Z:\漫\狂赌之渊\狂赌之渊S01\\"
obj = os.walk(path)

s = input()
match = re.search(r"- \d+", s)
i = match.span()[0] + 1
e = "S0" + str(1) + "E"
s1 = s[0:i]
s2 = s[i + 1:]
print(s1+e+s2)
