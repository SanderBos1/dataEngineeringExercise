install:
	venv\Scripts\activate \
	pip install --upgrade pip &&\
	pip install -r requirements.txt

make_vm:
	python -m venv venv


stream:
	uvicorn streamingfakeData:app --reload
