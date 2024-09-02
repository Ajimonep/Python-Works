employee={"name":"hari","dept":"r&d","salary":50000,"combo_offer":1000,"extra_working_day":3}

for k,v in employee.items():
    # print(k,v)

    if "extra_working_day" in employee:

        netpay=employee.get("salary")+employee.get("combo_offer")*employee.get("extra_working_day")

    else:
        netpay=employee.get("salary")

print(netpay)