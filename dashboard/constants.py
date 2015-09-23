## ENV
LIVE = 'live'
STAGING = 'staging'
DEV = 'dev'

## AUTH
AUTH_FACEBOOK = 'facebook'
AUTH_BASIC = 'basic'

AUTH_SERVICE_URL_MAP = {
    LIVE: 'https://gobbl-auth.herokuapp.com',
    STAGING: 'https://gobbl-auth.herokuapp.com',
    DEV: 'http://localhost:3000'
}

## API
API_SERVICE_URL_MAP = {
    LIVE: 'https://snakebite.herokuapp.com',
    STAGING: 'https://snakebite.herokuapp.com',
    DEV: 'http://localhost:8000'
}