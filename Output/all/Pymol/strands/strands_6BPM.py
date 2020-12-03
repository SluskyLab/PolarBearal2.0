from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/6BPM.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 74-79 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 119-120 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 123-124 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 129-131 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 134-135 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 147-154 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 168-174 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 182-190 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 194-204 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 209-221 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 229-241 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 247-260 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 266-267 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 302-319 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 322-343 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 360-386 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 391-410 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 418-419 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("Astrand18", "resi 434-455 & chain A ")
cmd.color ("red", "Astrand18")


cmd.select("Astrand19", "resi 460-480 & chain A ")
cmd.color ("green", "Astrand19")


cmd.select("Astrand20", "resi 500-522 & chain A ")
cmd.color ("orange", "Astrand20")


cmd.select("Astrand21", "resi 527-538 & chain A ")
cmd.color ("teal", "Astrand21")


cmd.select("Astrand22", "resi 564-577 & chain A ")
cmd.color ("yellow", "Astrand22")


cmd.select("Astrand23", "resi 582-599 & chain A ")
cmd.color ("blue", "Astrand23")


cmd.select("Astrand24", "resi 605-625 & chain A ")
cmd.color ("red", "Astrand24")


cmd.select("Astrand25", "resi 628-643 & chain A ")
cmd.color ("green", "Astrand25")


cmd.select("Astrand26", "resi 661-669 & chain A ")
cmd.color ("orange", "Astrand26")


cmd.select("Astrand27", "resi 675-684 & chain A ")
cmd.color ("teal", "Astrand27")


cmd.select("Astrand28", "resi 687-688 & chain A ")
cmd.color ("yellow", "Astrand28")


cmd.select("Astrand29", "resi 700-701 & chain A ")
cmd.color ("blue", "Astrand29")


cmd.select("Astrand30", "resi 704-714 & chain A ")
cmd.color ("red", "Astrand30")


cmd.select("Astrand31", "resi 719-726 & chain A ")
cmd.color ("green", "Astrand31")


cmd.select("Astrand32", "resi 734-737 & chain A ")
cmd.color ("orange", "Astrand32")


cmd.select("Astrand33", "resi 743-746 & chain A ")
cmd.color ("teal", "Astrand33")


cmd.select("Astrand34", "resi 751-759 & chain A ")
cmd.color ("yellow", "Astrand34")


cmd.select("Cstrand35", "resi 74-79 & chain C ")
cmd.color ("blue", "Cstrand35")


cmd.select("Cstrand36", "resi 119-120 & chain C ")
cmd.color ("red", "Cstrand36")


cmd.select("Cstrand37", "resi 123-124 & chain C ")
cmd.color ("green", "Cstrand37")


cmd.select("Cstrand38", "resi 129-131 & chain C ")
cmd.color ("orange", "Cstrand38")


cmd.select("Cstrand39", "resi 134-135 & chain C ")
cmd.color ("teal", "Cstrand39")


cmd.select("Cstrand40", "resi 147-154 & chain C ")
cmd.color ("yellow", "Cstrand40")


cmd.select("Cstrand41", "resi 168-174 & chain C ")
cmd.color ("blue", "Cstrand41")


cmd.select("Cstrand42", "resi 182-190 & chain C ")
cmd.color ("red", "Cstrand42")


cmd.select("Cstrand43", "resi 194-204 & chain C ")
cmd.color ("green", "Cstrand43")


cmd.select("Cstrand44", "resi 209-222 & chain C ")
cmd.color ("orange", "Cstrand44")


cmd.select("Cstrand45", "resi 225-241 & chain C ")
cmd.color ("teal", "Cstrand45")


cmd.select("Cstrand46", "resi 247-260 & chain C ")
cmd.color ("yellow", "Cstrand46")


cmd.select("Cstrand47", "resi 266-267 & chain C ")
cmd.color ("blue", "Cstrand47")


cmd.select("Cstrand48", "resi 302-319 & chain C ")
cmd.color ("red", "Cstrand48")


cmd.select("Cstrand49", "resi 322-343 & chain C ")
cmd.color ("green", "Cstrand49")


cmd.select("Cstrand50", "resi 360-387 & chain C ")
cmd.color ("orange", "Cstrand50")


cmd.select("Cstrand51", "resi 390-410 & chain C ")
cmd.color ("teal", "Cstrand51")


cmd.select("Cstrand52", "resi 418-419 & chain C ")
cmd.color ("yellow", "Cstrand52")


cmd.select("Cstrand53", "resi 434-455 & chain C ")
cmd.color ("blue", "Cstrand53")


cmd.select("Cstrand54", "resi 460-480 & chain C ")
cmd.color ("red", "Cstrand54")


cmd.select("Cstrand55", "resi 500-522 & chain C ")
cmd.color ("green", "Cstrand55")


cmd.select("Cstrand56", "resi 527-538 & chain C ")
cmd.color ("orange", "Cstrand56")


cmd.select("Cstrand57", "resi 564-577 & chain C ")
cmd.color ("teal", "Cstrand57")


cmd.select("Cstrand58", "resi 582-599 & chain C ")
cmd.color ("yellow", "Cstrand58")


cmd.select("Cstrand59", "resi 605-625 & chain C ")
cmd.color ("blue", "Cstrand59")


cmd.select("Cstrand60", "resi 628-643 & chain C ")
cmd.color ("red", "Cstrand60")


cmd.select("Cstrand61", "resi 661-669 & chain C ")
cmd.color ("green", "Cstrand61")


cmd.select("Cstrand62", "resi 675-684 & chain C ")
cmd.color ("orange", "Cstrand62")


cmd.select("Cstrand63", "resi 687-688 & chain C ")
cmd.color ("teal", "Cstrand63")


cmd.select("Cstrand64", "resi 700-701 & chain C ")
cmd.color ("yellow", "Cstrand64")


cmd.select("Cstrand65", "resi 704-714 & chain C ")
cmd.color ("blue", "Cstrand65")


cmd.select("Cstrand66", "resi 719-726 & chain C ")
cmd.color ("red", "Cstrand66")


cmd.select("Cstrand67", "resi 734-737 & chain C ")
cmd.color ("green", "Cstrand67")


cmd.select("Cstrand68", "resi 743-746 & chain C ")
cmd.color ("orange", "Cstrand68")


cmd.select("Cstrand69", "resi 751-759 & chain C ")
cmd.color ("teal", "Cstrand69")


cmd.select("barrel", "Astrand* or Cstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
