mobile={"name":"s23 ultra","brand":"samsung","price":80000,"is_available":True}

# for k,v in mobile.items():

    # print(k,v)

# mobile.pop("name")

# get(key)
# values()
# keys()
# items()
# pop()

mobile["offer"]=500

if "offer" in mobile:

    selling_price=mobile.get("price")-mobile.get("offer")

    print(selling_price)

else:
    selling_price=mobile.get("price")

    print(selling_price)

