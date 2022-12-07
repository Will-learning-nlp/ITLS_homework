# 阅读txt文件后可以发现，《文心雕龙》书中文白结构对应分明，每一篇原文以标题开始，'译文'二字标志着译文开始；
# 并且每一段 在 txt 中为1行

# 注意：整个代码完成后，发现原书epub文件中中有三处格式错误，造成对齐错误，本代码无法处理这个异常，只能手动修改后得到完美对齐文件。

# 首先提取目录中各篇标题
file_txt = open("wenxindiaolong.txt")


def read_content(file):
    content_lst = []
    while True:
        a_line = file.readline()  # 逐行读入内存，节约内存
        a_line = a_line.strip()  # 提取纯内容文本
        # Python strip() 方法用于移除字符串头尾指定的字符（默认为空格）或字符序列。
        # 注意：该方法只能删除开头或是结尾的字符，不能删除中间部分的字符。
        # print(a_line)
        if a_line != '':  # 判断 空行 不会提取到列表中
            content_lst.append(a_line)
        if a_line == "序志第五十":
            break
    return content_lst[2:]


content_lst = read_content(file_txt)
# content_lst.append('end')
print(content_lst)

# 遍历 原 txt 中每一行，识别 整篇 原文与译文


def get_article_txt(file):
    article_txt = open("article_txt.txt", 'w+')
    translation_txt = open("translation_txt.txt", 'w+')
    # for a_line_para in file:
    #     a_line_para = a_line_para.strip()
    while True:
        a_line_para = file.readline().strip()
        if a_line_para == '2014年9月':
            break  # file读取位置停在 '2014年9月' 标记处

    # for title in content_lst:  # 遍历每一篇文章标题
    for tittle_index in range(len(content_lst)):
        title = content_lst[tittle_index]
        while True:
            a_line_para = file.readline().strip()  # 逐行提取文本
            if a_line_para != '【译文】':  # 定位，在 【译文】 出现之前，都是原文，迭代存入原文txt
                if a_line_para != '':  # 排除空行，使格式整洁
                    article_txt.write(a_line_para+'\n')  # 写入原文存储txt：article_txt.txt
                    # align_para_txt.write(a_line_para+"\n")
            else:
                break  # 定位到 【译文】，退出循环
        translation_txt.write(title+'\n')   # 给即将存储的 译文 加上标题
        while True:
            a_line_para = file.readline().strip()  # 逐行提取译文文本
            if tittle_index == len(content_lst) - 1:  # 判断是否是最后一篇，若是，写入1行后退出循环
                if a_line_para !='':
                    translation_txt.write(a_line_para + '\n')
                    # align_para_txt.write(a_line_para + "\n")
                break
            if a_line_para != content_lst[tittle_index+1]:  # 若不是最后一篇，使用索引判断：下一篇标题是否出现
                # 在下一篇标题出现之前，迭代存储 译文文本，存储于 translation_txt.txt 文件
                if a_line_para !='':
                    translation_txt.write(a_line_para+'\n')
                    # align_para_txt.write(a_line_para + "\n")
            else:
                article_txt.write(a_line_para+'\n') # 若出现下一篇标题，将标题存入原文存储txt：article_txt.txt
                break
    while True:  # 单独处理最后一篇，因为上面的循环方式会使最后一篇 索引时超出列表长度
        a_line_para = file.readline().strip()
        if a_line_para != 'end':
            if a_line_para != '':
                translation_txt.write(a_line_para+'\n')
                # align_para_txt.write(a_line_para + "\n")
        else:
            break

    article_txt.close()
    translation_txt.close()
    return


# get_article_txt(file_txt)
file_txt.close()

# 上面的代码得到2个文件，分别存储了原文（article_txt.txt）与 译文（translation_txt.txt），
# 下面对齐每个段落，并存入align_para_txt.txt文件中

def alignPara(file_orig, file_trans):
    file1 = open(file_orig, 'a+')
    file2 = open(file_trans, 'a+')
    file1.write('\n'+'')
    file2.write('\n'+'')  # 文件末尾写入一个空格，用于随后代码循环中判断终止
    file1.seek(0)  # 特别注意此处，由于是 a+ 模式 打开文件，则指针默认在文件尾部，需要seek返回文件开头
    file2.seek(0)
    align_para_txt = open("align_para_txt.txt", 'w+')
    # for line in file1:
    #     align_para_txt.write('原文：'+line)
    stop = None
    # count = 0
    while not stop:
    # while count < 10:
        line_original = file1.readline()
        line_translation = file2.readline()  # 分别读取原文与译文的一段，依次写入新的文件align_para_txt.txt中
        align_para_txt.write('原文：' + line_original)
        align_para_txt.write('译文：' + line_translation+'\n')
        # count += 1
        if line_translation == '':
            stop = True
    align_para_txt.close()
    file1.close()
    file2.close()


# alignPara('article_txt.txt','translation_txt.txt')

# epub原文件有错漏，45篇译文缺失，导致对齐错误
# 有一篇，原文中有一句注释

