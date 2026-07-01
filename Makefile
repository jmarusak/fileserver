run:
	python app.py

serve:
	gunicorn --bind 0.0.0.0:8000 app:app

show:
	ip addr show
