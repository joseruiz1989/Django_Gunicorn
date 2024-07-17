# Django_Gunicorn`

```
pip install --upgrade gevent


source ../venv/wellpath/bin/activate
gunicorn -c gunicorn_config.py Django_Gunicorn.wsgi --bind 0.0.0.0:13579
```