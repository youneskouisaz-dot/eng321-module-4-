# Stack, Queue, and Bracket Checker

This project implements two basic data structures:

- Stack
- Queue

It also includes a bracket checker that validates whether brackets are correctly balanced and nested.

Supported brackets:

- `()`
- `[]`
- `{}`

## Features

### Stack
Supports:

- `push()`
- `pop()`
- `peek()`
- `is_empty()`
- `size()`

### Queue
Supports:

- `enqueue()`
- `dequeue()`
- `peek()`
- `is_empty()`
- `size()`

### Bracket Checker
The bracket checker uses a stack to determine whether brackets are properly matched.

Example:

```text
{[()]} -> Valid
{[(])} -> Invalid
