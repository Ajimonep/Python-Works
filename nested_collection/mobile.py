mobiles=[

    {"id":100,"title":"s23 ultra","brand":"samsung","price":125000,"network":"5g"},
    {"id":101,"title":"s23","brand":"samsung","price":54000,"network":"4g"},
    {"id":102,"title":"edge14pro","brand":"moto","price":25000,"network":"5g"},
    {"id":103,"title":"edgeneo","brand":"moto","price":22000,"network":"4g"},
    {"id":104,"title":"redminote13pro","brand":"mi","price":25000,"network":"5g"},
    {"id":105,"title":"redmi13","brand":"mi","price":12000,"network":"4g"},
]

max_price=0
for mob in mobiles:
    if mob.get("price")>max_price:    
        max_price=mob.get("price")
        #  print(max_price)
        
mobile_price=[mob.get("title")for mob in mobiles if mob.get("price")==max_price]

print(mobile_price)