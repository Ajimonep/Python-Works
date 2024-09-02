from re import fullmatch

# vehicle_num="KL08TN2020"
# pattern="(KL)[0-9]{2}[A-Z]{1,2}[0-9]{4}"

vehicle_num="KL-08-TN-2020"
pattern="(KL)(-)?[0-9]{2}(-)?[A-Z]{1,2}(-)?[0-9]{4}"

matcher=fullmatch(pattern,vehicle_num)

print("invalid" if matcher==None else "valid")