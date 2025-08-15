# 🕹️ Arcade Day Pass Tracker — Challenge Steps
#
# 1) Create variables to store:
customer_name = "Mubarik'"
number_of_passes = 7
tokens_per_pass = 90
price_per_pass = 9.99
tokens_required_per_game = 10

#Calculate
#total tokens
#total cost

# games available  (use 'floor division' to get a whole number)
total_tokens = number_of_passes * tokens_per_pass
total_cost = number_of_passes * price_per_pass
games_available = total_tokens // tokens_required_per_game

# 2) Print the variables
#    customer_name, number_of_passes, total_tokens, total_cost, games_available
print("===== ARCADE DAY PASS =====")
print ('customer name:', customer_name)
print ('passes_bought:', number_of_passes)
print ('total_tokens:', total_tokens)
print ('total_cost:', total_cost)
print('total_tokens:', total_tokens) 
print('games_available:', games_available)

# 3) Print a message to the customer
#    "Thank you, {customer_name}, for purchasing {number_of_passes} passes
#    for a total of {total_cost}. You have {total_tokens} tokens, which
#    allows you to play {games_available} games."
print(f'Thank you, {customer_name}, for purchasing {number_of_passes} passes \
for a total of {total_cost}. You have {total_tokens} tokens, which \
allows you to play {games_available} games.')
#    (use f-string formatting)
#    (use f-string formatting)
# 4) Add a comment to the code explaining what the code does
#    This code calculates the total tokens and cost for arcade passes,
