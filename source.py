from itertools import count
import base64
from collections import namedtuple
V={"P":100,"N":280,"B":320,"R":479,"Q":929,"K":60000}
T=tuple(x-256 if x>127 else x for x in base64.b64decode("AAAAAAAAAABOU1ZJZlJVWgcdFSwoHywH7xD+Dw4AD/PmAwoJBgEA6eoJBfX2/gPt4Qj529zyA+EAAAAAAAAAAL7LtbX2yca6/fpk3AQ+/PIKQwFKSRs+/hgYLSUhKRkR/wUfFRYjAgDuCg0WEg8L8unxAgACAOnstunm6O3d6rvFsq606ZXbzvUUI9bZHwLq9yfgKTT2HPIZERQiGhkPCg0KERcREAAHDhkYDwgZFA8TFAsGBwYUEPkC8fTy8fb2Ix0hBCUhODI3HThDNz4iPBMjHCEtGxkPAAUQDRL89/rk3fDr8+PS4tbk1ufn3ebSy9rh5uPV1Mvi6O4F/u7h4AYB+JhFGFgaDiA89hRMORj+KyA8SD8rAgHwFhEZFPP68vH++//27Ori+vP18PXw5dzuAO3x8eva2eLh8+Hc3tYENi+dnTxTwuAKNzg4NwoDwgzHLL0cJeHJMgv87Q0Az8nVzOTN0fjO0dbVscDg4+D8A/LOx+4NBBEe/fIG/ygS"))
S={}
for n,k in enumerate("PNBRQK"):
 t=T[n*64:n*64+64]
 def pr(r): return (0,)+tuple(x+V[k] for x in r)+(0,)
 S[k]=sum((pr(t[i*8:i*8+8]) for i in range(8)),())
 S[k]=(0,)*20+S[k]+(0,)*20
initial=("         \n"+"         \n"+" rnbqkbnr\n"+" pppppppp\n"+
 " ........\n"+" ........\n"+" ........\n"+" ........\n"+
 " PPPPPPPP\n"+" RNBQKBNR\n"+"         \n"+"         \n")
A1,H1,A8,H8=91,98,21,28
N,E,Sd,W=-10,1,10,-1
D={"P":(N,N+N,N+W,N+E),"N":(N+N+E,E+N+E,E+Sd+E,Sd+Sd+E,Sd+Sd+W,W+Sd+W,W+N+W,N+N+W),"B":(N+E,Sd+E,Sd+W,N+W),"R":(N,E,Sd,W),"Q":(N,E,Sd,W,N+E,Sd+E,Sd+W,N+W),"K":(N,E,Sd,W,N+E,Sd+E,Sd+W,N+W)}
ML=V["K"]-13*V["Q"]; MU=V["K"]+10*V["Q"]; QS=36; ER=15; BUD=80000
class P(namedtuple("P","bb sc wc bc ep kp")):
 def gm(self):
  for i,p in enumerate(self.bb):
   if p not in "PNBRQK": continue
   for d in D[p]:
    for j in count(i+d,d):
     q=self.bb[j]
     if q in " \nPNBRQK": break
     if p=="P":
      if d in (N,N+N) and q!=".": break
      if d==N+N and (i<A1+N or self.bb[i+N]!="."): break
      if d in (N+W,N+E) and q=="." and j!=self.ep and abs(j-self.kp)>1: break
      if A8<=j<=H8:
       for pr in "NBRQ": yield (i,j,pr)
       break
     yield (i,j,"")
     if p in "PNK" or q in "pnbrqk": break
     if i==A1 and self.bb[j+E]=="K" and self.wc[0]: yield (j+E,j+W,"")
     if i==H1 and self.bb[j+W]=="K" and self.wc[1]: yield (j+W,j+E,"")
 def rotate(self,nm=False): return P(self.bb[::-1].swapcase(),-self.sc,self.bc,self.wc,119-self.ep if self.ep and not nm else 0,119-self.kp if self.kp and not nm else 0)
 def move(self,m):
  i,j,pr=m
  put=lambda b,i,p: b[:i]+p+b[i+1:]
  p,q,b,wc,bc,ep,kp=self.bb[i],self.bb[j],self.bb,self.wc,self.bc,0,0
  score=self.sc+self.value(m)
  b=put(b,j,b[i]); b=put(b,i,".")
  wc=(wc[0] and i!=A1, wc[1] and i!=H1)
  bc=(bc[0] and j!=H8, bc[1] and j!=A8)
  if p=="K":
   wc=(False,False)
   if abs(j-i)==2:
    kp=(i+j)//2
    b=put(b,A1 if j<i else H1,".")
    b=put(b,kp,"R")
  if p=="P":
   if A8<=j<=H8: b=put(b,j,pr)
   if j-i==2*N: ep=i+N
   if j==self.ep: b=put(b,j+Sd,".")
  return P(b,score,wc,bc,ep,kp).rotate()
 def value(self,m):
  i,j,pr=m
  p,q=self.bb[i],self.bb[j]
  score=S[p][j]-S[p][i]
  if q in "pnbrqk": score+=S[q.upper()][119-j]
  if abs(j-self.kp)<2: score+=S["K"][119-j]
  if p=="K" and abs(i-j)==2:
   score+=S["R"][(i+j)//2]
   score-=S["R"][A1 if j<i else H1]
  if p=="P":
   if A8<=j<=H8: score+=S[pr][j]-S["P"][j]
   if j==self.ep: score+=S["P"][119-(j+Sd)]
  return score
 def kc(self):
  return next((m for m in self.gm() if self.bb[m[1]]=="k" or abs(m[1]-self.kp)<2),None)
class Stop(Exception): pass
class Se:
 def __init__(s):
  s.tp={}; s.tm={}; s.hist=set()
  s.nodes=0; s.bud=BUD
 def bd(s,pos,gamma,depth,root=False):
  s.nodes+=1
  if s.nodes>=s.bud: raise Stop
  depth=max(depth,0)
  if pos.sc<=-ML: return -MU
  if not root:
   entry=s.tp.get((pos,depth),(-MU,MU))
   if entry[0]>=gamma: return entry[0]
   if entry[1]<gamma: return entry[1]
   if pos in s.hist: return 0
  def moves():
   hm=s.tm.get(pos)
   if 2<depth<6 and not root: yield None,None
   if depth==0: yield None,None
   if hm: yield pos.value(hm),hm
   yield from sorted([(pos.value(m),m) for m in pos.gm() if m!=hm and (pos.value(m)>=QS or depth)], reverse=True)
  best,live=-MU,False
  for val,move in moves():
   if move is None and depth==0: score=pos.sc
   elif move is None:
    if (cap:=pos.sc+ER)>=gamma:
     score=min(cap,-s.bd(pos.rotate(nm=True),1-gamma,depth-4))
     if score>=gamma and (proof:=pos.kc()): move,score,live=proof,MU,True
    else: score=cap
   elif val>=ML: score,live=MU,True
   elif depth==0 and best+val<gamma: continue
   else:
    score=-s.bd(pos.move(move),1-gamma,depth-1)
    live|=score>-MU
   best=max(best,score)
   if best>=gamma:
    if move is not None and depth: s.tm[pos]=move
    break
  if depth and not live and all(pos.move(m).kc() for m in pos.gm()): best=max(1-MU,-ML-depth*ER) if pos.rotate(nm=True).kc() else 0
  if not root:
   s.tp[pos,depth]=(best,entry[1]) if best>=gamma else (entry[0],best)
  return best
 def search(s,history):
  s.nodes=0; s.hist=set(history); s.tp={}
  pos=history[-1]
  gamma=0; best=None
  for depth in range(1,1000):
   lower,upper=1-MU,MU
   while lower<upper-ER:
    score=s.bd(pos,gamma,depth,root=True)
    if score>=gamma: lower=score
    if score<gamma: upper=score
    yield depth,gamma,score,s.tm.get(pos)
    gamma=(lower+upper+1)//2
def parse(c): return A1+ord(c[0])-ord("a")-10*(int(c[1])-1)
def render(i): return chr((i-A1)%10+ord("a"))+str(1-(i-A1)//10)
def pof(fen):
 p=fen.split(); rows=[]
 for r in p[0].split("/"): rows.append(" "+"".join("."*int(c) if c.isdigit() else c for c in r)+"\n")
 b=(" "*9+"\n")*2+"".join(rows)+(" "*9+"\n")*2
 cas=p[2]; wc=('Q' in cas,'K' in cas); bc=('q' in cas,'k' in cas)
 pos=P(b,0,wc,bc,parse(p[3]) if p[3]!="-" else 0,0)
 return pos.rotate() if p[1]=='b' else pos
import json,os,urllib.request as u,urllib.error as e,sys
V=os.environ["MAKEFUN_ENV_URL"]
def post(a,b):
 try:
  with u.urlopen(u.Request(V+a,data=json.dumps(b).encode(),headers={"content-type":"application/json"})) as r: return json.load(r)
 except e.HTTPError: sys.exit(a)
while 1:
 g=post("/game",{})
 if g["status"]=="done": break
 while g["status"]=="your_move":
  pos=pof(g["fen"]); s=Se(); mov=None
  try:
   for _,_,_,m in s.search([pos]):
    if m: mov=m
  except Stop: pass
  if not mov or pos.move(mov).kc(): mov=next((m for m in pos.gm() if not pos.move(m).kc()),None)
  if g["fen"].split()[1]=="b": mov=(119-mov[0],119-mov[1],mov[2])
  g=post("/move",{"game":g["game"],"move":render(mov[0])+render(mov[1])+(mov[2].lower() if mov[2] else "")})
