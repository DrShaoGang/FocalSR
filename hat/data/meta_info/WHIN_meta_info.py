file1 = open('myfile.txt', 'w')
for i in range(1000):
    file1.writelines('0_' + str(i) +'.png (512,512,3)\n')