input_string = str(input())
array = []
for i in range(len(input_string)):
    if (ord(input_string[i]) - 97) % 2 == 0:
        array.append(input_string[i])
    else:
        array.append(input_string[i].upper())
array.sort(reverse=True)
answer = ' '.join(array)
print(answer)