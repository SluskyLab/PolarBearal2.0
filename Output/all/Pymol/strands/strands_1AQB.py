from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1AQB.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 22-30 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 39-48 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 52-63 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 67-78 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 85-92 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 99-110 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 114-124 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 129-139 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
