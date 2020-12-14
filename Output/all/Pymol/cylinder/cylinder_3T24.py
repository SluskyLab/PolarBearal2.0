from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3T24.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("group", "resi 7+7+8+9+10+11+12+13+14+15+16+17+18+19+20+21+22+23+26+27+28+29+30+31+32+33+34+35+36+37+38+39+40+41+42+43+58+59+60+61+62+63+64+65+66+89+90+91+92+93+94+95+96+97+98+99+100+101+104+105+106+107+108+109+110+111+129+130+131+132+133+134+135+136+137+150+151+152+153+154+155+156+157+158+159+160+161+185+186+187+188+189+190+191+192+193+194+195+198+199+200+201+202+203+204+205+206+207+211+212+213+214+215+216+217+218+219+220+221+222+223+224+225+228+229+230+231+232+233+234+235+236+237+238+239+240+241+242+243+244+245+246+247+248+249+250+251+252+253+254+255+256+257+258+259+260+263+264+265+266+267+268+269+270+271+272+273+303+304+305+306+307+308+309+310+311+312+321+322+323+324+325+326+327+328+329+330+331+332+333+334+341+342+343+344+345+346+347+348+349+350+351+352+353+354+364+365+366+367+368+369+370+371+372+373+374+379+380+381+382+383+384+385+386+387+388+389+390+391+392 & chain A")
cmd.load_cgo( [9.0, 30.405222,-3.1159725,-39.107136, -33.47607, 6.102418, -30.10413, 2.5, 1,1,0,1,1,0], "cylinder2" )
cmd.color ("red", "Group")


cmd.show("cartoon", "group")