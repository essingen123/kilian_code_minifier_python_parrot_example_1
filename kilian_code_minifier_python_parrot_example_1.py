import os
import sys
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def minify_code(code):
    lines = code.split('\n')
    minified_lines = []
    for line in lines:
        stripped = line.strip()
        if stripped and not stripped.startswith('#'):
            minified_lines.append(stripped)
    return ''.join(minified_lines)

def process_file(file_path, output_folder):
    try:
        with open(file_path, 'r') as file:
            code = file.read()
        minified_code = minify_code(code)
        output_path = os.path.join(output_folder, os.path.basename(file_path))
        with open(output_path, 'w') as output_file:
            output_file.write(minified_code)
        logging.info(f"Processed file: {file_path}")
    except Exception as e:
        logging.error(f"Failed to process file {file_path}: {e}")

def minify_folder(input_folder, output_folder='kilian_code_minifier_parrot_result'):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    for root, _, files in os.walk(input_folder):
        for file in files:
            if file.endswith('.py'):
                process_file(os.path.join(root, file), output_folder)

def add_to_bashrc():
    try:
        home = os.path.expanduser("~")
        bashrc_path = os.path.join(home, '.bashrc')
        script_path = os.path.realpath(__file__)
        command = f'alias kilian_minifier_parrot="python {script_path}"\n'
        with open(bashrc_path, 'a') as bashrc:
            bashrc.write(command)
        logging.info("Added to .bashrc. Restart your terminal or run 'source ~/.bashrc' to use the alias.")
    except Exception as e:
        logging.error(f"Failed to add alias to .bashrc: {e}")

def main():
    input_folder = os.getcwd()
    logging.info(f"Starting minification in folder: {input_folder}")
    minify_folder(input_folder)
    logging.info(f"Minified files are in the 'kilian_code_minifier_parrot_result' folder.")

if __name__ == "__main__":
    if '--install' in sys.argv:
        add_to_bashrc()
    else:
        main()
        script_name = os.path.basename(__file__)
        print("\nTo make this script easier to use, you can install it as a command in your bashrc.")
        print("Run the following command to do so:")
        print(f"python {script_name} --install")
        print("After running the install command, restart your terminal or run 'source ~/.bashrc'.")
        print("You can then use the alias 'kilian_minifier_parrot' to run the script in any directory.")
