#############################################
# Exemple de mauvaise idée.                 #
# NE PAS UTILISER // SATURE LA MÉMOIRE VIVE #
#############################################

#pond = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
##pond_copie = pond[:]
##pond.extend(pond_copie)
print(pond)
liste = []

for i in range(len(pond)):
    for j in range(len(pond)):
        for k in range(len(pond)):
            for l in range(len(pond)):
                for m in range(len(pond)):
                    for n in range(len(pond)):
                        for o in range(len(pond)):
                            for p in range(len(pond)):
                                for q in range(len(pond)):
                                    for r in range(len(pond)):
                                        for s in range(len(pond)):
                                            for t in range(len(pond)):
                                                for u in range(len(pond)):
                                                    liste.append([pond[i], pond[j], pond[k], pond[l], pond[m], pond[n], pond[o], pond[p], pond[q], pond[r], pond[s], pond[t], pond[u]])
with open("ponde.csv", 'rw') as f:
    f.write(liste)
