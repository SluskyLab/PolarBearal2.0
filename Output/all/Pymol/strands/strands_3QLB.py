from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3QLB.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 37-38 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 46-47 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 54-59 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 81-82 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 96-97 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 100-101 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 106-108 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 127-134 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 148-154 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 162-170 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 174-184 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 191-201 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 212-222 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 228-240 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 275-289 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 294-317 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 323-346 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 353-381 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("Astrand18", "resi 401-422 & chain A ")
cmd.color ("red", "Astrand18")


cmd.select("Astrand19", "resi 426-443 & chain A ")
cmd.color ("green", "Astrand19")


cmd.select("Astrand20", "resi 448-465 & chain A ")
cmd.color ("orange", "Astrand20")


cmd.select("Astrand21", "resi 471-482 & chain A ")
cmd.color ("teal", "Astrand21")


cmd.select("Astrand22", "resi 497-508 & chain A ")
cmd.color ("yellow", "Astrand22")


cmd.select("Astrand23", "resi 515-532 & chain A ")
cmd.color ("blue", "Astrand23")


cmd.select("Astrand24", "resi 540-558 & chain A ")
cmd.color ("red", "Astrand24")


cmd.select("Astrand25", "resi 563-577 & chain A ")
cmd.color ("green", "Astrand25")


cmd.select("Astrand26", "resi 595-604 & chain A ")
cmd.color ("orange", "Astrand26")


cmd.select("Astrand27", "resi 613-622 & chain A ")
cmd.color ("teal", "Astrand27")


cmd.select("Astrand28", "resi 625-626 & chain A ")
cmd.color ("yellow", "Astrand28")


cmd.select("Astrand29", "resi 634-635 & chain A ")
cmd.color ("blue", "Astrand29")


cmd.select("Astrand30", "resi 638-648 & chain A ")
cmd.color ("red", "Astrand30")


cmd.select("Astrand31", "resi 659-666 & chain A ")
cmd.color ("green", "Astrand31")


cmd.select("Astrand32", "resi 674-677 & chain A ")
cmd.color ("orange", "Astrand32")


cmd.select("Astrand33", "resi 682-684 & chain A ")
cmd.color ("teal", "Astrand33")


cmd.select("Astrand34", "resi 689-697 & chain A ")
cmd.color ("yellow", "Astrand34")


cmd.select("Bstrand35", "resi 37-38 & chain B ")
cmd.color ("blue", "Bstrand35")


cmd.select("Bstrand36", "resi 46-47 & chain B ")
cmd.color ("red", "Bstrand36")


cmd.select("Bstrand37", "resi 54-58 & chain B ")
cmd.color ("green", "Bstrand37")


cmd.select("Bstrand38", "resi 81-83 & chain B ")
cmd.color ("orange", "Bstrand38")


cmd.select("Bstrand39", "resi 95-97 & chain B ")
cmd.color ("teal", "Bstrand39")


cmd.select("Bstrand40", "resi 100-101 & chain B ")
cmd.color ("yellow", "Bstrand40")


cmd.select("Bstrand41", "resi 106-108 & chain B ")
cmd.color ("blue", "Bstrand41")


cmd.select("Bstrand42", "resi 127-134 & chain B ")
cmd.color ("red", "Bstrand42")


cmd.select("Bstrand43", "resi 148-154 & chain B ")
cmd.color ("green", "Bstrand43")


cmd.select("Bstrand44", "resi 163-170 & chain B ")
cmd.color ("orange", "Bstrand44")


cmd.select("Bstrand45", "resi 175-184 & chain B ")
cmd.color ("teal", "Bstrand45")


cmd.select("Bstrand46", "resi 191-201 & chain B ")
cmd.color ("yellow", "Bstrand46")


cmd.select("Bstrand47", "resi 213-222 & chain B ")
cmd.color ("blue", "Bstrand47")


cmd.select("Bstrand48", "resi 228-240 & chain B ")
cmd.color ("red", "Bstrand48")


cmd.select("Bstrand49", "resi 275-289 & chain B ")
cmd.color ("green", "Bstrand49")


cmd.select("Bstrand50", "resi 294-311 & chain B ")
cmd.color ("orange", "Bstrand50")


cmd.select("Bstrand51", "resi 314-317 & chain B ")
cmd.color ("teal", "Bstrand51")


cmd.select("Bstrand52", "resi 323-349 & chain B ")
cmd.color ("yellow", "Bstrand52")


cmd.select("Bstrand53", "resi 353-381 & chain B ")
cmd.color ("blue", "Bstrand53")


cmd.select("Bstrand54", "resi 400-422 & chain B ")
cmd.color ("red", "Bstrand54")


cmd.select("Bstrand55", "resi 426-443 & chain B ")
cmd.color ("green", "Bstrand55")


cmd.select("Bstrand56", "resi 450-465 & chain B ")
cmd.color ("orange", "Bstrand56")


cmd.select("Bstrand57", "resi 471-482 & chain B ")
cmd.color ("teal", "Bstrand57")


cmd.select("Bstrand58", "resi 497-508 & chain B ")
cmd.color ("yellow", "Bstrand58")


cmd.select("Bstrand59", "resi 515-532 & chain B ")
cmd.color ("blue", "Bstrand59")


cmd.select("Bstrand60", "resi 540-558 & chain B ")
cmd.color ("red", "Bstrand60")


cmd.select("Bstrand61", "resi 563-578 & chain B ")
cmd.color ("green", "Bstrand61")


cmd.select("Bstrand62", "resi 595-604 & chain B ")
cmd.color ("orange", "Bstrand62")


cmd.select("Bstrand63", "resi 613-622 & chain B ")
cmd.color ("teal", "Bstrand63")


cmd.select("Bstrand64", "resi 625-626 & chain B ")
cmd.color ("yellow", "Bstrand64")


cmd.select("Bstrand65", "resi 634-635 & chain B ")
cmd.color ("blue", "Bstrand65")


cmd.select("Bstrand66", "resi 638-648 & chain B ")
cmd.color ("red", "Bstrand66")


cmd.select("Bstrand67", "resi 659-666 & chain B ")
cmd.color ("green", "Bstrand67")


cmd.select("Bstrand68", "resi 674-677 & chain B ")
cmd.color ("orange", "Bstrand68")


cmd.select("Bstrand69", "resi 682-684 & chain B ")
cmd.color ("teal", "Bstrand69")


cmd.select("Bstrand70", "resi 689-697 & chain B ")
cmd.color ("yellow", "Bstrand70")


cmd.select("barrel", "Astrand* or Bstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
