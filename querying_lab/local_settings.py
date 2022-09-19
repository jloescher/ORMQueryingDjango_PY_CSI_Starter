# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '3tw(9e18zq178ivsp+nane92fg*(xjfibhdd)6fq)t1bp7kwd*'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'school_db',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True
        }
    }
}

