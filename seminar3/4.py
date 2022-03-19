# 4. Пользователь задаёт две строки. 
# Определить количество вхождений одной строки в другой.

a = "wgsdhfgfggfkhfg"
b = "fg"

#print(s1.count(s2))    решение в одну строчку

def find(str1, str2):
    i = 0
    count = 0
    l1 = len(str1)
    while l1 >= 0:
        l2 = len(str2) 
        j = 0
        while (str1[i] == str2[j]) and l2 >= 0 and l1 >= 0:
            if (str1[i] == str2[j]) and l2 >= 0 and l1 >= 0:
                print(str1[i])
                print(str2[i])
                i += 1
                j += 1
                l2 -= 1
                l1 -= 1
            count += 1
        l1 -= 1
        i += 1

print(find(a, b))