from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2JOZ.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("group", "resi 19+19+20+21+22+35+36+37+38+39+40+44+45+46+47+48+49+50+51+55+56+57+58+62+63+64+65+66+67+68+74+75+76+77+78+79+80+87+88+89+90+91+92+98+99+100+101+102+105+106+107+108+109+110+111 & chain A")
cmd.load_cgo( [9.0, 13.48598,-14.487072,-6.9775553, -11.629203, 18.539516, 4.0467033, 2.5, 1,1,0,1,1,0], "cylinder2" )
cmd.color ("red", "Group")


cmd.show("cartoon", "group")
