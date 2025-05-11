# Гроздов Николай Алексеевич

# Докуметация

## Получить все опросы со статистикой
curl http://localhost:8000/api/analytics/surveys/

## Получите аналитику конкретного опроса
curl http://localhost:8000/api/analytics/surveys/1/

## Фильтровать опросы, созданные после определенной даты
curl http://localhost:8000/api/analytics/surveys/?created_after=2023-01-01

## Сортировать опросы по количеству голосов (по убыванию)
curl http://localhost:8000/api/analytics/surveys/?ordering=-responses_count
