placement={"java":34,"python":65,"asp":45,"django":12}

# def get_value(key):
#     return placement.get(key)

srt=sorted(placement,key=lambda key:placement.get(key),reverse=True)

print(srt)