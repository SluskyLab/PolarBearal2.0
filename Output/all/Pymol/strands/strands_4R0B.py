from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4R0B.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 17-26 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 42-48 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 54-61 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 66-75 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 81-86 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 89-97 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 102-109 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 116-123 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 149-152 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
