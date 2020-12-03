from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2A13.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 28-38 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 41-53 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 60-67 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 74-84 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 89-96 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 101-109 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 114-123 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 128-138 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 141-150 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 156-165 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
