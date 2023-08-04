import sys
import os
import shutil

def print_help():
    print(f'Wrong numer of arguments.')
    print(f'Expected: python clone_directory.py <src_dir> <dst_dir> [-noscripts]')
    print(f'\t e.g: python clone_directory.py 0_data_step_2_withtout_classify ./ test_1')
    print(f'\t e.g: python clone_directory.py 0_data_step_2_withtout_classify ../runs_directory test_1')


if len(sys.argv) < 4:
    print_help()
    exit()

include_scripts = True
if len(sys.argv) > 4:
    if "-noscripts" == sys.argv[4]:
        include_scripts = False

SRC_DIR = sys.argv[1]
DST_DIR = sys.argv[2]
RUN_DIR = sys.argv[3]

print(f'Cloning from {SRC_DIR} -> {DST_DIR}')

if not os.path.exists(SRC_DIR):
    raise ValueError(f"Not found source directory {SRC_DIR}")

# if os.path.exists(DST_DIR):
#    raise  ValueError(f'Dst directory {DST_DIR} already exists')

if not os.path.exists(DST_DIR):
    os.mkdir(DST_DIR)

DATA_DIR = f'{DST_DIR}/{RUN_DIR}'
if os.path.exists(DATA_DIR):
    raise  ValueError(f'Dst directory {DATA_DIR} already exists')


print(f'Cloning data from {SRC_DIR} -> {DATA_DIR}')

shutil.copytree(SRC_DIR, DATA_DIR)

if include_scripts:
    print('Copying scripts...')
    python_scripts = os.listdir('./scripts')
    for script in python_scripts:
        print(f'Copying ./scripts/{script} -> {DST_DIR}')
        shutil.copy(f'./scripts/{script}', DST_DIR)

print('Done.')