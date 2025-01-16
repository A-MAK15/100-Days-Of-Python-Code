import art

print(art.logo)
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

calc_dict = {"+" : add,
             "-" : subtract,
             "*" : multiply,
             "/" : divide
}

# print(calc_dict["*"](4,8))

first_num = int(input("Enter Number : "))
for op in calc_dict:
    print(op)
operator = input("Enter operator of choice : ")
second_num = int(input("Enter Number : "))
ans = calc_dict[operator](first_num, second_num)
print(first_num , operator, second_num, "=", ans)
print(f"Answer is : {ans}")

prev_ans = input("Do you want to work with previous results ? 'Yes' or 'No'").lower()

while prev_ans == "yes":
    operator = input("Enter operator of choice : ")
    second_num = int(input("Enter Number : "))
    ans = calc_dict[operator](ans, second_num)
    print(ans, operator, second_num, "=", ans)
    print(f"Answer is : {ans}")
    prev_ans = input("Do you want to work with previous results ? 'Yes' or 'No'").lower()

print(f"Final answer is : {ans}")




