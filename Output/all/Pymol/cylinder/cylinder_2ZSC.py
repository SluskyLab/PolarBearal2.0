from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2ZSC.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("group", "resi 10+10+11+12+13+14+19+20+21+22+23+24+29+30+31+32+33+34+35+45+46+47+48+49+50+51+61+62+63+64+65+66+67+68+69+70+75+76+77+78+79+80+81+82+83+84+85+91+92+93+94+95+96+97+98+99+100+111+112+113+114+115+116+117+118+119 & chain A")
cmd.load_cgo( [9.0, -8.670327,42.121643,6.9739466, 13.205865, 10.989679, 6.973961, 2.5, 1,1,0,1,1,0], "cylinder2" )
cmd.color ("red", "Group")


cmd.show("cartoon", "group")
