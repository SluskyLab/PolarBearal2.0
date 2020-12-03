from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5LDV.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 13-28 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 42-58 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 61-73 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 89-99 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 104-112 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 126-134 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 140-150 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 164-167 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 170-174 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 184-194 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 198-209 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 213-224 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 231-243 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 256-267 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 270-286 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 316-331 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 335-347 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 357-369 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("Astrand18", "resi 374-385 & chain A ")
cmd.color ("red", "Astrand18")


cmd.select("Astrand19", "resi 395-407 & chain A ")
cmd.color ("green", "Astrand19")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
