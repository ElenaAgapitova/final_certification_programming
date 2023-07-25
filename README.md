# Итоговая контрольная работа по блоку специализация

1. Информация о проекте и задание: [ссылка](https://github.com/ElenaAgapitova/final_certification_programming/blob/master/%D0%98%D1%82%D0%BE%D0%B3%D0%BE%D0%B2%D0%B0%D1%8F%20%D0%BA%D0%BE%D0%BD%D1%82%D1%80%D0%BE%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F%20%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%B0.pdf)
2. Команды Linux: [ссылка](https://github.com/ElenaAgapitova/final_certification_programming/blob/master/Linux.pdf)
3. Диаграммы классов: [до разработки приложения](https://github.com/ElenaAgapitova/final_certification_programming/blob/master/diagrams/%D0%94%D0%B8%D0%B0%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B0%20%D0%BA%D0%BB%D0%B0%D1%81%D1%81%D0%BE%D0%B2.png) и [после проектирования и разработки приложения](https://github.com/ElenaAgapitova/final_certification_programming/blob/master/diagrams/%D0%94%D0%B8%D0%B0%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B0%20%D0%BA%D0%BB%D0%B0%D1%81%D1%81%D0%BE%D0%B2%20%D0%BF%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F.png)
4. База данных "Друзья человека"
    * [диаграмма](https://github.com/ElenaAgapitova/final_certification_programming/blob/master/database/DB_human_friends.jpg)
    * [скрипт базы данных и запросы](https://github.com/ElenaAgapitova/final_certification_programming/blob/master/database/Human_friends.sql)
5. Программный код консольного приложения: [ссылка](https://github.com/ElenaAgapitova/final_certification_programming/tree/master/App)
    * хранение данных осуществляется в базе данных SQlite human_friends2.db
    * консольное приложение разработано на языке программирования Python в парадигме ООП c использованием паттерна MVP
    * реализован следующий функционал:
        * чтение данных из базы данных SQlite
        * взаимодействие с пользователем 
        * вывод в консоль реестра всех животных питомника
        * добавление нового животного в питомник
        * вывод в консоль и добавление команд, которыми обучено животное
        * запись изменений в базу данных SQlite
        * класс Счетчик (class Counter) с методом add(), работа с которым осуществляется в блоке with, если заполнены не все поля будет выброшено исключение; счетчик будет закрыт вне зависимости от того, что введет пользователь.