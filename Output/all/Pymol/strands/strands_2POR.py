from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2POR.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 2-15 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 18-35 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 39-46 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 59-65 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 68-74 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 118-125 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 128-135 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 148-158 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 161-171 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 181-192 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 195-206 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 227-240 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 243-254 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 258-271 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 275-285 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 292-300 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
