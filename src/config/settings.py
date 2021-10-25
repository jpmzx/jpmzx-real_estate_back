from dotenv import dotenv_values

SECRETS = dotenv_values(".env")
if not SECRETS:
    # Trying to get .env file from the parent folder
    SECRETS = dotenv_values("../.env")
if not SECRETS:
    raise NotImplementedError(
        '''
        Please create the .env file before start the program.
        Check README.md for more information.
        '''
    )

# START: Http handler related configs
SERVER_NAME = SECRETS.get('SERVER_NAME', 'localhost')
PORT = int(SECRETS.get('SERVER_PORT', 5000))


DATABASE = {
    'HOST': SECRETS['DATABASE_HOST'],
    'PORT': SECRETS['DATABASE_PORT'],
    'DATABASE': SECRETS['DATABASE_DATABASE_NAME'],
    'USER': SECRETS['DATABASE_USER'],
    'PASSWORD': SECRETS['DATABASE_PASSWORD']
}
