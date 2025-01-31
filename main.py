import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

sample_letter = """
Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

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
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.
"""
site = "https://dvmn.org/profession-ref-program/"
friend = "Андрей"
my_name = "Павел"
message = sample_letter.replace("%website%", site).replace("%friend_name%", friend).replace("%my_name%", my_name)
email_from= "pashgaaaa@yandex.ru"
email_to= "pashgaaaa@yandex.ru"
letter = f"""From: {email_from}\nTo:{email_to}\nSubject: Приглашение!\nContent-Type: text/plain; charset="UTF-8";\n\n{message}"""

letter = letter.encode("utf-8")
server = smtplib.SMTP_SSL("smtp.yandex.ru", 465)
login = os.getenv("MAIL")
password = os.getenv("PASSWORD")
server.login(login, password)
server.sendmail(email_from, email_to, letter)
server.quit()
