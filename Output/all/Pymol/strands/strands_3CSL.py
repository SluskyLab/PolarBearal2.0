from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3CSL.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 123-126 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 149-150 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 163-164 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 174-177 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 180-181 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 203-210 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 224-230 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 243-252 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 258-266 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 271-282 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 322-335 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 339-355 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 359-360 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 369-370 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 373-390 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 400-415 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 426-448 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 451-470 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("Astrand18", "resi 482-497 & chain A ")
cmd.color ("red", "Astrand18")


cmd.select("Astrand19", "resi 501-518 & chain A ")
cmd.color ("green", "Astrand19")


cmd.select("Astrand20", "resi 521-524 & chain A ")
cmd.color ("orange", "Astrand20")


cmd.select("Astrand21", "resi 548-551 & chain A ")
cmd.color ("teal", "Astrand21")


cmd.select("Astrand22", "resi 554-571 & chain A ")
cmd.color ("yellow", "Astrand22")


cmd.select("Astrand23", "resi 578-589 & chain A ")
cmd.color ("blue", "Astrand23")


cmd.select("Astrand24", "resi 607-608 & chain A ")
cmd.color ("red", "Astrand24")


cmd.select("Astrand25", "resi 617-631 & chain A ")
cmd.color ("green", "Astrand25")


cmd.select("Astrand26", "resi 639-652 & chain A ")
cmd.color ("orange", "Astrand26")


cmd.select("Astrand27", "resi 656-658 & chain A ")
cmd.color ("teal", "Astrand27")


cmd.select("Astrand28", "resi 673-677 & chain A ")
cmd.color ("yellow", "Astrand28")


cmd.select("Astrand29", "resi 682-695 & chain A ")
cmd.color ("blue", "Astrand29")


cmd.select("Astrand30", "resi 699-709 & chain A ")
cmd.color ("red", "Astrand30")


cmd.select("Astrand31", "resi 715-716 & chain A ")
cmd.color ("green", "Astrand31")


cmd.select("Astrand32", "resi 725-727 & chain A ")
cmd.color ("orange", "Astrand32")


cmd.select("Astrand33", "resi 738-740 & chain A ")
cmd.color ("teal", "Astrand33")


cmd.select("Astrand34", "resi 749-750 & chain A ")
cmd.color ("yellow", "Astrand34")


cmd.select("Astrand35", "resi 766-773 & chain A ")
cmd.color ("blue", "Astrand35")


cmd.select("Astrand36", "resi 782-789 & chain A ")
cmd.color ("red", "Astrand36")


cmd.select("Astrand37", "resi 792-793 & chain A ")
cmd.color ("green", "Astrand37")


cmd.select("Astrand38", "resi 806-807 & chain A ")
cmd.color ("orange", "Astrand38")


cmd.select("Astrand39", "resi 810-820 & chain A ")
cmd.color ("teal", "Astrand39")


cmd.select("Astrand40", "resi 825-831 & chain A ")
cmd.color ("yellow", "Astrand40")


cmd.select("Astrand41", "resi 857-864 & chain A ")
cmd.color ("blue", "Astrand41")


cmd.select("Bstrand42", "resi 123-126 & chain B ")
cmd.color ("red", "Bstrand42")


cmd.select("Bstrand43", "resi 149-150 & chain B ")
cmd.color ("green", "Bstrand43")


cmd.select("Bstrand44", "resi 163-164 & chain B ")
cmd.color ("orange", "Bstrand44")


cmd.select("Bstrand45", "resi 174-177 & chain B ")
cmd.color ("teal", "Bstrand45")


cmd.select("Bstrand46", "resi 180-181 & chain B ")
cmd.color ("yellow", "Bstrand46")


cmd.select("Bstrand47", "resi 203-210 & chain B ")
cmd.color ("blue", "Bstrand47")


cmd.select("Bstrand48", "resi 224-230 & chain B ")
cmd.color ("red", "Bstrand48")


cmd.select("Bstrand49", "resi 243-252 & chain B ")
cmd.color ("green", "Bstrand49")


cmd.select("Bstrand50", "resi 258-266 & chain B ")
cmd.color ("orange", "Bstrand50")


cmd.select("Bstrand51", "resi 271-282 & chain B ")
cmd.color ("teal", "Bstrand51")


cmd.select("Bstrand52", "resi 322-335 & chain B ")
cmd.color ("yellow", "Bstrand52")


cmd.select("Bstrand53", "resi 339-355 & chain B ")
cmd.color ("blue", "Bstrand53")


cmd.select("Bstrand54", "resi 359-360 & chain B ")
cmd.color ("red", "Bstrand54")


cmd.select("Bstrand55", "resi 369-370 & chain B ")
cmd.color ("green", "Bstrand55")


cmd.select("Bstrand56", "resi 373-390 & chain B ")
cmd.color ("orange", "Bstrand56")


cmd.select("Bstrand57", "resi 400-415 & chain B ")
cmd.color ("teal", "Bstrand57")


cmd.select("Bstrand58", "resi 426-448 & chain B ")
cmd.color ("yellow", "Bstrand58")


cmd.select("Bstrand59", "resi 451-470 & chain B ")
cmd.color ("blue", "Bstrand59")


cmd.select("Bstrand60", "resi 482-497 & chain B ")
cmd.color ("red", "Bstrand60")


cmd.select("Bstrand61", "resi 501-518 & chain B ")
cmd.color ("green", "Bstrand61")


cmd.select("Bstrand62", "resi 521-524 & chain B ")
cmd.color ("orange", "Bstrand62")


cmd.select("Bstrand63", "resi 548-551 & chain B ")
cmd.color ("teal", "Bstrand63")


cmd.select("Bstrand64", "resi 554-571 & chain B ")
cmd.color ("yellow", "Bstrand64")


cmd.select("Bstrand65", "resi 578-589 & chain B ")
cmd.color ("blue", "Bstrand65")


cmd.select("Bstrand66", "resi 607-608 & chain B ")
cmd.color ("red", "Bstrand66")


cmd.select("Bstrand67", "resi 617-631 & chain B ")
cmd.color ("green", "Bstrand67")


cmd.select("Bstrand68", "resi 639-652 & chain B ")
cmd.color ("orange", "Bstrand68")


cmd.select("Bstrand69", "resi 656-658 & chain B ")
cmd.color ("teal", "Bstrand69")


cmd.select("Bstrand70", "resi 673-677 & chain B ")
cmd.color ("yellow", "Bstrand70")


cmd.select("Bstrand71", "resi 682-695 & chain B ")
cmd.color ("blue", "Bstrand71")


cmd.select("Bstrand72", "resi 699-709 & chain B ")
cmd.color ("red", "Bstrand72")


cmd.select("Bstrand73", "resi 715-716 & chain B ")
cmd.color ("green", "Bstrand73")


cmd.select("Bstrand74", "resi 725-727 & chain B ")
cmd.color ("orange", "Bstrand74")


cmd.select("Bstrand75", "resi 738-740 & chain B ")
cmd.color ("teal", "Bstrand75")


cmd.select("Bstrand76", "resi 749-750 & chain B ")
cmd.color ("yellow", "Bstrand76")


cmd.select("Bstrand77", "resi 766-773 & chain B ")
cmd.color ("blue", "Bstrand77")


cmd.select("Bstrand78", "resi 782-789 & chain B ")
cmd.color ("red", "Bstrand78")


cmd.select("Bstrand79", "resi 792-793 & chain B ")
cmd.color ("green", "Bstrand79")


cmd.select("Bstrand80", "resi 806-807 & chain B ")
cmd.color ("orange", "Bstrand80")


cmd.select("Bstrand81", "resi 810-820 & chain B ")
cmd.color ("teal", "Bstrand81")


cmd.select("Bstrand82", "resi 825-831 & chain B ")
cmd.color ("yellow", "Bstrand82")


cmd.select("Bstrand83", "resi 857-864 & chain B ")
cmd.color ("blue", "Bstrand83")


cmd.select("Cstrand84", "resi 4-7 & chain C ")
cmd.color ("red", "Cstrand84")


cmd.select("Cstrand85", "resi 44-46 & chain C ")
cmd.color ("green", "Cstrand85")


cmd.select("Cstrand86", "resi 51-58 & chain C ")
cmd.color ("orange", "Cstrand86")


cmd.select("Cstrand87", "resi 65-76 & chain C ")
cmd.color ("teal", "Cstrand87")


cmd.select("Cstrand88", "resi 84-99 & chain C ")
cmd.color ("yellow", "Cstrand88")


cmd.select("Cstrand89", "resi 107-116 & chain C ")
cmd.color ("blue", "Cstrand89")


cmd.select("Cstrand90", "resi 120-122 & chain C ")
cmd.color ("red", "Cstrand90")


cmd.select("Dstrand91", "resi 4-7 & chain D ")
cmd.color ("green", "Dstrand91")


cmd.select("Dstrand92", "resi 44-46 & chain D ")
cmd.color ("orange", "Dstrand92")


cmd.select("Dstrand93", "resi 51-58 & chain D ")
cmd.color ("teal", "Dstrand93")


cmd.select("Dstrand94", "resi 65-76 & chain D ")
cmd.color ("yellow", "Dstrand94")


cmd.select("Dstrand95", "resi 84-99 & chain D ")
cmd.color ("blue", "Dstrand95")


cmd.select("Dstrand96", "resi 107-116 & chain D ")
cmd.color ("red", "Dstrand96")


cmd.select("Dstrand97", "resi 120-122 & chain D ")
cmd.color ("green", "Dstrand97")


cmd.select("barrel", "Astrand* or Bstrand* or Cstrand* or Dstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
