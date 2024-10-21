# Midterm - REPL Calculator with Plugin and Command Pattern.

A calculator built using Python that supports Pandas for history management, plugin-based extensions, and arithmetic operations.

## Setup Instructions

### Branches

- **master**: The main branch with all the core functionality.
- **commands**: A branch focused on implementing different command classes.

### Cloning the Repository

```bash
    git clone https://github.com/SamuelSudeepAyyala/Homework5.git
```

### Install dependencies

```bash
    python3 install -r requirements.txt
```

### Features

- REPL interface with arithmetic operations like Add, Subtract, Multiply, Divide
- Calculation history being managed using Pandas.
- Plugin system to dynamically load the arithmetic commands and other additional commands.

### Setting Up github Actions for CI/CD 

- Create ```.github/workflows/``` directory in the repo to define the Github actions for the pytest automation testing.

- Create a ```python.yml``` file in the workflow folder that is created to run the pytest checks and lint checks.

### Commit Process

```bash
git add <filename>
git commit -m "Comments about the commit"
git push origin master
```




