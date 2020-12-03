from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/6FOK.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 27-30 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 54-57 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 65-68 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 71-72 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 76-80 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 107-112 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 126-131 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 141-151 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 155-166 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 169-180 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 195-206 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 212-225 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 233-249 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 255-272 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 290-308 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 311-332 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 337-339 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 347-363 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("Astrand18", "resi 369-384 & chain A ")
cmd.color ("red", "Astrand18")


cmd.select("Astrand19", "resi 388-389 & chain A ")
cmd.color ("green", "Astrand19")


cmd.select("Astrand20", "resi 398-399 & chain A ")
cmd.color ("orange", "Astrand20")


cmd.select("Astrand21", "resi 406-421 & chain A ")
cmd.color ("teal", "Astrand21")


cmd.select("Astrand22", "resi 427-438 & chain A ")
cmd.color ("yellow", "Astrand22")


cmd.select("Astrand23", "resi 465-477 & chain A ")
cmd.color ("blue", "Astrand23")


cmd.select("Astrand24", "resi 481-501 & chain A ")
cmd.color ("red", "Astrand24")


cmd.select("Astrand25", "resi 508-528 & chain A ")
cmd.color ("green", "Astrand25")


cmd.select("Astrand26", "resi 533-546 & chain A ")
cmd.color ("orange", "Astrand26")


cmd.select("Astrand27", "resi 551-552 & chain A ")
cmd.color ("teal", "Astrand27")


cmd.select("Astrand28", "resi 560-569 & chain A ")
cmd.color ("yellow", "Astrand28")


cmd.select("Astrand29", "resi 572-581 & chain A ")
cmd.color ("blue", "Astrand29")


cmd.select("Astrand30", "resi 591-592 & chain A ")
cmd.color ("red", "Astrand30")


cmd.select("Astrand31", "resi 605-615 & chain A ")
cmd.color ("green", "Astrand31")


cmd.select("Astrand32", "resi 620-627 & chain A ")
cmd.color ("orange", "Astrand32")


cmd.select("Astrand33", "resi 660-668 & chain A ")
cmd.color ("teal", "Astrand33")


cmd.select("Bstrand34", "resi 27-30 & chain B ")
cmd.color ("yellow", "Bstrand34")


cmd.select("Bstrand35", "resi 54-57 & chain B ")
cmd.color ("blue", "Bstrand35")


cmd.select("Bstrand36", "resi 65-68 & chain B ")
cmd.color ("red", "Bstrand36")


cmd.select("Bstrand37", "resi 71-72 & chain B ")
cmd.color ("green", "Bstrand37")


cmd.select("Bstrand38", "resi 76-80 & chain B ")
cmd.color ("orange", "Bstrand38")


cmd.select("Bstrand39", "resi 107-112 & chain B ")
cmd.color ("teal", "Bstrand39")


cmd.select("Bstrand40", "resi 126-131 & chain B ")
cmd.color ("yellow", "Bstrand40")


cmd.select("Bstrand41", "resi 141-151 & chain B ")
cmd.color ("blue", "Bstrand41")


cmd.select("Bstrand42", "resi 155-166 & chain B ")
cmd.color ("red", "Bstrand42")


cmd.select("Bstrand43", "resi 169-180 & chain B ")
cmd.color ("green", "Bstrand43")


cmd.select("Bstrand44", "resi 183-184 & chain B ")
cmd.color ("orange", "Bstrand44")


cmd.select("Bstrand45", "resi 190-191 & chain B ")
cmd.color ("teal", "Bstrand45")


cmd.select("Bstrand46", "resi 195-206 & chain B ")
cmd.color ("yellow", "Bstrand46")


cmd.select("Bstrand47", "resi 212-225 & chain B ")
cmd.color ("blue", "Bstrand47")


cmd.select("Bstrand48", "resi 233-249 & chain B ")
cmd.color ("red", "Bstrand48")


cmd.select("Bstrand49", "resi 255-272 & chain B ")
cmd.color ("green", "Bstrand49")


cmd.select("Bstrand50", "resi 290-308 & chain B ")
cmd.color ("orange", "Bstrand50")


cmd.select("Bstrand51", "resi 311-332 & chain B ")
cmd.color ("teal", "Bstrand51")


cmd.select("Bstrand52", "resi 337-339 & chain B ")
cmd.color ("yellow", "Bstrand52")


cmd.select("Bstrand53", "resi 347-366 & chain B ")
cmd.color ("blue", "Bstrand53")


cmd.select("Bstrand54", "resi 369-384 & chain B ")
cmd.color ("red", "Bstrand54")


cmd.select("Bstrand55", "resi 388-389 & chain B ")
cmd.color ("green", "Bstrand55")


cmd.select("Bstrand56", "resi 398-399 & chain B ")
cmd.color ("orange", "Bstrand56")


cmd.select("Bstrand57", "resi 406-421 & chain B ")
cmd.color ("teal", "Bstrand57")


cmd.select("Bstrand58", "resi 427-438 & chain B ")
cmd.color ("yellow", "Bstrand58")


cmd.select("Bstrand59", "resi 465-477 & chain B ")
cmd.color ("blue", "Bstrand59")


cmd.select("Bstrand60", "resi 481-503 & chain B ")
cmd.color ("red", "Bstrand60")


cmd.select("Bstrand61", "resi 506-528 & chain B ")
cmd.color ("green", "Bstrand61")


cmd.select("Bstrand62", "resi 533-546 & chain B ")
cmd.color ("orange", "Bstrand62")


cmd.select("Bstrand63", "resi 551-552 & chain B ")
cmd.color ("teal", "Bstrand63")


cmd.select("Bstrand64", "resi 560-569 & chain B ")
cmd.color ("yellow", "Bstrand64")


cmd.select("Bstrand65", "resi 572-581 & chain B ")
cmd.color ("blue", "Bstrand65")


cmd.select("Bstrand66", "resi 591-592 & chain B ")
cmd.color ("red", "Bstrand66")


cmd.select("Bstrand67", "resi 605-617 & chain B ")
cmd.color ("green", "Bstrand67")


cmd.select("Bstrand68", "resi 620-627 & chain B ")
cmd.color ("orange", "Bstrand68")


cmd.select("Bstrand69", "resi 660-668 & chain B ")
cmd.color ("teal", "Bstrand69")


cmd.select("barrel", "Astrand* or Bstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
