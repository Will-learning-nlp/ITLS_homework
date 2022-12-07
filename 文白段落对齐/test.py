fh = open("test.txt", 'a+')
# print(len(fh)) 报错，无长度

fh.write('ok'+'\n')
fh.write(' '+'\n')
fh.write('ok'+'\n')
fh.write('\n' + '')
fh.write('ok'+'\n')


fh.close()

fh1 = open('test.txt')

for i in range(5):
    print(fh1.readline())

def alignPara(file_orig, file_trans):
    file1 = open(file_orig, 'a+')
    file2 = open(file_trans, 'a+')
    file1.write('\n'+'')
    file2.write('\n'+'')
    align_para_txt = open("align_para_txt.txt", 'w+')

    # for line in file1:
    #     align_para_txt.write('原文：'+line)
    stop = None
    count = 0
    # while not stop:
    while count < 10:
        line_original = file1.readline()
        line_translation = file2.readline()
        align_para_txt.write('原文：' + line_original + '\n')
        align_para_txt.write('译文：' + line_translation + '\n')
        count += 1
        # if line_translation == '':
        #     stop = True

    align_para_txt.close()
    file1.close()
    file2.close()


alignPara('article_txt.txt','translation_txt.txt')

