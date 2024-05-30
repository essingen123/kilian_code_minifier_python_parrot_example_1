# kilian_code_minifier_python_parrot_example_1

## Overview

`kilian_code_minifier_python_parrot_example_1` is a Python script designed to minify Python code files. The script processes all `.py` files in a directory, removes unnecessary whitespace and comments, and outputs the minified versions to a new folder named `kilian_code_minifier_parrot_result`. Additionally, it can be installed as a command in your `.bashrc` for convenient usage.

## Features

- Minifies Python code by removing unnecessary whitespace and comments.
- Processes all `.py` files in a specified directory.
- Outputs minified files to `kilian_code_minifier_parrot_result` folder.
- Optionally installs itself as a command in `.bashrc` for easier usage.

## Usage

### Running the Script

1. Save the script as `kilian_code_minifier_parrot.py`.
2. Run the script to minify all Python files in the current directory:
   ```sh
   python kilian_code_minifier_parrot.py
   ```
3. The minified files will be located in the `kilian_code_minifier_parrot_result` folder.

### Installing as a Bash Command

To install the script as a command in your `.bashrc`:

1. Run the script with the `--install` option:
   ```sh
   python kilian_code_minifier_parrot.py --install
   ```
2. After running the install command, restart your terminal or source your `.bashrc`:
   ```sh
   source ~/.bashrc
   ```
3. You can now use the alias `kilian_minifier_parrot` to run the script in any directory:
   ```sh
   kilian_minifier_parrot
   ```

## Example

```sh
$ python kilian_code_minifier_parrot.py
2024-05-30 12:00:00 - INFO - Starting minification in folder: /path/to/your/files
2024-05-30 12:00:00 - INFO - Processed file: /path/to/your/files/example.py
2024-05-30 12:00:00 - INFO - Minified files are in the 'kilian_code_minifier_parrot_result' folder.

$ kilian_minifier_parrot
2024-05-30 12:00:00 - INFO - Starting minification in folder: /current/directory
2024-05-30 12:00:00 - INFO - Processed file: /current/directory/example.py
2024-05-30 12:00:00 - INFO - Minified files are in the 'kilian_code_minifier_parrot_result' folder.
```

## License

This project is licensed under the MIT License.
