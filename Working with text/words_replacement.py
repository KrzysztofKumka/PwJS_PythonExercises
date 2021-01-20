f = open('txt_1','r')
delete_list = [' się ',' nigdy ',' oraz ', ' dlaczego ', ' i ']


list = []
for line in f:
    for word in delete_list:
        if word in line:
            if word == ' i ':
                line = line.replace(word,' oraz ')
            if word == ' oraz ':
                line = line.replace(word,' i ')
            if word == ' nigdy ':
                line = line.replace(word,' prawie nigdy ')
            if word == ' dlaczego ':
                line = line.replace(word,' czemu ')

    list.append(line)
f.close()

new_f = open('word_replacement_text.txt','w')
for line in list:
    new_f.write(line)
new_f.close()