ori = [2, 8, 9, 48, 8, 22, -12, 2]
new = []
for value in ori:
    if value > 5:
        new.append(value + 2)
nnew = set(new)
print(ori)
print(nnew)