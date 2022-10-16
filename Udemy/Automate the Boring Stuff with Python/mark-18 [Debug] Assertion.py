#todo 1: Assertion definition
    # command line untuk menjalankan sanity check supaya code yg diberikan tidak melakukan sesuatu yg janggal
    # return the error and the error code will not executed
    # stopping the code from running further (set as crash)
    # format: assert 'passed_condition', 'returned expression'
'''Example code:
switching the traffic light color
- merotasi traffic light
    1. hijau ke kuning (3 red)
    2. kuning ke merah (3 red)
    3. merah ke hijau (3 red)
'''
traf_lig = {
'north': 'green',
    'east' : 'red',
    'south': 'red',
    'west': 'red'
}


def rotation(light):
    for x in light.keys():  # light.keys() is line to call the value, bukan key nya
        if light[x] == 'green':
            light[x] = 'yellow'
        elif light[x] == 'yellow':
            light[x] = 'red'
        elif light[x] == 'red':
            light[x] = 'green'
    assert 'red' in light.values(), f"WARNING: Red light is not detected. Current traffic {light}"
    # translation: AKU menegaskan 'red' harus ada di dalam value light dictionary, jika ga ada akan kuberikan error...


print(f'default traffic {traf_lig}')
# {'north': 'green', 'east': 'red', 'south': 'red', 'west': 'red'}
rotation(traf_lig)
print(f'Switched traffic {traf_lig}')
# Switched traffic {'north': 'yellow', 'east': 'green', 'south': 'green', 'west': 'green'}
'''BUGS Caught:
    1. semua lampu merah akan ke replace hijau
    2. tidak ada lampu merah yang menyala saat lampu kuning aktif
solutions: using assertive statement  (line 29)
'''