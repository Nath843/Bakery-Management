import pandas as pd
import matplotlib.pyplot as plt
import time
import os

# Create files if they don't exist
if not os.path.exists('pp.csv'):
    df = pd.DataFrame(columns=['PRICE', 'PRODUCT', 'TYPE'])
    df.to_csv('pp.csv', index=False)
if not os.path.exists('bill.csv'):
    bill = pd.DataFrame(columns=['pdct_id', 'pdct', 'qty', 'total'])
    bill.to_csv('bill.csv', index=False)
# Statistics function
def show_statistics():
    """Display bakery statistics"""
    print('\n' + '='*40)
    print('BAKERY STATISTICS')
    print('='*40)
    # Check if bill file exists and has data
    if not os.path.exists('bill.csv') or os.path.getsize('bill.csv') == 0:
        print('No sales data available yet!')
        print('Start selling to see statistics!')
        print('='*40)
        input('\nPress Enter to continue...')
        return
    bill_data = pd.read_csv('bill.csv')
    if len(bill_data) == 0:
        print('No sales records found!')
        print('='*40)
        input('\nPress Enter to continue...')
        return
    # Calculate statistics
    total_revenue = bill_data['total'].sum()
    total_orders = len(bill_data)
    total_items = bill_data['qty'].sum()
    avg_order_value = total_revenue / total_orders if total_orders > 0 else 0
    
    # Display summary
    print(f'\nSUMMARY')
    print(f'   Total Revenue: ₹{total_revenue:.2f}')
    print(f'   Total Orders: {total_orders}')
    print(f'   Total Items Sold: {total_items}')
    print(f'   Average Order: ₹{avg_order_value:.2f}')
    
    # Top products by quantity
    print(f'\nTOP 5 PRODUCTS (by quantity)')
    top_by_qty = bill_data.groupby('pdct')['qty'].sum().sort_values(ascending=False).head(5)
    if len(top_by_qty) > 0:
        for i, (product, qty) in enumerate(top_by_qty.items(), 1):
            print(f'   {i}. {product}: {qty} units')
    else:
        print('   No data available')
    # Top products by revenue
    print(f'\n💰 TOP 5 PRODUCTS (by revenue)')
    top_by_revenue = bill_data.groupby('pdct')['total'].sum().sort_values(ascending=False).head(5)
    if len(top_by_revenue) > 0:
        for i, (product, rev) in enumerate(top_by_revenue.items(), 1):
            print(f'   {i}. {product}: ₹{rev:.2f}')
    else:
        print('   No data available')
    # Optional: Ask if user wants to see graphs
    show_graphs = input('\nShow graphs? (y/n): ').lower()
    if show_graphs == 'y':
        try:
            if len(top_by_qty) > 0:
                # Bar chart for top products
                plt.figure(figsize=(10, 6))
                plt.bar(range(len(top_by_qty)), top_by_qty.values, color='skyblue')
                plt.xlabel('Products')
                plt.ylabel('Quantity Sold')
                plt.title('Top 5 Selling Products')
                plt.xticks(range(len(top_by_qty)), top_by_qty.index, rotation=45)
                plt.tight_layout()
                plt.show()
            if len(top_by_revenue) > 0:
                # Pie chart for revenue
                plt.figure(figsize=(8, 8))
                plt.pie(top_by_revenue.values, labels=top_by_revenue.index, autopct='%1.1f%%')
                plt.title('Revenue Distribution (Top 5 Products)')
                plt.show()
        except Exception as e:
            print(f'Error displaying graphs: {e}')
    print('='*40)
    input('\nPress Enter to continue...')
#introduction
def intro():
    df=pd.read_csv('pp.csv')
    bill=pd.read_csv('bill.csv')
    inloop=1
#greetings & login options
    while inloop:
        print('WELCOME TO ONLINE BAKERY')
        print('Enter')
        print('1.for admin login')
        print('2.for customer login')
        print('0. to exit')
#password for admin
        c1=input()
        if c1=='1':
            pw=input('Enter password')
            if pw=='ready_go':
                print('-------Welcome Admin-------')
#options for admin
                while True:
                    print('Enter')
                    print('1.to add item')
                    print('2.to remove an item')
                    print('3.update item price')
                    print('4.view menu')
                    print('5.view statistics')
                    print('6.exit')
                    c2=input()
#adding an item
                    if c2=='1':
                        while True:
                            n= input("Enter product name: ")
                            ip = int(input("Enter product price: "))
                            t=input('Enter product type:')
                            df.loc[len(df)]=[ip,n,t]
                            df.to_csv('pp.csv',index=False)
                            print('New item has been added.')
                            print('Enter \'y\' for continuation and \'n\' for no')
                            c3=input()
                            if c3=='n':
                                break
                        print(df)
#removing an item
                    elif c2=='2':
                        while True:
                            id=int(input('Enter product id'))
                            df=df.drop(id)
                            print('Required item has been removed.')
                            df.to_csv('pp.csv',index=False)
                            print('Enter \'y\' for continuation and \'n\' for no')
                            c3=input()
                            if c3=='n':
                                break
                        print(df)
#price updation
                    elif c2=='3':
                        print("Which product price you would like to update?")
                        while True:
                            id=int(input("Enter product ID:"))
                            price=int(input("Enter the updated price:"))
                            df.loc[id,'PRICE']=price
                            df.to_csv('pp.csv',index=False)
                            print("The item price has been updated!")
                            print('Enter \'y\' for continuation and \'n\' for no')
                            c3=input()
                            if c3=='n':
                                break
                        print(df)
#viewing menu
                    elif c2=='4':
                        print(df)
#viewing graph
                    elif c2=='5':
                        print("Statistics feature coming soon!")
#logging out
                    elif c2=='6':
                        print('Have a good day ahead!')
                        break
                    else:
                        print('Invalid choice')
                        time.sleep(1)
            else:
                print('Incorrect password!')
                time.sleep(1)
#collecting details from customer
        elif c1=='2':
                print('Welcome customer')
                c2=input('Enter 1 for billing \t 2 for exit')
                if c2=='1':
                    if len(df) == 0:
                        print('\n SORRY! Menu is empty. Please visit later.')
                        print('The bakery owner hasn\'t added any items yet.\n')
                        time.sleep(2)
                        continue
                    name = input("Enter the customer name:")
                    print(df)
                    print("What do you wanna buy ?")
                    time.sleep(0.5)
                    print()
                    t = 0
                    bill=pd.DataFrame(columns=['pdct_id','pdct','qty','total'])
#use details from customer to generate a new dataframe
                    while True:
                        id=int(input("Enter the product no.:"))
                        qty=int(input("Enter the quantity:"))
                        total=df.loc[id,'PRICE']*qty
                        pdct=df.loc[id,'PRODUCT']
                        bill.loc[len(bill)]=[id,pdct,qty,total]
                        t=t+total
                        i=input("Anything else?")
                        print("Answer Y for Yes and N for No! ")
                        if(i=='N' or i=='n'):
                            break
#printing a new dataframe
                    if(t!=0):
                        print('\n----------Online Bakery----------')
                        print('Billing details:')
                        print(bill)
                        
                        # Append to existing bill file instead of overwriting
                        if os.path.exists('bill.csv') and os.path.getsize('bill.csv') > 0:
                            old_bill = pd.read_csv('bill.csv')
                            combined_bill = pd.concat([old_bill, bill], ignore_index=True)
                            combined_bill.to_csv('bill.csv', index=False)
                        else:
                            bill.to_csv('bill.csv', index=False)
                            
                        print('Total: ₹',t)
                        print('Thank You! Have A Nice DAY!')
                else:
                    print('Thank you for visiting!')
#exit option
        elif c1=='0':
            print('Thank you for visiting! Goodbye!')
            break
        else:
            print('Invalid choice')
            time.sleep(1)

intro()