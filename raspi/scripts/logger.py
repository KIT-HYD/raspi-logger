import os
import json
from datetime import datetime as dt

from ds18b20 import read_sensor


def save_data(path=None, in_soil=False, **kwargs):
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
    with open(path, 'w') as js:
        json.dump(data, js, indent=4)

    # return the data for reuse
    return data


if __name__=='__main__':
    import fire
    fire.Fire(save_data)