from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1LKE.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 24-31 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 41-50 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 53-62 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 65-75 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 83-90 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 93-104 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 109-116 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 125-132 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 161-162 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
