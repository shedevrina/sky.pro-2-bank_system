from .src.masks import get_mask_card_number
from .src.masks import get_mask_account
from .src.widget import mask_account_card
from .src.widget import get_date


print(get_mask_card_number(7000792289606361))
print(get_mask_account(73654108430135874305))

print(mask_account_card('Visa Platinum 7000792289606361'))
print(mask_account_card('Счет 73654108430135874305'))

print(get_date('2024-03-11T02:26:18.671407'))



