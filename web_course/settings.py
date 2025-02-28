# ...existing code...

# Custom user model
AUTH_USER_MODEL = 'accounts.CustomUser'

# Login and logout redirect URLs
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'

# Media files settings
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# ...existing code...
