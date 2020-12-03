from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2A0A.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("group", "resi 6+6+7+8+9+10+39+40+41+42+43+44+49+50+51+52+53+60+61+62+63+64+123+124+125+126+127+128+129+130+112+113+114+115+116+117+118+102+103+104+105+106+107+108+91+92+93+94+95+96+78+79+80+81+82+83+84+85+86+87+70+71+72+73+74 & chain A")
cmd.load_cgo( [9.0, 0.4972067,-3.376833,-20.146473, -0.6487379, 0.041301727, 15.98363, 2.5, 1,1,0,1,1,0], "cylinder2" )
cmd.color ("red", "Group")


cmd.show("cartoon", "group")
