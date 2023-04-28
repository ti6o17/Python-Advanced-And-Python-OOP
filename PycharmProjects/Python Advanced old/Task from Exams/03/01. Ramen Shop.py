from collections import deque
que_bowls = deque([int(num) for num in input().split(', ')])
que_customers = deque([int(num) for num in input().split(', ')])

while que_bowls and que_customers:
    bowl = que_bowls.pop()
    customer = que_customers.popleft()
    if bowl > customer:
        bowl -= customer
        que_bowls.append(bowl)
    else:
        customer -= bowl
        que_customers.appendleft(customer)

if que_bowls:
    print("Great job! You served all the customers.")
    print(f"Bowls of ramen left: {', '.join([str(num) for num in que_bowls])}")
elif que_customers:
    if que_customers[0] == 0:
        print("Great job! You served all the customers.")
    else:
        print("Out of ramen! You didn't manage to serve all customers.")
        print(f"Customers left: {', '.join([str(num) for num in que_customers])}")
