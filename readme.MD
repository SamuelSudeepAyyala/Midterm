# MidTerm - Advanced Python Calculator

This project will implement a Python-based REPL (Read-Eval-Print Loop) calculator that will explain modern software engineering principles using plugin architecture and design patterns. This project is built using Command Pattern and a plugin-based system. This calculator will support basic arithmetic operations along with maintaining calculation history using Pandas integration. Because each activity appears as an individual command, the application's  design allows simple functionality extension through plugins, supporting loose coupling and maintainable code. Important features include continuous integration using GitHub Actions, extensive error handling, unit testing with pytest, and durable storage of calculation history in CSV format. The solution serves as a great example of how to create software applications that are expandable, maintainable, and thoroughly tested by showing the practical application of software design principles such as environment variable configuration, strong logging, and a plugin architecture.

You can find the explanation video [here](https://drive.google.com/file/d/17ab4A5PzCJrxYgaxVPLkqLxmixgGQFBc/view?usp=drive_link)

## Branches
Based on the project requirements, the branches in the repository are:
- **master**: This is the main branch containing all the core functionality which will contain the complete implementation of:
    - REPL calculator interface
    - Basic arithmetic operations (Add, Subtract, Multiply, Divide)
    - History management with Pandas
    - Plugin system 
    - CSV export functionality
    - Logging system
    - Test suite
- **commands**: This branch is specifically focused on implementing different command classes. Dedicated to the Command Pattern implementation. Contains the command-specific code for :
    - AddCommand
    - SubtractCommand
    - MultiplyCommand
    - DivideCommand
    - ExitCommand
- **plugins**: 
    - Dedicated to the implementation and management of the plugin system
    - Likely contains code for dynamically loading and managing calculator plugins
    - May include the framework for adding new features as plugins
    - Work on this branch when developing or improving the plugin architecture
- **Logging**: 
    - Focus on implementing or improving logging functionality
    - May contain enhancements to the existing logging setup
    - Use this branch for adding more detailed logs, log rotation, or other logging features
- **History**:
    - The history branch in this REPL Calculator project focuses on managing calculation history and CSV export functionality. 
    - It features a HistoryManager class that tracks operations, operands, and results, allowing easy addition and retrieval of history entries. 
    - The CsvCommand class handles exporting this history to a CSV file, supporting both new file creation and appending to existing files.
    - This branch integrates with the main calculator operations, ensuring each calculation is recorded.
    - It also interfaces with the exit command, offering users the option to save their session history.
    - The branch includes comprehensive testing for both history management and CSV export features, ensuring reliability and data integrity.

## Features

### 1. Basic Arithmetic Operations
- Addition (AddCommand)
- Subtraction (SubtractCommand)
- Multiplication (MultiplyCommand)
- Division (DivideCommand)
- Error handling for cases like division by zero

### 2. History Management
- Automatic tracking of all calculations
- Operation type, operands, and results storage
- View calculation history
- Export history to CSV file
- Optional history saving on exit

### 3. Plugin System
- Dynamic command loading
- Modular architecture
- Extensible operation support
- Organized plugin structure in `app/plugins/`

### 4. REPL Interface
- Interactive command-line interface
- User-friendly input prompts
- Clear result display
- Exit command with save options

### 5. Logging System
- Comprehensive operation logging
- Error tracking and debugging
- Configurable logging levels
- Log file management

## Workflow Details

The CI/CD pipeline performs the following steps:

1. **Environment Setup**:
   - Runs on the latest Ubuntu environment
   - Sets up Python 3.10

2. **Dependency Installation**:
   - Upgrades pip to the latest version
   - Installs `flake8` and `pytest`
   - Installs all dependencies listed in `requirements.txt` (if present)

3. **Testing**:
   - Runs pytest for unit testing
   - Executes pytest with pylint for code quality checks
   - Performs test coverage analysis using pytest and coverage

## Setup Instructions
1. Clone the repository:

    ```bash
    git clone https://github.com/SamuelSudeepAyyala/Midterm.git
    ```

2. Navigate to the project directory:

    ```bash
    cd Midterm
    ```

3. Checkout the `branchname` to access the latest plugin system implementation:

    ```bash
    git checkout plugins
    git checkout commands
    etc
    ```

4. Install any dependencies (if applicable).
    ```bash
    pip3 install -r requirements.txt
    ```

5. **Run the main Python file:**
    ```bash
    python main.py
    ```

6. **Execute a command:**
    The program will prompt for user input. For example, to add two numbers:
    ```
    Type 'menu' to show menu
    Type 'exit' to exit 
    >>> menu
    Welcome to the Basic Calcualator.
    Select the operation to be performed
    Add
    Subtract
    Multiply
    Divide
    >>> add
    Enter two space-seperated numbers: 23 2
    Addition result: 25
    ```

## Running Tests Locally

To replicate the CI environment locally, you can run the following commands:

```bash
# Install dependencies
pip install -r requirements.txt
pip install flake8 pytest pytest-pylint pytest-cov

# Run tests
pytest
pytest --pylint
pytest --pylint --cov
```
## Usage

To run the project:
```bash
python main.py
```

## History & Data Management

The calculator maintains a history of all operations in a CSV file format. The history is stored in `data/calculator_history.csv`.


When the application is exited, it checks for the existence of a `data` folder. If the folder does not exist, it will be created automatically. The application will then prompt the user to save the calculation history. 

### Saving History

- If the user chooses to save, the history will be exported to `calculation_history.csv` within the `data` folder.
- This ensures that all calculations performed during the session are preserved for future reference.

### Example Workflow

1. **Exit Command**: When you run the `exit` command, the application will:
   - Check for the `data` folder.
   - Prompt you with a message: "Do you want to save the calculation history? (yes/no)"
   
2. **User Decision**:
   - If you respond with `yes`, the application will create the `data` folder (if it doesn't exist) and save the history to `calculation_history.csv`.
   - If you respond with `no`, the history will not be saved.
## CSV File Structure

The history is stored with the following columns:


|   Operation     |   Operand1   |   Operand2   |   Result   |
|-----------------|---------------|---------------|------------|
|   Add           |   4.0        |   3.0        |   7.0      |
|   Subtract      |   4.0        |   5.0        |   -1.0     |
|   Multiplication |   5.0       |   3.0        |   15.0     |
|   Division      |   50.0       |   2.0        |   25.0     |

Each row in the CSV contains:
- **Operation**: Type of arithmetic operation (Addition, Subtraction, Multiplication, Division)
- **Operand1**: First number in the calculation
- **Operand2**: Second number in the calculation
- **Result**: Final result of the operation

The history can be saved upon exiting the calculator by selecting 'Y' when prompted.


## To work on these branches Git commands that can be useful
### Cloning the repository:
```bash
git clone https://github.com/SamuelSudeepAyyala/Midterm
cd Midterm
```
### Switching to the required branch:
```bash
git checkout main
git checkout <branch_name> # the branch names are mentioned above
```
### Viewing the branches
```bash
git branch -a
```
### Creating a new branch
```bash
git checkout -b new-feature-branch
```
###  Committing changes
```bash
git add .
git commit -m "Description of your changes"
```
### Pushing changes to the remote repository
```bash
git push origin <branch_name>
```
### Pulling changes from the remote repository
```bash
git pull origin <branch_name>
```
### Merging changes from one branch to another
```bash
git checkout main
git merge <branch_name>
```
**Note : Remember to always pull the latest changes before starting to work on a branch** 
```bash
git checkout branch-name
git pull origin branch-name
```
