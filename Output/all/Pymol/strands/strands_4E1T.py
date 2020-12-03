from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4E1T.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 148-148 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 151-159 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 163-163 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 166-173 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 176-178 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 181-192 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 195-208 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 211-221 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 227-238 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 241-249 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 252-257 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 260-260 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 263-279 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 282-282 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 285-295 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 298-299 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 308-308 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 312-323 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("Astrand18", "resi 326-335 & chain A ")
cmd.color ("red", "Astrand18")


cmd.select("Astrand19", "resi 340-351 & chain A ")
cmd.color ("green", "Astrand19")


cmd.select("Astrand20", "resi 361-361 & chain A ")
cmd.color ("orange", "Astrand20")


cmd.select("Astrand21", "resi 370-370 & chain A ")
cmd.color ("teal", "Astrand21")


cmd.select("Astrand22", "resi 380-389 & chain A ")
cmd.color ("yellow", "Astrand22")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
