'''
В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. 
Не учитывать знаки препинания и регистр символов. 
За основу возьмите любую статью из википедии или из документации к языку.
'''

text = 'Раз, два, три, четыре, пять вышел зайчик погулять. Пять, четыре, три, два, один кто ещё с тобой один.'

punctuations = ',.!&?/-=+()*@#$%^<>:;'
new_text = text.lower()
for item in punctuations:
    new_text = new_text.replace(item, '')

new_list = new_text.split(' ')

new_dic = {}
for item in new_list:
    new_dic[item] = new_dic.get(item, 0) + 1

sorted_dict_desc = dict(sorted(new_dic.items(), key=lambda item: item[1], reverse=True))

for nn, (key, value) in enumerate(sorted_dict_desc.items(), start=1):
    if nn <= 10:
        print(f'{nn}. {key} - {value}')
