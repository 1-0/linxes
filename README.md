# linxes - сервис аналог https://bitly.com/

# Usage:

## 1. Installation

- Install or/and check installed git and python3:
  - `git --version` for check or visit https://git-scm.com/ for installation instructions 
  - `python3 --version` for check or visit https://www.python.org for installation instructions
- `python3 -m pip venv linxes`
- `cd linxes`
- `source ./bin/activate` in nix OS or `.\Scripts\activate.bat` in Windows OS
- `python3 -m pip install -U pip`
- `git clone https://github.com/1-0/linxes`
- `mv linxes src` in nix OS or `move linxes src` in Windows OS
- `cd src`
- `python -m pip install -r requirements.txt`

## 2. Configuration

- `python manage.py createsuperuser`

## 3. Run Server

- `python manage.py runserver`

# Task 1:

- Сервис должен иметь простой веб интерфейс
  - одна страница  с одним полем для ввода ссылки на ресурс, которую нужно минифицировать
  - кнопа “отправить”
- После отправки данных сервис должен возвращать короткую ссылку.
- Если полная ссылка на ресурс уже была раньше обработана, то показать так же короткую ссылку и количество переходов по ней.
- При переходе по короткой ссылке, сервис должен перенаправить на ресурс используя полную ссылку.
