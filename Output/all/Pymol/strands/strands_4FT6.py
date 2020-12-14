from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4FT6.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 8-22 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 31-44 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 52-67 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 89-101 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 104-111 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 114-115 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 118-119 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 129-137 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 143-154 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 162-163 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 177-186 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 191-200 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 204-217 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 220-233 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 243-255 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 258-268 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 298-307 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 316-328 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("Astrand18", "resi 336-348 & chain A ")
cmd.color ("red", "Astrand18")


cmd.select("Astrand19", "resi 358-368 & chain A ")
cmd.color ("green", "Astrand19")


cmd.select("Astrand20", "resi 374-386 & chain A ")
cmd.color ("orange", "Astrand20")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
