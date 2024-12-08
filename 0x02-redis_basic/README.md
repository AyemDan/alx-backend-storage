# Redis Basic

This repository contains basic examples and exercises for working with Redis, a powerful in-memory data structure store.

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Introduction
Redis is an open-source, in-memory key-value store that can be used as a database, cache, and message broker. This project aims to provide a basic understanding of Redis and how to use it in various applications.

## Installation
To install Redis, follow these steps:

1. Download the Redis package from the [official website](https://redis.io/download).
2. Extract the package and navigate to the extracted directory.
3. Compile Redis by running `make`.
4. Start the Redis server by running `src/redis-server`.

Alternatively, you can use a package manager like `apt` (for Debian-based systems) or `brew` (for macOS) to install Redis.

## Usage
To interact with the Redis server, you can use the Redis CLI:

```sh
src/redis-cli
```

You can also use Redis with various programming languages. Below is an example using Python:

```python
import redis

# Connect to Redis server
r = redis.Redis(host='localhost', port=6379, db=0)

# Set a key-value pair
r.set('foo', 'bar')

# Get the value of a key
value = r.get('foo')
print(value)  # Output: b'bar'
```

## Examples
This repository includes several examples to help you get started with Redis:

- Basic CRUD operations
- Working with different data types (strings, lists, sets, hashes)
- Using Redis for caching
- Pub/Sub messaging

## Contributing
Contributions are welcome! Please fork this repository and submit a pull request with your changes.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.