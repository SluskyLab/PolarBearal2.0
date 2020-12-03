from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4ZGV.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 68-72 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 96-98 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 116-118 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 127-130 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 175-181 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 196-201 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 211-219 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 248-259 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 264-281 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 286-304 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 310-317 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 320-325 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 333-348 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 354-371 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 376-382 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 402-407 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 411-427 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 436-454 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("Astrand18", "resi 458-461 & chain A ")
cmd.color ("red", "Astrand18")


cmd.select("Astrand19", "resi 493-497 & chain A ")
cmd.color ("green", "Astrand19")


cmd.select("Astrand20", "resi 500-518 & chain A ")
cmd.color ("orange", "Astrand20")


cmd.select("Astrand21", "resi 522-533 & chain A ")
cmd.color ("teal", "Astrand21")


cmd.select("Astrand22", "resi 538-550 & chain A ")
cmd.color ("yellow", "Astrand22")


cmd.select("Astrand23", "resi 557-567 & chain A ")
cmd.color ("blue", "Astrand23")


cmd.select("Astrand24", "resi 583-587 & chain A ")
cmd.color ("red", "Astrand24")


cmd.select("Astrand25", "resi 599-601 & chain A ")
cmd.color ("green", "Astrand25")


cmd.select("Astrand26", "resi 615-626 & chain A ")
cmd.color ("orange", "Astrand26")


cmd.select("Astrand27", "resi 630-642 & chain A ")
cmd.color ("teal", "Astrand27")


cmd.select("Astrand28", "resi 646-652 & chain A ")
cmd.color ("yellow", "Astrand28")


cmd.select("Astrand29", "resi 655-661 & chain A ")
cmd.color ("blue", "Astrand29")


cmd.select("Astrand30", "resi 666-677 & chain A ")
cmd.color ("red", "Astrand30")


cmd.select("Astrand31", "resi 687-701 & chain A ")
cmd.color ("green", "Astrand31")


cmd.select("Astrand32", "resi 738-748 & chain A ")
cmd.color ("orange", "Astrand32")


cmd.select("Astrand33", "resi 753-762 & chain A ")
cmd.color ("teal", "Astrand33")


cmd.select("Astrand34", "resi 766-770 & chain A ")
cmd.color ("yellow", "Astrand34")


cmd.select("Astrand35", "resi 775-777 & chain A ")
cmd.color ("blue", "Astrand35")


cmd.select("Astrand36", "resi 792-794 & chain A ")
cmd.color ("red", "Astrand36")


cmd.select("Astrand37", "resi 797-801 & chain A ")
cmd.color ("green", "Astrand37")


cmd.select("Astrand38", "resi 805-817 & chain A ")
cmd.color ("orange", "Astrand38")


cmd.select("Astrand39", "resi 823-830 & chain A ")
cmd.color ("teal", "Astrand39")


cmd.select("Astrand40", "resi 839-843 & chain A ")
cmd.color ("yellow", "Astrand40")


cmd.select("Astrand41", "resi 850-853 & chain A ")
cmd.color ("blue", "Astrand41")


cmd.select("Astrand42", "resi 859-866 & chain A ")
cmd.color ("red", "Astrand42")


cmd.select("Bstrand43", "resi 68-72 & chain B ")
cmd.color ("green", "Bstrand43")


cmd.select("Bstrand44", "resi 96-98 & chain B ")
cmd.color ("orange", "Bstrand44")


cmd.select("Bstrand45", "resi 116-118 & chain B ")
cmd.color ("teal", "Bstrand45")


cmd.select("Bstrand46", "resi 127-130 & chain B ")
cmd.color ("yellow", "Bstrand46")


cmd.select("Bstrand47", "resi 175-181 & chain B ")
cmd.color ("blue", "Bstrand47")


cmd.select("Bstrand48", "resi 196-201 & chain B ")
cmd.color ("red", "Bstrand48")


cmd.select("Bstrand49", "resi 211-219 & chain B ")
cmd.color ("green", "Bstrand49")


cmd.select("Bstrand50", "resi 247-259 & chain B ")
cmd.color ("orange", "Bstrand50")


cmd.select("Bstrand51", "resi 264-281 & chain B ")
cmd.color ("teal", "Bstrand51")


cmd.select("Bstrand52", "resi 286-304 & chain B ")
cmd.color ("yellow", "Bstrand52")


cmd.select("Bstrand53", "resi 310-317 & chain B ")
cmd.color ("blue", "Bstrand53")


cmd.select("Bstrand54", "resi 320-325 & chain B ")
cmd.color ("red", "Bstrand54")


cmd.select("Bstrand55", "resi 333-337 & chain B ")
cmd.color ("green", "Bstrand55")


cmd.select("Bstrand56", "resi 340-348 & chain B ")
cmd.color ("orange", "Bstrand56")


cmd.select("Bstrand57", "resi 354-371 & chain B ")
cmd.color ("teal", "Bstrand57")


cmd.select("Bstrand58", "resi 376-382 & chain B ")
cmd.color ("yellow", "Bstrand58")


cmd.select("Bstrand59", "resi 402-407 & chain B ")
cmd.color ("blue", "Bstrand59")


cmd.select("Bstrand60", "resi 411-427 & chain B ")
cmd.color ("red", "Bstrand60")


cmd.select("Bstrand61", "resi 436-454 & chain B ")
cmd.color ("green", "Bstrand61")


cmd.select("Bstrand62", "resi 458-460 & chain B ")
cmd.color ("orange", "Bstrand62")


cmd.select("Bstrand63", "resi 493-497 & chain B ")
cmd.color ("teal", "Bstrand63")


cmd.select("Bstrand64", "resi 500-518 & chain B ")
cmd.color ("yellow", "Bstrand64")


cmd.select("Bstrand65", "resi 522-533 & chain B ")
cmd.color ("blue", "Bstrand65")


cmd.select("Bstrand66", "resi 538-551 & chain B ")
cmd.color ("red", "Bstrand66")


cmd.select("Bstrand67", "resi 557-567 & chain B ")
cmd.color ("green", "Bstrand67")


cmd.select("Bstrand68", "resi 582-587 & chain B ")
cmd.color ("orange", "Bstrand68")


cmd.select("Bstrand69", "resi 599-602 & chain B ")
cmd.color ("teal", "Bstrand69")


cmd.select("Bstrand70", "resi 605-607 & chain B ")
cmd.color ("yellow", "Bstrand70")


cmd.select("Bstrand71", "resi 615-626 & chain B ")
cmd.color ("blue", "Bstrand71")


cmd.select("Bstrand72", "resi 630-642 & chain B ")
cmd.color ("red", "Bstrand72")


cmd.select("Bstrand73", "resi 646-652 & chain B ")
cmd.color ("green", "Bstrand73")


cmd.select("Bstrand74", "resi 655-661 & chain B ")
cmd.color ("orange", "Bstrand74")


cmd.select("Bstrand75", "resi 666-677 & chain B ")
cmd.color ("teal", "Bstrand75")


cmd.select("Bstrand76", "resi 687-701 & chain B ")
cmd.color ("yellow", "Bstrand76")


cmd.select("Bstrand77", "resi 738-748 & chain B ")
cmd.color ("blue", "Bstrand77")


cmd.select("Bstrand78", "resi 753-762 & chain B ")
cmd.color ("red", "Bstrand78")


cmd.select("Bstrand79", "resi 766-770 & chain B ")
cmd.color ("green", "Bstrand79")


cmd.select("Bstrand80", "resi 797-801 & chain B ")
cmd.color ("orange", "Bstrand80")


cmd.select("Bstrand81", "resi 805-817 & chain B ")
cmd.color ("teal", "Bstrand81")


cmd.select("Bstrand82", "resi 823-830 & chain B ")
cmd.color ("yellow", "Bstrand82")


cmd.select("Bstrand83", "resi 839-843 & chain B ")
cmd.color ("blue", "Bstrand83")


cmd.select("Bstrand84", "resi 850-853 & chain B ")
cmd.color ("red", "Bstrand84")


cmd.select("Bstrand85", "resi 859-866 & chain B ")
cmd.color ("green", "Bstrand85")


cmd.select("barrel", "Astrand* or Bstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
