import masks


def mask_account_card(card_info: str) -> str:
    card_info_list = card_info.split()
    card_number = int(card_info_list[-1])
    if card_info_list[0] == 'Счет':
        mask_number = masks.get_mask_account(card_number)
        return card_info_list[0] + " " + mask_number
    else:
        mask_number = masks.get_mask_card_number(card_number)
        return " ".join(card_info_list[:-1]) + " " + mask_number


print(mask_account_card('Visa Gold 12354886532111123546'))