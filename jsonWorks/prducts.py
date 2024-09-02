from json import load


f=open("C:\\Users\\HP\\Desktop\\PythonLuminarJune\\jsonWorks\\product.json",encoding="UTF-8")

data=load(f)

# print(len(data))

tiltles=[d.get("title") for d in data]

# print(tiltles)

jewellary_catagary=[d.get("title") for d in data if d.get("category")=="jewelery"]

print(jewellary_catagary)

price_above_100=[d.get("title") for d in data if d.get("price")>100]

# print(price_above_100)

range_100_to150=[d.get("title") for d in data if d.get("price")>100 and d.get("price")<150]
# print(range_100_to150)

def get_rating_count(dic):
    return dic.get("rating").get("count")

top_rating=max(data,key=get_rating_count)
# print(top_rating.get("title"))

lowest_rating=min(data,key=get_rating_count)
# print(lowest_rating.get("title"))

