# books.py
book1_name = "Pragmatic Thinking and Learning"
book1_price = 30
qty = 1
book2_name = "Learn You a Haskell"
book2_price = 0
qty = qty + 1
book3_name = "The Healthy Programmer"
book3_price = 50
qty = qty + 1
book4_name = "Code Complete"
book4_price = 60
qty = qty + 1
book5_name = "The Pragmatic Programmer"
book5_price = 20
qty = qty + 1
book6_name = "Pro Git"
book6_price = 0
qty = qty + 1
book7_name = "Introduction to Algorithms"
book7_price = 80
qty = qty + 1
book8_name = "Concrete Mathematics"
book8_price = 100
qty = qty + 1

#displays inventory and prices
print("Title: " + book1_name + " - Price: {}lv.".format(book1_price))
print("Title: " + book2_name + " - Price: {}lv.".format(book2_price))
print("Title: " + book3_name + " - Price: {}lv.".format(book3_price))
print("Title: " + book4_name + " - Price: {}lv.".format(book4_price))
print("Title: " + book5_name + " - Price: {}lv.".format(book5_price))
print("Title: " + book6_name + " - Price: {}lv.".format(book6_price))
print("Title: " + book7_name + " - Price: {}lv.".format(book7_price))
print("Title: " + book8_name + " - Price: {}lv.\n".format(book8_price))

#displays the sum of all books
print("Total Cost of all Books: {}lv.\n".format(book1_price + book2_price + book3_price + book4_price + book5_price + book6_price + book7_price + book8_price))

#displays total count of books in store
print("Total Books in Store: {}pcs\n".format(qty))

#displays bundle price
discount = 25
bundle_price = book7_price + book8_price
print( "Discount Bundle ({}) Price: {}lv.\n".format(book7_name + " + " + book8_name, bundle_price - bundle_price * discount / 100))

#select books according budget 
budget = 150
print("For you Budget of {}lv. Chose one of Following Scenarios:\n".format(budget))
print("First Scenario: \n1. " + book2_name + "\n2. " + book6_name + "\n3. " + book5_name + "\nAvailable Credit: {}lv.\n".format(budget - book2_price - book6_price - book5_price))
print("Second Scenario: \n1. " + book2_name + "\n2. " + book6_name + "\n3. " + book5_name + "\n4. " + book1_name + "\nAvailable Credit: {}lv.\n".format(budget - book2_price - book6_price - book5_price - book1_price))
print("Third Scenario: \n1. " + book2_name + "\n2. " + book6_name + "\n3. " + book5_name + "\n4. " + book1_name + "\n5. " + book3_name + "\nAvailable Credit: {}lv.\n".format(budget - book2_price - book6_price - book5_price - book1_price - book3_price))
print("Fourth Scenario: \n1. " + book2_name + "\n2. " + book6_name + "\n3. " + book5_name + "\n4. " + book1_name + "\n5. " + book3_name + "\n6. " + book4_name + "\nAvailable Credit: {}lv.\n".format(budget - book2_price - book6_price - book5_price - book1_price - book3_price - book4_price))
print("Fifth Scenario: \n1. " + book2_name + "\n2. " + book6_name + "\n3. " + book5_name + "\n4. " + book1_name + "\n5. " + book3_name + "\n6. " + book4_name + "\n7. " + book7_name + "\nAvailable Credit: {}lv.\n".format(budget - book2_price - book6_price - book5_price - book1_price - book3_price - book4_price - book7_price))
print("Sixth Scenario: \n1. " + book2_name + "\n2. " + book6_name + "\n3. " + book5_name + "\n4. " + book1_name + "\n5. " + book3_name + "\n6. " + book4_name + "\n7. " + book7_name + "\n8. " + book8_name + "\nAvailable Credit: {}lv.\n".format(budget - book2_price - book6_price - book5_price - book1_price - book3_price - book4_price - book7_price - book8_price))





