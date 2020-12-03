from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2YNK.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 26-27 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 52-56 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 92-99 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 115-127 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 130-142 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 156-161 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 164-170 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 174-175 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 193-199 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 216-224 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 235-246 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 249-259 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 289-299 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 308-320 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 323-338 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 343-352 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 374-375 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 378-379 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("Astrand18", "resi 389-398 & chain A ")
cmd.color ("red", "Astrand18")


cmd.select("Astrand19", "resi 404-414 & chain A ")
cmd.color ("green", "Astrand19")


cmd.select("Astrand20", "resi 429-443 & chain A ")
cmd.color ("orange", "Astrand20")


cmd.select("Astrand21", "resi 446-456 & chain A ")
cmd.color ("teal", "Astrand21")


cmd.select("Astrand22", "resi 465-475 & chain A ")
cmd.color ("yellow", "Astrand22")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
