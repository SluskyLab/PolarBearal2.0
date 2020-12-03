from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1QTT.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 14+15+16 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 22+23+24+25 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 29+30+31+32+33+34+35+36+37+38 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 41+42+43+44+45+46+47+48+49+50+51 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 98+99+100+101+102+103+104+105+106 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 85+86+87+88+91+92+93+94+95 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 78+79+80 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 70+71+72+73+74 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
