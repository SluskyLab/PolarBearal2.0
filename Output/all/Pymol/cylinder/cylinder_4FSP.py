from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4FSP.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("group", "resi 8+8+9+10+11+12+13+14+15+16+17+18+19+20+21+22+31+32+33+34+35+36+37+38+39+40+41+42+43+51+52+53+54+55+56+57+58+59+60+61+62+63+64+89+90+91+92+93+94+95+96+97+98+99+100+103+104+105+106+107+108+109+110+129+130+131+132+133+134+135+136+142+143+144+145+146+147+148+149+150+151+152+181+182+183+184+185+186+187+188+189+190+191+194+195+196+197+198+199+200+201+202+203+207+208+209+210+211+212+213+214+215+216+217+218+219+224+225+226+227+228+229+230+231+232+233+234+235+236+246+247+248+249+250+251+252+253+254+255+256+257+262+263+264+265+266+267+268+269+270+271+272+302+303+304+305+306+307+308+309+310+311+320+321+322+323+324+325+326+327+328+329+330+342+343+344+345+346+347+348+349+350+351+352+362+363+364+365+366+367+368+369+370+371+372+378+379+380+381+382+383+384+385+386+387+388+389+390 & chain A")
cmd.load_cgo( [9.0, -37.05808,39.168953,-30.171747, -18.980423, 8.421192, 24.99195, 2.5, 1,1,0,1,1,0], "cylinder2" )
cmd.color ("red", "Group")


cmd.show("cartoon", "group")