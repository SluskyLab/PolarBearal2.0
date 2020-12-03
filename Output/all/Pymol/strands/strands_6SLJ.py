from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/6SLJ.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 122-125 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 179-182 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 200-206 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 223-228 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 239-250 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 329-340 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 345-357 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 365-378 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 383-397 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 455-470 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 476-495 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 507-517 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 520-530 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 535-560 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 581-600 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 604-615 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 624-634 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 647-661 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("Astrand18", "resi 673-675 & chain A ")
cmd.color ("red", "Astrand18")


cmd.select("Astrand19", "resi 685-687 & chain A ")
cmd.color ("green", "Astrand19")


cmd.select("Astrand20", "resi 698-711 & chain A ")
cmd.color ("orange", "Astrand20")


cmd.select("Astrand21", "resi 716-728 & chain A ")
cmd.color ("teal", "Astrand21")


cmd.select("Astrand22", "resi 731-735 & chain A ")
cmd.color ("yellow", "Astrand22")


cmd.select("Astrand23", "resi 744-748 & chain A ")
cmd.color ("blue", "Astrand23")


cmd.select("Astrand24", "resi 751-764 & chain A ")
cmd.color ("red", "Astrand24")


cmd.select("Astrand25", "resi 774-788 & chain A ")
cmd.color ("green", "Astrand25")


cmd.select("Astrand26", "resi 795-798 & chain A ")
cmd.color ("orange", "Astrand26")


cmd.select("Astrand27", "resi 803-806 & chain A ")
cmd.color ("teal", "Astrand27")


cmd.select("Astrand28", "resi 818-821 & chain A ")
cmd.color ("yellow", "Astrand28")


cmd.select("Astrand29", "resi 828-830 & chain A ")
cmd.color ("blue", "Astrand29")


cmd.select("Astrand30", "resi 864-873 & chain A ")
cmd.color ("red", "Astrand30")


cmd.select("Astrand31", "resi 877-887 & chain A ")
cmd.color ("green", "Astrand31")


cmd.select("Astrand32", "resi 946-957 & chain A ")
cmd.color ("orange", "Astrand32")


cmd.select("Astrand33", "resi 971-979 & chain A ")
cmd.color ("teal", "Astrand33")


cmd.select("Astrand34", "resi 983-985 & chain A ")
cmd.color ("yellow", "Astrand34")


cmd.select("Astrand35", "resi 1006-1016 & chain A ")
cmd.color ("blue", "Astrand35")


cmd.select("Bstrand36", "resi 122-126 & chain B ")
cmd.color ("red", "Bstrand36")


cmd.select("Bstrand37", "resi 179-182 & chain B ")
cmd.color ("green", "Bstrand37")


cmd.select("Bstrand38", "resi 200-206 & chain B ")
cmd.color ("orange", "Bstrand38")


cmd.select("Bstrand39", "resi 223-228 & chain B ")
cmd.color ("teal", "Bstrand39")


cmd.select("Bstrand40", "resi 238-249 & chain B ")
cmd.color ("yellow", "Bstrand40")


cmd.select("Bstrand41", "resi 329-341 & chain B ")
cmd.color ("blue", "Bstrand41")


cmd.select("Bstrand42", "resi 345-357 & chain B ")
cmd.color ("red", "Bstrand42")


cmd.select("Bstrand43", "resi 365-380 & chain B ")
cmd.color ("green", "Bstrand43")


cmd.select("Bstrand44", "resi 383-397 & chain B ")
cmd.color ("orange", "Bstrand44")


cmd.select("Bstrand45", "resi 455-470 & chain B ")
cmd.color ("teal", "Bstrand45")


cmd.select("Bstrand46", "resi 476-495 & chain B ")
cmd.color ("yellow", "Bstrand46")


cmd.select("Bstrand47", "resi 507-530 & chain B ")
cmd.color ("blue", "Bstrand47")


cmd.select("Bstrand48", "resi 535-560 & chain B ")
cmd.color ("red", "Bstrand48")


cmd.select("Bstrand49", "resi 581-600 & chain B ")
cmd.color ("green", "Bstrand49")


cmd.select("Bstrand50", "resi 604-615 & chain B ")
cmd.color ("orange", "Bstrand50")


cmd.select("Bstrand51", "resi 624-634 & chain B ")
cmd.color ("teal", "Bstrand51")


cmd.select("Bstrand52", "resi 647-661 & chain B ")
cmd.color ("yellow", "Bstrand52")


cmd.select("Bstrand53", "resi 673-675 & chain B ")
cmd.color ("blue", "Bstrand53")


cmd.select("Bstrand54", "resi 685-687 & chain B ")
cmd.color ("red", "Bstrand54")


cmd.select("Bstrand55", "resi 698-711 & chain B ")
cmd.color ("green", "Bstrand55")


cmd.select("Bstrand56", "resi 716-728 & chain B ")
cmd.color ("orange", "Bstrand56")


cmd.select("Bstrand57", "resi 731-735 & chain B ")
cmd.color ("teal", "Bstrand57")


cmd.select("Bstrand58", "resi 744-748 & chain B ")
cmd.color ("yellow", "Bstrand58")


cmd.select("Bstrand59", "resi 751-764 & chain B ")
cmd.color ("blue", "Bstrand59")


cmd.select("Bstrand60", "resi 772-788 & chain B ")
cmd.color ("red", "Bstrand60")


cmd.select("Bstrand61", "resi 795-797 & chain B ")
cmd.color ("green", "Bstrand61")


cmd.select("Bstrand62", "resi 804-806 & chain B ")
cmd.color ("orange", "Bstrand62")


cmd.select("Bstrand63", "resi 864-874 & chain B ")
cmd.color ("teal", "Bstrand63")


cmd.select("Bstrand64", "resi 877-887 & chain B ")
cmd.color ("yellow", "Bstrand64")


cmd.select("Bstrand65", "resi 946-957 & chain B ")
cmd.color ("blue", "Bstrand65")


cmd.select("Bstrand66", "resi 971-979 & chain B ")
cmd.color ("red", "Bstrand66")


cmd.select("Bstrand67", "resi 983-985 & chain B ")
cmd.color ("green", "Bstrand67")


cmd.select("Bstrand68", "resi 1007-1016 & chain B ")
cmd.color ("orange", "Bstrand68")


cmd.select("Cstrand69", "resi 71-73 & chain C ")
cmd.color ("teal", "Cstrand69")


cmd.select("Cstrand70", "resi 308-311 & chain C ")
cmd.color ("yellow", "Cstrand70")


cmd.select("Cstrand71", "resi 314-317 & chain C ")
cmd.color ("blue", "Cstrand71")


cmd.select("Cstrand72", "resi 321-323 & chain C ")
cmd.color ("red", "Cstrand72")


cmd.select("Dstrand73", "resi 71-73 & chain D ")
cmd.color ("green", "Dstrand73")


cmd.select("Dstrand74", "resi 308-311 & chain D ")
cmd.color ("orange", "Dstrand74")


cmd.select("Dstrand75", "resi 314-317 & chain D ")
cmd.color ("teal", "Dstrand75")


cmd.select("Dstrand76", "resi 321-323 & chain D ")
cmd.color ("yellow", "Dstrand76")


cmd.select("barrel", "Astrand* or Bstrand* or Cstrand* or Dstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
