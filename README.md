# dprkdict
A web-based viewer for North Korean dictionary files provided by the E-C-K app.

## English - DPRK Dictionary

The dictionary that contains the word definitions has been extracted from a dictionary app that is available on Woolim tablet PCs in North Korea. All words and definitions have been extracted and deobfuscated and are now available in the `eng_kor_deobfuscated.dic.sqlite3` database. 

*Note*: This repository requires `git lfs`. Install on Ubuntu:
    
```bash
sudo apt install git-lfs
```

# Usage

It is recommended to run the app via Docker (docker-compose required). Just run the following command in this directory:
    
```bash
docker-compose up
```

The server will bind to TCP port 8000 on localhost:

```
http://localhost:8000/engdprk
```

If Docker is not available, it can be used as follows:

```bash
virtualenv env
env/bin/pip install -r requirements.txt
env/bin/python manage.py runserver
```

