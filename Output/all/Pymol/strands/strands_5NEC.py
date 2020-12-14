from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5NEC.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 52-55 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 78-81 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 92-95 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 98-99 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 104-106 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 109-110 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 122-128 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 144-149 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 157-165 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 170-180 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 185-198 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 201-217 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 223-236 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 242-243 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 274-289 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 294-314 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 325-352 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 355-377 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("Astrand18", "resi 401-403 & chain A ")
cmd.color ("red", "Astrand18")


cmd.select("Astrand19", "resi 417-419 & chain A ")
cmd.color ("green", "Astrand19")


cmd.select("Astrand20", "resi 424-442 & chain A ")
cmd.color ("orange", "Astrand20")


cmd.select("Astrand21", "resi 445-462 & chain A ")
cmd.color ("teal", "Astrand21")


cmd.select("Astrand22", "resi 469-486 & chain A ")
cmd.color ("yellow", "Astrand22")


cmd.select("Astrand23", "resi 492-501 & chain A ")
cmd.color ("blue", "Astrand23")


cmd.select("Astrand24", "resi 532-543 & chain A ")
cmd.color ("red", "Astrand24")


cmd.select("Astrand25", "resi 548-559 & chain A ")
cmd.color ("green", "Astrand25")


cmd.select("Astrand26", "resi 577-589 & chain A ")
cmd.color ("orange", "Astrand26")


cmd.select("Astrand27", "resi 594-607 & chain A ")
cmd.color ("teal", "Astrand27")


cmd.select("Astrand28", "resi 637-648 & chain A ")
cmd.color ("yellow", "Astrand28")


cmd.select("Astrand29", "resi 651-660 & chain A ")
cmd.color ("blue", "Astrand29")


cmd.select("Astrand30", "resi 663-664 & chain A ")
cmd.color ("red", "Astrand30")


cmd.select("Astrand31", "resi 672-673 & chain A ")
cmd.color ("green", "Astrand31")


cmd.select("Astrand32", "resi 676-686 & chain A ")
cmd.color ("orange", "Astrand32")


cmd.select("Astrand33", "resi 691-698 & chain A ")
cmd.color ("teal", "Astrand33")


cmd.select("Astrand34", "resi 706-709 & chain A ")
cmd.color ("yellow", "Astrand34")


cmd.select("Astrand35", "resi 714-717 & chain A ")
cmd.color ("blue", "Astrand35")


cmd.select("Astrand36", "resi 722-731 & chain A ")
cmd.color ("red", "Astrand36")


cmd.select("Bstrand37", "resi 52-56 & chain B ")
cmd.color ("green", "Bstrand37")


cmd.select("Bstrand38", "resi 78-81 & chain B ")
cmd.color ("orange", "Bstrand38")


cmd.select("Bstrand39", "resi 92-95 & chain B ")
cmd.color ("teal", "Bstrand39")


cmd.select("Bstrand40", "resi 98-99 & chain B ")
cmd.color ("yellow", "Bstrand40")


cmd.select("Bstrand41", "resi 104-106 & chain B ")
cmd.color ("blue", "Bstrand41")


cmd.select("Bstrand42", "resi 109-110 & chain B ")
cmd.color ("red", "Bstrand42")


cmd.select("Bstrand43", "resi 122-128 & chain B ")
cmd.color ("green", "Bstrand43")


cmd.select("Bstrand44", "resi 144-149 & chain B ")
cmd.color ("orange", "Bstrand44")


cmd.select("Bstrand45", "resi 157-165 & chain B ")
cmd.color ("teal", "Bstrand45")


cmd.select("Bstrand46", "resi 170-180 & chain B ")
cmd.color ("yellow", "Bstrand46")


cmd.select("Bstrand47", "resi 185-198 & chain B ")
cmd.color ("blue", "Bstrand47")


cmd.select("Bstrand48", "resi 201-217 & chain B ")
cmd.color ("red", "Bstrand48")


cmd.select("Bstrand49", "resi 223-236 & chain B ")
cmd.color ("green", "Bstrand49")


cmd.select("Bstrand50", "resi 242-243 & chain B ")
cmd.color ("orange", "Bstrand50")


cmd.select("Bstrand51", "resi 274-291 & chain B ")
cmd.color ("teal", "Bstrand51")


cmd.select("Bstrand52", "resi 294-314 & chain B ")
cmd.color ("yellow", "Bstrand52")


cmd.select("Bstrand53", "resi 325-352 & chain B ")
cmd.color ("blue", "Bstrand53")


cmd.select("Bstrand54", "resi 355-377 & chain B ")
cmd.color ("red", "Bstrand54")


cmd.select("Bstrand55", "resi 401-403 & chain B ")
cmd.color ("green", "Bstrand55")


cmd.select("Bstrand56", "resi 417-419 & chain B ")
cmd.color ("orange", "Bstrand56")


cmd.select("Bstrand57", "resi 424-442 & chain B ")
cmd.color ("teal", "Bstrand57")


cmd.select("Bstrand58", "resi 445-462 & chain B ")
cmd.color ("yellow", "Bstrand58")


cmd.select("Bstrand59", "resi 469-486 & chain B ")
cmd.color ("blue", "Bstrand59")


cmd.select("Bstrand60", "resi 492-502 & chain B ")
cmd.color ("red", "Bstrand60")


cmd.select("Bstrand61", "resi 532-543 & chain B ")
cmd.color ("green", "Bstrand61")


cmd.select("Bstrand62", "resi 548-559 & chain B ")
cmd.color ("orange", "Bstrand62")


cmd.select("Bstrand63", "resi 577-589 & chain B ")
cmd.color ("teal", "Bstrand63")


cmd.select("Bstrand64", "resi 594-607 & chain B ")
cmd.color ("yellow", "Bstrand64")


cmd.select("Bstrand65", "resi 637-648 & chain B ")
cmd.color ("blue", "Bstrand65")


cmd.select("Bstrand66", "resi 651-660 & chain B ")
cmd.color ("red", "Bstrand66")


cmd.select("Bstrand67", "resi 663-664 & chain B ")
cmd.color ("green", "Bstrand67")


cmd.select("Bstrand68", "resi 672-673 & chain B ")
cmd.color ("orange", "Bstrand68")


cmd.select("Bstrand69", "resi 676-686 & chain B ")
cmd.color ("teal", "Bstrand69")


cmd.select("Bstrand70", "resi 691-698 & chain B ")
cmd.color ("yellow", "Bstrand70")


cmd.select("Bstrand71", "resi 706-709 & chain B ")
cmd.color ("blue", "Bstrand71")


cmd.select("Bstrand72", "resi 714-717 & chain B ")
cmd.color ("red", "Bstrand72")


cmd.select("Bstrand73", "resi 722-731 & chain B ")
cmd.color ("green", "Bstrand73")


cmd.select("barrel", "Astrand* or Bstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
