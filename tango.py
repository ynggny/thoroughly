import csv
import random

def mark():
    dotli = ['     ■  ■']
    underd = ['        ■']
    return dotli,underd

def oono0 ():
    voc = []
    with open ('ooba.csv','r') as e :
        csvv = csv.reader(e)
        for o in csvv :
            voc.append(o)
    return voc
    pass
def oono ():
    ass = []
    with open ('nihonja.csv','r') as f :
        a = csv.reader(f)
        for i in a :
            ass.append(i)
    return ass
def choiceng():
    jcon = []
    engg =[]
    engli = oono0()
    japo = oono()
    eng = random.sample(engli,20)
    return eng
def addjap():
    ull =[]
    eigo1=[]
    eigo = choiceng()
    engliq = oono0()
    japo = oono()
    for d in range(len(eigo)):
        che = eigo[d]
        sar = engliq.index(che)
        jap = japo[sar]
        yyc = japo[sar] + list("")
        are = eigo[d] + list("     ⓪①")
        eigo1.append(are)
        ull.append(yyc)
    return eigo1 , ull


levels = []
er,re = mark()
ae = oono()
aw = oono0()
a,b = addjap()
c,d = addjap()
levels.extend(list(er))
levels.extend(a)
levels.extend(list(re))
levels.extend(list(er))
levels.extend(c)
levels.extend(list(re))
levels.extend(list(er))
levels.extend(b)
levels.extend(list(re))
levels.extend(list(er))
levels.extend(d)
levels.extend(list(re))
print(levels)
anal = open("tunaki.csv","w",encoding="utf_8_sig")
anal1 = csv.writer(anal)
anal1.writerows(levels)
anal.close()

#with open ('otinpo.csv','w') as f:
    #mankov = csv.writer(f)
    #mankov.writerows(tinko)
