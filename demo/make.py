import math, random
random.seed(4)
W,H=1600,1000
BG="#0f172a"; FG="#e2e8f0"; DIM="#94a3b8"; GRID="#1e293b"
def svg(name, body, bg=BG):
    open(name+".svg","w").write(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" font-family="Helvetica, Arial, sans-serif"><rect width="100%" height="100%" fill="{bg}"/>{body}</svg>')
def title(t, sub):
    return f'<text x="90" y="110" fill="{FG}" font-size="54" font-weight="700">{t}</text><text x="90" y="165" fill="{DIM}" font-size="30">{sub}</text>'

# 1 bar chart
names=["api","web","worker","cli","docs","infra"]; vals=[212,348,96,41,63,155]
b=title("Build time by package","seconds, main branch, last 30 runs")
x0,y0,ch=150,880,600
for i in range(5):
    y=y0-i*ch/4; b+=f'<line x1="{x0}" x2="1500" y1="{y}" y2="{y}" stroke="{GRID}" stroke-width="2"/><text x="{x0-20}" y="{y+10}" fill="{DIM}" font-size="26" text-anchor="end">{i*100}</text>'
for i,(n,v) in enumerate(zip(names,vals)):
    x=x0+40+i*220; h=v/400*ch
    b+=f'<rect x="{x}" y="{y0-h}" width="140" height="{h}" rx="10" fill="#38bdf8"/><text x="{x+70}" y="{y0-h-18}" fill="{FG}" font-size="30" text-anchor="middle">{v}s</text><text x="{x+70}" y="{y0+44}" fill="{DIM}" font-size="28" text-anchor="middle">{n}</text>'
svg("build-times",b)

# 2 line chart
b=title("p95 latency, before and after the cache","milliseconds per request, 24 hours")
def line(pts,col):
    return f'<polyline fill="none" stroke="{col}" stroke-width="6" stroke-linejoin="round" points="{" ".join(f"{x:.0f},{y:.0f}" for x,y in pts)}"/>'
x0,y0=150,880
for i in range(5):
    y=y0-i*150; b+=f'<line x1="{x0}" x2="1500" y1="{y}" y2="{y}" stroke="{GRID}" stroke-width="2"/><text x="{x0-20}" y="{y+10}" fill="{DIM}" font-size="26" text-anchor="end">{i*100}</text>'
before=[(x0+i*56, y0-(330+80*math.sin(i/3)+random.uniform(-30,30))*1.5) for i in range(25)]
after=[(x0+i*56, y0-(120+25*math.sin(i/3)+random.uniform(-12,12))*1.5) for i in range(25)]
b+=line(before,"#f97316")+line(after,"#34d399")
b+=f'<rect x="1150" y="210" width="28" height="28" rx="6" fill="#f97316"/><text x="1195" y="234" fill="{FG}" font-size="28">before</text><rect x="1330" y="210" width="28" height="28" rx="6" fill="#34d399"/><text x="1375" y="234" fill="{FG}" font-size="28">after</text>'
svg("latency",b)

# 3 login UI mock
L="#f8fafc"
b=f'<rect x="0" y="0" width="{W}" height="70" fill="#e2e8f0"/><circle cx="40" cy="35" r="11" fill="#f87171"/><circle cx="75" cy="35" r="11" fill="#fbbf24"/><circle cx="110" cy="35" r="11" fill="#4ade80"/><rect x="300" y="17" width="1000" height="36" rx="18" fill="#fff"/><text x="330" y="44" fill="#64748b" font-size="22">localhost:5173/login</text>'
b+=f'<rect x="550" y="190" width="500" height="640" rx="24" fill="#fff" stroke="#e2e8f0" stroke-width="2"/><text x="800" y="290" fill="#0f172a" font-size="44" font-weight="700" text-anchor="middle">Welcome back</text><text x="800" y="340" fill="#64748b" font-size="24" text-anchor="middle">Sign in to continue</text>'
for i,(lab,val) in enumerate([("Email","ada@example.com"),("Password","••••••••••")]):
    y=400+i*130; b+=f'<text x="610" y="{y}" fill="#334155" font-size="22">{lab}</text><rect x="610" y="{y+15}" width="380" height="64" rx="12" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/><text x="635" y="{y+57}" fill="#0f172a" font-size="24">{val}</text>'
b+=f'<rect x="610" y="680" width="380" height="68" rx="12" fill="#4f46e5"/><text x="800" y="723" fill="#fff" font-size="26" font-weight="700" text-anchor="middle">Sign in</text><text x="800" y="795" fill="#4f46e5" font-size="22" text-anchor="middle">Forgot password?</text>'
svg("login-page",b,bg=L)

# 4 architecture diagram
b=title("Request flow","browser → edge → app → database")
boxes=[("Browser",130,"#a78bfa"),("Edge proxy",500,"#38bdf8"),("App server",870,"#34d399"),("Postgres",1240,"#fbbf24")]
for i,(n,x,c) in enumerate(boxes):
    b+=f'<rect x="{x}" y="440" width="260" height="150" rx="20" fill="none" stroke="{c}" stroke-width="5"/><text x="{x+130}" y="527" fill="{FG}" font-size="32" text-anchor="middle">{n}</text>'
    if i<3: b+=f'<line x1="{x+270}" y1="515" x2="{x+355}" y2="515" stroke="{DIM}" stroke-width="5"/><polygon points="{x+360},515 {x+340},503 {x+340},527" fill="{DIM}"/>'
b+=f'<rect x="870" y="700" width="260" height="110" rx="20" fill="none" stroke="#f472b6" stroke-width="5" stroke-dasharray="14 10"/><text x="1000" y="765" fill="{FG}" font-size="30" text-anchor="middle">Redis cache</text><line x1="1000" y1="600" x2="1000" y2="690" stroke="{DIM}" stroke-width="5" stroke-dasharray="10 8"/>'
svg("request-flow",b)

# 5 donut
b=title("Test suite","1,284 tests, 41 s")
parts=[(1201,"#34d399","passed"),(52,"#fbbf24","skipped"),(31,"#f87171","failed")]
tot=sum(p[0] for p in parts); a=-math.pi/2; cx,cy,r=560,580,260
for v,c,_ in parts:
    a2=a+v/tot*2*math.pi; large=1 if a2-a>math.pi else 0
    b+=f'<path d="M{cx+r*math.cos(a):.1f},{cy+r*math.sin(a):.1f} A{r},{r} 0 {large} 1 {cx+r*math.cos(a2):.1f},{cy+r*math.sin(a2):.1f}" fill="none" stroke="{c}" stroke-width="90"/>'; a=a2
b+=f'<text x="{cx}" y="{cy+20}" fill="{FG}" font-size="64" font-weight="700" text-anchor="middle">93.5%</text>'
for i,(v,c,n) in enumerate(parts):
    y=450+i*90; b+=f'<rect x="1000" y="{y-30}" width="36" height="36" rx="8" fill="{c}"/><text x="1060" y="{y}" fill="{FG}" font-size="36">{n}</text><text x="1400" y="{y}" fill="{DIM}" font-size="36" text-anchor="end">{v}</text>'
svg("test-results",b)

# 6 abstract render
b='<defs><radialGradient id="g" cx="35%" cy="35%" r="70%"><stop offset="0" stop-color="#fde68a"/><stop offset="0.45" stop-color="#f472b6"/><stop offset="1" stop-color="#312e81"/></radialGradient><linearGradient id="s" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0b1026"/><stop offset="1" stop-color="#1e1b4b"/></linearGradient></defs><rect width="100%" height="100%" fill="url(#s)"/>'
for i in range(120):
    b+=f'<circle cx="{random.uniform(0,W):.0f}" cy="{random.uniform(0,H*0.6):.0f}" r="{random.uniform(1,3):.1f}" fill="#fff" opacity="{random.uniform(.3,.9):.2f}"/>'
b+='<ellipse cx="800" cy="900" rx="900" ry="160" fill="#0b1026" opacity="0.7"/><circle cx="800" cy="520" r="300" fill="url(#g)"/><ellipse cx="800" cy="520" rx="470" ry="80" fill="none" stroke="#c4b5fd" stroke-width="10" opacity="0.8" transform="rotate(-14 800 520)"/>'
svg("planet-render",b,bg="#0b1026")
