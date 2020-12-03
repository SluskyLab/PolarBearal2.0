from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2FR2.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 17-25 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 33-43 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 48-57 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 63-73 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 78-85 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 89-100 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 103-109 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 115-118 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 125-135 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 138-147 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 150-162 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
