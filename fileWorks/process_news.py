f=open("C:\\Users\\HP\\Desktop\\PythonLuminarJune\\fileWorks\\news.txt","r")

word_list=[w for line in f for w in line.rstrip("\n").split(" ") if w!=""]



word_count={w:word_list.count(w) for w in word_list}



# for w in word_list:

#     if w in word_count:

#         word_count[w]+=1

#     else:
#         word_count[w]=1

# print(word_count)

srt=sorted(word_count,key=lambda key:word_count.get(key),reverse=True)
print(srt)




