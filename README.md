# Google Search in Terminal using Python

A simple Python script that allows you to perform Google searches directly from the terminal. It takes a query as input and provides the top 10 search results.

## Features

- Perform Google searches directly from the terminal.
- Fetch the top 10 search result links for the entered query.
- Lightweight and easy to use.

## Prerequisites

Make sure you have Python installed on your system. You also need the `googlesearch-python` library.

To install the required library, run:

```bash
pip install googlesearch-python
```

## How to Use

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   ```

2. Navigate to the repository:

   ```bash
   cd your-repo-name
   ```

3. Run the script:

   ```bash
   python google_search.py
   ```

4. Enter your query when prompted. The script will output the top 10 links for your search.

## Code Overview

```python
try:
    from googlesearch import search
except ImportError:
    print("MODULE NOT FOUND")

query = input("Enter Query PLz and we will provide top 10 links")

for i in search(query, tld="com", num=10, stop=10, pause=2):
    print(i)
```

### Explanation
- **`googlesearch` module**: Used to fetch Google search results.
- **Query Input**: The user provides a search query.
- **Search Execution**: The script fetches the top 10 links using the `search()` function.

## Example Usage

```bash
Enter Query PLz and we will provide top 10 links
Python programming tutorials
https://www.python.org/
https://realpython.com/
https://docs.python.org/3/tutorial/
...
```

## Contributing

Contributions are welcome! If you have suggestions or improvements, feel free to submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author

[Dhairya Vora](https://github.com/DR-Vora)

Make sure to replace `https://github.com/your-username/your-repo-name.git` with the actual URL of your repository. Let me know if you'd like to tweak it further!
