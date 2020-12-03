from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1PBY.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 29-31 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 112-114 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 175-183 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 187-198 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 201-209 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 214-224 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 228-235 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 238-247 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 250-257 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 260-271 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 277-282 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 285-287 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 292-299 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 305-306 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 311-317 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 322-329 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 334-340 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 343-350 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("Astrand18", "resi 355-359 & chain A ")
cmd.color ("red", "Astrand18")


cmd.select("Astrand19", "resi 362-366 & chain A ")
cmd.color ("green", "Astrand19")


cmd.select("Astrand20", "resi 379-387 & chain A ")
cmd.color ("orange", "Astrand20")


cmd.select("Astrand21", "resi 400-405 & chain A ")
cmd.color ("teal", "Astrand21")


cmd.select("Astrand22", "resi 408-413 & chain A ")
cmd.color ("yellow", "Astrand22")


cmd.select("Astrand23", "resi 428-430 & chain A ")
cmd.color ("blue", "Astrand23")


cmd.select("Astrand24", "resi 435-438 & chain A ")
cmd.color ("red", "Astrand24")


cmd.select("Astrand25", "resi 455-462 & chain A ")
cmd.color ("green", "Astrand25")


cmd.select("Astrand26", "resi 471-479 & chain A ")
cmd.color ("orange", "Astrand26")


cmd.select("Bstrand27", "resi 2-8 & chain B ")
cmd.color ("teal", "Bstrand27")


cmd.select("Bstrand28", "resi 12-17 & chain B ")
cmd.color ("yellow", "Bstrand28")


cmd.select("Bstrand29", "resi 22-28 & chain B ")
cmd.color ("blue", "Bstrand29")


cmd.select("Bstrand30", "resi 39-41 & chain B ")
cmd.color ("red", "Bstrand30")


cmd.select("Bstrand31", "resi 47-52 & chain B ")
cmd.color ("green", "Bstrand31")


cmd.select("Bstrand32", "resi 57-62 & chain B ")
cmd.color ("orange", "Bstrand32")


cmd.select("Bstrand33", "resi 68-73 & chain B ")
cmd.color ("teal", "Bstrand33")


cmd.select("Bstrand34", "resi 79-82 & chain B ")
cmd.color ("yellow", "Bstrand34")


cmd.select("Bstrand35", "resi 87-89 & chain B ")
cmd.color ("blue", "Bstrand35")


cmd.select("Bstrand36", "resi 95-105 & chain B ")
cmd.color ("red", "Bstrand36")


cmd.select("Bstrand37", "resi 110-112 & chain B ")
cmd.color ("green", "Bstrand37")


cmd.select("Bstrand38", "resi 116-121 & chain B ")
cmd.color ("orange", "Bstrand38")


cmd.select("Bstrand39", "resi 126-132 & chain B ")
cmd.color ("teal", "Bstrand39")


cmd.select("Bstrand40", "resi 140-142 & chain B ")
cmd.color ("yellow", "Bstrand40")


cmd.select("Bstrand41", "resi 149-152 & chain B ")
cmd.color ("blue", "Bstrand41")


cmd.select("Bstrand42", "resi 156-160 & chain B ")
cmd.color ("red", "Bstrand42")


cmd.select("Bstrand43", "resi 165-170 & chain B ")
cmd.color ("green", "Bstrand43")


cmd.select("Bstrand44", "resi 197-205 & chain B ")
cmd.color ("orange", "Bstrand44")


cmd.select("Bstrand45", "resi 217-225 & chain B ")
cmd.color ("teal", "Bstrand45")


cmd.select("Bstrand46", "resi 231-238 & chain B ")
cmd.color ("yellow", "Bstrand46")


cmd.select("Bstrand47", "resi 245-248 & chain B ")
cmd.color ("blue", "Bstrand47")


cmd.select("Bstrand48", "resi 254-258 & chain B ")
cmd.color ("red", "Bstrand48")


cmd.select("Bstrand49", "resi 261-266 & chain B ")
cmd.color ("green", "Bstrand49")


cmd.select("Bstrand50", "resi 271-277 & chain B ")
cmd.color ("orange", "Bstrand50")


cmd.select("Bstrand51", "resi 284-287 & chain B ")
cmd.color ("teal", "Bstrand51")


cmd.select("Bstrand52", "resi 293-297 & chain B ")
cmd.color ("yellow", "Bstrand52")


cmd.select("Bstrand53", "resi 302-307 & chain B ")
cmd.color ("blue", "Bstrand53")


cmd.select("Bstrand54", "resi 313-318 & chain B ")
cmd.color ("red", "Bstrand54")


cmd.select("Bstrand55", "resi 331-334 & chain B ")
cmd.color ("green", "Bstrand55")


cmd.select("barrel", "Astrand* or Bstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
