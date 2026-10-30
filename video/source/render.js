const {chromium}=require('playwright');
const [,,mode,a,b]=process.argv; // preview t1,t2,... | frames start end
(async()=>{const br=await chromium.launch({args:['--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const p=await br.newPage({viewport:{width:1280,height:720}});p.on('console',m=>console.log('C:',m.text()));p.on('pageerror',e=>console.log('ERR',e.message));
await p.goto('http://localhost:8765/scene.html');await p.waitForFunction(()=>window.ready===true,null,{timeout:30000});
if(mode==='preview'){for(const t of a.split(',').map(Number)){await p.evaluate(t=>window.renderAt(t),t);await p.screenshot({path:`prev_${t}.jpg`,quality:85});console.log('shot',t);}}
else{const s=+a,e=+b;const fs=require('fs');for(let f=s;f<e;f++){const fp=`frames/f${String(f).padStart(5,'0')}.jpg`;if(fs.existsSync(fp))continue;await p.evaluate(t=>window.renderAt(t),f/25);await p.screenshot({path:`frames/f${String(f).padStart(5,'0')}.jpg`,quality:92});if(f%100==0)console.log('frame',f);}}
await br.close();})();
