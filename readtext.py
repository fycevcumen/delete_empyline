
text = open('file_opening/reading.txt','r')
lines = [line for line in text]
for elem in lines:
    if elem =='\n':
        lines.remove('\n')
print(lines)
print(len(lines))
