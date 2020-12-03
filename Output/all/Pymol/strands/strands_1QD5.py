from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1QD5.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 33-34 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 39-45 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 65-79 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 86-98 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 109-128 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 131-144 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 154-166 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 169-173 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 176-178 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 197-203 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 206-214 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 221-230 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 236-245 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 255-264 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
