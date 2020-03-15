# WeLightProject

_Se trata de un aplicación sobre registros eléctricos. En él se muestra las consultas básicas de base de datos_

## Construido con 🛠️

* [Python](https://www.python.org/downloads/) - Lenguaje
* [Django](https://www.djangoproject.com/download/) - Framework
* [MySQL](https://dev.mysql.com/downloads/installer/) - Base de datos

### Instalación y puesta en marcha desde cero 🔧

_Creación de proyecto en python_

```
py -m venv *nombreproyecto*
```

_Activación del entorno virtual_

```
c\..\nombreproyecto\scripts\activate
```

_Instalación django_
``` 
pip install django
pip freeze // para asegurarnos que está instalado correctamente
``` 
_Creación proyecto django_
```
django-admin startproject *nombreproyecto*
```

_Poner en marcha el servidor_
```
python manage.py runserver  // Se debe estar ubicado en el directorio donde aparece manage.py
```

_Creación de aplicación_
```
python manage.py startapp generar
```

_Instalación de base de datos y migraciones correspondientes_
```
pip install pymysql
python manage.py makemigrations // Migrar modelos creados desde el proyecto
python manage.py migrate // Migrar modelos de datos básicos de django y los creados
```

_Recordad que para que funcione con mysql, hay que cambiar en el setting.py la configuración:_
```
DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'nameBD',
            'USER': 'user',
            'PASSWORD': 'password',
            'HOST': 'localhost',
            'PORT': '3306',
        }
    }
```
