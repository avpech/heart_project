####  Heart Risk Prediction
---
Сервис для предсказаний риска сердечного приступа на основе анкетных, биохимических и медицинских данных пациентов

---
### Стек технологий:
- Python
- FastAPI
- CatBoost
- scikit-learn

### Требования:
- Python 3.12
- Docker

---
### Подготовка к установке

- Клонировать репозиторий и перейти в него в командной строке.

### Запуск сервиса в Docker
Для запуска сервиса ввести команду
```bash
docker-compose up -d
```

### Локальная установка и запуск сервиса
- Установить и активировать виртуальное окружение c учетом версии Python 3.12 или выше, обновить менеджер пакетов pip:

Git Bash
```bash
python -m venv venv
```
```bash
source venv/Scripts/activate
```
```bash
python -m pip install --upgrade pip
```
Linux
```bash
python3 -m venv venv
```
```bash
source venv/bin/activate
```
```bash
python3 -m pip install --upgrade pip
```

- Установить все зависимости из файла requirements.txt

```bash
pip install -r requirements.txt
```

- Запустить сервис

```bash
uvicorn src.main:app --host 127.0.0.1 --port 8000 --reload
```

---
Сервис будет доступен по адресу http://localhost:8000
### API сервиса
После запуска сервиса интерактивную документацию к API в формате Swagger можно увидеть по адресу:
- http://localhost:8000/docs 

Эндпоинты:

- `POST /api/predict_csv`  принимает csv-файл с входными признаками, возвращает json с предсказаниями в теле ответа.
- `POST /api/predict`  предсказание риска сердечного приступа для отдельного пациента, принимает json в теле запроса, возвращает json с предсказаниями в теле ответа.
- `POST /api/get_predictions_csv`  принимает csv-файл с входными признаками, в качестве ответа отдает csv-файл с предсказаниями.

Более подробную документацию можно увидеть по адресу http://localhost:8000/docs  после запуска сервиса.

Для получения файла с предсказаними на тестовой выборке:
- запустить сервис
- перейти в сваггер  http://localhost:8000/docs
- выбрать эндпоинт `POST /api/get_predictions_csv`
- нажать `try it out`
- выбрать файл для загрузки
- нажать `execute`
- нажать `Download file`

В репозитории уже присутствует готовый файл с предсказаниями на тестовой выборке (`predictions.csv` в корне проекта)

##### Об авторе
Артур Печенюк
- :white_check_mark: [avpech](https://github.com/avpech)