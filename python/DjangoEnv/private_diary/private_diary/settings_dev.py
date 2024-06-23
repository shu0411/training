from .settings_common import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-8ba&=tkfdv@kbk#lsvs8dyf87u-8x+&h6r4jk4$$=e-rsa=533'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

#ロギング設定
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'loggers': {
        # Djangoが利用するロガー
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
        },
        # diaryアプリケーションが利用するロガー
        'diary': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'dev'
        },
    },
    'formatters': {
        'dev': {
            'format': '\t'.join([
                '%(asctime)s',
                '[%(levelname)s]',
                '%(pathname)s:%(lineno)d',
                '%(message)s'
            ])
        },
    },
}

# メールバックエンドの設定
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

#メディアファイルの配置場所
MEDIA_ROOT = os.path.join(BASE_DIR,'media')