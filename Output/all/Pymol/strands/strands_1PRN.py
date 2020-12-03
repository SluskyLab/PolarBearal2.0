from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1PRN.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 2-16 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 25-41 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 45-56 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 69-75 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 78-84 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 131-139 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 142-150 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 163-172 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 175-183 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 193-201 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 206-214 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 222-245 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 252-261 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 265-274 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 278-288 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
