import sys
import os
import shutil

def print_help():
    print(f'Wrong numer of arguments.')
    print(f'Expected: python clone_directory.py <src_dir> <dst_dir>')
    print(f'\t e.g: python clone_directory.py 0_data_step_2_withtout_classify 0_run_1')


if len(sys.argv) < 3:
    print_help()
    exit()

SRC_DIR = sys.argv[1]
DST_DIR = sys.argv[2]

print(f'Clonning from {SRC_DIR} -> {DST_DIR}')

if not os.path.exists(SRC_DIR):
    raise ValueError(f"Not found source directory {SRC_DIR}")

if os.path.exists(DST_DIR):
    raise  ValueError(f'Dst directory {DST_DIR} already exists')

print(f'Clonning from {SRC_DIR} -> {DST_DIR}')

shutil.copytree(SRC_DIR, DST_DIR)

print('Done.')