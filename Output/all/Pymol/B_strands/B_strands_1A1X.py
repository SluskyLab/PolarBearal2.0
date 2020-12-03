from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1A1X.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 13+14+15+16+17+18 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 21+22+23+24 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 29+30+31+32+33+34+35+36 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 41+42+43+44+45+46 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 97+98+99+100+101+102+103+104 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 85+86+87+88+89+90+91+92+93+94 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 77+78+79+80 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 69+70+71+72+73 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
