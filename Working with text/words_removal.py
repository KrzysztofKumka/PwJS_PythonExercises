f = open('txt_1','r')
delete_list = [' się ',' nigdy ',' oraz ', ' dlaczego ', ' i ']


list = []
for line in f:
    for word in delete_list:
        if word in line:
            line = line.replace(word,' ')
    list.append(line)
f.close()

new_f = open('words_removal_text.txt','w')
for line in list:
    new_f.write(line)
new_f.close()