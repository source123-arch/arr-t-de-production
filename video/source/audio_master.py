import numpy as np, wave
from scipy.signal import lfilter
sr=44100; D=80.0; N=int(sr*D); t=np.arange(N)/sr; rng=np.random.default_rng(21)
def onepole(x,fc): a=1-np.exp(-2*np.pi*fc/sr); return lfilter([a],[1,-(1-a)],x)
def env(a,b,fi=0.6,fo=0.6): return np.clip((t-a)/fi,0,1)*np.clip((b-t)/fo,0,1)
out=np.zeros(N); white=rng.standard_normal(N)
brown=np.cumsum(white); brown-=onepole(brown,0.5); brown/=np.abs(brown).max()
hall=onepole(white,300)*0.6+brown*0.5+0.12*np.sin(2*np.pi*50*t)+0.06*np.sin(2*np.pi*100*t)+0.08*onepole(white,2000)*(0.5+0.5*np.sin(2*np.pi*0.13*t))
out+=hall*0.25*(env(0,31.3,1.5,0.4)+env(42.8,56.2,0.4,0.4)+env(69.8,80,0.6,0.5))
out+=onepole(hall,180)*0.18*(env(31,42.5,0.5,1.0)+env(56,59.8,0.3,0.4))
def add(t0,s,amp=1):
    i=int(t0*sr); m=min(len(s),N-i); out[i:i+m]+=amp*s[:m]
def step(t0,amp):
    n=int(0.15*sr); tt=np.arange(n)/sr; add(t0,onepole(rng.standard_normal(n),900)*np.exp(-tt*40)*3+np.sin(2*np.pi*90*tt)*np.exp(-tt*35),amp)
def clank(t0,amp):
    n=int(0.6*sr); tt=np.arange(n)/sr; s=sum(np.sin(2*np.pi*f*tt+p)*np.exp(-tt*d) for f,d,p in [(523,9,0),(1310,14,1),(2210,20,2),(3470,30,.5)])
    add(t0,s+rng.standard_normal(n)*np.exp(-tt*80)*0.6,amp*0.3)
def thud(t0):
    n=int(0.8*sr); tt=np.arange(n)/sr; add(t0,onepole(rng.standard_normal(n),200)*np.exp(-tt*12)*6+np.sin(2*np.pi*55*tt)*np.exp(-tt*8),0.6)
for tc in np.arange(8.4,14.4,0.48): step(tc,0.25)
for tc in [19.4,19.62,19.84]:
    n=int(0.12*sr); tt=np.arange(n)/sr; add(tc,(onepole(rng.standard_normal(n),3000)-onepole(rng.standard_normal(n),600))*np.sin(np.pi*tt/0.12),0.25)
for tc in np.arange(24.8,30.6,0.8): clank(tc+rng.uniform(-.05,.05),0.5+0.3*rng.random())
br=onepole(white,900)-onepole(white,250)
f=np.where(t<35.8,0.28,0.28+0.5*np.clip((t-35.8)/4,0,1)); ph=np.cumsum(2*np.pi*f/sr)
out+=br*np.clip(np.sin(ph),0,1)**2*(0.35+0.25*np.clip((t-35.8)/3.5,0,1))*env(17.2,40.6,0.5,0.2)*np.where((t>24)&(t<31),0,1)
out+=0.05*np.sin(2*np.pi*4200*t)*(env(37,42.4,2,0.6)+env(57.5,59.8,1,0.3))
thud(40.6);clank(40.65,0.4)
for tc in np.arange(43.1,46.7,0.31): step(tc,0.35)
for tc in np.arange(51.4,55.6,0.8): clank(tc,0.6)
f2=0.6; out+=br*np.clip(np.sin(2*np.pi*f2*t),0,1)**2*0.45*env(56,59.3,0.3,0.1)
thud(59.3)
for tc in np.arange(60.6,69.5,0.95):
    for d,a in [(0,1),(0.22,0.7)]:
        n=int(0.25*sr); tt=np.arange(n)/sr; add(tc+d,np.sin(2*np.pi*48*tt)*np.exp(-tt*18),0.5*a)
for tc in np.cumsum(rng.uniform(0.7,2.2,12))+31.3:
    if tc<40: n=int(.12*sr); tt=np.arange(n)/sr; add(tc,np.sin(2*np.pi*(1500+3000*tt)*tt)*np.exp(-tt*45),0.12)
# pen on paper
def scratch(t0,dur,amp):
    n=int(dur*sr); tt=np.arange(n)/sr; s=onepole(rng.standard_normal(n),5000)-onepole(rng.standard_normal(n),1500); add(t0,s*np.sin(np.pi*tt/dur)*(0.6+0.4*np.sin(2*np.pi*18*tt)),amp)
for i in range(7): scratch(73.6+i*0.6,0.18,0.35)
for i in range(3): scratch(77.95+i*0.5,0.45,0.3)
dr=0.06*(np.sin(2*np.pi*55*t)+0.6*np.sin(2*np.pi*82.5*t)+0.4*np.sin(2*np.pi*110.3*t))
out+=dr*(env(0,8,1.5,0.6)+env(69.8,73.3,0.5,0.6))
dk=0.07*(np.sin(2*np.pi*41.2*t)+0.5*np.sin(2*np.pi*61.7*t))*(0.7+0.3*np.sin(2*np.pi*0.3*t))
out+=dk*env(60,69.8,1,0.6)
src=out*(env(31,42.6,0.5,0.3)+env(56,60,0.2,0.2)); wet=sum(lfilter([1],np.r_[1,np.zeros(int(d*sr)-1),-g],src) for d,g in [(0.031,.55),(0.047,.5),(0.067,.45),(0.089,.4)])
out+=0.18*onepole(wet,3000)
out*=np.clip(t/0.8,0,1)
out=np.tanh(out*1.2); out/=np.abs(out).max()*1.12
st=np.stack([out,np.roll(out,int(0.0007*sr))],1)
with wave.open('audio_m1.wav','wb') as w: w.setnchannels(2);w.setsampwidth(2);w.setframerate(sr);w.writeframes((st*32767).astype(np.int16).tobytes())
print('ok')
