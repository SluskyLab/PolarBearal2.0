from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3PPT.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 7-15 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 40-46 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 49-55 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 60-66 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 71-74 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 80-88 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 91-97 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 102-109 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 112-119 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 122-131 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
