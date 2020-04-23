def move(point={'pozx', 'pozy'}, vector={'pozx', 'pozy'}):
    point['pozx'] += vector['pozx']
    point['pozy'] += vector['pozy']
    print(point)
