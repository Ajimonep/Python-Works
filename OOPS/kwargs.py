# *args (arguent tuple)
# **kwargs (keyword argumnets dictionary)

def get_person(**kwargs):
    print(kwargs.get("name"))
    print(kwargs.get("w_place"))

get_person(name="allen",w_place="kochi",n_place="kottayam") 