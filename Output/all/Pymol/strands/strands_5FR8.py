from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5FR8.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 38-42 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 65-68 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 81-84 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 92-96 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 99-100 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 129-136 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 150-156 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 164-174 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 182-194 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 198-209 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 229-244 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 247-261 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 287-302 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 305-320 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 340-358 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 362-377 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 404-419 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 424-435 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("Astrand18", "resi 439-451 & chain A ")
cmd.color ("red", "Astrand18")


cmd.select("Astrand19", "resi 456-467 & chain A ")
cmd.color ("green", "Astrand19")


cmd.select("Astrand20", "resi 479-482 & chain A ")
cmd.color ("orange", "Astrand20")


cmd.select("Astrand21", "resi 495-498 & chain A ")
cmd.color ("teal", "Astrand21")


cmd.select("Astrand22", "resi 506-518 & chain A ")
cmd.color ("yellow", "Astrand22")


cmd.select("Astrand23", "resi 522-538 & chain A ")
cmd.color ("blue", "Astrand23")


cmd.select("Astrand24", "resi 545-550 & chain A ")
cmd.color ("red", "Astrand24")


cmd.select("Astrand25", "resi 561-588 & chain A ")
cmd.color ("green", "Astrand25")


cmd.select("Astrand26", "resi 591-605 & chain A ")
cmd.color ("orange", "Astrand26")


cmd.select("Astrand27", "resi 618-627 & chain A ")
cmd.color ("teal", "Astrand27")


cmd.select("Astrand28", "resi 632-641 & chain A ")
cmd.color ("yellow", "Astrand28")


cmd.select("Astrand29", "resi 644-645 & chain A ")
cmd.color ("blue", "Astrand29")


cmd.select("Astrand30", "resi 671-672 & chain A ")
cmd.color ("red", "Astrand30")


cmd.select("Astrand31", "resi 675-684 & chain A ")
cmd.color ("green", "Astrand31")


cmd.select("Astrand32", "resi 690-697 & chain A ")
cmd.color ("orange", "Astrand32")


cmd.select("Astrand33", "resi 721-728 & chain A ")
cmd.color ("teal", "Astrand33")


cmd.select("Bstrand34", "resi 38-42 & chain B ")
cmd.color ("yellow", "Bstrand34")


cmd.select("Bstrand35", "resi 65-68 & chain B ")
cmd.color ("blue", "Bstrand35")


cmd.select("Bstrand36", "resi 81-84 & chain B ")
cmd.color ("red", "Bstrand36")


cmd.select("Bstrand37", "resi 92-96 & chain B ")
cmd.color ("green", "Bstrand37")


cmd.select("Bstrand38", "resi 99-100 & chain B ")
cmd.color ("orange", "Bstrand38")


cmd.select("Bstrand39", "resi 129-136 & chain B ")
cmd.color ("teal", "Bstrand39")


cmd.select("Bstrand40", "resi 150-156 & chain B ")
cmd.color ("yellow", "Bstrand40")


cmd.select("Bstrand41", "resi 164-174 & chain B ")
cmd.color ("blue", "Bstrand41")


cmd.select("Bstrand42", "resi 182-194 & chain B ")
cmd.color ("red", "Bstrand42")


cmd.select("Bstrand43", "resi 198-209 & chain B ")
cmd.color ("green", "Bstrand43")


cmd.select("Bstrand44", "resi 229-244 & chain B ")
cmd.color ("orange", "Bstrand44")


cmd.select("Bstrand45", "resi 247-261 & chain B ")
cmd.color ("teal", "Bstrand45")


cmd.select("Bstrand46", "resi 287-302 & chain B ")
cmd.color ("yellow", "Bstrand46")


cmd.select("Bstrand47", "resi 305-320 & chain B ")
cmd.color ("blue", "Bstrand47")


cmd.select("Bstrand48", "resi 340-358 & chain B ")
cmd.color ("red", "Bstrand48")


cmd.select("Bstrand49", "resi 362-377 & chain B ")
cmd.color ("green", "Bstrand49")


cmd.select("Bstrand50", "resi 404-419 & chain B ")
cmd.color ("orange", "Bstrand50")


cmd.select("Bstrand51", "resi 424-435 & chain B ")
cmd.color ("teal", "Bstrand51")


cmd.select("Bstrand52", "resi 439-451 & chain B ")
cmd.color ("yellow", "Bstrand52")


cmd.select("Bstrand53", "resi 456-467 & chain B ")
cmd.color ("blue", "Bstrand53")


cmd.select("Bstrand54", "resi 479-482 & chain B ")
cmd.color ("red", "Bstrand54")


cmd.select("Bstrand55", "resi 495-498 & chain B ")
cmd.color ("green", "Bstrand55")


cmd.select("Bstrand56", "resi 506-518 & chain B ")
cmd.color ("orange", "Bstrand56")


cmd.select("Bstrand57", "resi 522-538 & chain B ")
cmd.color ("teal", "Bstrand57")


cmd.select("Bstrand58", "resi 545-550 & chain B ")
cmd.color ("yellow", "Bstrand58")


cmd.select("Bstrand59", "resi 561-588 & chain B ")
cmd.color ("blue", "Bstrand59")


cmd.select("Bstrand60", "resi 591-605 & chain B ")
cmd.color ("red", "Bstrand60")


cmd.select("Bstrand61", "resi 618-627 & chain B ")
cmd.color ("green", "Bstrand61")


cmd.select("Bstrand62", "resi 632-641 & chain B ")
cmd.color ("orange", "Bstrand62")


cmd.select("Bstrand63", "resi 644-645 & chain B ")
cmd.color ("teal", "Bstrand63")


cmd.select("Bstrand64", "resi 671-672 & chain B ")
cmd.color ("yellow", "Bstrand64")


cmd.select("Bstrand65", "resi 675-684 & chain B ")
cmd.color ("blue", "Bstrand65")


cmd.select("Bstrand66", "resi 690-697 & chain B ")
cmd.color ("red", "Bstrand66")


cmd.select("Bstrand67", "resi 721-729 & chain B ")
cmd.color ("green", "Bstrand67")


cmd.select("barrel", "Astrand* or Bstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
