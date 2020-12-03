from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1AVG.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("group", "resi 24+24+25+26+27+28+51+52+53+54+55+56+37+38+39+40+41+42+43+66+67+68+69+70+71+80+81+82+83+84+85+86+92+93+94+95+96+97+98+99+100+101+106+107+108+109+110+111+112+113+114+115+122+123+124+125+126+127+128 & chain I")
cmd.load_cgo( [9.0, -13.001044,44.937492,99.01785, 6.1281824, 21.02961, 84.79611, 2.5, 1,1,0,1,1,0], "cylinder2" )
cmd.color ("red", "Group")


cmd.show("cartoon", "group")
