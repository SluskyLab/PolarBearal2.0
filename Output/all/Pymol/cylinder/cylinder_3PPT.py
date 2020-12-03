from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3PPT.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("group", "resi 7+7+8+9+10+11+12+13+14+15+40+41+42+43+44+45+46+49+50+51+52+53+54+55+60+61+62+63+64+65+66+122+123+124+125+126+127+128+129+130+131+112+113+114+115+116+117+118+119+102+103+104+105+106+107+108+109+91+92+93+94+95+96+97+80+81+82+83+84+85+86+87+88+71+72+73+74 & chain A")
cmd.load_cgo( [9.0, 20.534185,48.442085,-19.15204, 19.610315, 48.442017, 18.620802, 2.5, 1,1,0,1,1,0], "cylinder2" )
cmd.color ("red", "Group")


cmd.show("cartoon", "group")
