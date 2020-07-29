import networkx as nx
import matplotlib.pyplot as plt
import sys
from readFile import *


save = []


def countJarak(simpul1, simpul2, edgesData, path):
    # method yang akan mengembalikan tupple yang berisi jarak dari simpul1 ke simpul2 beserta path yang dilaluinya
    # masukkan kota asal ke path
    save.append(simpul1)
    if simpul1 in edgesData:
        if simpul2 in edgesData[simpul1]:
            # masukkan kota tujuan ke save
            save.append(simpul2)
            # masukkan path fix ke path
            path.extend(save)
            # menghapus path yang disimpan sebelumnya
            save.clear()
            return (float(edgesData[simpul1][simpul2]), path)
        else:
            # cek satu" simpul tujuan yang bisa dituju dari simpul1
            for sisi in edgesData[simpul1]:
                # path yang dilalui dibatasi sampai 10 kota
                if (len(save) > 10):
                    save.pop()
                    return None
                elif(sisi in save):
                    # jika sisi merupakan elemen terakhir
                    if sisi == list(edgesData[simpul1])[-1]:
                        save.pop()
                        return None
                    # jika tidak, lanjutkan iterasi
                    else:
                        continue

                else:
                    jarak = countJarak(sisi, simpul2, edgesData, path)
                    if jarak:
                        # jika jarak tidak bernilai none
                        return (float(edgesData[simpul1][sisi]) + jarak[0], path)
                    else:
                        # jika jarak menghasilkan nilai none
                        # hapus path yang salah
                        # maka lanjutkan iterasi
                        if sisi == list(edgesData[simpul1])[-1]:
                            save.pop()
                            return None
                        else:
                            continue
    else:
        save.pop()
        return None


def graph(pusat, tujuan):
    # method ini digunakan untuk mengembalikan matriks jarak upagraf dalam bentuk dict
    # serta menampilkan upagraf dengan memanfaatkan matplotlib dan networkx
    # pusat => simpul awal / kantor pusat perusahaan (start state)
    # tujuan => list simpul tujuan
    path = []
    pathh = []
    nodes = []

    G = nx.Graph()
    n = readNode("OL_node.txt")
    # adding just one nodes
    if pusat in n:
        koord = n.get(pusat)
        G.add_node(pusat, pos=(float(koord[0]), float(koord[1])))
    else:
        print(str(pusat)+" bukan merupakan jalanan di kota Oldenburg.")
    # adding a list of nodes into graph
    for el in tujuan:
        if el in n:
            koor = n.get(el)
            G.add_node(el, pos=(float(koor[0]), float(koor[1])))
        else:
            print(str(el)+" bukan merupakan jalanan di kota Oldenburg.")
    # nodes adalah kumpulan simpul yang akan ditampilkan
    nodes.append(pusat)
    nodes.extend(tujuan)
    # eges adalah kumpulan jalanan pada kota Oldenburg
    edges = readEdge("OL_edge.txt")
    # lakukan iterasi di setiap 2 simpul secara terstruktur
    for i in range(len(nodes)):
        for j in range(len(nodes)-i-1):
            # simpul 1
            nodes1 = nodes[i]
            # simpul 2
            nodes2 = nodes[j+i+1]
            # jarak dari simpul1 -> simpul2
            jaraka = countJarak(nodes1, nodes2, edges, path)
            if jaraka:
                jarak1 = jaraka[0]
                path1 = jaraka[1]

            else:
                jarak1 = None
            # jarak dari simpul2 -> simpul1
            jarakb = countJarak(nodes2, nodes1, edges, pathh)
            if jarakb:
                jarak2 = jarakb[0]
                path2 = jarakb[1]

            else:
                jarak2 = None

            # kasus-kasus untuk menentukan jarak terbaik antar dua simpul
            if(jarak1 is None) and (jarak2 is not None):
                edge = (nodes2, nodes1)
                G.add_edge(*edge, weight=round(jarak2, 2))
                print("Rute perjalanan dari "+nodes2 +
                      " ke "+nodes1+" adalah : ")
                print(path2)
            elif(jarak1 is not None)and(jarak2 is None):
                edge = (nodes1, nodes2)
                G.add_edge(*edge, weight=round(jarak1, 2))
                print("Rute perjalanan dari "+nodes1 +
                      " ke "+nodes2+" adalah : ")
                print(path1)
            elif(jarak1 is None)and(jarak2 is None):
                print("Tidak ada jalan yang bisa ditelusuri dari " +
                      nodes1+" ke "+nodes2+" dan sebaliknya.")
            elif(jarak1 < jarak2):
                edge = (nodes1, nodes2)
                G.add_edge(*edge, weight=round(jarak1, 2))
                print("Rute perjalanan dari "+nodes1 +
                      " ke "+nodes2+" adalah : ")
                print(path1)
            elif(jarak1 >= jarak2):
                edge = (nodes2, nodes1)
                G.add_edge(*edge, weight=round(jarak2, 2))
                print("Rute perjalanan dari "+nodes2 +
                      " ke "+nodes1+" adalah : ")
                print(path2)
            path.clear()
            pathh.clear()

    pos = nx.get_node_attributes(G, 'pos')
    # elabel adalah matriks jarak antar upagraf lengkap
    elabel = nx.get_edge_attributes(G, 'weight')
    # matriks jarak antar upagraf
    print("Matriks Jarak antar Upagraf")
    for el in elabel:
        print(el[0] + " , " + el[1] + " => " + str(elabel[el]))

    nx.draw_networkx_labels(G, pos, font_size=10, font_family='sans-serif')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=elabel)
    nx.draw(G, pos)
    plt.savefig("testing.png")
    plt.show()
    return elabel


def kurirRute(elabel, pusat, tujuan):
    # path yang ditempuh dari pusat ke kota tujuan
    path = []
    path.append(pusat)
    # menyimpan semua nodes
    nodes = []
    nodes.append(pusat)
    nodes.extend(tujuan)
    # method ini digunakan untuk menampilkan rute terpendek dari pusat pengiriman ke seluruh tujuan dan kembali lagi ke simpul awal
    # serta menampilkan jarak terpendek dari perjalanan tersebut
    # jumlah jarak/cost yang akan ditempuh
    cost = 0
    # pusat => simpul awal / kantor pusat perusahaan (start state)
    # tujuan => list simpul tujuan
    G = nx.Graph()
    n = readNode("OL_node.txt")
    # adding just one nodes
    if pusat in n:
        koord = n.get(pusat)
        G.add_node(pusat, pos=(float(koord[0]), float(koord[1])))
    else:
        print(str(pusat)+" bukan merupakan jalanan di kota Oldenburg.")
    # adding a list of nodes into graph
    for el in tujuan:
        if el in n:
            koor = n.get(el)
            G.add_node(el, pos=(float(koor[0]), float(koor[1])))
        else:
            print(str(el)+" bukan merupakan jalanan di kota Oldenburg.")

    # jarak dari pusat terlebih dahulu, cari ke simpul tujuan dengan jarak terpendek
    # menyimpan jarak terpendek sementara dengan simpul tujuan

    for i in range(len(nodes)-1):
        # inisiasi nilai minim terlebih dahulu
        minim = sys.float_info.max
        kotaMin = nodes[i+1]  # inisiasi kota
        for j in range(len(nodes)-1):
            if nodes[j+1] in path:
                # jika kota tujuan sudah pernah ada dalam path maka abaikan
                # lanjutkan iterasi
                continue
            else:

                jarakMin1 = elabel.get((path[len(path)-1], nodes[j+1]))
                jarakMin2 = elabel.get((nodes[j+1], path[len(path)-1]))
                if jarakMin1:
                    if jarakMin1 < minim:
                        minim = jarakMin1
                        kotaMin = nodes[j+1]
                elif jarakMin2:
                    if jarakMin2 < minim:
                        minim = jarakMin2
                        kotaMin = nodes[j+1]
        # gambar edge
        edge = (path[len(path)-1], kotaMin)
        G.add_edge(*edge, weight=round(minim, 2))
        # push nodes with minim cost to path
        path.append(kotaMin)
        cost += minim
    # menambahkan cost kembali ke kantor pusat
    # gambar edge
    edge = (kotaMin, pusat)
    jarak2 = elabel.get((pusat, kotaMin))
    jarak3 = elabel.get((kotaMin, pusat))
    if jarak2:
        G.add_edge(*edge, weight=round(jarak2, 2))
        cost += jarak2
    elif jarak3:
        G.add_edge(*edge, weight=round(jarak3, 2))
        cost += jarak3

    # push nodes with minim cost to path
    path.append(pusat)

    pos = nx.get_node_attributes(G, 'pos')
    # elabel adalah matriks jarak antar upagraf lengkap
    elabel = nx.get_edge_attributes(G, 'weight')
    # menampilkan jumlah cost
    print("Jumlah cost yang ditempuh adalah "+str(round(cost, 2)))
    print("Jalur yang dilewati oleh kurir secara terurut adalah : ")
    print(path)
    nx.draw_networkx_labels(G, pos, font_size=10, font_family='sans-serif')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=elabel)
    nx.draw_networkx_edges(G, pos, edge_color='r')
    nx.draw(G, pos)
    plt.show()
