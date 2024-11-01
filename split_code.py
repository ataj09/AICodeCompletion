import os
import random

def read_files_from_repo(repo_path):
    code_files = []
    for root, dirs, files in os.walk(repo_path):
        for file in files:
            if file.endswith('.py'):  # python files selected for this example
                with open(os.path.join(root, file), 'r') as f:
                    code_files.append(f.read())
    return code_files


def split_code(code, num_splits=30, min_chars2fill = 10, max_chars2fill = 100):
    split_examples = []
    code_lines = code.split('\n')
    max_try_count = 10

    for _ in range(num_splits):
        if len(code_lines) < 5:  # Skip files with insufficient code
            continue

        middle = ""
        prefix = ""
        suffix = ""

        try_count = 0

        while True:
            split_point_start = random.randint(1, len(code_lines) // 2)
            split_point_end = random.randint(split_point_start, len(code_lines) - 2)

            prefix = '\n'.join(code_lines[:split_point_start])
            middle = '\n'.join(code_lines[split_point_start:split_point_end])
            suffix = '\n'.join(code_lines[split_point_end:])

            try_count += 1
            if try_count > max_try_count:
                break

            if len(middle) > min_chars2fill and len(middle) < max_chars2fill:
                split_examples.append({
                    'prefix': prefix,
                    'middle': middle,
                    'suffix': suffix
                })
                break


    return split_examples

def generate_dataset(repo_path, num_examples=30):
    files = read_files_from_repo(repo_path)
    dataset = []

    for file in files:
        splits = split_code(file, num_splits=num_examples // len(files))
        dataset.extend(splits)

    return dataset

