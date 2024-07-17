# Django_Gunicorn`

```
pip install --upgrade gevent


source ../venv/wellpath/bin/activate
gunicorn -c gunicorn_config.py Django_Gunicorn.wsgi --bind 0.0.0.0:13579

sudo service nginx start
sudo service nginx stop

```

docker
https://www.youtube.com/watch?v=vJAfq6Ku4cI&ab_channel=Djangoroad

server
https://www.youtube.com/watch?v=YnrgBeIRtvo&t=2s&ab_channel=Djangoroad
