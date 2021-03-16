def bonAppetit(bill, k, b):
    cost_of_shared_item = sum(bill) - bill[k]  
    charged = cost_of_shared_item // 2
    result = b - charged
    
    if result > 0:
         print(result)
    else:
         print("Bon Appetit")

if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
