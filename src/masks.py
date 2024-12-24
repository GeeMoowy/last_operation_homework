import logging
from pathlib import Path

PATH_TO_ROOT = Path(__file__).parent.parent
PATH_TO_FILE = Path(PATH_TO_ROOT, 'logs', 'masks.log')


logger = logging.getLogger('masks')
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(PATH_TO_FILE, 'w', encoding='UTF-8')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(number_card: str) -> str:
    """функция принимает номер карты и возвращает маску номера карты в заданном формате"""
    logger.info(f'Функция {get_mask_card_number.__name__} запущена')
    if len(number_card) != 16:
        logger.error(f'Некорректное значение. Количество символов: {len(str(number_card))}')
        raise ValueError('Ошибка! Номер карты должен содержать 16 цифр')
    mask_card = number_card
    logger.info(f'Функция {get_mask_card_number.__name__} корректно завершила работу')
    return mask_card[:4] + ' ' + mask_card[4:6] + '** **** ' + mask_card[12:]


def get_mask_account(account_number: str) -> str:
    """функция принимает номер счета и возвращает маску номера счета в заданном формате"""
    logger.info('Функция запущена')
    if len(str(account_number)) != 20:
        logger.error('Некорректное значение')
        raise ValueError('Ошибка! Номер счета должен содержать 14 цифр')
    mask_account = account_number
    logger.info('Функция корректно завершила работу')
    return '**' + mask_account[-4:]
