from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4BJ8.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("group", "resi 10+10+11+12+13+14+19+20+21+22+23+24+25+28+29+30+31+32+33+34+49+50+51+52+53+54+55+56+63+64+65+66+67+68+69+75+76+77+78+79+80+81+82+83+84+90+91+92+93+94+95+96+97+98+99+112+113+114+115+116+117+118+119+120+121 & chain A")
cmd.load_cgo( [9.0, 179.7954,24.030504,25.515156, 194.6892, 47.179657, -1.8531866, 2.5, 1,1,0,1,1,0], "cylinder2" )
cmd.color ("red", "Group")


cmd.show("cartoon", "group")
