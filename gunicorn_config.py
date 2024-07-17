import multiprocessing

command = '/home/joseruiz/codes/venv/wellpath/bin/gunicorn'
pythonpath = '/home/joseruiz/codes/Django_Gunicorn/Django_Gunicorn'
bind = '127.0.0.1:13579'
# Número de trabajadores (2 x núm. de CPUs) + 1
# workers = (2 * multiprocessing.cpu_count()) + 1
workers = 4

# Clase de trabajador
worker_class = 'gevent'  # Puedes probar 'gevent' o 'eventlet' para aplicaciones de I/O intensivo

# Número de conexiones por trabajador
worker_connections = 1000  # Ajusta este valor según tus necesidades

# Tiempo de espera en segundos
timeout = 2400
graceful_timeout = 240
keepalive = 5

# Otras configuraciones
loglevel = 'info'
errorlog = '-'
accesslog = '-'

