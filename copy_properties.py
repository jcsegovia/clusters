import sys
import os
import shutil

BASE_PROPERTIES_DIR = './0_properties_base'


def print_help():
    print(f'Wrong numer of arguments.')
    print(f'Expected: python copy_prperties.py <dst_dir>')
    print(f'\t e.g: python copy_properties.py 0_run_1')


if len(sys.argv) < 2:
    print_help()
    exit()

DST_DIR = sys.argv[1]
print(DST_DIR)

property_file_dirs = os.listdir(BASE_PROPERTIES_DIR)
for property_file_dir in property_file_dirs:
    if property_file_dir.startswith('.'):
        continue
    property_file_name = f'{property_file_dir}/config.properties'
    src_file = f'{BASE_PROPERTIES_DIR}/{property_file_name}'
    dst_file = f'./{DST_DIR}/{property_file_name}'
    print(f'Property file: {src_file} -> {dst_file}')
    shutil.copy(src_file, dst_file)

print('Done\n')

