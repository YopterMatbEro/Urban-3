def send_email(message, recipient, sender='Illidan_Stormrage@wow.com'):
    """Сохранил стрелки (<>) для удобности чтения адресов при выводе уведомлений"""
    if '@' not in recipient or '@' not in sender:
        print(f'Невозможно отправить письмо с адреса <{sender}> на адрес <{recipient}>')

    elif not recipient.endswith('.com') and not recipient.endswith('.ru') and not recipient.endswith('.net'):
        print(f'Невозможно отправить письмо с адреса <{sender}> на адрес <{recipient}>')

    elif not sender.endswith('.com') and not sender.endswith('.ru') and not sender.endswith('.net'):
        print(f'Невозможно отправить письмо с адреса <{sender}> на адрес <{recipient}>')

    elif recipient == sender:
        print('Нельзя отправить письмо самому себе!')

    elif sender == 'Illidan_Stormrage@wow.com':
        print(f'Письмо успешно отправлено с адреса <{sender}> на адрес <{recipient}>')

    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса <{sender}> на адрес <{recipient}>')


send_email('Hello', 'Illidan_Stormrage@wow.com', 'Illidan_Stormrage@wow.com')  # нельзя отправить письмо самому себе
send_email('Hello', 'Malfurion_Stormrage@wow.ru', 'Illidan_Stormrage@wow.com')  # успешно
send_email('Hello', 'Malfurion_Stormrage@wow.ru', 'Illidan_Stormrage@wow.net')  # успешно, НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ
send_email('Hello', 'Malfurion_Stormrage@wow', 'Illidan_Stormrage@wow.com')  # нет .ru
send_email('Hello', 'Malfurion_Stormrage@wow.ru', 'Illidan_Stormrage_wow.ru')  # нет @

print('\n\t\t', send_email.__doc__)
