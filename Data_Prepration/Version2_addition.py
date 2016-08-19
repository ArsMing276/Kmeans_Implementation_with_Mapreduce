import re
import os

# read input from R to Python
save_path = 'F:/U course/ECS 289/kmeans/YangMR75.txt'
f = open(save_path, 'r')
lines = f.readlines()
f2 = open('F:/U course/ECS 289/kmeans/YangMR75_2.txt', 'a')

# clean data to formatted data
for line in lines:
    re_key1 = re.compile(',')
    #re_key2 = re.compile("'")
    re_key5 = re.compile("\n")
    #re_key3 = re.compile(" ")
    line = re_key5.sub('',line)
    a = re_key1.split(line)
    #b = re_key2.sub('', b)
    #b = re_key3.sub('',b)
    output = a[0] + '|' + a[3] + '|' + a[1] +','+ a[2] +'\n'
    f2.write(output)


f2.close()
f.close()

		