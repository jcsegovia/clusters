import sys
import os
import shutil

def print_help():
    print(f'Wrong numer of arguments.')
    print(f'Expected: python clone_directory.py <src_dir> <dst_dir> [-noscripts]')
    print(f'Or      : python clone_directory.py <dst_dir> -onlyscripts')
    print(f'\t e.g: python clone_directory.py 0_data_step_2_withtout_classify ./ test_1')
    print(f'\t e.g: python clone_directory.py 0_data_step_2_withtout_classify ../runs_directory test_1')
    print(f'\t e.g: python clone_directory.py ../runs_directory -onlyscripts')


if len(sys.argv) < 2:
    print_help()
    exit()

only_scripts = False
if len(sys.argv) == 3:
    if "-onlyscripts" != sys.argv[2]:
        print_help()
        exit()
    else:
        only_scripts = True

if not only_scripts and len(sys.argv) < 4:
    print_help()
    exit()

include_scripts = True
if len(sys.argv) > 4:
    if "-noscripts" == sys.argv[4]:
        include_scripts = False

if not only_scripts:
    SRC_DIR = sys.argv[1]
    DST_DIR = sys.argv[2]
    RUN_DIR = sys.argv[3]
    print(f'Cloning from {SRC_DIR} -> {DST_DIR}')
    if not os.path.exists(SRC_DIR):
        raise ValueError(f"Not found source directory {SRC_DIR}")
    DATA_DIR = f'{DST_DIR}/{RUN_DIR}'
    if os.path.exists(DATA_DIR):
        raise ValueError(f'Dst directory {DATA_DIR} already exists')
else:
    DST_DIR = sys.argv[1]
    print(f'Cloning scripts only to -> {DST_DIR}')


if not os.path.exists(DST_DIR):
    os.mkdir(DST_DIR)

if not only_scripts:
    print(f'Cloning data from {SRC_DIR} -> {DATA_DIR}')
    shutil.copytree(SRC_DIR, DATA_DIR)

if include_scripts:
    print('Copying scripts...')
    python_scripts = os.listdir('./scripts')
    for script in python_scripts:
        print(f'Copying ./scripts/{script} -> {DST_DIR}')
        shutil.copy(f'./scripts/{script}', DST_DIR)

print('Done.')
