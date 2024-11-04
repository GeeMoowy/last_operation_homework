def get_mask_card_number(number_card: int) -> str:
    """функция принимает номер карты и возвращает маску номера карты в заданном формате"""
    mask_card = str(number_card)
    return mask_card[:4] + ' ' + mask_card[4:6] + '** **** ' + mask_card[12:]


def get_mask_account(account_number: int) -> str:
    """функция принимает номер счета и возвращает маску номера счета в заданном формате"""
    mask_account = str(account_number)
    return '**' + mask_account[-4:]
