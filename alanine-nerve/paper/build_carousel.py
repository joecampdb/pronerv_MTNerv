"""Create an eight-page, portrait LinkedIn document carousel from project renders."""
from pathlib import Path
from math import atan2, cos, sin, pi
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor
from reportlab.lib.utils import ImageReader
from PIL import Image

ROOT = Path(__file__).resolve().parents[2]
FIG = ROOT/"alanine-nerve/paper/figures"
OUT = ROOT/"output/pdf"
OUT.mkdir(parents=True, exist_ok=True)
for name, file in [("Sans","segoeui.ttf"),("Bold","segoeuib.ttf"),("Serif","georgia.ttf")]:
    pdfmetrics.registerFont(TTFont(name,str(Path("C:/Windows/Fonts")/file)))
W,H = 1080,1350
BG="#0B1522"; CARD="#142535"; WHITE="#EDF5F5"; MUTED="#A9BDC9"
MINT="#8DE7C1"; GOLD="#F3C784"; BLUE="#9BC7F4"
c=canvas.Canvas(str(OUT/"molecular-atlas-linkedin-carousel.pdf"),pagesize=(W,H))
c.setTitle("Molecules, Landscapes & Composition")
c.setAuthor("Joseph Campagna, PSM")
c.setSubject("Alanine dipeptide and chignolin CLN025: exploratory categorical molecular atlas")


def text(s,x,y,size=30,color=WHITE,font="Sans"):
    c.setFillColor(HexColor(color));c.setFont(font,size);c.drawString(x,H-y-size,s)


def para(s,x,y,width=930,size=31,color=MUTED,font="Sans",leading=1.35):
    words=s.split();line="";lines=[]
    for word in words:
        test=(line+" "+word).strip()
        if pdfmetrics.stringWidth(test,font,size)>width and line:
            lines.append(line);line=word
        else:line=test
    if line:lines.append(line)
    for i,line in enumerate(lines):text(line,x,y+i*size*leading,size,color,font)
    return y+len(lines)*size*leading


def rect(x,y,w,h,color=CARD,r=22):
    c.setFillColor(HexColor(color));c.roundRect(x,H-y-h,w,h,r,fill=1,stroke=0)


def image(name,x,y,w,h):
    im=Image.open(FIG/name)
    # Contain the original render: never crop molecular geometry.
    iw,ih=im.size;s=min(w/iw,h/ih);dw,dh=iw*s,ih*s
    c.drawImage(ImageReader(im),x+(w-dw)/2,H-y-(h+dh)/2,dw,dh,mask="auto")


def base(n,kicker):
    c.setFillColor(HexColor(BG));c.rect(0,0,W,H,fill=1,stroke=0)
    text("MOLECULAR ATLAS",72,48,20,MINT,"Bold")
    text(kicker.upper(),72,87,18,MUTED)
    c.setStrokeColor(HexColor("#2C4352"));c.setLineWidth(1)
    c.line(72,100,1008,100)
    text("Joseph Campagna, PSM",72,1268,23,WHITE,"Bold")
    text(f"{n:02d} / 08",914,1270,20,MUTED)


def title(lines):
    for i,s in enumerate(lines):text(s,72,158+i*76,62,WHITE,"Bold")


def arrow(a,b,label=None,dashed=False,color=MINT):
    x1,y1=a;x2,y2=b
    c.saveState();c.setStrokeColor(HexColor(color));c.setFillColor(HexColor(color));c.setLineWidth(5)
    if dashed:c.setDash(14,10)
    c.line(x1,H-y1,x2,H-y2)
    c.setDash()
    angle=atan2(y2-y1,x2-x1)
    p=c.beginPath();p.moveTo(x2,H-y2)
    for off in [-.48,.48]:
        p.lineTo(x2-22*cos(angle+off),H-(y2-22*sin(angle+off)))
    p.close();c.drawPath(p,fill=1,stroke=0);c.restoreState()
    if label:text(label,(x1+x2)/2-25,(y1+y2)/2-58,36,color,"Bold")


def node(label,x,y,color=MINT,r=52):
    c.setFillColor(HexColor(CARD));c.setStrokeColor(HexColor(color));c.setLineWidth(3)
    c.circle(x,H-y,r,stroke=1,fill=1)
    c.setFont("Bold",38);c.setFillColor(HexColor(color))
    c.drawCentredString(x,H-y-13,label)


# 1. A clear visual hook.
base(1,"An experiment in structural bioinformatics")
title(["What if a landscape", "were made of molecules?"])
para("And the composition of transitions were something we could see?",72,340,size=34,color=MINT)
image("landscape-nerve.png",35,470,1010,660)
text("ALANINE DIPEPTIDE  +  CHIGNOLIN CLN025",72,1147,24,WHITE,"Bold")
text("Recorded MD geometry. Deforming skins. Simplicial nerves.",72,1190,26,MUTED)
c.showPage()

# 2. Molecular identity, before abstraction.
base(2,"Meet the molecular examples")
title(["Two systems.", "Different complexity."])
rect(72,355,936,365)
image("alanine-cartoon.png",96,370,440,320)
text("ALANINE DIPEPTIDE",575,415,25,MINT,"Bold")
para("A compact torsional benchmark.",575,470,375,32,WHITE)
para("Backbone trace with heavy-atom context.",575,580,375,26)
rect(72,756,936,425)
image("chignolin-compact-cartoon.png",90,790,445,290)
image("chignolin-extended-cartoon.png",545,790,445,290)
text("CHIGNOLIN CLN025  /  10 RESIDUES",100,1095,26,GOLD,"Bold")
text("Compact and extended recorded Cα conformations",100,1140,26)
text("Cartoons show backbone geometry, not assigned helices or sheets.",72,1202,24,MUTED)
c.showPage()

# 3. Two actual landscapes, with honest statistics.
base(3,"From recorded conformations to a molecular atlas")
title(["Geometry becomes", "the landscape."])
text("ALANINE  /  750,000 FRAMES",72,355,25,MINT,"Bold")
image("landscape-nerve.png",72,400,600,375)
para("Backbone angles",705,470,300,30,WHITE,"Bold")
para("φ and ψ define the chart.",705,568,280,28)
text("CLN025  /  63,999 FRAMES",72,800,25,GOLD,"Bold")
image("chignolin-landscape-nerve.png",72,844,600,350)
para("Molecular shape",705,888,300,30,WHITE,"Bold")
para("Cα radius of gyration and end-to-end distance.",705,980,290,28)
text("CLN025 color/height encodes pooled occupancy, not equilibrium free energy.",72,1204,23,MUTED)
c.showPage()

# 4. Show actual motion with static frames appropriate to a PDF.
base(4,"The surfaces themselves change")
title(["The geometry moves.", "Not just the highlights."])
para("Three visual phases, with camera and lighting held fixed.",72,345,size=31)
for row,(prefix,label,col) in enumerate([("","ALANINE  /  A → C",MINT),("chignolin-","CLN025  /  A → C",GOLD)]):
    y=460+row*350
    text(label,72,y,25,col,"Bold")
    for k,phase in enumerate(["0","⅓","⅔"]):
        x=72+k*318
        image(prefix+f"phase-{k}.png",x,y+55,300,255)
        text("PHASE "+phase,x+73,y+307,20,MUTED)
para("Mesh vertices follow an MD-attached deformation field. These are visual phases, not three instantaneous MD structures.",72,1180,930,25,MUTED,leading=1.25)
c.showPage()

# 5. A vector nerve illustration: conceptual, labelled.
base(5,"Nerve 1 / overlap and inclusion")
title(["Which neighborhoods", "overlap?"])
para("A sampled conformation can witness membership in several neighborhoods.",72,345,900,32)
c.saveState()
for x,y,col in [(420,610,MINT),(650,610,BLUE),(535,790,GOLD)]:
    c.setFillColor(HexColor(col));c.setFillAlpha(.25);c.circle(x,H-y,170,stroke=0,fill=1)
c.restoreState()
text("U₀",297,540,38,MINT,"Bold");text("U₁",715,540,38,BLUE,"Bold");text("U₂",515,860,38,GOLD,"Bold")
c.setFillColor(HexColor(WHITE));c.circle(535,H-665,8,fill=1,stroke=0)
text("shared witness",582,683,23,WHITE)
rect(72,1000,936,112)
text("{0}   →   {0, 1}   →   {0, 1, 2}",153,1028,41,MINT,"Bold")
para("An inclusion chain is a 2-simplex in the face-poset nerve.",72,1146,930,31,WHITE)
text("Schematic cover. No configuration-space homotopy recovery is claimed.",72,1200,23,MUTED)
c.showPage()

# 6. Formal composition, not a shortcut.
base(6,"Nerve 2 / transitions and composition")
title(["A path can compose.", "A shortcut is different."])
para("Observed route types generate a category of paths.",72,346,930,32)
node("A",205,865);node("B",540,520);node("C",875,865)
arrow((245,823),(500,563),"f")
arrow((580,563),(835,823))
text("g",740,650,36,MINT,"Bold")
arrow((267,865),(813,865),dashed=True,color=GOLD)
text("g",473,904,46,GOLD,"Bold")
c.setStrokeColor(HexColor(GOLD));c.setLineWidth(3);c.circle(526,H-934,7,stroke=1,fill=0)
text("f",550,904,46,GOLD,"Bold")
rect(72,1025,936,150)
para("A → B → C need not be a directly observed A → C transition.",107,1051,866,35,WHITE,"Bold")
text("Matching endpoints permits formal composition, not a spliced MD trajectory.",72,1205,23,MUTED)
c.showPage()

# 7. Positive scope and concrete limits without drowning the story.
base(7,"What the prototype establishes")
title(["A visual experiment.", "A precise distinction."])
items=[
    ("IMPLEMENTED",MINT,"MD-derived molecular geometry, deforming surfaces, and inspectable overlap/path nerves."),
    ("NOT YET VALIDATED",GOLD,"Equilibrium free energies, folding kinetics, or composition of complete dynamical systems."),
    ("LIMITATIONS ARE EXPLICIT",BLUE,"Adaptive sampling, projection loss, interpolation artifacts, and conflicting CLN025 timing metadata.")
]
for i,(label,col,body) in enumerate(items):
    y=375+i*260
    rect(72,y,936,226)
    text(label,102,y+28,24,col,"Bold")
    para(body,102,y+78,865,32,WHITE)
text("The paper documents the methods, obstacles and future directions.",72,1200,26,MUTED)
c.showPage()

# 8. Shareable public links, clickable in the PDF.
base(8,"An invitation to discuss")
title(["How should molecular", "dynamical models", "compose?"])
para("What should the interfaces be?",72,435,930,39,MINT,"Bold")
para("Contacts? Torsions? Boundary conditions?",72,501,930,32,WHITE)
para("What evidence would show that composition preserves meaningful behavior?",72,578,930,32)
links=[
    ("EXPLORE THE VIEWER","joecampdb.github.io/pronerv_MTNerv/","https://joecampdb.github.io/pronerv_MTNerv/"),
    ("CODE + REPRODUCTION","github.com/joecampdb/pronerv_MTNerv","https://github.com/joecampdb/pronerv_MTNerv"),
    ("ILLUSTRATED PAPER","joecampdb.github.io/pronerv_MTNerv/paper.pdf","https://joecampdb.github.io/pronerv_MTNerv/paper.pdf")
]
for i,(label,display,url) in enumerate(links):
    y=750+i*135;rect(72,y,936,110)
    text(label,100,y+17,20,MINT,"Bold");text(display,100,y+51,28,WHITE)
    c.linkURL(url,(72,H-y-110,1008,H-y),relative=0,thickness=0)
text("DATA: MDshare · Pérez Culubret & De Fabritiis (CC BY 4.0)",72,1180,22,MUTED)
text("Sources and scientific limitations are linked in the paper.",72,1216,22,MUTED)
c.showPage()
c.save()
print(OUT/"molecular-atlas-linkedin-carousel.pdf")
