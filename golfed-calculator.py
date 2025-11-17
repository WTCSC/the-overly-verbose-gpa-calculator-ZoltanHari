import sys,time
def type_out(t,d=.03):
    for c in t:sys.stdout.write(c);sys.stdout.flush();time.sleep(d)
    print()
while 1:
    type_out("Oi, git! Chuck in all yer gradez, wiv spacez between 'em (Ex. 3.2 4.0 2.9): ")
    try:
        g=list(map(float,input().split()))
    except:print("Use numbaz, ya grot! Wot are ya, stoopid?.");continue
    if any(x>4 or x<=0 for x in g):
        print("Da gradez gotta be between 0.0 an' 4.0, or I'll krump ya!");continue
    tot=round(sum(g)/len(g),2);h=len(g)//2;break
type_out(f"Yer total krumpin' average fer da year iz {tot}")
while 1:
    type_out("Wich bit d'ya wanna looksee at? Da furst 'alf or da sekund 'alf (type 1 or 2):")
    s=input()
    if s in("1","2"):
        a=g[:h]if s=="1"else g[h:]
        r=round(sum(a)/len(a),2)
        if r==tot:type_out(f"Yer krumpin' average fer da {'furst'if s=='1'else'sekund'} 'alf iz da same as da whole zoggin' year.");break
        m="betta dan"if r>tot else"rubbish compared ta"
        type_out(f"Yer krumpin' average fer da {'furst'if s=='1'else'sekund'} 'alf of {r} is {m} yer total!");break
    type_out("Dat's da rong choice, ya git! Pick 1 or 2!")
while 1:
    type_out("Wot's da krumpin' average ya wanna get?")
    try:t=float(input())
    except:type_out("Dat 'ent a numba! Put in a proppa one!");continue
    if t>4 or t<=0:type_out("Itz gotta be between 0.0 an' 4.0, ya stoopid git.");continue
    if tot>=t:type_out("Zog me, you'ze already done it! Dat's proppa kunnin'!");break
    for i in range(len(g)):
        ng=g.copy();ng[i]=4
        n=round(sum(ng)/len(ng),2)
    if n>=t:type_out(f"If ya change grade numba {i+1} ta a 4.0, ya get {n:.2f}, an' dat stomps all over yer target!")
    else:type_out("Zog it! Changin' just wun grade ta 4.0 'ent gonna be enuff.")
    break