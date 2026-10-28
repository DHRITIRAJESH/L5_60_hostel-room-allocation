# Static Code Analysis Issues

| Issue | Type | Line(s) | Description | Fix Approach |
|-------|------|---------|-------------|--------------|
| Flask debug mode enabled (`B201`) | Security - High | 80 | The Flask application was started with `debug=True`, which can expose debugging functionality and create a security risk. | Changed `debug=True` to `debug=False`. |
| Unsafe YAML loading (`B506`) | Security - Medium | 21 | `yaml.load()` with an unsafe loader can execute arbitrary Python objects from untrusted YAML input. | Replaced `yaml.load()` with `yaml.safe_load()`. |
| Insecure logging configuration listener (`B612`) | Security - Medium | 72 | `logging.config.listen()` starts a network listener for logging configuration and can introduce a security risk. | Replaced the remote logging listener with local `logging.basicConfig()` configuration. |
| Non-cryptographic random generator (`B311`) | Security - Low | 56 | The `random` module was used for the room lottery. Bandit flags it because it is not suitable for security-sensitive randomness. | Replaced `random` with `secrets` and used `secrets.randbelow()` to select students. |
| Hardcoded database password (`B106`) | Security - Low | 66 | A database password was directly written in the source code, which can expose credentials. | Removed the hardcoded password and read it from the `WARDEN_DB_PASSWORD` environment variable. |
| Dangerous mutable default argument (`W0102`) | Code Quality | 28 | `preferred=[]` uses a mutable list as a default argument, which can lead to shared state between function calls. | Changed the default to `None` and initialized an empty list inside the function. |
| Missing module docstring (`C0114`) | Code Quality | 1 | The Python module did not contain a module-level documentation string. | Added a module docstring describing the program. |
| Missing function docstrings (`C0116`) | Code Quality | Multiple | Several functions did not have documentation strings explaining their purpose. | Added docstrings to the functions. |
| Invalid function naming (`C0103`) | Code Quality | Multiple | Function names used camelCase instead of the recommended Python snake_case convention. | Renamed functions such as `loadConfig()` to `load_config()` and `allocateRoom()` to `allocate_room()`. |
| Type comparison using `type()` (`C0123`, `E721`) | Code Quality / Style | 30 | The code compared a value's type directly using `type(year) != int`. | Replaced it with `not isinstance(year, int)`. |
| Unused imports (`W0611`, `F401`) | Code Quality / Style | 1-5 | The `os` and `sys` imports were unused in the original version. | Removed unused imports; `os` was later reintroduced when the database password was moved to an environment variable. |
| Dictionary iteration (`C0206`) | Code Quality | 60 | The code iterated over dictionary keys and then accessed the dictionary again. | Changed the iteration to use `rooms.items()`. |
| Line too long (`C0301`, `E501`) | Style | Multiple | Several lines exceeded the recommended line length. | Reformatted the affected lines and split long statements across multiple lines. |
| Incorrect blank lines (`E302`) | Style | Multiple | Top-level definitions did not have the required number of blank lines between them. | Added the required blank lines between top-level definitions. |
| Incorrect blank lines at end of file (`E305`) | Style | 101 | The original file did not have the correct spacing after the final function definition. | Corrected the file structure and used an `if __name__ == "__main__":` entry point. |

## Final Verification

- **Pylint:** 9.89/10
- **Bandit:** 0 issues identified
- **Flake8:** 0 errors
- All Bandit security issues identified in the baseline analysis were fixed.
- The final Pylint score is above the required target of 9.5.
- The final Flake8 report contains no output, indicating that no Flake8 violations remain.
