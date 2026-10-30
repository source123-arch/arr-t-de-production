import numpy as np, wave
sr=44100; D=80.0; N=int(sr*D); t=np.arange(N)/sr
rng=np.random.default_rng(7)
def lp(x,a):  # one-pole lowpass, a in (0,1)
    from scipy.signal import lfilter
    return lfilter([a],[1,-(1-a)],x)
try:
    import scipy.signal as ss
except ImportError:
    ss=None
def onepole(x,fc):
    a=1-np.exp(-2*np.pi*fc/sr); y=np.empty_like(x); s=0.0
    # vectorised via scipy if present
    if ss is not None: return ss.lfilter([a],[1,-(1-a)],x)
    for i in range(len(x)): s+=a*(x[i]-s); y[i]=s
    return y
def env(a,b,fi=0.6,fo=0.6):
    e=np.clip((t-a)/fi,0,1)*np.clip((b-t)/fo,0,1); return e
def seg(a,b): return (t>=a)&(t<b)
out=np.zeros(N)
white=rng.standard_normal(N)
brown=np.cumsum(white); brown=brown-onepole(brown,0.5); brown/=np.abs(brown).max()
# hall ambience: rumble + 50Hz hum harmonics + distant machinery
hall=onepole(white,300)*0.6+brown*0.5+0.12*np.sin(2*np.pi*50*t)+0.06*np.sin(2*np.pi*100*t)+0.03*np.sin(2*np.pi*150*t+1)
hall+=0.08*onepole(white,2000)*(0.5+0.5*np.sin(2*np.pi*0.13*t))
outside=env(0,35.4,1.5,0.8)+env(59.6,80,0.8,3)
out+=hall*0.25*outside
# muffled hall from inside
out+=onepole(hall,180)*0.18*env(35,60,1.5,0.6)
# fan: broadband + blade-pass tone, loud in s3, continuing faint
fan=onepole(white,1500)-onepole(white,200)
fan=fan/np.abs(fan).max()+0.25*np.sin(2*np.pi*118*t)+0.1*np.sin(2*np.pi*236*t)
fanlvl=0.5*env(27.3,35,1.2,0.4)+0.15*env(35,45,0.3,0.5)+0.28*env(44.5,60,1,0.5)+0.12*env(60,70,0.4,1)
out+=fan*fanlvl
# breathing POV
br=onepole(white,900)-onepole(white,250)
cyc=np.sin(2*np.pi*0.28*t); faster=np.sin(2*np.pi*0.55*t)
breath=np.where(t<54.4,np.clip(cyc,0,1)**2,np.clip(faster,0,1)**2)
out+=br*breath*0.35*env(35.3,60,0.8,0.5)
# ladder clanks during descent
def clank(t0,amp=0.5):
    n=int(0.6*sr); tt=np.arange(n)/sr; s=sum(np.sin(2*np.pi*f*tt+p)*np.exp(-tt*d) for f,d,p in [(523,9,0),(1310,14,1),(2210,20,2),(3470,30,.5)])
    s+=rng.standard_normal(n)*np.exp(-tt*80)*0.6; i=int(t0*sr); m=min(n,N-i); out[i:i+m]+=amp*s[:m]*0.3
for k,tc in enumerate(np.arange(35.8,44.2,0.82)): clank(tc+rng.uniform(-0.05,0.05),0.5+0.3*rng.random())
# drips inside
def drip(t0):
    n=int(0.12*sr); tt=np.arange(n)/sr; f=1400+600*rng.random(); s=np.sin(2*np.pi*(f+3000*tt)*tt)*np.exp(-tt*45); i=int(t0*sr); out[i:i+n]+=0.12*s
for tc in np.cumsum(rng.uniform(0.7,2.2,40))+41:
    if tc<59.5: drip(tc)
# detector beeps: confirmation at 21.5, alarm from 54.4 to 66
def beep(t0,dur,f,amp):
    n=int(dur*sr); tt=np.arange(n)/sr; s=np.sign(np.sin(2*np.pi*f*tt))*0.6+np.sin(2*np.pi*f*tt)*0.4
    s*=np.clip(tt/0.005,0,1)*np.clip((dur-tt)/0.005,0,1); i=int(t0*sr); out[i:i+n]+=amp*s
beep(21.5,0.12,2600,0.08); beep(21.7,0.12,2600,0.08)
for k,tc in enumerate(np.arange(54.4,66,0.25)):
    amp=0.16 if tc<60 else 0.07
    beep(tc,0.12,3100 if k%2==0 else 2700,amp)
# winch ratchet clicks in s6
for tc in np.arange(60.8,68,0.11):
    n=int(0.03*sr); tt=np.arange(n)/sr; s=rng.standard_normal(n)*np.exp(-tt*300)+np.sin(2*np.pi*3800*tt)*np.exp(-tt*200)*0.5
    i=int(tc*sr); out[i:i+n]+=0.12*s
# simple reverb inside (comb filters)
inside=env(35.5,60,1.0,0.3)
wet=np.zeros(N); src=out*inside
for dly,g in [(0.031,0.55),(0.047,0.5),(0.067,0.45),(0.089,0.4)]:
    d=int(dly*sr); y=src.copy()
    if ss is not None: y=ss.lfilter([1],np.r_[1,np.zeros(d-1),-g],src)
    wet+=y
out+=0.18*onepole(wet,3000)
# title/end drone
dr=0.06*(np.sin(2*np.pi*55*t)+0.6*np.sin(2*np.pi*82.5*t)+0.4*np.sin(2*np.pi*110.3*t))*(0.7+0.3*np.sin(2*np.pi*0.2*t))
out+=dr*(env(0,6.2,1.5,0.6)+env(70,80,1,2.5))
# master fade, normalise
out*=np.clip(t/0.8,0,1)*np.clip((D-t)/1.5,0,1)
out=np.tanh(out*1.2); out/=np.abs(out).max()*1.12
stereo=np.stack([out,np.roll(out,int(0.0007*sr))],1)
with wave.open('audio.wav','wb') as w:
    w.setnchannels(2);w.setsampwidth(2);w.setframerate(sr);w.writeframes((stereo*32767).astype(np.int16).tobytes())
print('ok')
