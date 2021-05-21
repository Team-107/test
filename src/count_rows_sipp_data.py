import os

current_working_direc = os.getcwd()
parent_dir = os.path.abspath(os.path.join(current_working_direc, os.pardir))
data_dir = os.path.join(parent_dir, "data")
raw_data_dir = os.path.join(data_dir, "raw")
sipp_data_dir = os.path.join(raw_data_dir, "sipp_2018")
sipp_data_path = os.path.join(sipp_data_dir, "pu2018.csv")


with open(sipp_data_path) as fp:
    count = 0
    for _ in fp:
        count += 1
        if count % 100000 == 0:
            print(f'So far: {count:,}')

print("Done iterating")
print("File has {0} rows".format(count))
print(f'{count:,}')
print(count)
print(f'{count:,} is a formatted number')
print("Okay I''m done printing")
