from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5DL7.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 7-21 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 31-43 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 51-64 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 90-102 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 105-112 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 115-116 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 119-120 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 130-138 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 144-155 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 166-167 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 178-179 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 183-191 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 195-204 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 208-220 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 225-238 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 248-260 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 263-273 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 303-312 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("Astrand18", "resi 317-318 & chain A ")
cmd.color ("red", "Astrand18")


cmd.select("Astrand19", "resi 321-322 & chain A ")
cmd.color ("green", "Astrand19")


cmd.select("Astrand20", "resi 326-338 & chain A ")
cmd.color ("orange", "Astrand20")


cmd.select("Astrand21", "resi 348-360 & chain A ")
cmd.color ("teal", "Astrand21")


cmd.select("Astrand22", "resi 369-380 & chain A ")
cmd.color ("yellow", "Astrand22")


cmd.select("Astrand23", "resi 391-403 & chain A ")
cmd.color ("blue", "Astrand23")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
