from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4RYS.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 12-22 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 25-36 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 41-48 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 92-100 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 105-115 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 118-128 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 148-155 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 160-170 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 176-187 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 199-208 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 217-227 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
