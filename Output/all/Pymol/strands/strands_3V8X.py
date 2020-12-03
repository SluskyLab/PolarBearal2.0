from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3V8X.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 60-64 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 86-90 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 96-101 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 104-105 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 109-113 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 116-117 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 148-155 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 169-175 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 188-197 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 202-213 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 216-228 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 240-243 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 246-250 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 257-260 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 277-284 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 287-290 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 305-314 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 317-319 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("Astrand18", "resi 325-341 & chain A ")
cmd.color ("red", "Astrand18")


cmd.select("Astrand19", "resi 380-382 & chain A ")
cmd.color ("green", "Astrand19")


cmd.select("Astrand20", "resi 388-390 & chain A ")
cmd.color ("orange", "Astrand20")


cmd.select("Astrand21", "resi 394-415 & chain A ")
cmd.color ("teal", "Astrand21")


cmd.select("Astrand22", "resi 425-447 & chain A ")
cmd.color ("yellow", "Astrand22")


cmd.select("Astrand23", "resi 465-488 & chain A ")
cmd.color ("blue", "Astrand23")


cmd.select("Astrand24", "resi 494-527 & chain A ")
cmd.color ("red", "Astrand24")


cmd.select("Astrand25", "resi 547-560 & chain A ")
cmd.color ("green", "Astrand25")


cmd.select("Astrand26", "resi 575-592 & chain A ")
cmd.color ("orange", "Astrand26")


cmd.select("Astrand27", "resi 596-610 & chain A ")
cmd.color ("teal", "Astrand27")


cmd.select("Astrand28", "resi 620-632 & chain A ")
cmd.color ("yellow", "Astrand28")


cmd.select("Astrand29", "resi 638-649 & chain A ")
cmd.color ("blue", "Astrand29")


cmd.select("Astrand30", "resi 673-686 & chain A ")
cmd.color ("red", "Astrand30")


cmd.select("Astrand31", "resi 689-712 & chain A ")
cmd.color ("green", "Astrand31")


cmd.select("Astrand32", "resi 717-742 & chain A ")
cmd.color ("orange", "Astrand32")


cmd.select("Astrand33", "resi 756-771 & chain A ")
cmd.color ("teal", "Astrand33")


cmd.select("Astrand34", "resi 775-779 & chain A ")
cmd.color ("yellow", "Astrand34")


cmd.select("Astrand35", "resi 790-798 & chain A ")
cmd.color ("blue", "Astrand35")


cmd.select("Astrand36", "resi 804-813 & chain A ")
cmd.color ("red", "Astrand36")


cmd.select("Astrand37", "resi 822-826 & chain A ")
cmd.color ("green", "Astrand37")


cmd.select("Astrand38", "resi 832-836 & chain A ")
cmd.color ("orange", "Astrand38")


cmd.select("Astrand39", "resi 845-855 & chain A ")
cmd.color ("teal", "Astrand39")


cmd.select("Astrand40", "resi 860-867 & chain A ")
cmd.color ("yellow", "Astrand40")


cmd.select("Astrand41", "resi 906-914 & chain A ")
cmd.color ("blue", "Astrand41")


cmd.select("Bstrand42", "resi 6-7 & chain B ")
cmd.color ("red", "Bstrand42")


cmd.select("Bstrand43", "resi 37-38 & chain B ")
cmd.color ("green", "Bstrand43")


cmd.select("Bstrand44", "resi 60-63 & chain B ")
cmd.color ("orange", "Bstrand44")


cmd.select("Bstrand45", "resi 78-83 & chain B ")
cmd.color ("teal", "Bstrand45")


cmd.select("Bstrand46", "resi 94-102 & chain B ")
cmd.color ("yellow", "Bstrand46")


cmd.select("Bstrand47", "resi 117-119 & chain B ")
cmd.color ("blue", "Bstrand47")


cmd.select("Bstrand48", "resi 157-158 & chain B ")
cmd.color ("red", "Bstrand48")


cmd.select("Bstrand49", "resi 202-206 & chain B ")
cmd.color ("green", "Bstrand49")


cmd.select("Bstrand50", "resi 223-226 & chain B ")
cmd.color ("orange", "Bstrand50")


cmd.select("Bstrand51", "resi 232-234 & chain B ")
cmd.color ("teal", "Bstrand51")


cmd.select("Bstrand52", "resi 244-253 & chain B ")
cmd.color ("yellow", "Bstrand52")


cmd.select("Bstrand53", "resi 302-304 & chain B ")
cmd.color ("blue", "Bstrand53")


cmd.select("Bstrand54", "resi 342-346 & chain B ")
cmd.color ("red", "Bstrand54")


cmd.select("Bstrand55", "resi 366-370 & chain B ")
cmd.color ("green", "Bstrand55")


cmd.select("Bstrand56", "resi 388-391 & chain B ")
cmd.color ("orange", "Bstrand56")


cmd.select("Bstrand57", "resi 405-411 & chain B ")
cmd.color ("teal", "Bstrand57")


cmd.select("Bstrand58", "resi 426-433 & chain B ")
cmd.color ("yellow", "Bstrand58")


cmd.select("Bstrand59", "resi 449-451 & chain B ")
cmd.color ("blue", "Bstrand59")


cmd.select("Bstrand60", "resi 483-484 & chain B ")
cmd.color ("red", "Bstrand60")


cmd.select("Bstrand61", "resi 530-534 & chain B ")
cmd.color ("green", "Bstrand61")


cmd.select("Bstrand62", "resi 559-562 & chain B ")
cmd.color ("orange", "Bstrand62")


cmd.select("Bstrand63", "resi 568-570 & chain B ")
cmd.color ("teal", "Bstrand63")


cmd.select("Bstrand64", "resi 580-582 & chain B ")
cmd.color ("yellow", "Bstrand64")


cmd.select("Bstrand65", "resi 586-589 & chain B ")
cmd.color ("blue", "Bstrand65")


cmd.select("Bstrand66", "resi 637-640 & chain B ")
cmd.color ("red", "Bstrand66")


cmd.select("barrel", "Astrand* or Bstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
