# TestingTriangles
The algorithm to determine triangle types was implemented in python using pytest. Different test cases were implemented to prove its consistency and correct functioning.

Installation of pytest is required. The following command must be executed:
```
pip install pytest
```
To check installation and see version:
```
pytest --version
```
Once installed and being in the directory of the project run to execute the tests:
```
pytest .\Test_Triangle.py
```

##Output
In the best case, all the nine tests should be passed without problem.
![image](https://user-images.githubusercontent.com/102324051/222635353-fc5af576-f91b-43df-9aa2-9c0e2e7b2f9c.png)

Nevertheless, as random functions are used when testing Scalene and Isosceles cases, sometimes those tests won't pass. This happens because, as parameters for the test come from a random function, sometimes this parameters will trigger the "Not a triangle" option, because the sum of two of the random numbers will be bigger than the third one.
 
This happens mostly in the scalene tests, because 3 random parameters are generated to be used as the 3 different sizes. However, this does not mean that the code missfunctions, it only means that the test did not pass because other constraint was activated and the code always verifies that all the rules for creating a triangle are considered. 

![image](https://user-images.githubusercontent.com/102324051/222636068-32826791-8519-4269-ac26-8ab730d96997.png)
