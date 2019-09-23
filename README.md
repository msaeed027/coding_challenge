# Coding challenge

## Run using docker-compose
The following command will run the app on port 80
```sh
docker-compose up -d --build
```
To stop the app just run
```sh
docker-compose down
```

> You will find a Postman collection under `postman/` directory contains the `combine endpoint` and 3 examples.

## Local ENV Installion
#### Install
Just create a virtual env and run pip as following
```sh
cd {project_dir}
python3 -m venv venv
venv\Scripts\activate # instead for linux use: . venv/bin/activate
pip install -e .[test]
```
#### Run the application
Make sure that you inside venv

For Linux and Mac:
```sh
export FLASK_APP=app
export FLASK_ENV=development
flask run
```
For Windows cmd, use set instead of export:
```sh
set FLASK_APP=app
set FLASK_ENV=development
flask run
```
For Windows PowerShell, use $env: instead of export:
```sh
$env:FLASK_APP = "app"
$env:FLASK_ENV = "development"
flask run
```

#### Run testing
```sh
# to run the test
pytest
# to run test coverage
coverage run -m pytest
coverage report
```

## Thinking

The problem indicated in this task fall under Cartesian product operation (All combinations between lists)

### Time complexity
lets imagine we have the following list of lists
```python
[
    [1, 2],
    ['A', 'B', 'C'],
]
```
the expected result (Cartesian product)
```python
[
    [1, 'A'], [1, 'B'], [1, 'C'], [2, 'A'], [2, 'B'], [2, 'C'], 
]
```

So the time complexity for the previous example will be the `len(list[0]) * len(list[1])` 
which in previous case will be `2 * 3 = 6`

> Because there's an assumption that we will have request with list of unlimited number of lists and each of these lists also contain unlimited number of items. lets define `n = len(list)` and `m = len(of the longest list)` out time complexity will be **O(m<sup>n</sup>)**  

So the time complexity for this problem will be **O(m<sup>n</sup>)** where `n = len(list)` and `m = len(of the longest list)` which is very bad time complexity but as per my knowledge until now I did't find any proper optimization

> Also if we have four lists we can solve them two by two then combine the result from each solve to get the final result (so each solve is mutually exclusive)

### Ways to improve the performance (Beyond the scope)
- Using map reduce to map our tasks to small problem and solve them on different machine then reduce them to a single result.
- Using threads so we can split our tasks to small problem and solve them on different machine then reduce them to a single result.

## Provided solution
Because in the task email you mentioned "*We expect you to create your own combination algorithm.*" I created 3 different method to solve this problem

Please note that the following method has different performance and they are ordered by the most performant come first and so on

### 1. py_combine
this method depends on python built-in method [itertools.product](https://docs.python.org/3/library/itertools.html#itertools.product)

### 2. custom_combine
this is a custom implementation for Cartesian product which based on we can solve them two by two.
#### More explanation
1. Take the first two list then solve them and get the result
2. Take the result from the previous operation and solve it with the third list and get the result
3. repeat step 2 until there's no more items in the list

### 3. rx_combine
this method is based on reactivex (RxPY) and the custom combine idea

I created an RxPY custom `cartesian_product` operator and used this operator to convert stream of lists to stream of all possible combination between these lists.

but what bother me a lot after using reactivex at this point that i faced a problem that i should convert the output stream to list to return a valid HTTP response and I have created a method to do so `observable_to_list` but i feel this a bad use for Reactive programming or it's not a good fit this context but i left it as it

## Endpoints
### Combination
```http
POST /combine
```
Combine by default use `py_combine`
- to change this behaviour to `custom_combine`
    ```http
    POST /combine?combination_type=custom
    ```
- to change this behaviour to `rx_combine`
    ```http
    POST /combine?combination_type=rx
    ```
#### Request Payload
```json
[
    ["product", ...],
    [...],
    ...
]
```
#### Response Payload
All possible combinations between the request lists
```json
[
    ["product", ...],
    [..., ...],
    ...
]
```