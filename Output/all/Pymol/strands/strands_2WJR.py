from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2WJR.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 3-10 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 15-25 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 30-41 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 54-61 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 69-80 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 83-97 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 100-111 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 115-116 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 122-123 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 127-137 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 142-153 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 165-175 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 181-189 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 194-196 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 199-202 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 205-213 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
