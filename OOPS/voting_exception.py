def poll(age):
    if age<18:
        raise Exception("invalid age")

    else:

        print("voted")


try:
    poll(19)

except Exception as e:
    print(e)