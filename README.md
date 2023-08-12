# Likes-Services-V1

**Likes-Services-V1** is a microservice designed to encapsulate and manage all processing related to Likes within our (hypothetical) system. This microservice provides functionality to store Like events, check if a user has liked a particular content, and retrieve the total number of likes for a content. Additionally, it includes a placeholder implementation to showcase how push notifications would be handled when a user receives 100 likes.

## Architecture


## Tech Stack

- Programming Language: Python
- Web Framework: Django
- Database: SQLite3
- Containerization: Docker
- Message Broker: RabbitMQ (for handling events and notifications)
- Placeholder Push Notification Handling: Custom code to simulate  push notifications
- Version Control: Git
- Deployment: Docker Compose (for local development) and Kubernetes (for production)



## Features
The Likes-Services-V1 microservice offers the following features:

- Store Like Event
- Check User Liked Content
- Total Likes for Content
- Push Notification Placeholder
    - When a user receives 100 likes, the microservice showcases a placeholder code to demonstrate how push notifications would be handled. This serves as an example of how the system could respond when a significant milestone is reached.

## Run Locally
- **The entiree project is **Dockerized****

Clone the project

```bash
  git clone https://github.com/pnaskardev/Likes-Service-v1
```

Go to the project directory

```bash
  cd Likes-Service-v1
```

Install dependencies

```bash
    docker-compose up
```

**The microservices will struggle to connect with RabbitMQ at start but after 2-3 starts they will be able to connect and ready to recieve requests**



## API Reference

#### Get all Quotes

```http
  GET http://localhost:8000/quotes/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `None` | `None` | Get all the Quotes |

#### Post a Quote

```http
  Post http://localhost:8000/quotes/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `title`      | `string` | **Required**. Title of the Quote |
| `created_by`      | `Positive Integer` | **Required**. Id of the created user |

#### Post a Like
```http
  Post http://localhost:5000/api/post-like/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `user_id`      | `Positive Integer` | **Required**. Id of the User |
| `post_id`      | `Positive Integer` | **Required**. Id of the Quote |

#### Get Like Count
```http
  http://localhost:5000/api/like/like-count/
```
| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `post_id`      | `Positive Integer` | **Required**. Id of the Quote |

#### Check Like Status
```http
  http://localhost:5000/api/like/check-like-status/
```
| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `post_id`      | `Positive Integer` | **Required**. Id of the Quote |
| `user_id`      | `Positive Integer` | **Required**. Id of the User |



## Screenshots




## Authors

- [@pnaskardev](https://github.com/pnaskardev/)

