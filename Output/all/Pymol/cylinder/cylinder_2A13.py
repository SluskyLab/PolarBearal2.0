from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2A13.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("group", "resi 28+28+29+30+31+32+33+34+35+36+37+38+41+42+43+44+45+46+47+48+49+50+51+52+53+60+61+62+63+64+65+66+67+74+75+76+77+78+79+80+81+82+83+84+89+90+91+92+93+94+95+96+101+102+103+104+105+106+107+108+109+114+115+116+117+118+119+120+121+122+123+128+129+130+131+132+133+134+135+136+137+138+141+142+143+144+145+146+147+148+149+150+156+157+158+159+160+161+162+163+164+165 & chain A")
cmd.load_cgo( [9.0, -1.121995,61.331997,31.17415, 19.298054, 80.86963, -2.679041, 2.5, 1,1,0,1,1,0], "cylinder2" )
cmd.color ("red", "Group")


cmd.show("cartoon", "group")
