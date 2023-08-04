import sys
import os
import shutil

def print_help():
    print(f'Wrong numer of arguments.')
    print(f'Expected: python copy_sampling.py <src_dir> <dst_dir>')
    print(f'\t e.g: python copy_sampling.py 0_data_step_2_withtout_classify 0_run_1')


if len(sys.argv) < 3:
    print_help()
    exit()

SRC_DIR = sys.argv[1]
print(SRC_DIR)

DST_DIR = sys.argv[2]
print(DST_DIR)

print(f'Copy sampling from {SRC_DIR} -> {DST_DIR}')

sampling_file_dirs = os.listdir(SRC_DIR)
for sampling_file_dir in sampling_file_dirs:
    if sampling_file_dir.startswith('.'):
        continue
    # print(f'{sampling_file_dir}')
    output_src = f'./{SRC_DIR}/{sampling_file_dir}/output'
    output_dst_base = f'./{DST_DIR}/{sampling_file_dir}/output'
    sampling_files = os.listdir(output_src)
    for sampling_file in sampling_files:
        if sampling_file.find('sample') > 0:
            # print(f'{sampling_file}')
            src_file = f'{output_src}/{sampling_file}'
            dst_file = f'{output_dst_base}/{sampling_file}'
            print(f'{src_file} -> {dst_file}')
            shutil.copy(src_file, dst_file)
