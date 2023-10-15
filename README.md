FastQuiz - backend приложение, написанное на FastAPI.

Для запуска приложения использовать следующие команды:
1) git clone https://github.com/EvgGitHub198/FastQuiz
2) docker-compose up -d --build
3) Перейти по маршруту http://0.0.0.0:8000/docs
4) Протестировать API через документацию
5) Либо вручную отправить запрос через API сервис: указав в качестве API-эндпоинта: http://0.0.0.0:8000/get_random_questions/?questions_num=1


Для просмотра содержимого таблицы questions использовать следующие команды:
1) docker exec -it <DB_CONTAINER_ID>  psql -U postgres -d fastquiz
2) После перехода в консоль psql, выполнить SQL запрос к БД: SELECT * FROM questions;




