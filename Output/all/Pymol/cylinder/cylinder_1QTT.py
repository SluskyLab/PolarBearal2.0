from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1QTT.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("group", "resi 14+14+15+16+22+23+24+25+29+30+31+32+33+34+35+36+37+38+41+42+43+44+45+46+47+48+49+50+51+70+71+72+73+74+78+79+80+85+86+87+88+98+99+100+101+102+103+104+105+106+91+92+93+94+95 & chain A")
cmd.load_cgo( [9.0, 2.8566911,-1.2842954,3.2266111, 4.6976423, -1.284223, -32.156834, 2.5, 1,1,0,1,1,0], "cylinder2" )
cmd.color ("red", "Group")


cmd.show("cartoon", "group")
