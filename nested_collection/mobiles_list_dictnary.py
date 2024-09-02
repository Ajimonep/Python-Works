mobiles=[

    {"id":100,"title":"s23 ultra","brand":"samsung","price":12500,"network":"5g"},
    {"id":101,"title":"s23","brand":"samsung","price":54000,"network":"4g"},
    {"id":102,"title":"edge14pro","brand":"moto","price":25000,"network":"5g"},
    {"id":103,"title":"edgeneo","brand":"moto","price":22000,"network":"4g"},
    {"id":104,"title":"redminote13pro","brand":"mi","price":25000,"network":"5g"},
    {"id":105,"title":"redmi13","brand":"mi","price":12000,"network":"4g"},
]

all_mobile_name=[mob.get("title")for mob in mobiles]

# print(all_mobile_name)


all_brand_name=[mob.get("brand") for mob in mobiles]

# print(all_brand_name)

all_brand=[mob.get("title") for mob in mobiles if mob.get("brand") =="samsung"]

# print(all_brand)

all_price=[mob .get("title") for mob in mobiles if mob.get("price") in range(23000,40000)]

print(all_price)
