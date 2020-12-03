from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4ES7.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("group", "resi 16+16+17+18+19+20+21+22+23+24+25+40+41+42+43+44+45+46+52+53+54+55+56+57+58+59+60+61+64+65+66+67+68+69+70+71+72+73+74+80+81+82+83+84+85+90+91+92+93+94+95+96+97+98+99+104+105+106+107+108+109+110+111+112+113+119+120+121+122+123+124+125+126+153+154+155 & chain A")
cmd.load_cgo( [9.0, -0.097709656,-10.226349,-26.676098, 26.595896, -5.8706384, 8.37407, 2.5, 1,1,0,1,1,0], "cylinder2" )
cmd.color ("red", "Group")


cmd.show("cartoon", "group")
