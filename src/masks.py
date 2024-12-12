import logging

logger = logging.getLogger('masks')
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('logs/masks.log', 'w', encoding='UTF-8')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(number_card: int) -> str:
    """функция принимает номер карты и возвращает маску номера карты в заданном формате"""
    logger.info(f'Функция {get_mask_card_number.__name__} запущена')
    if type(number_card) is not int:
        logger.error(f'Некорректный тип данных: {type(number_card)}')
        raise TypeError('Ошибка! Некорректный тип данных, введите целое число')
    elif len(str(number_card)) != 16:
        logger.error(f'Некорректное значение. Количество символов: {len(str(number_card))}')
        raise ValueError('Ошибка! Номер карты должен содержать 16 цифр')
    mask_card = str(number_card)
    logger.info(f'Функция {get_mask_card_number.__name__} корректно завершила работу')
    return mask_card[:4] + ' ' + mask_card[4:6] + '** **** ' + mask_card[12:]


def get_mask_account(account_number: int) -> str:
    """функция принимает номер счета и возвращает маску номера счета в заданном формате"""
    logger.info('Функция запущена')
    if type(account_number) is not int:
        logger.error('Некорректный тип данных')
        raise TypeError('Ошибка! Некорректный тип данных, введите целое число')
    elif len(str(account_number)) != 14:
        logger.error('Некорректное значение')
        raise ValueError('Ошибка! Номер счета должен содержать 14 цифр')
    mask_account = str(account_number)
    logger.info('Функция корректно завершила работу')
    return '**' + mask_account[-4:]
