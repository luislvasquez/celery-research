# Celery research

This repository contains the roadmap for celery usage as a task/job queue

## Components
### Core
* Backend (emulates backend)
* Thinking service (emulates heavy-cpu service)
    * Async version
    * Sync version
* Sender service (emulates result (from thinking service) sending service)

### To design
* Celery task queue per client
* Redis message broker and cache memory store

##  Research ToDo

* [ ] Redis integration: Store specific timestamp of delivered item to validate