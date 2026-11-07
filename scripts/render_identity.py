"""Original generative identity for the profile: math and SVG, no browser scripts.

Run with Python's standard library. Animations respect reduced-motion settings.
The knot is a projected trefoil with six strands, sampled through a 3D rotation.
Project illustrations are schematic artwork, not application screenshots.
"""
from html import escape
from math import sin, cos, pi, sqrt
from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"
BG = "#080F1A"
PANEL = "#101C2B"
LINE = "#273C51"
INK = "#EDF3F7"
MUTED = "#97ACC0"
CYAN = "#75EAF5"
VIOLET = "#BBA4FF"

STYLE = '''<style>
.still{display:none}.flow{stroke-dasharray:3 19;animation:flow 12s linear infinite}.pulse{animation:pulse 4s ease-in-out infinite}.draw{stroke-dasharray:900;stroke-dashoffset:900;animation:draw 8s ease-in-out infinite}.scan{animation:scan 5s ease-in-out infinite}.bar{transform-box:fill-box;transform-origin:bottom;animation:bars 6s ease-in-out infinite}.orbit{transform-origin:1080px 315px;animation:orbit 70s linear infinite}.inverse{animation-direction:reverse}
@keyframes flow{to{stroke-dashoffset:-220}}@keyframes pulse{50%{opacity:.35}}@keyframes draw{0%,10%{stroke-dashoffset:900}55%,90%{stroke-dashoffset:0}100%{stroke-dashoffset:900}}@keyframes scan{0%,100%{transform:translateY(0)}50%{transform:translateY(80px)}}@keyframes bars{0%,100%{transform:scaleY(.5)}50%{transform:scaleY(1)}}@keyframes orbit{to{transform:rotate(360deg)}}
@media(prefers-reduced-motion:reduce){.motion{display:none}.still{display:block}.flow,.pulse,.draw,.scan,.bar,.orbit{animation:none}.draw{stroke-dashoffset:0}}
</style>'''

def text(x,y,value,size=18,color=INK,weight=400,spacing=0,anchor="start",family="Arial,Helvetica,sans-serif"):
    return f'<text x="{x}" y="{y}" fill="{color}" font-family="{family}" font-size="{size}" font-weight="{weight}" letter-spacing="{spacing}" text-anchor="{anchor}">{escape(value)}</text>'

def start(width,height,title,description):
    return [f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{width}" height="{height}" viewBox="0 0 {width} {height}" fill="none" role="img" aria-labelledby="title desc"><title id="title">{escape(title)}</title><desc id="desc">{escape(description)}</desc>', STYLE]

def save(name,parts):
    svg = "\n".join(parts + ["</svg>"])
    ET.fromstring(svg)
    (ASSETS / name).write_text(svg,encoding="utf-8")
    print(name, len(svg.encode("utf-8")), "bytes")

def dot(x,y,color=CYAN,r=4,css=""):
    return f'<circle class="{css}" cx="{x}" cy="{y}" r="{r}" fill="{color}"/>'

def knot_point(t,strand,angle):
    # A tube around the analytic trefoil. A stable perpendicular basis follows it.
    p=((2+cos(3*t))*cos(2*t),(2+cos(3*t))*sin(2*t),sin(3*t))
    tangent=(-3*sin(3*t)*cos(2*t)-2*(2+cos(3*t))*sin(2*t),-3*sin(3*t)*sin(2*t)+2*(2+cos(3*t))*cos(2*t),3*cos(3*t))
    length=sqrt(sum(v*v for v in tangent))
    tx,ty,tz=(v/length for v in tangent)
    normal_length=sqrt(tx*tx+ty*ty)
    nx,ny,nz=-ty/normal_length,tx/normal_length,0
    bx,by,bz=ty*nz-tz*ny,tz*nx-tx*nz,tx*ny-ty*nx
    v=strand*2*pi/6
    x,y,z=(p[i]+.19*(cos(v)*(nx,ny,nz)[i]+sin(v)*(bx,by,bz)[i]) for i in range(3))
    x,z=x*cos(angle)+z*sin(angle),-x*sin(angle)+z*cos(angle)
    pitch=.64
    y,z=y*cos(pitch)-z*sin(pitch),y*sin(pitch)+z*cos(pitch)
    perspective=8/(8-z)
    return 1080+x*68*perspective,315+y*68*perspective

def knot_path(strand,angle):
    points=[knot_point(i*2*pi/128,strand,angle) for i in range(128)]
    return "M"+"L".join(f"{x:.1f},{y:.1f}" for x,y in points)+"Z"

def hero():
    p=start(1440,640,"Bharath — Intelligence, engineered.","An original animated 3D trefoil sculpture, a computational drawing of six rotating strands. AI/ML and Python developer, Hyderabad, India.")
    p += ['<defs><radialGradient id="aura"><stop stop-color="#234258" stop-opacity=".55"/><stop offset="1" stop-color="#080F1A" stop-opacity="0"/></radialGradient><linearGradient id="wire" x1="850" y1="120" x2="1310" y2="530" gradientUnits="userSpaceOnUse"><stop stop-color="#A0FCFF"/><stop offset=".4" stop-color="#71DCED"/><stop offset=".75" stop-color="#B59FF9"/><stop offset="1" stop-color="#EBD7FF"/></linearGradient><pattern id="grid" width="32" height="32" patternUnits="userSpaceOnUse"><path d="M32 0H0V32" stroke="#29415B" stroke-width=".6" opacity=".3"/></pattern></defs>',f'<rect width="1440" height="640" rx="18" fill="{BG}"/><rect x="790" y="92" width="610" height="460" fill="url(#grid)"/><ellipse cx="1080" cy="315" rx="320" ry="285" fill="url(#aura)"/>',f'<path d="M46 83H1394M46 558H1394" stroke="{LINE}"/>',text(46,48,"BHARATH / HUMAN BEHIND THE SYSTEMS",14,MUTED,600,2),dot(1195,43,CYAN,4,"pulse"),text(1211,48,"HYDERABAD, INDIA",12,MUTED,400,1.1),text(49,142,"AI / ML & PYTHON DEVELOPER",14,CYAN,600,2.1),text(40,277,"BHARATH.",135,INK,800,-8),text(46,365,"Intelligence,",69,INK,600,-2.8),text(46,443,"engineered.",69,CYAN,600,-2.8),text(49,498,"Models → tools → useful applications.",20,MUTED),f'<circle cx="1080" cy="315" r="236" stroke="{LINE}"/><circle class="orbit" cx="1080" cy="315" r="248" stroke="#465874" stroke-dasharray="2 27"/><ellipse class="orbit inverse" cx="1080" cy="315" rx="268" ry="88" stroke="#65879E" stroke-opacity=".45"/>']
    # Explicit still geometry is available for reduced-motion readers.
    for strand in range(6):
        path=knot_path(strand,0)
        values=";".join(knot_path(strand,frame*2*pi/32) for frame in range(33))
        opacity=.42+strand*.09
        p.append(f'<path class="motion" d="{path}" stroke="url(#wire)" stroke-width="2.2" opacity="{opacity:.2f}"><animate attributeName="d" dur="18s" repeatCount="indefinite" values="{values}"/></path>')
        p.append(f'<path class="still" d="{path}" stroke="url(#wire)" stroke-width="2.2" opacity="{opacity:.2f}"/>')
    p += [text(1080,112,"A STUDY IN CONNECTION",11,MUTED,400,2,"middle"),text(47,601,"RAG + LLMS",14,CYAN,600,1.2),text(246,601,"MACHINE LEARNING",14,"#A8BFF0",600,1.2),text(553,601,"MCP SYSTEMS",14,VIOLET,600,1.2),text(1394,601,"OPEN TO INTERNSHIPS ↗",13,MUTED,600,1.2,"end")]
    save("hero.svg",p)

def mobile_hero():
    p=start(720,650,"Bharath — Intelligence, engineered.","AI and ML developer. Python, RAG, and MCP. Hyderabad, India.")
    p += [f'<rect width="720" height="650" rx="16" fill="{BG}"/>',f'<path d="M36 78H684M36 566H684" stroke="{LINE}"/>',text(36,47,"BHARATH LINGA REDDY PALEM",18,MUTED,600,1.1),text(36,133,"AI / ML & PYTHON DEVELOPER",17,CYAN,600,1.1),text(28,250,"BHARATH.",112,INK,800,-7),text(36,340,"Intelligence,",70,INK,600,-3),text(36,421,"engineered.",70,CYAN,600,-3),text(36,488,"Models → tools → useful applications.",23,MUTED),text(36,539,"HYDERABAD, INDIA / CLASS OF 2027",17,MUTED,400,1),text(36,610,"RAG / ML / MCP / PYTHON",19,CYAN,600,1.1)]
    save("hero-mobile.svg",p)

def constellation():
    p=start(1440,590,"Bharath's AI project constellation","A curated map of public projects: Data Agent for analytics, Expense MCP for connected tools, Educational RAG for retrieval, and forecasting and classification for machine learning. Animated paths are illustrative.")
    p += [f'<rect width="1440" height="590" rx="14" fill="{BG}"/>',text(36,44,"THE PROJECT CONSTELLATION",17,INK,600,1.7),text(1404,44,"FOUR DIRECTIONS / ONE BUILDER",12,MUTED,400,1.3,"end"),f'<path d="M36 67H1404M36 541H1404" stroke="{LINE}"/>']
    points=[(320,173),(1110,173),(320,418),(1110,418)]
    paths=["M530 173C630 173 615 295 714 295","M914 173C815 173 827 295 728 295","M530 418C630 418 615 305 714 305","M914 418C815 418 827 305 728 305"]
    colors=[CYAN,VIOLET,"#9FBFF7","#F5C6A1"]
    for i,path in enumerate(paths):
        p += [f'<path d="{path}" stroke="{LINE}" stroke-width="4"/>',f'<path class="flow" d="{path}" stroke="{colors[i]}" stroke-width="2"/>',f'<circle class="motion" r="5" fill="{colors[i]}"><animateMotion path="{path}" dur="{5+i}s" repeatCount="indefinite"/></circle>']
    for radius in [84,106,133]:
        p.append(f'<circle cx="720" cy="300" r="{radius}" stroke="{LINE}" stroke-dasharray="{0 if radius==84 else 4} {0 if radius==84 else 8}"/>')
    p += [f'<circle cx="720" cy="300" r="80" fill="{PANEL}" stroke="{CYAN}"/>',text(720,319,"B.",64,INK,700,-3,"middle"),text(720,471,"INTELLIGENCE → EXPERIENCE",11,MUTED,400,1.1,"middle")]
    nodes=[(36,105,"01 / ANALYTICS","Data Agent","Clean → compare → predict",CYAN),(914,105,"02 / CONNECTED TOOLS","Expense MCP","Conversation → action",VIOLET),(36,350,"03 / KNOWLEDGE","Educational RAG","Documents → retrieved context","#9FBFF7"),(914,350,"04 / PREDICTION","The ML lab","Forecasting / recommendation / vision","#F5C6A1")]
    for x,y,label,title,subtitle,color in nodes:
        p += [f'<rect x="{x}" y="{y}" width="490" height="136" rx="10" fill="{PANEL}" stroke="{LINE}"/>',dot(x+22,y+27,color,4,"pulse"),text(x+37,y+32,label,13,color,600,1),text(x+22,y+75,title,31,INK,600,-.7),text(x+22,y+108,subtitle,17,MUTED)]
    p += [text(36,571,"A CURATED MAP OF MY WORK / FOLLOW THE PROJECT LINKS BELOW",11,MUTED,400,1.1),text(1404,571,"SIGNAL IS VISUAL; THE PROJECTS ARE REAL.",11,MUTED,400,1.1,"end")]
    save("project-constellation.svg",p)

def mobile_constellation():
    p=start(720,850,"Bharath's project constellation","Four directions: analytics, connected tools, educational retrieval, and predictive machine learning.")
    p += [f'<rect width="720" height="850" rx="14" fill="{BG}"/>',text(35,48,"FOUR DIRECTIONS / ONE BUILDER",20,MUTED,600,1.3)]
    nodes=[("01 / ANALYTICS","Data Agent","Clean → compare → predict",CYAN),("02 / CONNECTED TOOLS","Expense MCP","Conversation → action",VIOLET),("03 / KNOWLEDGE","Educational RAG","Documents → context","#9FBFF7"),("04 / PREDICTION","The ML lab","Forecasting / recommendation / vision","#F5C6A1")]
    p.append(f'<path class="flow" d="M50 80V765" stroke="{CYAN}" stroke-width="2"/>')
    for i,(tag,title,subtitle,color) in enumerate(nodes):
        y=85+i*178
        p += [dot(50,y+70,color,8,"pulse"),f'<path d="M58 {y+70}H80" stroke="{LINE}"/><rect x="80" y="{y}" width="605" height="147" rx="12" fill="{PANEL}" stroke="{LINE}"/>',text(105,y+34,tag,18,color,600,1),text(105,y+82,title,38,INK,600,-1),text(105,y+118,subtitle,22,MUTED)]
    p += [text(35,821,"BHARATH / INTELLIGENCE → EXPERIENCE",17,MUTED,400,1)]
    save("project-constellation-mobile.svg",p)

def card(name,index,tag,title,subtitle,color,art):
    p=start(720,300,title,f"Schematic animated artwork for {title}. {subtitle}")
    p += [f'<rect width="720" height="300" rx="10" fill="{BG}"/>',f'<path d="M28 60H692M28 257H692" stroke="{LINE}"/>',dot(32,32,color,3,"pulse"),text(45,37,tag,13,color,600,1.3),text(690,38,index,17,MUTED,400,0,"end"),text(28,129,title,35,INK,600,-1.1),text(28,167,subtitle,14,MUTED),text(28,282,"BHARATH / SYSTEM "+index,10,MUTED,400,1.3),text(690,282,"EXPLORE ↗",11,color,600,1,"end"),art]
    save(name,p)

def cards():
    art=f'<path d="M475 225H680" stroke="{LINE}"/>'
    for i,height in enumerate([45,80,58,110,130]):
        x=487+i*38
        art+=f'<rect class="bar" x="{x}" y="{225-height}" width="20" height="{height}" rx="3" fill="{CYAN}" opacity="{.24+i*.17:.2f}" style="animation-delay:{-i*.65}s"/>'
    art+=f'<path class="draw" d="M478 195L518 165L555 180L596 129L635 143L679 95" stroke="#C8F9FF" stroke-width="2.5"/>'
    card("data-agent.svg","01","THE ANALYTICAL WORKSPACE","Data → decisions.","EXPLORE / CLEAN / TRAIN / REPORT",CYAN,art)
    path="M526 139H561C578 139 578 211 595 211H629"
    art=f'<rect x="479" y="99" width="50" height="78" rx="10" fill="{PANEL}" stroke="#5A517B"/><path d="M490 119H518M490 132H511M490 145H518" stroke="{VIOLET}" stroke-width="2"/><path class="flow" d="{path}" stroke="{VIOLET}" stroke-width="2"/><circle class="motion" r="4" fill="#E0CBFF"><animateMotion path="{path}" dur="4s" repeatCount="indefinite"/></circle><rect x="593" y="99" width="85" height="55" rx="9" fill="#24253D" stroke="{VIOLET}"/>'+text(635,132,"MCP",18,VIOLET,600,1,"middle")+f'<ellipse cx="636" cy="195" rx="37" ry="10" stroke="#9F8FC3"/><path d="M599 195V225C599 238 673 238 673 225V195" stroke="#9F8FC3"/><path d="M599 211C599 224 673 224 673 211" stroke="#9F8FC3"/>'
    card("expense-mcp.svg","02","THE CONVERSATIONAL INTERFACE","Intent → action.","ASSISTANT / TOOLS / PERSISTENCE",VIOLET,art)
    art=f'<rect x="483" y="98" width="82" height="114" rx="6" fill="#101D2B" stroke="#527492"/><path d="M500 121H549M500 139H540M500 157H549M500 175H532" stroke="#8FBDEB" stroke-width="2"/><path class="scan" d="M474 109H573" stroke="{CYAN}" stroke-width="3"/>'
    for i,(x,y) in enumerate([(608,112),(651,136),(601,168),(655,195),(620,227)]):
        art+=f'<path d="M568 157L{x} {y}" stroke="#334D69"/>'+dot(x,y,"#92BBF8",5,"pulse")
    card("educational-rag.svg","03","THE KNOWLEDGE INTERFACE","Context → answers.","DOCUMENTS / RETRIEVAL / LLMS","#9FBFF7",art)
    art=f'<path d="M475 224H682M475 91V224" stroke="{LINE}"/><path d="M485 199L519 175L552 187L589 141L617 154" stroke="#F7C7A1" stroke-width="2.5"/><path d="M617 154L649 110L680 92V160L649 169Z" fill="#F7C7A1" opacity=".13"/><path class="flow" d="M617 154L649 140L680 125" stroke="#F7C7A1" stroke-width="2"/>'+dot(617,154,"#F7C7A1",5,"pulse")
    card("retail-forecast.svg","04","THE PREDICTIVE WORKSPACE","History → foresight.","SALES / SIGNALS / FUTURE DEMAND","#F7C7A1",art)

def footer():
    p=start(1440,180,"Let's build something that matters.","Connect with Bharath Linga Reddy Palem on LinkedIn. Open to AI and ML and Python internships.")
    p += [f'<rect width="1440" height="180" rx="12" fill="{BG}"/>',f'<path class="flow" d="M40 140H1400" stroke="{CYAN}" stroke-width="1.5"/>',text(40,50,"NEXT CONNECTION / YOUR IDEA",12,MUTED,600,2),text(37,108,"Let’s build something that matters.",48,INK,600,-1.7),text(1394,106,"↗",62,CYAN,400,0,"end")]
    save("connect-banner.svg",p)

if __name__=="__main__":
    ASSETS.mkdir(exist_ok=True)
    hero()
    mobile_hero()
    constellation()
    mobile_constellation()
    cards()
    footer()
