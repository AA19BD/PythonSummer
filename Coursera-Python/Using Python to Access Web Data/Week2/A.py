import re 
file=open('A.txt')
lst=list()
sum=0
count=0
for line in file:
    line=line.rstrip()
    words=line.split()
    for word in words:
        my_num=re.findall('[0-9]+',word)#возвращает нам лист из чисел из за этого делаем так ->my_num[0]
        if len(my_num)==0:#будет смотреть на лист,лист может быть пустым ->из за этого мы проверяем на пустоту (если на равно 1) то пропускай
            continue
        for i in my_num:
            # count+=1
            sum+=int(i)
        # count+=1
        # real_num=int(my_num[0])#выводим первое число в списке
        # sum+=real_num
        #  # print(real_num)
print(sum)
# print("Sum",(sum),"Count",(count))   
# print("Count",count)

