FROM python:3.9.15

RUN pip install --upgrade pip

ADD app.py .
ADD Dataset ./Dataset
ADD results ./results
ADD requirements.txt .
ADD GenerateNames.py .
ADD modeling.ipynb .
ADD TestScript.py .
ADD Visualization.ipynb .

RUN pip install -r  requirements.txt
EXPOSE 8000

CMD ["python", "./app.py"]