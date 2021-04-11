def read_file():
    lines = []
    with open('text(71).txt','r')as f:
        for line in f:
            lines.append(line.strip())
        return lines

word_count = 0
lines = read_file()
for i in lines:
    for letter in i:
        if letter == ' ':
            word_count += 1

print(lines)
print('總共有', len(lines), '行')
print('總共有', word_count+len(lines),'個字')