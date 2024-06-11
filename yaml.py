# Scalars: Basic values like strings, numbers, booleans, and null.
key: value

# Lists: Ordered collections of items.
items:
  - item1
  - item2
  - item3

# Dictionaries: Collections of key-value pairs.
person:
  name: John
  age: 30
  address:
    city: New York
    state: NY

# Data Types
string1: "Hello, World"
string2: Hello, World
integer: 42
float: 3.14
is_active: true
empty_value: null

# This is a comment
key: value

# Multiple Docuement Seperater
---
document1:
  key1: value1
---
document2:
  key2: value2

# Anchors and Aliases
defaults: &defaults
  adapter: postgres
  host: localhost

development:
  <<: *defaults
  database: dev_db


# Complex Structures:
- step: &id001
    instrument: Laser spectrometer
    measurements: [1, 2, 3]
- step: &id002
    instrument: Ion microprobe
    measurements: [4, 5, 6]
- step:
    instrument: Ion microprobe
    measurements: *id002

# Configuration Files:
version: '3'
services:
  web:
    image: nginx
    ports:
      - "8080:80"

# Automation Scripts
name: CI Pipeline
on: [push]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2



# Example
# Application configuration
application:
  name: MyApp
  version: 1.0.0
  debug: true

# Database configuration
database:
  adapter: mysql
  host: localhost
  port: 3306
  username: root
  password: password

# List of servers
servers:
  - name: server1
    ip: 192.168.1.1
    role: frontend
  - name: server2
    ip: 192.168.1.2
    role: backend

# Nested configuration with anchors and aliases
defaults: &defaults
  adapter: postgres
  host: localhost

environments:
  development:
    <<: *defaults
    database: dev_db
  production:
    <<: *defaults
    database: prod_db
