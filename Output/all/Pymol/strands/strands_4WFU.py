from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4WFU.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 7-8 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 14-25 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 36-38 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 41-45 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 50-59 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 62-71 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 74-74 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 77-82 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 85-94 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 97-105 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 109-119 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 140-140 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 146-147 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 152-152 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
