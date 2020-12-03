from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/6EHD.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 2-6 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 9-24 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 30-31 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 37-47 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 50-59 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 67-77 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 80-88 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 117-128 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 131-138 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 147-157 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 160-181 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 184-205 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 208-221 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 227-242 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 245-258 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 263-278 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 281-299 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 304-324 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
