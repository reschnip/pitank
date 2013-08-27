from gluon.storage import Storage
settings = Storage()

settings.migrate = True
settings.title = 'My New App'
settings.subtitle = 'powered by web2py'
settings.author = 'you'
settings.author_email = 'you@example.com'
settings.keywords = ''
settings.description = ''
settings.layout_theme = 'Default'
settings.database_uri = 'sqlite://storage.sqlite'
settings.security_key = 'bd572829-3f3a-4567-a2eb-2bab8b72fd41'
settings.email_server = 'smtp.gmail.com:587'
settings.email_sender = 'beardedowen@googlemail.com'
settings.email_login = 'beardedowen@googlemail.com:bad666ger'
settings.login_method = 'local'
settings.login_config = ''
settings.plugins = []
