import os


def save_extensions(dir_name, first_level=False):
    """
    Search through the first level of the directory only and write information about each found file in report.txt.
    For testing is added subfolder folder(second_level) with file but is not included in report.txt.
    """

    for file_name in os.listdir(dir_name):
        file = os.path.join(dir_name, file_name)

        if os.path.isfile(file):
            extension = file_name.split('.')[-1]
            extensions[extension] = extensions.get(extension, []) + [file_name]

        elif os.path.isdir(file) and not first_level:
            save_extensions(file, first_level=True)


directory = 'test_directory'
output_file = 'report.txt'
extensions = {}
result = []

try:
    save_extensions(directory)
except FileNotFoundError:
    print('Directory does not exist')

extensions = sorted(extensions.items(), key=lambda x: (x[0]))

for extension, files in extensions:
    result.append(f'.{extension}')
    for file in sorted(files):
        result.append(f'- - - {file}')

with open(output_file, 'w') as f:
    f.write('\n'.join(result))
