from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3OHN.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 141-153 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 159-171 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 176-187 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 197-209 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 214-222 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 232-239 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 257-260 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 264-270 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 273-280 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 283-286 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 299-305 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 310-315 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 329-339 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 349-358 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 364-372 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 375-387 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 390-402 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 408-420 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("Astrand18", "resi 430-437 & chain A ")
cmd.color ("red", "Astrand18")


cmd.select("Astrand19", "resi 452-453 & chain A ")
cmd.color ("green", "Astrand19")


cmd.select("Astrand20", "resi 474-475 & chain A ")
cmd.color ("orange", "Astrand20")


cmd.select("Astrand21", "resi 480-492 & chain A ")
cmd.color ("teal", "Astrand21")


cmd.select("Astrand22", "resi 496-507 & chain A ")
cmd.color ("yellow", "Astrand22")


cmd.select("Astrand23", "resi 513-524 & chain A ")
cmd.color ("blue", "Astrand23")


cmd.select("Astrand24", "resi 529-538 & chain A ")
cmd.color ("red", "Astrand24")


cmd.select("Astrand25", "resi 545-556 & chain A ")
cmd.color ("green", "Astrand25")


cmd.select("Astrand26", "resi 575-583 & chain A ")
cmd.color ("orange", "Astrand26")


cmd.select("Astrand27", "resi 586-597 & chain A ")
cmd.color ("teal", "Astrand27")


cmd.select("Astrand28", "resi 602-611 & chain A ")
cmd.color ("yellow", "Astrand28")


cmd.select("Astrand29", "resi 619-628 & chain A ")
cmd.color ("blue", "Astrand29")


cmd.select("Astrand30", "resi 633-641 & chain A ")
cmd.color ("red", "Astrand30")


cmd.select("Astrand31", "resi 645-655 & chain A ")
cmd.color ("green", "Astrand31")


cmd.select("Bstrand32", "resi 142-153 & chain B ")
cmd.color ("orange", "Bstrand32")


cmd.select("Bstrand33", "resi 160-172 & chain B ")
cmd.color ("teal", "Bstrand33")


cmd.select("Bstrand34", "resi 175-186 & chain B ")
cmd.color ("yellow", "Bstrand34")


cmd.select("Bstrand35", "resi 197-209 & chain B ")
cmd.color ("blue", "Bstrand35")


cmd.select("Bstrand36", "resi 214-222 & chain B ")
cmd.color ("red", "Bstrand36")


cmd.select("Bstrand37", "resi 232-240 & chain B ")
cmd.color ("green", "Bstrand37")


cmd.select("Bstrand38", "resi 257-260 & chain B ")
cmd.color ("orange", "Bstrand38")


cmd.select("Bstrand39", "resi 264-270 & chain B ")
cmd.color ("teal", "Bstrand39")


cmd.select("Bstrand40", "resi 273-280 & chain B ")
cmd.color ("yellow", "Bstrand40")


cmd.select("Bstrand41", "resi 283-286 & chain B ")
cmd.color ("blue", "Bstrand41")


cmd.select("Bstrand42", "resi 299-304 & chain B ")
cmd.color ("red", "Bstrand42")


cmd.select("Bstrand43", "resi 310-315 & chain B ")
cmd.color ("green", "Bstrand43")


cmd.select("Bstrand44", "resi 329-338 & chain B ")
cmd.color ("orange", "Bstrand44")


cmd.select("Bstrand45", "resi 349-358 & chain B ")
cmd.color ("teal", "Bstrand45")


cmd.select("Bstrand46", "resi 363-372 & chain B ")
cmd.color ("yellow", "Bstrand46")


cmd.select("Bstrand47", "resi 375-385 & chain B ")
cmd.color ("blue", "Bstrand47")


cmd.select("Bstrand48", "resi 391-402 & chain B ")
cmd.color ("red", "Bstrand48")


cmd.select("Bstrand49", "resi 408-420 & chain B ")
cmd.color ("green", "Bstrand49")


cmd.select("Bstrand50", "resi 430-437 & chain B ")
cmd.color ("orange", "Bstrand50")


cmd.select("Bstrand51", "resi 452-453 & chain B ")
cmd.color ("teal", "Bstrand51")


cmd.select("Bstrand52", "resi 474-475 & chain B ")
cmd.color ("yellow", "Bstrand52")


cmd.select("Bstrand53", "resi 480-491 & chain B ")
cmd.color ("blue", "Bstrand53")


cmd.select("Bstrand54", "resi 496-507 & chain B ")
cmd.color ("red", "Bstrand54")


cmd.select("Bstrand55", "resi 513-524 & chain B ")
cmd.color ("green", "Bstrand55")


cmd.select("Bstrand56", "resi 529-538 & chain B ")
cmd.color ("orange", "Bstrand56")


cmd.select("Bstrand57", "resi 546-556 & chain B ")
cmd.color ("teal", "Bstrand57")


cmd.select("Bstrand58", "resi 575-583 & chain B ")
cmd.color ("yellow", "Bstrand58")


cmd.select("Bstrand59", "resi 586-590 & chain B ")
cmd.color ("blue", "Bstrand59")


cmd.select("Bstrand60", "resi 593-596 & chain B ")
cmd.color ("red", "Bstrand60")


cmd.select("Bstrand61", "resi 603-611 & chain B ")
cmd.color ("green", "Bstrand61")


cmd.select("Bstrand62", "resi 619-627 & chain B ")
cmd.color ("orange", "Bstrand62")


cmd.select("Bstrand63", "resi 634-642 & chain B ")
cmd.color ("teal", "Bstrand63")


cmd.select("Bstrand64", "resi 645-656 & chain B ")
cmd.color ("yellow", "Bstrand64")


cmd.select("barrel", "Astrand* or Bstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
