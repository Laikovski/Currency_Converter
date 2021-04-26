import ast
# print('Meet a conicoin!')
insert_coin = int(input('Please, enter the number of conicoins you have: '))
insert_rate = ast.literal_eval(input('Please, enter the exchange rate:'))
print(f'The total amount of dollars: {insert_coin * insert_rate}')