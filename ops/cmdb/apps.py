from django.apps import AppConfig
import os

class CmdbConfig(AppConfig):
    name = 'cmdb'
    DATABASES = {'default': {'ENGINE': 'django.db.backends.mysql', 'NAME': 'mydjango',
                             'USER': os.environ.get('MYSQL_USER', None), 'PASSWORD': os.environ.get('MYSQL_PSWD', None),
                             "HOST": '192.168.100.30', 'PORT': 3306,
                             'OPTIONS':{'isolation_level': None}
                             }
                 }
    LANGUAGE_CODE = 'zh-Hans'
    TIME_ZONE = 'Asia/Shanghai'
