from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1R0U.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 2-2 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 5-17 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 20-35 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 38-47 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 52-59 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 62-68 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 71-78 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 81-89 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 92-108 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 111-121 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 129-137 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
