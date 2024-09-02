expenses=[12000,13000,11000,14000,15000,21000,22000,13000]

expense_count=len(expenses)
sum=0
# for i in range(0,expense_count):
#     print(expenses[i])

for i in range(0,expense_count):
    # if expenses[i]>15000:

        # print(expenses[i])

        sum=sum+expenses[i]

print(sum)

avg_expense=sum/expense_count
print(avg_expense)