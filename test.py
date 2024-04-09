from src.masks import mask_account, mask_card

card_number = input("Введите номер карты: ")
masked_card = mask_card(card_number)
print(masked_card)

account_number = input("Введите номер счета: ")
masked_account = mask_account(account_number)
print(masked_account)
