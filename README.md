# comment_service
REST API for comments

## Installation
You should create a .env based on .env.example and change the default values.

## Deploy
Run `docker compose up`

## API Documentation
The api documentation can be found at http://localhost/docs

## TODOs
- More API verbs
- Caching system (at least HTTP with etags)
- A service layer or command handlers
- Improve project tooling (linter/testing lib)
- A status in the comments and the associated rules (draft/published/...)
- Use a DI container to inject repositories
- Split DTOs
- Improve testing (update/delete/post tests should not have to create first => I would have add some InMemoryRepository)
- Move the current tests into a dedicated directory (actual tests are a bit more e2e than controller testing)
- Improve containers security (change USER, multistage, add express account, ...)
- Improve application security
- Improve compose (healthcheck/restart...)

## To consider
- More DDD: create a real domain, convert thread to a real aggregate, ...
- CQRS
- HATEOAS
- Sending messages to a queue when create/update/delete succeed or fail
- Use another framework
