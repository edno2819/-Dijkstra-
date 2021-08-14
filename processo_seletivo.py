
def mergeSort(alist, status=False):
    if len(alist)>1 and status:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    else: return alist.sort()

try:
    n = int(input())
except: ...
vaga=[]
for i in range(1,n+1):
    vaga.append(input().split())

for c in vaga:
    vagas=int(c[0])
    candidatos=int(c[1])
    notas=[float(c[x]) for x in range(2,len(c))]

    mergeSort(notas)
    v=round(notas[(len(notas)-vagas)],2)
    print("%.2f"% v)

    
