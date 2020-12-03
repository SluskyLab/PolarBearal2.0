from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1T16.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 44-60 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 77-87 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 92-99 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 104-107 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 120-134 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 140-158 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 196-218 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 221-228 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 231-240 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 263-271 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 274-284 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 287-296 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 303-307 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 313-318 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 324-333 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 339-348 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 366-376 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 381-392 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("Astrand18", "resi 395-399 & chain A ")
cmd.color ("red", "Astrand18")


cmd.select("Astrand19", "resi 402-420 & chain A ")
cmd.color ("green", "Astrand19")


cmd.select("Bstrand20", "resi 44-60 & chain B ")
cmd.color ("orange", "Bstrand20")


cmd.select("Bstrand21", "resi 77-87 & chain B ")
cmd.color ("teal", "Bstrand21")


cmd.select("Bstrand22", "resi 92-99 & chain B ")
cmd.color ("yellow", "Bstrand22")


cmd.select("Bstrand23", "resi 104-107 & chain B ")
cmd.color ("blue", "Bstrand23")


cmd.select("Bstrand24", "resi 120-134 & chain B ")
cmd.color ("red", "Bstrand24")


cmd.select("Bstrand25", "resi 142-158 & chain B ")
cmd.color ("green", "Bstrand25")


cmd.select("Bstrand26", "resi 196-218 & chain B ")
cmd.color ("orange", "Bstrand26")


cmd.select("Bstrand27", "resi 221-228 & chain B ")
cmd.color ("teal", "Bstrand27")


cmd.select("Bstrand28", "resi 231-240 & chain B ")
cmd.color ("yellow", "Bstrand28")


cmd.select("Bstrand29", "resi 263-271 & chain B ")
cmd.color ("blue", "Bstrand29")


cmd.select("Bstrand30", "resi 274-282 & chain B ")
cmd.color ("red", "Bstrand30")


cmd.select("Bstrand31", "resi 287-296 & chain B ")
cmd.color ("green", "Bstrand31")


cmd.select("Bstrand32", "resi 303-308 & chain B ")
cmd.color ("orange", "Bstrand32")


cmd.select("Bstrand33", "resi 313-318 & chain B ")
cmd.color ("teal", "Bstrand33")


cmd.select("Bstrand34", "resi 324-333 & chain B ")
cmd.color ("yellow", "Bstrand34")


cmd.select("Bstrand35", "resi 339-348 & chain B ")
cmd.color ("blue", "Bstrand35")


cmd.select("Bstrand36", "resi 366-376 & chain B ")
cmd.color ("red", "Bstrand36")


cmd.select("Bstrand37", "resi 381-392 & chain B ")
cmd.color ("green", "Bstrand37")


cmd.select("Bstrand38", "resi 395-399 & chain B ")
cmd.color ("orange", "Bstrand38")


cmd.select("Bstrand39", "resi 402-420 & chain B ")
cmd.color ("teal", "Bstrand39")


cmd.select("barrel", "Astrand* or Bstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
