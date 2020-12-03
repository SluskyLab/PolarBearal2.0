from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4FRX.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 11-22 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 31-44 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 53-65 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 96-108 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 111-118 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 121-122 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 125-126 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 136-144 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 150-161 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 168-170 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 189-197 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 202-211 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 215-228 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 231-244 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 260-261 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 270-271 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 274-286 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 289-299 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("Astrand18", "resi 334-343 & chain A ")
cmd.color ("red", "Astrand18")


cmd.select("Astrand19", "resi 352-364 & chain A ")
cmd.color ("green", "Astrand19")


cmd.select("Astrand20", "resi 371-383 & chain A ")
cmd.color ("orange", "Astrand20")


cmd.select("Astrand21", "resi 393-428 & chain A ")
cmd.color ("teal", "Astrand21")


cmd.select("Bstrand22", "resi 8-22 & chain B ")
cmd.color ("yellow", "Bstrand22")


cmd.select("Bstrand23", "resi 31-44 & chain B ")
cmd.color ("blue", "Bstrand23")


cmd.select("Bstrand24", "resi 53-65 & chain B ")
cmd.color ("red", "Bstrand24")


cmd.select("Bstrand25", "resi 96-108 & chain B ")
cmd.color ("green", "Bstrand25")


cmd.select("Bstrand26", "resi 111-118 & chain B ")
cmd.color ("orange", "Bstrand26")


cmd.select("Bstrand27", "resi 121-122 & chain B ")
cmd.color ("teal", "Bstrand27")


cmd.select("Bstrand28", "resi 125-126 & chain B ")
cmd.color ("yellow", "Bstrand28")


cmd.select("Bstrand29", "resi 136-144 & chain B ")
cmd.color ("blue", "Bstrand29")


cmd.select("Bstrand30", "resi 150-161 & chain B ")
cmd.color ("red", "Bstrand30")


cmd.select("Bstrand31", "resi 168-170 & chain B ")
cmd.color ("green", "Bstrand31")


cmd.select("Bstrand32", "resi 189-197 & chain B ")
cmd.color ("orange", "Bstrand32")


cmd.select("Bstrand33", "resi 202-211 & chain B ")
cmd.color ("teal", "Bstrand33")


cmd.select("Bstrand34", "resi 215-228 & chain B ")
cmd.color ("yellow", "Bstrand34")


cmd.select("Bstrand35", "resi 231-244 & chain B ")
cmd.color ("blue", "Bstrand35")


cmd.select("Bstrand36", "resi 260-261 & chain B ")
cmd.color ("red", "Bstrand36")


cmd.select("Bstrand37", "resi 270-271 & chain B ")
cmd.color ("green", "Bstrand37")


cmd.select("Bstrand38", "resi 274-286 & chain B ")
cmd.color ("orange", "Bstrand38")


cmd.select("Bstrand39", "resi 289-299 & chain B ")
cmd.color ("teal", "Bstrand39")


cmd.select("Bstrand40", "resi 334-343 & chain B ")
cmd.color ("yellow", "Bstrand40")


cmd.select("Bstrand41", "resi 352-364 & chain B ")
cmd.color ("blue", "Bstrand41")


cmd.select("Bstrand42", "resi 371-383 & chain B ")
cmd.color ("red", "Bstrand42")


cmd.select("Bstrand43", "resi 393-429 & chain B ")
cmd.color ("green", "Bstrand43")


cmd.select("barrel", "Astrand* or Bstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
