import os

def get_serial_number():
    # dummy versions
    versions = dict(
        hardware='xxxxxxx',
        revision='0000000',
        serial='0000000000000000'
    )

    # open cpu info and read
    try:
        with open('/proc/cpuinfo', 'r') as info:
            for line in info:
                if line.startswith('Hardware'):
                    versions['hardware'] = line.split(':')[1].strip()
                elif line.startswith('Revision'):
                    versions['revision'] = line.split(':')[1].strip()
                elif line.startswith('Serial'):
                    version['serial'] = line.split(':')[1].strip()

    except:
        versions = dict(
        hardware='ERRORxx',
        revision='ERROR00',
        serial='ERROR00000000000'
    )

    return versions
        