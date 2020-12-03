from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2FHL.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("group", "resi 8+8+9+10+11+12+17+18+19+20+28+29+30+31+32+33+34+47+48+49+50+51+52+53+61+62+63+64+65+66+67+74+75+76+77+78+79+80+81+82+83+89+90+91+92+93+94+95+96+97+98+111+112+113+114+115+116+117+118+119+120 & chain A")
cmd.load_cgo( [9.0, -0.2618122,43.80449,18.505629, 34.94258, 57.424377, 13.835505, 2.5, 1,1,0,1,1,0], "cylinder2" )
cmd.color ("red", "Group")


cmd.show("cartoon", "group")
