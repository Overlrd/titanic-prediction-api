# titanic-prediction-api
[APi for Titanic - Machine Learning from Disaster](https://titanic-prediction-api-0.herokuapp.com/) on Heroku.


The APi expect a python dictionnary structured as below :

```json
{
  "Pclass": "int",
  "Sex": "int",
  "Sibsp": "int",
  "Parch": "int",
  "Embarked": "int",
  "CabinBool": "Bool",
  "AgeGroup": "int",
  "Title": "int",
  "Fareband": "int"
}
```

   - The passenger Ticket class
   - The passenger Gender
   - Number of siblings / spouses aboard the Titanic	
   - Number of parents / children aboard the Titanic	
   - Port of Embarkation	
   - The passenger have a Cabin NUmber or Not
   - Passenger Age Group
   - Title
   - Passenger fare	
   
   

 The Data is then Passed to a Keras Model trainde on the  [*Titanic - ML from disaster Dataset*](https://www.kaggle.com/competitions/titanic/data)
 
 The output is a dictionnary with *1* or *0* for if passenger survived or not
 
 
 ![image](https://user-images.githubusercontent.com/90383672/197556773-8d633118-5603-4ad4-a777-1900ad5d3d82.png)
