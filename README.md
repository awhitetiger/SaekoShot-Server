A locally hosted replacement for ShareX or Gyazo. This is the server backend of the application. For the client see this repo: https://github.com/awhitetiger/SaekoShot-Client/

***Configuration***

Edit the top variables in saeko.py

```
WEB_ROOT = '127.0.0.1' < The IP/Hostname of your Instance
ADMIN_USERNAME = "admin" < Authentication username for the index page
ADMIN_PASSWORD = "password" < Authentication password for the index page
API_KEY = "123" < User created API Key for uploading screenshots
```

You can browse your upload screenshots by navigating to the Web root of your server.
