import jieba

text = "我爱自然语言处理技术"
seg_list = jieba.cut(text, cut_all=False)

print(" ".join(seg_list))
