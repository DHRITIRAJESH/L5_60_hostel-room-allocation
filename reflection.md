### 1. What did you learn from using Pylint, Bandit, and Flake8?

I learned that different static analysis tools focus on different aspects of code quality. Pylint helped identify code-quality and maintainability issues such as missing documentation, naming conventions, unsafe default arguments, and unused code. Bandit focused specifically on security vulnerabilities, such as unsafe YAML loading, hardcoded passwords, insecure logging configuration, and Flask debug mode. Flake8 mainly identified style and formatting problems such as unused imports, excessive line length, and incorrect spacing. Using all three tools together provided a more complete analysis of the program.

### 2. Which tool did you find most useful and why?

Bandit was particularly useful because it identified security issues that might not be obvious during normal testing. For example, it detected the hardcoded database password, unsafe use of `yaml.load()`, insecure logging configuration, and Flask debug mode. These issues could create security risks even though the program itself could still execute successfully.

### 3. How did static analysis improve your code?

Static analysis improved the readability, maintainability, security, and consistency of the program. I added appropriate documentation, changed function names to follow Python naming conventions, removed unused imports, corrected formatting issues, replaced unsafe YAML loading, removed the hardcoded password, and disabled Flask debug mode. The final code achieved a Pylint score of 9.89/10, with Bandit reporting no issues and Flake8 reporting no errors.

### 4. Were there any issues you chose not to fix? Why?

The final Pylint report contains one warning for the unused `gender` argument (`W0613`). I chose not to remove it because it is part of the existing `allocate_room()` function interface and removing it could unnecessarily change the program's interface. The Pylint score was already 9.89/10, which satisfies the required score of above 9.5.

### 5. What was the difference between the initial and final analysis?

The initial analysis reported multiple Pylint, Bandit, and Flake8 issues. The Pylint score was initially 5.84/10. After the fixes, the score increased to 9.89/10. Bandit initially reported five security issues and finally reported zero issues. Flake8 initially reported multiple formatting and style errors and finally produced no output, indicating that no Flake8 violations remained.

### 6. What are the benefits of using multiple static analysis tools?

Using multiple tools provides broader coverage because each tool detects different types of problems. Pylint evaluates overall Python code quality and maintainability, Bandit concentrates on security vulnerabilities, and Flake8 checks style and formatting. Therefore, using them together can identify problems that might be missed if only one tool were used.
