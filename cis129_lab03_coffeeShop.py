


# 1) Black Coffee 
# 2) Expresso 
# 3) Latte 
# 4) Cappicino 


# ask name 
# ask coffee type 
# ask quantity 
# display total 

prices = {
    1: 2.00, 
    2: 3.15, 
    3: 4.00,
    4: 4.99
}

class CoffeeShop: 
    global data 
    data = {}

    def promptUser(self):
        print("\nHello, welcome to our coffee shop, what is your name?")
        name =- input("")

        print("\n\tOur menu\n\n\t1) Black coffee\n\t2) Expresso\n\t3) Latte\n\t4) Cappicino\n\t5)")
        order = int(input("\t"))

        print("\Quanitity: ")
        quanitity = int(input())

        if order == 1: # black coffee 
            total = prices[1] * quanitity
            data['name'] = name 
            data['type'] = 'Black Coffee'
            data['total'] = str(math.floor(total))


        elif  order == 2:
            total = prices[2] * quanitity
            data['name'] = name 
            data['type'] = 'Expresso' 
            data['total'] = str(math.floor(total))

        elif  order == 3:
            total = prices[3] * quanitity
            data['name'] = name 
            data['type'] = 'Latte' 
            data['total'] = str(math.floor(total))

        elif  order == 4:
            total = prices[4] * quanitity
            data['name'] = name 
            data['type'] = 'Cappicino' 
            data['total'] = str(math.floor(total))

        return data 
    
    def recipet(self, promptUser):

        print("Recipet for customer")

        name = promtUser['name']
        type = promptUser['type']
        total = promptUser['total']

        print("Name: " + name 
              +"\nCoffee type: " + type
              +"\nTotal: $" + total + "\n")
        


coffee = CoffeeShop()
coffee.recipet(coffee.promptUser())

print("\nDo you want to calculate for another customer?")
choice = input("")

if choice != "No":
    coffee.recipet(coffee.promptUser())
else: 
    exit(0)


