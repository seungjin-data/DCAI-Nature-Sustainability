import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.lines as mlines
import numpy as np, os
from matplotlib import rcParams
from pathlib import Path
REPO = Path(__file__).parent.parent

rcParams.update({'font.family':'Liberation Sans','pdf.fonttype':42,'ps.fonttype':42})

C_STR='#9A9080'; C_IMPL='#4472A0'; C_REP='#1A3F6F'
BG_STR='#FAF9F6'; BG_REP='#ECF2FA'

data=[
    (5.0,'CEI-1','AI/digital in NDC',   'or LT-LEDS',             4.0,'4% (1/25)',   None,C_STR, 'strategic'),
    (4.0,'CEI-2','AI strategy:',        'energy/climate targets',  0.0,'0% (0/25)',   None,C_STR, 'strategic'),
    (3.0,'CEI-4','AI/data-centre',      'carbon pricing',          0.0,'0% (0/25)',   None,C_STR, 'strategic'),
    (2.0,'CEI-3','Data-centre energy',  'efficiency mandate',     40.0,'40% (10/25)',34.8,C_IMPL,'implement'),
    (1.0,'CEI-5','AI\u2013climate',     'coordination',           44.0,'44% (11/25)',39.1,C_IMPL,'implement'),
    (0.0,'CEI-6','Mandatory carbon',    'reporting',              80.0,'80% (20/25)',None,C_REP, 'reporting'),
]
BH={'strategic':0.42,'implement':0.56,'reporting':0.68}
YLIM_B=-0.80;YLIM_T=5.80;YR=YLIM_T-YLIM_B
def y2ax(y): return (y-YLIM_B)/YR

fig,ax=plt.subplots(figsize=(170/25.4,118/25.4))
L=0.40;R=0.83;T=0.80;B=0.15
plt.subplots_adjust(left=L,right=R,top=T,bottom=B)

ax.axhspan(2.62,YLIM_T,color=BG_STR,zorder=0)
ax.axhspan(YLIM_B,0.60,color=BG_REP,zorder=0)
for xg in [25,50,75,100]:
    ax.axvline(xg,color='#E5E5E5',lw=0.5,zorder=1)
ax.axvline(0,color='#CCCCCC',lw=0.7,zorder=1)
for yh in [2.62,0.60]:
    ax.axhline(yh,color='#BBBBBB',lw=0.8,zorder=2)

# ── 컬러 사이드바: 데이터 좌표, xlim 확장 ─────────────────────────────────────
ax.set_xlim(-6,100)
ax.plot([-3.2,-3.2],[3.0-0.26,5.0+0.26],color=C_STR, lw=6,solid_capstyle='round',zorder=4,clip_on=False)
ax.plot([-3.2,-3.2],[1.0-0.30,2.0+0.30],color=C_IMPL,lw=6,solid_capstyle='round',zorder=4,clip_on=False)
ax.plot([-3.2,-3.2],[0.0-0.36,0.0+0.36],color=C_REP, lw=6,solid_capstyle='round',zorder=4,clip_on=False)

# ── 막대 ─────────────────────────────────────────────────────────────────────
for y,code,l1,l2,pct,frac,sens,col,grp in data:
    draw=pct if pct>0 else 0.3
    ax.barh(y,draw,height=BH[grp],color=col,edgecolor='none',zorder=3)
    if sens:
        ax.scatter(sens,y,s=44,facecolors='white',edgecolors=col,linewidths=1.6,zorder=5)
    if grp=='reporting':
        # CEI-6: 막대 안 흰색
        ax.text(pct-1.5,y,frac,va='center',ha='right',
                fontsize=7.5,color='white',fontweight='bold',zorder=6)
    else:
        ax.text(max(pct,0)+1.4,y,frac,va='center',ha='left',
                fontsize=7.0,color='#333')

# ── Y축 레이블 ───────────────────────────────────────────────────────────────
for y,code,l1,l2,pct,frac,sens,col,grp in data:
    ay=y2ax(y)
    fc=C_REP if grp=='reporting' else '#111'
    ax.text(-0.014,ay+0.046,code,transform=ax.transAxes,
            fontsize=7.0,fontweight='bold',color=fc,ha='right',va='center',clip_on=False)
    ax.text(-0.014,ay+0.004,l1,transform=ax.transAxes,
            fontsize=6.3,color='#333',ha='right',va='center',clip_on=False)
    ax.text(-0.014,ay-0.038,l2,transform=ax.transAxes,
            fontsize=6.3,color='#555',ha='right',va='center',clip_on=False)

# ── 왼쪽 그룹 레이블 ─────────────────────────────────────────────────────────
for ay,txt,col in [
    (y2ax(4.52),'Strategic alignment /\ndirect policy linkage','#555'),
    (y2ax(1.50),'Implementation /\ncoordination',              '#444'),
    (y2ax(0.00),'Reporting visibility',                        '#333'),
]:
    ax.text(-0.295,ay,txt,transform=ax.transAxes,fontsize=6.0,color=col,
            ha='right',va='center',clip_on=False,style='italic',
            linespacing=1.38,multialignment='right')

# ── 오른쪽 상태 레이블 (경계 안) ─────────────────────────────────────────────
for ay,t1,t2,col,fs in [
    (y2ax(4.0),'Sparse', '0\u20134%',   '#AAAAAA',6.8),
    (y2ax(1.5),'Partial','40\u201344%', C_IMPL,   7.0),
    (y2ax(0.0),'Common', '80%',         C_REP,    7.0),
]:
    ax.text(1.012,ay+0.028,t1,transform=ax.transAxes,fontsize=fs,
            color=col,ha='left',va='center',clip_on=False,
            fontweight='bold' if col==C_REP else 'normal')
    ax.text(1.012,ay-0.026,t2,transform=ax.transAxes,fontsize=fs-0.5,
            color=col,ha='left',va='center',clip_on=False)

# ── 축 ───────────────────────────────────────────────────────────────────────
ax.set_xticks([0,25,50,75,100])
ax.set_xticklabels(['0','25','50','75','100'],fontsize=7.0)
ax.set_xlabel('Component prevalence among confirmed-tier countries (%)',fontsize=7.5,labelpad=4)
ax.set_ylim(YLIM_B,YLIM_T); ax.set_yticks([])
for sp in ['top','right','left']: ax.spines[sp].set_visible(False)
ax.spines['bottom'].set_color('#AAAAAA'); ax.spines['bottom'].set_linewidth(0.6)
ax.tick_params(axis='x',length=2.5,width=0.5,pad=2,color='#AAAAAA')

# ── 범례 ─────────────────────────────────────────────────────────────────────
h1=patches.Patch(facecolor=C_IMPL,edgecolor='none',label='Component prevalence')
h2=mlines.Line2D([],[],marker='o',color=C_IMPL,markerfacecolor='white',
    markersize=5,linestyle='None',label='Excl. CHN/ARE (sensitivity)')
fig.legend(handles=[h1,h2],fontsize=6.5,ncol=2,
    loc='lower center',bbox_to_anchor=(L+(R-L)/2,0.010),
    bbox_transform=fig.transFigure,frameon=False,
    handlelength=1.1,handletextpad=0.5,borderpad=0,columnspacing=1.5)

# ── 제목 & 부제 ───────────────────────────────────────────────────────────────
fig.text(L,0.972,'Reporting visibility is common;',
    fontsize=9.2,fontweight='bold',color='#000',ha='left',va='top')
fig.text(L,0.928,'strategic alignment remains sparse',
    fontsize=9.2,fontweight='bold',color='#000',ha='left',va='top')
fig.text(L,0.882,'CEIS component prevalence among 25 confirmed-tier countries',
    fontsize=7.0,color='#444',ha='left',va='top')
fig.text(L,0.848,'Components grouped by CEIS function, not numeric order',
    fontsize=5.8,color='#888',ha='left',va='top',style='italic')

# ── 저장 ─────────────────────────────────────────────────────────────────────
OUT=str(REPO / 'figures/Figure3'); os.makedirs(OUT,exist_ok=True)
BASE=f'{OUT}/Figure3_DCAI_CEISComponents_REPRODUCED'
fig.savefig(f'{BASE}.pdf',bbox_inches='tight')
fig.savefig(f'{BASE}.png',dpi=300,bbox_inches='tight')
plt.close()

from PIL import Image
img=Image.open(f'{BASE}.png')
w=img.size[0]/300*25.4; h=img.size[1]/300*25.4
print(f"PNG: {w:.1f}x{h:.1f}mm")
