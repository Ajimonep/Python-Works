mobiles=[

    {"id":100,"title":"s23 ultra","brand":"samsung","price":125000,"network":"5g"},
    {"id":101,"title":"s23","brand":"samsung","price":54000,"network":"4g"},
    {"id":102,"title":"edge14pro","brand":"moto","price":25000,"network":"5g"},
    {"id":103,"title":"edgeneo","brand":"moto","price":22000,"network":"4g"},
    {"id":104,"title":"redminote13pro","brand":"mi","price":25000,"network":"5g"},
    {"id":105,"title":"redmi13","brand":"mi","price":12000,"network":"4g"},
]


def get_price(mob):
    return mob.get("price")

costly_mobile=max(mobiles,key=get_price)
print(costly_mobile)

cheapest_mobile=min(mobiles,key=get_price)
print(cheapest_mobile)

sorted_mobiles=sorted(mobiles,key=get_price,reverse=True)
print(sorted_mobiles)

total_price=sum([mob.get("price") for mob in mobiles])
print(total_price)