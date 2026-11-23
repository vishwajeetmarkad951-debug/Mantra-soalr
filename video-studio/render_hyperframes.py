import os, re, html, json
from pathlib import Path

raw = os.environ.get("MANTRA_SCRIPT", "").strip()
seconds = max(3, min(15, int(os.environ.get("SCENE_SECONDS", "6"))))
if not raw:
    raise SystemExit("Please provide a Marathi script in the workflow input.")
lines = [x.strip() for x in raw.splitlines() if x.strip()]
clips = []
for i, line in enumerate(lines):
    parts = [x.strip() for x in re.split(r"[.!?।]+", line) if x.strip()]
    title = parts[0] if parts else f"Scene {i+1}"
    body = "। ".join(parts[1:]) if len(parts) > 1 else line
    start = i * seconds
    clips.append(f"""
    <div class="clip title" id="title-{i}" data-start="{start}" data-duration="{seconds}" data-track-index="1">{html.escape(title)}</div>
    <div class="clip subtitle" id="subtitle-{i}" data-start="{start}" data-duration="{seconds}" data-track-index="2">{html.escape(body)}</div>
    """)
total = len(lines) * seconds
blocks = "\\n".join(clips)
page = r'''<!doctype html><html lang="mr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+Devanagari:wght@400;600;700;800;900&display=swap');
*{box-sizing:border-box}html,body{margin:0;width:720px;height:1280px;overflow:hidden;background:#080c14;font-family:'Noto Sans Devanagari',sans-serif}
#root{position:relative;width:720px;height:1280px;overflow:hidden;background:#080c14}
#scene{position:absolute;inset:0;width:720px;height:1280px}
.brand{position:absolute;top:36px;left:38px;color:#f6c45d;font-size:24px;font-weight:900;z-index:4}
.kicker{position:absolute;top:42px;right:35px;color:#18191d;background:#f5c85a;border-radius:20px;padding:9px 16px;font-size:14px;font-weight:900;z-index:4}
.title{position:absolute;left:38px;right:38px;top:155px;min-height:150px;display:flex;align-items:center;justify-content:center;text-align:center;color:#fff;font-size:49px;line-height:1.3;font-weight:900;text-shadow:0 4px 18px #000;z-index:5}
.subtitle{position:absolute;left:38px;right:38px;bottom:155px;min-height:150px;padding:30px 25px;display:flex;align-items:center;justify-content:center;text-align:center;color:#fff;font-size:27px;line-height:1.5;font-weight:700;background:rgba(5,8,14,.82);border:1px solid rgba(255,255,255,.2);border-radius:22px;z-index:5}
.footer{position:absolute;bottom:40px;left:0;width:720px;text-align:center;color:#f6c45d;font-size:24px;font-weight:900;z-index:5}
.clip{opacity:0}
</style></head><body><div id="root" data-composition-id="mantra-solar" data-width="720" data-height="1280">
<canvas id="scene" width="720" height="1280"></canvas>
<div class="brand">☀ MANTRA SOLAR</div><div class="kicker">3D SOLAR EXPLAINER</div>
__CLIPS__
<div class="footer">MANTRA SOLAR • 9226198204 • www.mantrasolar.in</div>
</div>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
<script type="module">
import * as THREE from 'https://cdn.jsdelivr.net/npm/three@0.180.0/build/three.module.js';
const W=720,H=1280,canvas=document.getElementById('scene');
const renderer=new THREE.WebGLRenderer({canvas,antialias:true,alpha:false,powerPreference:'high-performance'});
renderer.setSize(W,H,false);renderer.setPixelRatio(1);renderer.shadowMap.enabled=true;renderer.shadowMap.type=THREE.PCFSoftShadowMap;
const scene=new THREE.Scene();scene.background=new THREE.Color('#080d17');scene.fog=new THREE.Fog('#101827',14,34);
const camera=new THREE.PerspectiveCamera(34,W/H,.1,100);camera.position.set(8,7,13);camera.lookAt(0,1.4,0);
scene.add(new THREE.HemisphereLight(0x9dbbe0,0x17131a,1.8));
const sunLight=new THREE.DirectionalLight(0xffd28a,3.2);sunLight.position.set(-5,10,7);sunLight.castShadow=true;scene.add(sunLight);
const ground=new THREE.Mesh(new THREE.PlaneGeometry(100,100),new THREE.MeshStandardMaterial({color:'#111722',roughness:1}));ground.rotation.x=-Math.PI/2;ground.position.y=-.06;ground.receiveShadow=true;scene.add(ground);
const house=new THREE.Group();scene.add(house);
const standard=(color,roughness=.7,metalness=0)=>new THREE.MeshStandardMaterial({color,roughness,metalness});
const wall=new THREE.Mesh(new THREE.BoxGeometry(5,2.8,4),standard('#d1c9bd'));wall.position.y=1.4;wall.castShadow=true;house.add(wall);
const roof1=new THREE.Mesh(new THREE.BoxGeometry(3.05,.18,4.5),standard('#333947')),roof2=roof1.clone();roof1.position.set(-.78,3.02,0);roof1.rotation.z=-.48;roof2.position.set(.78,3.02,0);roof2.rotation.z=.48;house.add(roof1,roof2);
const panels=new THREE.Group();panels.position.set(-.8,3.22,.1);panels.rotation.z=-.48;house.add(panels);
const panel=new THREE.Mesh(new THREE.BoxGeometry(2.15,.07,3.3),standard('#082a52',.25,.65));panels.add(panel);
const cellMat=new THREE.MeshStandardMaterial({color:'#55a9e8',emissive:'#123b6d',emissiveIntensity:.5,metalness:.55,roughness:.3});
for(let x=0;x<4;x++)for(let z=0;z<5;z++){const m=new THREE.Mesh(new THREE.BoxGeometry(.5,.025,.59),cellMat);m.position.set(-.79+x*.53,.055,-1.28+z*.64);panels.add(m)}
const door=new THREE.Mesh(new THREE.BoxGeometry(.8,1.9,.06),standard('#29384d'));door.position.set(.6,.95,2.04);house.add(door);
for(const x of [-1.65,1.65]){const w=new THREE.Mesh(new THREE.BoxGeometry(.85,.85,.07),new THREE.MeshStandardMaterial({color:'#6cc5ed',emissive:'#174c71',emissiveIntensity:.4}));w.position.set(x,1.7,2.06);house.add(w)}
const inverter=new THREE.Mesh(new THREE.BoxGeometry(.55,.85,.25),standard('#e5e8ec',.35));inverter.position.set(2.15,1.35,2.13);house.add(inverter);
const battery=new THREE.Mesh(new THREE.BoxGeometry(.62,1.1,.55),standard('#29394b',.35,.35));battery.position.set(3.25,.55,1.6);house.add(battery);
const sun=new THREE.Mesh(new THREE.SphereGeometry(.72,32,24),new THREE.MeshBasicMaterial({color:'#ffc45d'}));sun.position.set(-4.5,7,-5);scene.add(sun);
const sunGlow=new THREE.PointLight('#ffb84d',50,24);sunGlow.position.copy(sun.position);scene.add(sunGlow);
const path=new THREE.CatmullRomCurve3([new THREE.Vector3(-.8,3.6,.2),new THREE.Vector3(0,3.9,1.4),new THREE.Vector3(2.2,2.4,2.3),new THREE.Vector3(3.2,1.4,1.7)]);
scene.add(new THREE.Mesh(new THREE.TubeGeometry(path,48,.025,8,false),new THREE.MeshBasicMaterial({color:'#f6bd56'})));
const particles=[];for(let i=0;i<18;i++){const p=new THREE.Mesh(new THREE.SphereGeometry(.055,8,8),new THREE.MeshBasicMaterial({color:'#ffe08a'}));scene.add(p);particles.push(p)}
const total=__TOTAL_DURATION__;
const tl=gsap.timeline({paused:true});
tl.to(camera.position,{x:7.2,y:6.7,z:12.4,duration:total,ease:'none'},0);
tl.to(panels.rotation,{z:-.48+.025,duration:total,ease:'sine.inOut'},0);
tl.to(sunGlow,{intensity:58,duration:total/2,yoyo:true,repeat:1,ease:'sine.inOut'},0);
tl.eventCallback('onUpdate',()=>{const time=tl.time();particles.forEach((p,i)=>p.position.copy(path.getPoint((time*.2+i/particles.length)%1)));camera.lookAt(0,1.4,0);renderer.render(scene,camera)});
window.__timelines=window.__timelines||{};window.__timelines['mantra-solar']=tl;
renderer.render(scene,camera);
</script></body></html>'''.replace("__CLIPS__", blocks).replace("__TOTAL_DURATION__", str(total))
Path("index.html").write_text(page, encoding="utf-8")
print(f"Generated {len(lines)} scenes, {total}s total.")
