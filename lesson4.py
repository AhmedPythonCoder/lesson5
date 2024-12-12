'''1) Basic sales tax is applicable at a rate of 10% on all goods, except books,food, and medical products that are exempt.
2) Import duty is an additional sales tax applicable on all imported goods at a rate of 5%, with no exemptions.
Here we have allowed the user to enter the quantity of item, name, price,whether they are exempted or not and whether they are imported or not. From this data, we have calculated the sales tax and created a receipt  which lists the name of all the purchased items and their price (including tax), finishing with the total cost of the items, and the total amounts of sales taxes paid'''
tax = 0
importedtax = 0

item = input('Is the item a book, food, or a medical product?(y/n) ')
imported = input('Is your item imported from another country?(y/n)')
cost = float(input('How much does the item cost in $?: '))
if item == 'y':
    print('No tax is added to your item.')
elif item == 'n':
    tax = cost * 0.1
    costwithtax = cost + tax
else:
    print('y or n only!')
    quit()
if imported == 'y':
    importedtax = cost * 0.05
    costwithimportedtax = cost + importedtax
else:
    print('y or n only!')
    quit()

alltax = tax + importedtax
finalcost = cost + alltax
print(f'Your item costs {finalcost} including VAT')
input()