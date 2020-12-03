from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4FSP.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 8-22 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 31-43 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 51-64 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 89-100 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 103-110 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 118-119 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 129-136 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 142-152 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 163-164 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 177-178 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 181-191 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 194-203 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 207-219 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 224-236 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 246-257 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 262-272 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 283-284 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 302-311 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("Astrand18", "resi 320-330 & chain A ")
cmd.color ("red", "Astrand18")


cmd.select("Astrand19", "resi 342-352 & chain A ")
cmd.color ("green", "Astrand19")


cmd.select("Astrand20", "resi 362-372 & chain A ")
cmd.color ("orange", "Astrand20")


cmd.select("Astrand21", "resi 378-390 & chain A ")
cmd.color ("teal", "Astrand21")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
