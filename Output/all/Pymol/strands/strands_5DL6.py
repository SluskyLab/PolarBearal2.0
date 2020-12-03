from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5DL6.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 8-21 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 31-43 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 52-66 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 89-101 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 104-111 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 129-137 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 143-154 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 161-163 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 181-191 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 194-203 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 207-219 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 224-235 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 248-259 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 262-272 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 302-311 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 319-333 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 338-354 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 362-373 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("Astrand18", "resi 384-397 & chain A ")
cmd.color ("red", "Astrand18")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
