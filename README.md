# Perancangan dan Pemrograman Web (PPW) SI 2019 Fasilkom UI

## Status

[![pipeline status](pipeline.svg)]
[![coverage report](coverage.svg)]

## Step

- Windows

```bash
python -m venv venv
venv\Scripts\activate.bat
pip install -r requirements.txt

python manage.py migrate --run-syncdb
python manage.py runserver
```