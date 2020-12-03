from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1LFO.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 6-8 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 11-13 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 35-44 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 47-54 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 57-64 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 67-73 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 78-86 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 90-95 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 98-105 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 108-115 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 118-125 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
