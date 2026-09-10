# Finance tracker
#### Video Demo:  <https://youtu.be/EXtdcwVf3gQ>
Have you ever thought:
> I spend too much money but I don't understand where!

or

> I should be more responsible for how and when I spend money.

<ins>You are not alone</ins>. Banks often provide us with basic spendings summary but that usually is not enough to analyze your finances considering that you might spend your money in cash or on something specific. **The Finance Tracker** was created for *managing* and *analyzing finances* in one place.

## About the project
The project is built on `Python` programming language for ***CS50 Introduction to programming with Python course***. It is a **CLI-based** program that prompts the user to choose from the menu to:
1. `Add transaction` - prompts the user to fill the transaction details. If confirmed the transactions is added to a `CSV` file.
2. `View balance` - calculates balance from investments and ordinary payments that are within the `CSV` file and shows it to the user.
3. `View (un)filtered summary` - prompts the user to fill the filter details and if there `CSV` file exists, it contains data and the filters match the results, the user gets the filtered summary. Unfiltered summary can be shown if the user skips all the filters.
4. `Export wallet to Excel` - converts `CSV` file to `xlsx` and produces a file that can be opened in Excel for further analysis. If there is no data, action will be canceled.

To plan the project [Jira Kanban board](https://edx-project.atlassian.net/?continue=https%3A%2F%2Fedx-project.atlassian.net%2Fwelcome%2Fsoftware%3FprojectId%3D10000&atlOrigin=eyJpIjoiZjQ5ZDM1M2VhYWI4NGI5NTkxN2Y0NGFhNzJiNjYyNDIiLCJwIjoiamlyYS1zb2Z0d2FyZSJ9) was used, though it was not necessary but the goal was to improve, learn, experience and challenge myself.

## How to Run

### Requirements
To run the program `pytest`, `pandas` and `openpyxl` libraries are required.

### Installation
To install the project's dependencies, use command `pip install -r requirements.txt`

### Running the program
> [!NOTE]
> If you haven't added a transaction yet, don't use options 2, 3 or 4.
> `CSV` file does not exist on the first run.

To run the program, navigate to the project folder and then use command `python project.py`

### Testing the program
To test the program, navigate to the project folder and then use command `pytest test_project.py -v`

## Files

### Source files
Project's library contains 6 files in total:
- **analysis.py**
    - Holds functions used for analysis with Pandas library:
        - `load_data` - loads *CSV* file (if exists with data) to a pandas dataframe.
        - `filter_by` - filters the dataframe with user provided filters.
        - `export_to_excel` - exports *CSV* file to excel.
- **models.py**
    - Holds classes, global variables
- **project.py**
    - Main project file.
    - Holds functions including:
        - `main` - handles CLI flow;
        - `validate_transaction_date` - handles user entered transaction's date validation;
        - `validate_transaction_type` - handles user entered transaction's type validation;
        - `validate_amount` - handles user entered amount validation;
        - `validate_currency` - handles user entered currency validation;
        - `validate_category` - handles user entered category validation;
        - `get_valid_input` - handles user entered transaction or filter details's input validation and retry logic except for category validation;
        - `get_valid_category` - handles user entered transaction or filter category input custom validation;
        - `display_progress` - handles the display of user entered and validated transaction details.
        - 4 helper functions, that prints repeatable messages:
            - `control_c`
            - `control_c_trans`
            - `clear_CLI`
            - `enter_to_continue`
- **README.md**
    - Project's documentation.
- **requirements.txt**
    - All project's dependencies / `pip`-installable libraries are listed in this file.
- **test_project.py**
    - Project's testing file.
    - Holds testing functions including:
        - `test_validate_transaction_date` - tests *validate_transaction_date* function;
        - `test_validate_transaction_type` - tests *validate_transaction_type* function;
        - `test_validate_amount` - tests *validate_amount* function;
        - `test_validate_currency` - tests *validate_currency* function;
        - `test_validate_category` - tests *validate_category* function;

### Generated files
The program generates 2 files, both of them do not exist at first.
- **transactions.csv**
    - Is generated if the **first** transaction is created successfully.
    - Holds transactions created by user.
    - A file consists of 6 columns:
        - *transaction_date* - contains transaction date;
        - *transaction_type* - contains transaction type;
        - *amount* - contains amount;
        - *currency* - contains currency;
        - *category* - contains category of transaction;
        - *details* - contains details of transaction.
- **transaction_analysis.xlsx**
    - Is generated if the user wants to export transactions to *Excel* and if the `CSV` file exists with data
## Design decisions

### Why `CLI` for ***adding*** <ins>transactions</ins>?
The main reason for choosing `CLI` over ***front-end library*** was because it required to use the knowledge from `CS50` and it was more beginner friendly. The plan was to use *front-end library* later on, after finishing the `CLI` until the realisation that it would require to overwrite the whole program.

### Why `CSV` for ***storing*** <ins>transactions</ins>?
Choosing `CSV` was not a hard choice. This file format is commonly used for structured data. Choosing `TXT` file format instead would've been a poor choice for learning and it makes more sense to actually learn the right way to store related rows.

### Why `csv.DictReader` / `csv.DictWriter` for ***reading / writing*** <ins>transactions</ins>?
When choosing the right method - either `Pandas` library or `csv.DictReader + csv.DictWriter` - for reading and writing rows to the `CSV`, there was a few things to consider which took quite some time. Pandas are generally faster, more optimized and there are less code for reading. But since the code was headed towards dictionaries it was time to give up the easy method and use the skills `CS50` taught.

### Why ***separate*** `get_valid_*` from `validate_*`?
At first both functions were tied together until the realization that it could be compressed - the code to validate input repeats itself so `get_valid_*` became an universal function which prompts for `validate_*` to validate whatever the *\* ending* is. This split makes `validate_*` functions testable meaning that input should return a value. The `get_valid_*` function is not testable because it prompts the user for input which blocks waiting for a human.

### Why ***constrained*** <ins>categories</ins>?
The reason for constraining categories is simple: to make user's life simpler. By excluding options that do not belong to that transaction type the program gives less options to choose from and takes less of the user's time. For this to work, separate *get_valid* function `get_valid_category` was necessary because it included additional features.

### Why `models.py`?
When code gets complicated, separate files and folders makes a clear program structure. File `models.py` was meant for storing classes and global variables.

### Why `analysis.py`?
This file was separated because its purpose is to use `Pandas` for analysis and export. It is important to keep the CLI flow and I/O separate.

### Why no `GUI` and only `CLI` with `Pandas`?
At first there was ambitious goals to make a `Flet` front-end for this program. But soon enough the decision was made to not use it and just do a regular *CLI* because for the career path it was not relevant and just a waste of time. `Pandas` on the other hand might and will be helpful in the future and now.
