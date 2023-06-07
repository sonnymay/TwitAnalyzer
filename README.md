# TwitAnalyzer

Hello! This is **TwitAnalyzer**, a simple Python project that fetches recent tweets of a specified user and performs a basic sentiment analysis on them. It leverages the power of the `tweepy` and `textblob` libraries.

Created by **sonnymay**.

## Features

- Fetches recent tweets from a user's timeline
- Performs basic sentiment analysis on the tweets

## Getting Started

### Prerequisites

- Python 3.6+
- `tweepy` library
- `textblob` library

You can install the required Python libraries with pip:

```shell
pip install tweepy textblob
```

### Setting up

1. Clone this repository to your local machine.

    ```shell
    git clone https://github.com/sonnymay/TwitAnalyzer.git
    ```

2. Navigate to the project directory.

    ```shell
    cd TwitAnalyzer
    ```

3. Open `main.py` and replace `'consumer_key'`, `'consumer_secret'`, `'access_token'`, `'access_token_secret'` with your Twitter API credentials.

4. Run `main.py` with Python.

    ```shell
    python main.py
    ```

## Usage

The main functionality is provided by the `TwitterAnalyzer` class. 

To analyze the sentiment of a user's tweets, use the `analyze_user_tweets` method:

```python
analyzer = TwitterAnalyzer('consumer_key', 'consumer_secret', 'access_token', 'access_token_secret')
print(analyzer.analyze_user_tweets('elonmusk', count=100))
```

This will print a dictionary with counts of 'Positive', 'Neutral', and 'Negative' tweets.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)

---

Remember to replace `'consumer_key'`, `'consumer_secret'`, `'access_token'`, `'access_token_secret'` with your Twitter API credentials and `'elonmusk'` with the Twitter handle of the user you wish to analyze.
