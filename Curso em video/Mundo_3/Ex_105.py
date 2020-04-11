def notas(*n, sit=False):
    r = {}
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if(sit):
        if(r['media'] >= 7):
            r['situacao'] = 'BOA'
        elif(r['media'] >= 5):
            r['situacao'] = 'RAZOÁVEL'
        else:
            r['situacao'] = 'RUIM'
    return r

print(notas(5.5, 2.5, 1.5, sit=True))
print(notas(7, 3, 4, sit=True))
print(notas(7, 10, 9, sit=True))