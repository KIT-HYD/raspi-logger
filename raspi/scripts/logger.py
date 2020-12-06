import os
import json
from datetime import datetime as dt
from time import time, sleep

from ds18b20 import read_sensor
from util import parse_interval_to_seconds


def save_data(path=None, in_soil=False, dry=False, **kwargs):
    # create a new file per day
    if path is None:
        date = dt.now().date()
        fname = '%d_%d_%d_raw_log.json' % (date.year, date.month, date.day)
        path = os.path.join(os.path.expanduser('~'), fname)

    # build up an in_soil list if needed
    data = []
    if isinstance(in_soil, (list, tuple)):
        for s in in_soil:
            data.extend(read_sensor(in_soil=s, **kwargs))
    else:
        data = read_sensor(in_soil=in_soil, **kwargs)
    
    # save data
    if not dry:
        try:
            with open(path, 'r') as f:
                old_data = json.load(f)
        except:
            old_data = []
        with open(path, 'w') as js:
            old_data.extend(data)
            json.dump(old_data, js, indent=4)

    # return the data for reuse
    return data


def stream(interval='15sec', dry=False, **kwargs):
    # get the start time
    t1 = time()
    
    if isinstance(interval, str):
        interval = parse_interval_to_seconds(interval)
    
    data = save_data(dry=dry, **kwargs)

    # stringify
    outstr = json.dumps(data, indent=4)

    # print
    print(outstr)

    # sleep for the remaining time
    sleep(interval - (time() - t1))

    # call again
    stream(interval=interval, dry=dry, **kwargs)


def run(interval='15sec', **kwargs):
    # run with given interval and no print to stdout
    pass


if __name__=='__main__':
    import fire
    fire.Fire({
        'save': save_data,
        'stream': stream
    })
