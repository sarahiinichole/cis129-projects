Main   
     
        Declare String tax
        Declare Integer 6%
        Declare Real .78        
        
        //Get input from the customer 
        Display "What are you purchasing?"
        Input Coffee
        Display "Please enter the number of items bought"
        Input 1
        Display "Please enter the price of the item"
        Input 5.00
        
        //Calculate the total cost
        Declare Real totalCost
        5.00 = 1 * 5.00
       
        //Get input from the customer 
        Display "What are you purchasing?"
        Input Muffin
        Display "Please enter the number of items bought"
        Input 2
        Display "Please enter the price of the item"
        Input 4.00
        
        //Calculate the total cost
        Declare Real totalCost
        8.00 = 2 * 4.00
        
        //Display the receipt to the customer
        Display "------ Receipt ------"
        Display "Item Purchased: ", nameOfItem
        Display "Number purchased: ", numberOfItemsPurchased
        Display "Price of Each Item: ", priceOfItem
        Display "Total Cost: 13.78 ", totalCost

        Receipt: 
        ***************************************
        My Coffee and Muffin Shop
        Number of coffees bought?
        1
        Number of muffins bought?
        2
        ***************************************

        ***************************************
        My Coffee and Muffin Shop Receipt
        1 Coffee at $5 each: $ 5.00
        2 Muffins at $4 each: $ 8.00
        6% tax: $ .78
        ---------
        Total: $ 13.78
        ***************************************
End Main
