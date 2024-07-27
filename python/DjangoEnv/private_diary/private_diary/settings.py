from .settings_common import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [os.environ.get('ALLOWED_HOSTS')]

# 静的ファイルの配置場所
STATIC_ROOT = '/usr/share/nginx/html/static'
MEDIA_ROOT = '/usr/share/nginx/html/media'

#Amazon SESを利用するための設定
AWS_SES_ACCESS_KEY_ID = os.environ.get('AWS_SES_ACCESS_KEY_ID')
AWS_SES_SECRET_ACCESS_KEY = os.environ.get('AWS_SES_SECRET_ACCESS_KEY')
EMAIL_BACKEND = 'django_ses.SESBackend'

#ロギング設定
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    # ロガーの設定
    'loggers': {
        # Djangoが利用するロガー
        'django': {
            'handlers': ['file'],
            'level': 'INFO',
        },
        # diaryアプリケーションが利用するロガー
        'diary': {
            'handlers': ['file'],
            'level': 'INFO',
        },
    },
    # ハンドラの設定
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/django.log'),
            'formatter': 'prod',
            'when': 'D', # ログローテーションの単位(D=日次)
            'interval': 1, # ログローテーション間隔
            'backupCount': 7, # 保存しておくログファイル数
        },
    },
    #フォーマッタの設定
    'formatters': {
        'prod': {
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