def word_counter(text):
    word_list=text.split()
    word_dict={}
    for word in word_list:
        if word in word_dict:
            word_dict[word] += 1
        else :
            word_dict[word] = 1
    return word_dict
user_input=input('英語で文章を入力してください。')
word_dict=word_counter(user_input)
for word, freq in word_dict.items():
    print("単語"+str(word)+str(freq)+"回")