from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3SZV.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 7-21 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 32-42 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 50-64 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 89-100 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 103-110 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 128-139 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 142-153 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 163-165 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 169-172 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 175-183 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 188-197 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 201-213 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 219-231 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 239-251 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 254-264 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 294-303 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 312-326 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 329-344 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("Astrand18", "resi 354-364 & chain A ")
cmd.color ("red", "Astrand18")


cmd.select("Astrand19", "resi 370-383 & chain A ")
cmd.color ("green", "Astrand19")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
