list=["fly","flyin","flyout","flyoff","out","in"]


# fly=[n for n in list if n[0:3]=="fly"]

fly=[n for n in list if n.startswith("fly")]



print(fly)