def read_file():
    lines = []
    with open('text(71).txt','r')as f:
        for line in f:
            lines.append(line.strip())
        return lines

word_count = 1
lines = read_file()
for i in lines[0: ]:
    if i == ' ':
        word_count += 1
print(lines)
print('總共有', len(lines), '行')
print('總共有', word_count, '個字')

