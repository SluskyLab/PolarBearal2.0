from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1JSG.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("group", "resi 8+8+9+10+91+92+93+94+95+96+97+98+99+100+84+85+86+75+76+77+78+17+18+19+20+21+22+25+26+27+28+34+35+36+37+38+39+40+41+42+46+47+48+49+50+51+52+53+103+104+105+106+107+108+109+110+111 & chain A")
cmd.load_cgo( [9.0, -0.18746185,8.045491,39.774918, 38.052143, 16.130867, 39.77501, 2.5, 1,1,0,1,1,0], "cylinder2" )
cmd.color ("red", "Group")


cmd.show("cartoon", "group")
