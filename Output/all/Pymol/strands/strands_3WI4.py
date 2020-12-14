from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3WI4.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 3-21 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 26-29 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 32-37 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 41-51 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 54-63 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 78-84 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 87-95 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 125-132 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 139-146 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 158-167 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 170-181 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 190-204 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 207-220 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 227-238 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 247-253 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 267-277 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 282-293 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 300-312 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
