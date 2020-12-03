from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2HZQ.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 4-5 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 24-31 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 40-48 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 54-61 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 67-76 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 84-88 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 96-103 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 108-116 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 121-130 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 158-159 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
