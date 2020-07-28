def readNode(path):
    # mengembalikan array of tupple (node,x,y) yang merupakan koordinat dari node
    # membagi isi file per line
    with open(path) as f:
        line = f.read().splitlines()

    # dict
    nodes = {}
    # tiap line dibagi menjadi x dan y
    for l in line:
        # split by whitespace
        getKoor = l.split()

        # simpan data
        node = getKoor[0]
        koor = [getKoor[1], getKoor[2]]

        # add to dict
        nodes[node] = koor

    # return array of koordinat
    return nodes


def readEdge(path):
    # mengembalikan dict dimana key adalah kota start dan value dalam bentuk array of tuple (final,jarak)

    # membagi isi file per line
    with open(path) as f:
        line = f.read().splitlines()

    # dictionary
    dictt = {}

    # tiap line dibagi menjadi x dan y
    for l in line:
        # split by whitespace
        getEdge = l.split()
        node1 = getEdge[1]
        node2 = getEdge[2]
        jarak = getEdge[3]

        if node1 in dictt:
            dictt[node1][node2] = jarak
        else:
            dictt[node1] = {node2: jarak}
        if node2 in dictt:
            dictt[node2][node1] = jarak
        else:
            dictt[node2] = {node1: jarak}

    # return array of sisi
    return dictt
