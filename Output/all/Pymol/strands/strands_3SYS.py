from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3SYS.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 10-23 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 34-46 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 55-68 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 91-103 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 106-113 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 116-117 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 120-121 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 131-139 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 145-156 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 166-168 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 171-176 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 179-188 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 193-202 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 206-219 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 222-235 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 245-257 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 260-271 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 301-310 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("Astrand18", "resi 319-331 & chain A ")
cmd.color ("red", "Astrand18")


cmd.select("Astrand19", "resi 339-351 & chain A ")
cmd.color ("green", "Astrand19")


cmd.select("Astrand20", "resi 361-371 & chain A ")
cmd.color ("orange", "Astrand20")


cmd.select("Astrand21", "resi 377-389 & chain A ")
cmd.color ("teal", "Astrand21")


cmd.select("Bstrand22", "resi 10-24 & chain B ")
cmd.color ("yellow", "Bstrand22")


cmd.select("Bstrand23", "resi 34-46 & chain B ")
cmd.color ("blue", "Bstrand23")


cmd.select("Bstrand24", "resi 54-67 & chain B ")
cmd.color ("red", "Bstrand24")


cmd.select("Bstrand25", "resi 91-103 & chain B ")
cmd.color ("green", "Bstrand25")


cmd.select("Bstrand26", "resi 106-113 & chain B ")
cmd.color ("orange", "Bstrand26")


cmd.select("Bstrand27", "resi 116-117 & chain B ")
cmd.color ("teal", "Bstrand27")


cmd.select("Bstrand28", "resi 120-121 & chain B ")
cmd.color ("yellow", "Bstrand28")


cmd.select("Bstrand29", "resi 131-139 & chain B ")
cmd.color ("blue", "Bstrand29")


cmd.select("Bstrand30", "resi 145-156 & chain B ")
cmd.color ("red", "Bstrand30")


cmd.select("Bstrand31", "resi 167-168 & chain B ")
cmd.color ("green", "Bstrand31")


cmd.select("Bstrand32", "resi 171-175 & chain B ")
cmd.color ("orange", "Bstrand32")


cmd.select("Bstrand33", "resi 179-188 & chain B ")
cmd.color ("teal", "Bstrand33")


cmd.select("Bstrand34", "resi 193-202 & chain B ")
cmd.color ("yellow", "Bstrand34")


cmd.select("Bstrand35", "resi 206-219 & chain B ")
cmd.color ("blue", "Bstrand35")


cmd.select("Bstrand36", "resi 222-235 & chain B ")
cmd.color ("red", "Bstrand36")


cmd.select("Bstrand37", "resi 245-257 & chain B ")
cmd.color ("green", "Bstrand37")


cmd.select("Bstrand38", "resi 260-271 & chain B ")
cmd.color ("orange", "Bstrand38")


cmd.select("Bstrand39", "resi 301-310 & chain B ")
cmd.color ("teal", "Bstrand39")


cmd.select("Bstrand40", "resi 319-333 & chain B ")
cmd.color ("yellow", "Bstrand40")


cmd.select("Bstrand41", "resi 336-351 & chain B ")
cmd.color ("blue", "Bstrand41")


cmd.select("Bstrand42", "resi 361-371 & chain B ")
cmd.color ("red", "Bstrand42")


cmd.select("Bstrand43", "resi 377-389 & chain B ")
cmd.color ("green", "Bstrand43")


cmd.select("barrel", "Astrand* or Bstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
