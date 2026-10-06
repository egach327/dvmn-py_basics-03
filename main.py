from dotenv import load_dotenv
import os
import smtplib
load_dotenv()

my_mail = os.getenv('MAIL')
my_pasw = os.getenv('ODPAS')

server = smtplib.SMTP_SSL('smtp.mail.ru', 465)
server.login(my_mail, my_pasw)

letter = """\
From: egor.shirokov.23@mail.ru
To: egor.shirokov.23@mail.ru
Subject: Приглашение!
Content-Type: text/plain; charset="UTF-8";"""

text = """Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → %website%  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл."""
friend_name = 'Кирилл'
my_name = 'Егор'
site_name = 'https://dvmn.org/profession-ref-program/egor.shirokov.23/CRb1c/'
text = text.replace('%website%', 'https://dvmn.org/profession-ref-program/egor.shirokov.23/CRb1c/')
text = text.replace('%friend_name%', friend_name)
text = text.replace('%', '')
text = text.replace('my_name', my_name)
letter = text
letter = letter.encode("UTF-8")
print(letter)

server.sendmail('egor.shirokov.23@mail.ru', 'egor.shirokov.23@mail.ru', letter)
server.quit()
