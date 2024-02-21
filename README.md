# Polling App

### Задача

>  **Создайте веб-приложение на базе Django для проведения опросов и возможностью динамического отображения
> вопросов в зависимости от ответов пользователя.**

### Требования

>Приложение должно включать в себя модели для опросов, вопросов и ответов, а также следующие функции: 
>
>- [x] Создание и редактирование опросов и вопросов через админку.
>- [x] Реализацию веб-интерфейса, позволяющего пользователям проходить опросы и отвечать на вопросы.
>- [x] Сохранение ответов пользователей в связке с соответствующими опросами.
>- [x] Логику, позволяющую определить, какие вопросы показывать или скрывать в зависимости от предыдущих ответов пользователя (т.е. дерево)
>- [x] Вывод результатов опросов, включая статистику ответов на каждый вопрос, после завершения опроса.
>    
>    Реализовать с помощью минимального кол-ва SQL-запросов *без использования ORM*:`Использовал ORM - запросы гораздо понятнее, легковеснее, проще внести изменения. Но ORM не панацея`
>    
>    - [x] Общее кол-во участников опроса (например, 100)
>    - На каждый вопрос:
>         
>        - [x] Кол-во ответивших и их доля от общего кол-ва участников опроса (например, 95 / 95%)
>        - [x] Порядковый номер вопроса по кол-ву ответивших. Если кол-во совпадает, то и номер должен совпадать (например, для трех вопросов с 95, 95, 75 ответивших получаются соответствующие им номера 1, 1, 2)
>        - [x] Кол-во ответивших на каждый из вариантов ответа и их доля от общего кол-ва ответивших на этот вопрос после завершения опроса.

### Вспомогательные источники

- Large Question Answering Datasets https://github.com/ad-freiburg/large-qa-datasets
- Django modelform https://stackoverflow.com/questions/45670804/how-to-change-the-rendered-field-in-djangos-modelform-queryset
- tree in db - https://www.baeldung.com/cs/storing-tree-in-rdb
- Django Documentation - https://docs.djangoproject.com
