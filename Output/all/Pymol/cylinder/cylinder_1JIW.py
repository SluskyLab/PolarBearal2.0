from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1JIW.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("group", "resi 13+13+14+15+16+17+18+19+25+26+27+28+29+30+31+32+33+34+35+40+41+42+43+44+45+60+61+62+63+64+67+68+69+70+71+77+78+79+80+81+82+83+84+85+88+89+90+91+92+98+99+100+101+102+103 & chain I")
cmd.load_cgo( [9.0, 49.06276,36.19438,-20.987715, 48.572723, 62.832542, -42.93895, 2.5, 1,1,0,1,1,0], "cylinder2" )
cmd.color ("red", "Group")


cmd.show("cartoon", "group")
