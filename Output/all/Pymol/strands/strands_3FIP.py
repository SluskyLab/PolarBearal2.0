from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3FIP.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 147-158 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 165-176 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 181-188 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 191-194 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 201-204 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 207-217 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 222-230 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 240-248 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 266-268 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 273-278 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 281-287 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 291-293 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 305-311 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 320-323 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 336-344 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 356-365 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 370-379 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 382-392 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("Astrand18", "resi 398-409 & chain A ")
cmd.color ("red", "Astrand18")


cmd.select("Astrand19", "resi 415-425 & chain A ")
cmd.color ("green", "Astrand19")


cmd.select("Astrand20", "resi 437-444 & chain A ")
cmd.color ("orange", "Astrand20")


cmd.select("Astrand21", "resi 467-478 & chain A ")
cmd.color ("teal", "Astrand21")


cmd.select("Astrand22", "resi 485-495 & chain A ")
cmd.color ("yellow", "Astrand22")


cmd.select("Astrand23", "resi 501-510 & chain A ")
cmd.color ("blue", "Astrand23")


cmd.select("Astrand24", "resi 521-527 & chain A ")
cmd.color ("red", "Astrand24")


cmd.select("Astrand25", "resi 538-545 & chain A ")
cmd.color ("green", "Astrand25")


cmd.select("Astrand26", "resi 552-557 & chain A ")
cmd.color ("orange", "Astrand26")


cmd.select("Astrand27", "resi 563-572 & chain A ")
cmd.color ("teal", "Astrand27")


cmd.select("Astrand28", "resi 579-605 & chain A ")
cmd.color ("yellow", "Astrand28")


cmd.select("Astrand29", "resi 609-618 & chain A ")
cmd.color ("blue", "Astrand29")


cmd.select("Astrand30", "resi 623-634 & chain A ")
cmd.color ("red", "Astrand30")


cmd.select("Bstrand31", "resi 148-154 & chain B ")
cmd.color ("green", "Bstrand31")


cmd.select("Bstrand32", "resi 168-169 & chain B ")
cmd.color ("orange", "Bstrand32")


cmd.select("Bstrand33", "resi 172-173 & chain B ")
cmd.color ("teal", "Bstrand33")


cmd.select("Bstrand34", "resi 176-177 & chain B ")
cmd.color ("yellow", "Bstrand34")


cmd.select("Bstrand35", "resi 181-193 & chain B ")
cmd.color ("blue", "Bstrand35")


cmd.select("Bstrand36", "resi 202-216 & chain B ")
cmd.color ("red", "Bstrand36")


cmd.select("Bstrand37", "resi 222-231 & chain B ")
cmd.color ("green", "Bstrand37")


cmd.select("Bstrand38", "resi 239-248 & chain B ")
cmd.color ("orange", "Bstrand38")


cmd.select("Bstrand39", "resi 264-265 & chain B ")
cmd.color ("teal", "Bstrand39")


cmd.select("Bstrand40", "resi 273-278 & chain B ")
cmd.color ("yellow", "Bstrand40")


cmd.select("Bstrand41", "resi 281-282 & chain B ")
cmd.color ("blue", "Bstrand41")


cmd.select("Bstrand42", "resi 294-295 & chain B ")
cmd.color ("red", "Bstrand42")


cmd.select("Bstrand43", "resi 305-311 & chain B ")
cmd.color ("green", "Bstrand43")


cmd.select("Bstrand44", "resi 319-323 & chain B ")
cmd.color ("orange", "Bstrand44")


cmd.select("Bstrand45", "resi 336-344 & chain B ")
cmd.color ("teal", "Bstrand45")


cmd.select("Bstrand46", "resi 356-365 & chain B ")
cmd.color ("yellow", "Bstrand46")


cmd.select("Bstrand47", "resi 370-379 & chain B ")
cmd.color ("blue", "Bstrand47")


cmd.select("Bstrand48", "resi 382-391 & chain B ")
cmd.color ("red", "Bstrand48")


cmd.select("Bstrand49", "resi 399-409 & chain B ")
cmd.color ("green", "Bstrand49")


cmd.select("Bstrand50", "resi 415-422 & chain B ")
cmd.color ("orange", "Bstrand50")


cmd.select("Bstrand51", "resi 439-444 & chain B ")
cmd.color ("teal", "Bstrand51")


cmd.select("Bstrand52", "resi 467-473 & chain B ")
cmd.color ("yellow", "Bstrand52")


cmd.select("Bstrand53", "resi 489-495 & chain B ")
cmd.color ("blue", "Bstrand53")


cmd.select("Bstrand54", "resi 501-528 & chain B ")
cmd.color ("red", "Bstrand54")


cmd.select("Bstrand55", "resi 537-542 & chain B ")
cmd.color ("green", "Bstrand55")


cmd.select("Bstrand56", "resi 555-557 & chain B ")
cmd.color ("orange", "Bstrand56")


cmd.select("Bstrand57", "resi 564-566 & chain B ")
cmd.color ("teal", "Bstrand57")


cmd.select("Bstrand58", "resi 580-583 & chain B ")
cmd.color ("yellow", "Bstrand58")


cmd.select("Bstrand59", "resi 599-603 & chain B ")
cmd.color ("blue", "Bstrand59")


cmd.select("Bstrand60", "resi 609-616 & chain B ")
cmd.color ("red", "Bstrand60")


cmd.select("Bstrand61", "resi 626-633 & chain B ")
cmd.color ("green", "Bstrand61")


cmd.select("barrel", "Astrand* or Bstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
