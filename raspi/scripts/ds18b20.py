import os
import re
import glob
from datetime import datetime as dt

from util import get_serial_number
import keywords


def _get_sensors(path):
    return glob.glob(path + '28-*')


def _get_temperature(sensor_path):
    with open(sensor_path + '/w1_slave', 'r') as f: 
        c = f.read().split('\n')
    
    m = re.match(r"([0-9a-f]{2} ){9}t=([+-]?[0-9]+)", c[1])
    if m:
        value = float(m.group(2)) / 1000.
    else:
        value = 'NaN'

    return value, '\n'.join(c)


def read_sensor(path='/sys/bus/w1/devices/', in_soil=False, omit_sensor=False, omit_keyword=False):
    data = []

    # get the Raspi serial number
    versions = get_serial_number()

    # add the correct variable and sensor information
    _uuid = keywords.SOIL_TEMPERATURE if in_soil else keywords.AIR_TEMPERATURE
    variable = dict(
        variableName='SOIL TEMPERATURE' if in_soil else 'AIR TEMPERATURE',
        gcmdURL=keywords.CONCEPT_URL.format(uuid=_uuid, fmt='xml'),
        gcmdUUID=_uuid
    )

    for p in _get_sensors(path):
        temperature, hextemp = _get_temperature(p)

        d = dict(
            value=temperature,
            tstamp=dt.now().isoformat(),
            identifier=os.path.basename(p),
            rawData=hextemp,
            sensorName='DS18B20'
        )

        # extend
        if not omit_sensor:
            d.update(versions)
        if not omit_keyword:
            d.update(variable)

        data.append(d)
    
    # return
    return data


if __name__ == '__main__':
    import fire
    fire.Fire(read_sensor)
