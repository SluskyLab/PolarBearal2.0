from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5FP2.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 33-34 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 37-41 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 64-66 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 81-83 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 91-95 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 98-99 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 128-135 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 149-155 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 163-173 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 181-191 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 196-207 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 232-246 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 249-261 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 289-303 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 306-320 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 342-358 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 364-378 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 405-422 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("Astrand18", "resi 425-436 & chain A ")
cmd.color ("red", "Astrand18")


cmd.select("Astrand19", "resi 440-452 & chain A ")
cmd.color ("green", "Astrand19")


cmd.select("Astrand20", "resi 457-468 & chain A ")
cmd.color ("orange", "Astrand20")


cmd.select("Astrand21", "resi 480-481 & chain A ")
cmd.color ("teal", "Astrand21")


cmd.select("Astrand22", "resi 499-500 & chain A ")
cmd.color ("yellow", "Astrand22")


cmd.select("Astrand23", "resi 508-521 & chain A ")
cmd.color ("blue", "Astrand23")


cmd.select("Astrand24", "resi 524-535 & chain A ")
cmd.color ("red", "Astrand24")


cmd.select("Astrand25", "resi 539-540 & chain A ")
cmd.color ("green", "Astrand25")


cmd.select("Astrand26", "resi 556-560 & chain A ")
cmd.color ("orange", "Astrand26")


cmd.select("Astrand27", "resi 564-578 & chain A ")
cmd.color ("teal", "Astrand27")


cmd.select("Astrand28", "resi 581-592 & chain A ")
cmd.color ("yellow", "Astrand28")


cmd.select("Astrand29", "resi 607-616 & chain A ")
cmd.color ("blue", "Astrand29")


cmd.select("Astrand30", "resi 622-631 & chain A ")
cmd.color ("red", "Astrand30")


cmd.select("Astrand31", "resi 656-666 & chain A ")
cmd.color ("green", "Astrand31")


cmd.select("Astrand32", "resi 671-678 & chain A ")
cmd.color ("orange", "Astrand32")


cmd.select("Astrand33", "resi 705-713 & chain A ")
cmd.color ("teal", "Astrand33")


cmd.select("Bstrand34", "resi 33-34 & chain B ")
cmd.color ("yellow", "Bstrand34")


cmd.select("Bstrand35", "resi 37-41 & chain B ")
cmd.color ("blue", "Bstrand35")


cmd.select("Bstrand36", "resi 64-66 & chain B ")
cmd.color ("red", "Bstrand36")


cmd.select("Bstrand37", "resi 81-83 & chain B ")
cmd.color ("green", "Bstrand37")


cmd.select("Bstrand38", "resi 91-95 & chain B ")
cmd.color ("orange", "Bstrand38")


cmd.select("Bstrand39", "resi 98-99 & chain B ")
cmd.color ("teal", "Bstrand39")


cmd.select("Bstrand40", "resi 128-135 & chain B ")
cmd.color ("yellow", "Bstrand40")


cmd.select("Bstrand41", "resi 149-155 & chain B ")
cmd.color ("blue", "Bstrand41")


cmd.select("Bstrand42", "resi 163-173 & chain B ")
cmd.color ("red", "Bstrand42")


cmd.select("Bstrand43", "resi 181-191 & chain B ")
cmd.color ("green", "Bstrand43")


cmd.select("Bstrand44", "resi 196-207 & chain B ")
cmd.color ("orange", "Bstrand44")


cmd.select("Bstrand45", "resi 232-246 & chain B ")
cmd.color ("teal", "Bstrand45")


cmd.select("Bstrand46", "resi 249-261 & chain B ")
cmd.color ("yellow", "Bstrand46")


cmd.select("Bstrand47", "resi 289-303 & chain B ")
cmd.color ("blue", "Bstrand47")


cmd.select("Bstrand48", "resi 306-321 & chain B ")
cmd.color ("red", "Bstrand48")


cmd.select("Bstrand49", "resi 341-358 & chain B ")
cmd.color ("green", "Bstrand49")


cmd.select("Bstrand50", "resi 363-378 & chain B ")
cmd.color ("orange", "Bstrand50")


cmd.select("Bstrand51", "resi 405-422 & chain B ")
cmd.color ("teal", "Bstrand51")


cmd.select("Bstrand52", "resi 425-436 & chain B ")
cmd.color ("yellow", "Bstrand52")


cmd.select("Bstrand53", "resi 440-452 & chain B ")
cmd.color ("blue", "Bstrand53")


cmd.select("Bstrand54", "resi 457-468 & chain B ")
cmd.color ("red", "Bstrand54")


cmd.select("Bstrand55", "resi 497-500 & chain B ")
cmd.color ("green", "Bstrand55")


cmd.select("Bstrand56", "resi 508-521 & chain B ")
cmd.color ("orange", "Bstrand56")


cmd.select("Bstrand57", "resi 524-535 & chain B ")
cmd.color ("teal", "Bstrand57")


cmd.select("Bstrand58", "resi 539-540 & chain B ")
cmd.color ("yellow", "Bstrand58")


cmd.select("Bstrand59", "resi 545-547 & chain B ")
cmd.color ("blue", "Bstrand59")


cmd.select("Bstrand60", "resi 554-560 & chain B ")
cmd.color ("red", "Bstrand60")


cmd.select("Bstrand61", "resi 564-578 & chain B ")
cmd.color ("green", "Bstrand61")


cmd.select("Bstrand62", "resi 581-591 & chain B ")
cmd.color ("orange", "Bstrand62")


cmd.select("Bstrand63", "resi 607-617 & chain B ")
cmd.color ("teal", "Bstrand63")


cmd.select("Bstrand64", "resi 622-631 & chain B ")
cmd.color ("yellow", "Bstrand64")


cmd.select("Bstrand65", "resi 656-666 & chain B ")
cmd.color ("blue", "Bstrand65")


cmd.select("Bstrand66", "resi 671-678 & chain B ")
cmd.color ("red", "Bstrand66")


cmd.select("Bstrand67", "resi 705-713 & chain B ")
cmd.color ("green", "Bstrand67")


cmd.select("barrel", "Astrand* or Bstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
