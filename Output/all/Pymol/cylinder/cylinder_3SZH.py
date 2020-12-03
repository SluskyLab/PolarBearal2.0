from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3SZH.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("group", "resi 11+11+12+13+14+20+21+22+23+24+25+26+31+32+33+34+35+36+37+50+51+52+53+54+55+56+57+60+61+62+63+64+65+66+67+68+73+74+75+76+77+78+79+80+81+82+83+84+85+92+93+94+95+96+97+98+99+100+101+111+112+113+114+115+116+117+118+119 & chain A")
cmd.load_cgo( [9.0, 10.2351265,-4.4368052,-3.9636855, -23.623962, 5.3797603, -19.799448, 2.5, 1,1,0,1,1,0], "cylinder2" )
cmd.color ("red", "Group")


cmd.show("cartoon", "group")
