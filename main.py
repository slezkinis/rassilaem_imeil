import os
import smtplib


login = os.environ["LOGIN"]
password = os.environ["PASSWORD"]
server = smtplib.SMTP_SSL('smtp.yandex.ru:465')
server.login(login, password)
friend_name='Анна'
my_name='Иван'
my_email='slezkinis@yandex.ru'
friend_email='ekanna2005@gmail.com'
begin_letter=f'''From: {my_email}
To: {friend_email}
Subject: Приглашение!
Content-Type: text/plain; charset="UTF-8";
'''
text='''Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

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
На модули, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.
 '''
text=text.replace('%website%', 'https://dvmn.org/referrals/JCMJRVzt9M2LpOjQoOK8u6CejHLzrfa8wGSwCq0Y/').replace('%friend_name%', friend_name).replace('%my_name%', my_name)
letter=begin_letter + '\n' + text
letter=letter.encode("UTF-8")
server.sendmail(my_email, friend_email, letter)
server.quit()
