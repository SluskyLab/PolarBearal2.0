from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1A1X.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("group", "resi 13+13+14+15+16+17+18+21+22+23+24+29+30+31+32+33+34+35+36+41+42+43+44+45+46+97+98+99+100+101+102+103+104+85+86+87+88+89+90+91+92+93+94+77+78+79+80+69+70+71+72+73 & chain A")
cmd.load_cgo( [9.0, 21.453518,30.923023,32.302795, 9.332915, 48.50239, 57.66046, 2.5, 1,1,0,1,1,0], "cylinder2" )
cmd.color ("red", "Group")


cmd.show("cartoon", "group")
