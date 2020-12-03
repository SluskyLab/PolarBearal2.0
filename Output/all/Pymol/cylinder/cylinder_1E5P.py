from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1E5P.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("group", "resi 7+7+8+9+10+11+12+13+14+15+16+17+18+19+35+36+37+38+39+44+45+46+47+48+49+50+51+52+53+30+31+32+56+57+58+59+60+61+62+63+64+65+66+67+71+72+73+74+75+76+79+80+81+82+83+91+92+93+94+95+96+97+98+99+100+86+87+88+105+106+107+108+109+110+111+112+113+140+141+142 & chain B")
cmd.load_cgo( [9.0, -25.856812,56.162636,36.85486, -57.24276, 60.783813, 7.3936996, 2.5, 1,1,0,1,1,0], "cylinder2" )
cmd.color ("red", "Group")


cmd.show("cartoon", "group")
