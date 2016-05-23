from instagram.client import InstagramAPI

client_id = 'acb84376812747f0b6086b14e905332b'

client_secret = 'b638f8a09d28480d8e20541a2c51bafc'

redirect_uri = 'http://127.0.0.1:5000/authorization-completed/'

scope = 'public_content'

api = InstagramAPI(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri)
