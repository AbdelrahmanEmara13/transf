import os

files=open('sites.txt', 'r')
real_files=files.read().split()

for file in files:
    try:

        os.system(f'gcloud storage cp gs://holland_bkp/{file} .')
    except Exception as e: print(e)
