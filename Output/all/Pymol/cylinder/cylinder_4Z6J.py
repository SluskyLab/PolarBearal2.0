from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4Z6J.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("group", "resi 18+18+19+20+21+22+27+28+29+30+31+32+33+34+41+42+43+44+45+46+47+48+49+61+62+63+64+65+66+67+68+69+74+75+76+77+78+79+80+81+82+87+88+89+90+91+92+93+94+95+96+97+98+99+106+107+108+109+110+111+112+113+114+115+116+117+120+121+122+123+124+125+126+127+128+129+130+131+132 & chain A")
cmd.load_cgo( [9.0, 39.14147,24.023956,19.238468, -12.50573, 24.023838, 19.238556, 2.5, 1,1,0,1,1,0], "cylinder2" )
cmd.color ("red", "Group")


cmd.show("cartoon", "group")
