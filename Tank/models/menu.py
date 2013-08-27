response.title = settings.title
response.subtitle = settings.subtitle
response.meta.author = '%(author)s <%(author_email)s>' % settings
response.meta.keywords = settings.keywords
response.meta.description = settings.description
response.menu = [
(T('Overview'),URL('default','index')==URL(),URL('default','index'),[]),
(T('Graphs'),URL('default','graphs')==URL(),URL('default','graphs'),[]),
(T('Configuration'),URL('default','config')==URL(),URL('default','config'),[]),
]
