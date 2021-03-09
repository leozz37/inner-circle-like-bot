# Inner Circle Like Bot

**This is a WIP**

[![Unit Tests](https://github.com/leozz37/inner-circle-like-bot/actions/workflows/unit-tests.yml/badge.svg)](https://github.com/leozz37/inner-circle-like-bot/actions/workflows/unit-tests.yml)

Inner Circle is a dating app, where you must "like" a person and vice versa so that you can chat!
Sometimes clicking like several times in a row can be a tiring task, so we created a bot to automate that task!

## Running

First you need an Inner Circle account (create one [here](https://theinnercircle.co/) if you don't have one) and
have [Python](https://www.python.org/downloads/) installed on your machine.

Clone or download this repository:

```shell
$ git clone https://github.com/leozz37/inner-circle-like-bot
```

This project uses **pipenv** and **pre-commit** in order to run some static
checks and formatting on the code. After clone the repository you need to create
a new **virtual environment** and install the dependencies:

```shell
$ pipenv shell
$ pipenv install
```

To run the bot, run the following command:

```shell
$ python3 bot.py
```
