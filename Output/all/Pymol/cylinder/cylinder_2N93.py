from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2N93.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("group", "resi 6+6+7+8+9+10+11+12+13+40+41+42+43+44+49+50+51+52+53+59+60+61+62+121+122+123+124+125+126+127+128+129+112+113+114+115+116+117+118+103+104+105+106+88+89+90+91+92+93+94+76+77+78+79+80+81+82+83+84+66+67+68+69+70+71 & chain A")
cmd.load_cgo( [9.0, 47.96447,40.449436,31.658096, 11.517748, 28.42838, 31.658123, 2.5, 1,1,0,1,1,0], "cylinder2" )
cmd.color ("red", "Group")


cmd.show("cartoon", "group")
