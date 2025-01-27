# becskasszasch-2

# Szükséges libek



Szükséges [könyvtárak](./requirements.txt) telepítése
```bash
pip install -r requirements.txt
```

# Futtatás 

## Lokálisan

```bash
python main-py
```

## Gunicorn-al

```bash
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```

## Helpful videók
[Python Website Full Tutorial - Flask, Authentication, Databases & More](https://www.youtube.com/watch?v=dam0GPOAvVI)
