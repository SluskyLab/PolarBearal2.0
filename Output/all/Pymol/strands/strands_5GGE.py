from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5GGE.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 7-14 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 39-45 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 48-54 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 59-64 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 70-73 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 79-87 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 90-95 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 101-108 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 111-118 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 121-129 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
