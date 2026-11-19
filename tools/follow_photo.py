import sys
from PIL import Image, ImageDraw, ImageFont, ImageEnhance, ImageFilter
out, handle, srcf, cx, cy, cw, img_h = sys.argv[1], sys.argv[2], sys.argv[3], int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6]), int(sys.argv[7])
W,H=1080,1350; BG=(10,11,16); TEAL=(45,226,208); PINK=(255,61,143)
src=Image.open(srcf).convert("RGB")
ch=round(cw*img_h/W)
fr=src.crop((cx,cy,cx+cw,cy+ch)).resize((W,img_h),Image.LANCZOS)
fr=ImageEnhance.Contrast(fr).enhance(1.06); fr=ImageEnhance.Color(fr).enhance(1.15)
fr=fr.filter(ImageFilter.UnsharpMask(radius=2,percent=60,threshold=2))
canvas=Image.new("RGB",(W,H),BG); canvas.paste(fr,(0,0))
grad=Image.new("L",(1,H),0); px=grad.load()
g0,g1=img_h-230,img_h
for y in range(H):
    t=0 if y<g0 else (1 if y>=g1 else (y-g0)/(g1-g0))
    px[0,y]=int(255*(t*t*(3-2*t)))
canvas.paste(Image.new("RGB",(W,H),BG),(0,0),grad.resize((W,H)))
d=ImageDraw.Draw(canvas)
ANTON="/usr/share/fonts/truetype/google-fonts/ofl/anton/Anton-Regular.ttf"
POP="/usr/share/fonts/truetype/google-fonts/Poppins-%s.ttf"
sz=140
while True:
    fh=ImageFont.truetype(ANTON,sz)
    if max(d.textlength("REAL GTA 6 GAMEPLAY.",font=fh),d.textlength("NEW CLIPS EVERY DAY.",font=fh))<=952: break
    sz-=2
LH=int(sz*1.16)
def center(parts,y,font,track=0):
    total=sum(d.textlength(t,font=font) for t,_ in parts)
    x=(W-total)/2
    for t,c in parts:
        d.text((x,y),t,font=font,fill=c); x+=d.textlength(t,font=font)
y=img_h-24
center([("REAL GTA 6 GAMEPLAY.","white")],y,fh)
y+=LH
center([("NEW CLIPS ","white"),("EVERY DAY.",TEAL)],y,fh)
y+=LH+58
# follow row centred: logo + text
L=76
fp=ImageFont.truetype(POP%"Medium",40)
t1,t2="FOLLOW  ",handle
tw=d.textlength(t1,font=fp)+d.textlength(t2,font=fp)
x=(W-(L+22+tw))/2
logo=Image.open("logo.png").convert("RGB").resize((L,L),Image.LANCZOS)
mask=Image.new("L",(L*4,L*4),0); ImageDraw.Draw(mask).ellipse((0,0,L*4-1,L*4-1),fill=255); mask=mask.resize((L,L),Image.LANCZOS)
d.ellipse((x-3,y-3,x+L+3,y+L+3),fill=(60,62,74))
canvas.paste(logo,(int(x),int(y)),mask)
x+=L+22
d.text((x,y+L/2),t1,font=fp,fill=(170,174,190),anchor="lm"); x+=d.textlength(t1,font=fp)
d.text((x,y+L/2),t2,font=fp,fill=PINK,anchor="lm")
print("bottom",y+L)
canvas.save(out,quality=95)
