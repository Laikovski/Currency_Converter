import ast

currency = {
    'RUB': 2.98,
    'ARS': 0.82,
    'HNL': 0.17,
    'AUD': 1.9622,
    'MAD': 0.208
}
insert = ast.literal_eval(input())

for item in currency:
    print(f'I will get {round(currency[item] * insert, 2)} {item} from the sale of {insert} conicoins.')