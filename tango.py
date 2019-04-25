import csv
import random

def mark():##ドットを追加
    dotli = ['     ■  ■']
    underd = ['        ■']
    return dotli,underd

def oono0 ():##日本語
    voc = []
    with open ('japanese.csv','r') as e :
        csvv = csv.reader(e)
        for o in csvv :
            voc.append(o)
    return voc
    pass
def oono ():##英語
    ass = []
    with open ('english.csv','r') as f :
        a = csv.reader(f)
        for i in a :
            ass.append(i)
    return ass
def choiceng():##ランダムに英単語を抽出
    jcon = []
    engg =[]
    engli = oono0()
    japo = oono()
    eng = random.sample(engli,20)
    return eng
def addjap():##対応する日本語訳を追加
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

##整形してリストに追加
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
writeing = open("任意のファイル名.csv","w",encoding="utf_8_sig")#英単語帳の出力
writeng = csv.writer(writeing)
writeng.writerows(levels)
anal.close()
