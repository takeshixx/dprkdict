# dprkdict
A web-based viewer for North Korean dictionary files provided by the E-C-K app built with [Django](https://www.djangoproject.com/).

## English - DPRK Dictionary

The dictionary that contains the word definitions has been extracted from a dictionary app that is available on Woolim tablet PCs in North Korea. All words and definitions have been extracted and deobfuscated and are now available in the `eng_kor_deobfuscated.dic.sqlite3` database. 

# Usage

It is recommended to use virtualenv to create a environment:

```bash
virtualenv env
env/bin/pip install -r requirements.txt
env/bin/python manage.py runserver
```

The server will bind to TCP port 8000 on localhost:

```
http://localhost:8000/engkor
```
