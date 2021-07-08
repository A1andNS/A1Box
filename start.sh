gunicorn -w 4 -b 0.0.0.0:5000 app:app -D
cd share && python3 -m http.server 8000 --cgi
