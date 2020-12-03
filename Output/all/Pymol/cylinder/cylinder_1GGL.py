from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1GGL.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("group", "resi 6+6+7+8+9+10+11+12+13+14+39+40+41+42+43+44+48+49+50+51+52+53+54+60+61+62+63+64+65+124+125+126+127+128+129+130+131+132+114+115+116+117+118+119+120+121+105+106+107+108+109+110+111+93+94+95+96+97+98+81+82+83+84+85+86+87+88+70+71+72+73 & chain A")
cmd.load_cgo( [9.0, 28.760967,11.81255,-5.212228, 18.68766, 33.988766, 22.597427, 2.5, 1,1,0,1,1,0], "cylinder2" )
cmd.color ("red", "Group")


cmd.show("cartoon", "group")
