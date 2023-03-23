# Digified

## How to build the docker image

You can clone the repository or dowenload it, after that go the repositort directory and run this command

```
docker-compose build
```
the image will be built and you access API via 

```
http://localhost:8000
```


## How to test the model

You can test the model throw the API you can send request using postman, web browser or you can edit TestScript.py by changing
name variable in the file and run thr file using the command.
```
python TestScript.py
```

The output is the predicted label and the confidance score if the predicted label if normal the confidance score will be 1 - confidance score
An Example:
```
input: "احمد محمد محود"
ouput: {'Prediction': 'Normal', 'confidence': '0.9978874372318387'}

input: "احمدد محمد محود"
ouput: {'Prediction': 'Fake', 'confidence': '0.85792416'}

```


## Support the claims and resuls

test the model with test data and this is the classifiaction report 
```
          precision    recall  f1-score   support

      normal       0.98      0.62      0.76      2011
        fake       0.72      0.99      0.83      1989

    accuracy                           0.80      4000
   macro avg       0.85      0.80      0.80      4000
weighted avg       0.85      0.80      0.80      4000
```
from the classification report, we can find that the model can detect fake names well but it has a problem with normal names it see paert of the normal names as fake names

