import os
import glob
import datetime
import time
import sqlalchemy
import pandas as pd


msd_main_path = r'C:\Users\Fahim\Downloads\millionsongsubset'
msd_data_path = os.path.join(msd_main_path, 'data')
msd_add_path = os.path.join(msd_main_path, 'additionalfiles')
assert os.path.isdir(msd_main_path), "wrong path given" #debug for existing directory check

#Time lag in seconds
def time_taken(start,finish):
    return str(datetime.timedelta(seconds = finish-start))


filepath = r'C:\Users\Fahim\Downloads\millionsongsubset\data1.json'

def process_file(cur, path):
    """
    Process a song file and insert record into db
    :param cur: cursor reference
    :param filepath: complete file path for the file to load
    """
    
    df = pd.DataFrame([pd.read_json(path, typ='series')])

    for value in df.values:
        artistName, time, similars, tags, trackId, title = value
    
    songData = (artistName, time, trackId, title)
    cur.execute(songInsert, songData)
    
    print(f"Records inserted for file {path}")

def process_data(cur, conn, path, func):
    """
    Driver function to load all songs into db
    :param cur: a database cursor reference
    :param conn: database connection reference
    :param path: parent directory where the files exists
    :param func: function to call
    """
    # get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(path):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, path))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))


def main():
    """
    Driver function for loading songs into db
    """
    #conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=root password=red8Horse")
    cur = conn.cursor()
    process_data(cur, conn, path= filepath, func=process_file)
    conn.close()

if __name__ == "__main__":
    main()
    print("\n\nFinished processing!\n\n")