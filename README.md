## Long running task queue

A project I've built during a take-home test.

### What does it do ?

- The application uses FastApi to expose endpoints.
- The request sets off a function which sends the received element to the task queue and returns the "task_id"
- The user can check the status of the task during the execution and after the execution using the previously mentione "
  task id"

API : FastApi, Task Queue : Celery, Message Broker/Backend : Redis

Install notes :

1) Install docker + docker-compose
2) Clone the repo
3) Switch to cloned directory
4) Execute : docker-compose -f docker-compose.yml
5) Test the endpoints using Postman/Curl/etc.

Endpoints :

- http://127.0.0.1 - Allowed : GET - A list of all items
- https://127.0.0.1/tasks - Allowed : POST - add an item to the queue
  (format : {"item_id": "test_element1"})
- https://127.0.0.1/tasks/{task_id} - Allowed : GET - Return a specific task