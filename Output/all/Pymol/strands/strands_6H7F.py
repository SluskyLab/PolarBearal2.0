from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/6H7F.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 43-45 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 51-53 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 61-65 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 132-139 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 156-162 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 170-178 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 181-193 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 199-211 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 218-231 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 235-249 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 279-296 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 299-322 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 328-355 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 358-378 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 388-391 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 409-428 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 433-448 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 458-470 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("Astrand18", "resi 475-486 & chain A ")
cmd.color ("red", "Astrand18")


cmd.select("Astrand19", "resi 505-517 & chain A ")
cmd.color ("green", "Astrand19")


cmd.select("Astrand20", "resi 521-543 & chain A ")
cmd.color ("orange", "Astrand20")


cmd.select("Astrand21", "resi 546-550 & chain A ")
cmd.color ("teal", "Astrand21")


cmd.select("Astrand22", "resi 553-566 & chain A ")
cmd.color ("yellow", "Astrand22")


cmd.select("Astrand23", "resi 572-587 & chain A ")
cmd.color ("blue", "Astrand23")


cmd.select("Astrand24", "resi 604-615 & chain A ")
cmd.color ("red", "Astrand24")


cmd.select("Astrand25", "resi 619-630 & chain A ")
cmd.color ("green", "Astrand25")


cmd.select("Astrand26", "resi 646-659 & chain A ")
cmd.color ("orange", "Astrand26")


cmd.select("Astrand27", "resi 662-671 & chain A ")
cmd.color ("teal", "Astrand27")


cmd.select("Astrand28", "resi 694-702 & chain A ")
cmd.color ("yellow", "Astrand28")


cmd.select("Bstrand29", "resi 43-45 & chain B ")
cmd.color ("blue", "Bstrand29")


cmd.select("Bstrand30", "resi 51-53 & chain B ")
cmd.color ("red", "Bstrand30")


cmd.select("Bstrand31", "resi 61-65 & chain B ")
cmd.color ("green", "Bstrand31")


cmd.select("Bstrand32", "resi 132-139 & chain B ")
cmd.color ("orange", "Bstrand32")


cmd.select("Bstrand33", "resi 156-162 & chain B ")
cmd.color ("teal", "Bstrand33")


cmd.select("Bstrand34", "resi 170-178 & chain B ")
cmd.color ("yellow", "Bstrand34")


cmd.select("Bstrand35", "resi 181-193 & chain B ")
cmd.color ("blue", "Bstrand35")


cmd.select("Bstrand36", "resi 199-211 & chain B ")
cmd.color ("red", "Bstrand36")


cmd.select("Bstrand37", "resi 218-231 & chain B ")
cmd.color ("green", "Bstrand37")


cmd.select("Bstrand38", "resi 235-249 & chain B ")
cmd.color ("orange", "Bstrand38")


cmd.select("Bstrand39", "resi 279-296 & chain B ")
cmd.color ("teal", "Bstrand39")


cmd.select("Bstrand40", "resi 299-322 & chain B ")
cmd.color ("yellow", "Bstrand40")


cmd.select("Bstrand41", "resi 328-355 & chain B ")
cmd.color ("blue", "Bstrand41")


cmd.select("Bstrand42", "resi 358-378 & chain B ")
cmd.color ("red", "Bstrand42")


cmd.select("Bstrand43", "resi 388-391 & chain B ")
cmd.color ("green", "Bstrand43")


cmd.select("Bstrand44", "resi 409-428 & chain B ")
cmd.color ("orange", "Bstrand44")


cmd.select("Bstrand45", "resi 433-448 & chain B ")
cmd.color ("teal", "Bstrand45")


cmd.select("Bstrand46", "resi 458-470 & chain B ")
cmd.color ("yellow", "Bstrand46")


cmd.select("Bstrand47", "resi 475-486 & chain B ")
cmd.color ("blue", "Bstrand47")


cmd.select("Bstrand48", "resi 505-517 & chain B ")
cmd.color ("red", "Bstrand48")


cmd.select("Bstrand49", "resi 521-543 & chain B ")
cmd.color ("green", "Bstrand49")


cmd.select("Bstrand50", "resi 546-550 & chain B ")
cmd.color ("orange", "Bstrand50")


cmd.select("Bstrand51", "resi 553-566 & chain B ")
cmd.color ("teal", "Bstrand51")


cmd.select("Bstrand52", "resi 572-587 & chain B ")
cmd.color ("yellow", "Bstrand52")


cmd.select("Bstrand53", "resi 604-615 & chain B ")
cmd.color ("blue", "Bstrand53")


cmd.select("Bstrand54", "resi 619-630 & chain B ")
cmd.color ("red", "Bstrand54")


cmd.select("Bstrand55", "resi 646-659 & chain B ")
cmd.color ("green", "Bstrand55")


cmd.select("Bstrand56", "resi 662-671 & chain B ")
cmd.color ("orange", "Bstrand56")


cmd.select("Bstrand57", "resi 694-702 & chain B ")
cmd.color ("teal", "Bstrand57")


cmd.select("Cstrand58", "resi 43-45 & chain C ")
cmd.color ("yellow", "Cstrand58")


cmd.select("Cstrand59", "resi 51-53 & chain C ")
cmd.color ("blue", "Cstrand59")


cmd.select("Cstrand60", "resi 61-65 & chain C ")
cmd.color ("red", "Cstrand60")


cmd.select("Cstrand61", "resi 132-139 & chain C ")
cmd.color ("green", "Cstrand61")


cmd.select("Cstrand62", "resi 156-162 & chain C ")
cmd.color ("orange", "Cstrand62")


cmd.select("Cstrand63", "resi 170-178 & chain C ")
cmd.color ("teal", "Cstrand63")


cmd.select("Cstrand64", "resi 181-193 & chain C ")
cmd.color ("yellow", "Cstrand64")


cmd.select("Cstrand65", "resi 199-211 & chain C ")
cmd.color ("blue", "Cstrand65")


cmd.select("Cstrand66", "resi 218-231 & chain C ")
cmd.color ("red", "Cstrand66")


cmd.select("Cstrand67", "resi 235-249 & chain C ")
cmd.color ("green", "Cstrand67")


cmd.select("Cstrand68", "resi 279-296 & chain C ")
cmd.color ("orange", "Cstrand68")


cmd.select("Cstrand69", "resi 299-322 & chain C ")
cmd.color ("teal", "Cstrand69")


cmd.select("Cstrand70", "resi 328-355 & chain C ")
cmd.color ("yellow", "Cstrand70")


cmd.select("Cstrand71", "resi 358-378 & chain C ")
cmd.color ("blue", "Cstrand71")


cmd.select("Cstrand72", "resi 388-391 & chain C ")
cmd.color ("red", "Cstrand72")


cmd.select("Cstrand73", "resi 409-428 & chain C ")
cmd.color ("green", "Cstrand73")


cmd.select("Cstrand74", "resi 433-448 & chain C ")
cmd.color ("orange", "Cstrand74")


cmd.select("Cstrand75", "resi 458-470 & chain C ")
cmd.color ("teal", "Cstrand75")


cmd.select("Cstrand76", "resi 475-486 & chain C ")
cmd.color ("yellow", "Cstrand76")


cmd.select("Cstrand77", "resi 505-517 & chain C ")
cmd.color ("blue", "Cstrand77")


cmd.select("Cstrand78", "resi 521-543 & chain C ")
cmd.color ("red", "Cstrand78")


cmd.select("Cstrand79", "resi 546-550 & chain C ")
cmd.color ("green", "Cstrand79")


cmd.select("Cstrand80", "resi 553-566 & chain C ")
cmd.color ("orange", "Cstrand80")


cmd.select("Cstrand81", "resi 572-587 & chain C ")
cmd.color ("teal", "Cstrand81")


cmd.select("Cstrand82", "resi 604-615 & chain C ")
cmd.color ("yellow", "Cstrand82")


cmd.select("Cstrand83", "resi 619-630 & chain C ")
cmd.color ("blue", "Cstrand83")


cmd.select("Cstrand84", "resi 646-659 & chain C ")
cmd.color ("red", "Cstrand84")


cmd.select("Cstrand85", "resi 662-671 & chain C ")
cmd.color ("green", "Cstrand85")


cmd.select("Cstrand86", "resi 694-702 & chain C ")
cmd.color ("orange", "Cstrand86")


cmd.select("barrel", "Astrand* or Bstrand* or Cstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
