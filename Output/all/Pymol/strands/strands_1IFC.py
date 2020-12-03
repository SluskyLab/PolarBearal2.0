from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1IFC.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 2-12 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 34-42 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 47-52 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 57-62 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 67-71 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 76-84 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 89-94 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 100-108 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 113-118 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 123-130 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
