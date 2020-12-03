from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4AIP.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 67-72 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 95-97 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 107-109 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 118-121 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 144-151 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 165-171 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 185-194 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 198-209 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 212-223 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 246-259 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 264-279 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 302-318 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 323-339 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 355-373 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 376-390 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 438-452 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 455-469 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 475-492 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("Astrand18", "resi 495-506 & chain A ")
cmd.color ("red", "Astrand18")


cmd.select("Astrand19", "resi 522-525 & chain A ")
cmd.color ("green", "Astrand19")


cmd.select("Astrand20", "resi 532-544 & chain A ")
cmd.color ("orange", "Astrand20")


cmd.select("Astrand21", "resi 548-560 & chain A ")
cmd.color ("teal", "Astrand21")


cmd.select("Astrand22", "resi 575-578 & chain A ")
cmd.color ("yellow", "Astrand22")


cmd.select("Astrand23", "resi 582-597 & chain A ")
cmd.color ("blue", "Astrand23")


cmd.select("Astrand24", "resi 600-609 & chain A ")
cmd.color ("red", "Astrand24")


cmd.select("Astrand25", "resi 635-644 & chain A ")
cmd.color ("green", "Astrand25")


cmd.select("Astrand26", "resi 648-658 & chain A ")
cmd.color ("orange", "Astrand26")


cmd.select("Astrand27", "resi 661-662 & chain A ")
cmd.color ("teal", "Astrand27")


cmd.select("Astrand28", "resi 681-682 & chain A ")
cmd.color ("yellow", "Astrand28")


cmd.select("Astrand29", "resi 685-695 & chain A ")
cmd.color ("blue", "Astrand29")


cmd.select("Astrand30", "resi 702-709 & chain A ")
cmd.color ("red", "Astrand30")


cmd.select("Astrand31", "resi 733-741 & chain A ")
cmd.color ("green", "Astrand31")


cmd.select("Bstrand32", "resi 67-73 & chain B ")
cmd.color ("orange", "Bstrand32")


cmd.select("Bstrand33", "resi 95-97 & chain B ")
cmd.color ("teal", "Bstrand33")


cmd.select("Bstrand34", "resi 107-109 & chain B ")
cmd.color ("yellow", "Bstrand34")


cmd.select("Bstrand35", "resi 112-113 & chain B ")
cmd.color ("blue", "Bstrand35")


cmd.select("Bstrand36", "resi 118-121 & chain B ")
cmd.color ("red", "Bstrand36")


cmd.select("Bstrand37", "resi 144-151 & chain B ")
cmd.color ("green", "Bstrand37")


cmd.select("Bstrand38", "resi 165-171 & chain B ")
cmd.color ("orange", "Bstrand38")


cmd.select("Bstrand39", "resi 185-194 & chain B ")
cmd.color ("teal", "Bstrand39")


cmd.select("Bstrand40", "resi 198-209 & chain B ")
cmd.color ("yellow", "Bstrand40")


cmd.select("Bstrand41", "resi 212-223 & chain B ")
cmd.color ("blue", "Bstrand41")


cmd.select("Bstrand42", "resi 246-259 & chain B ")
cmd.color ("red", "Bstrand42")


cmd.select("Bstrand43", "resi 264-279 & chain B ")
cmd.color ("green", "Bstrand43")


cmd.select("Bstrand44", "resi 302-318 & chain B ")
cmd.color ("orange", "Bstrand44")


cmd.select("Bstrand45", "resi 325-339 & chain B ")
cmd.color ("teal", "Bstrand45")


cmd.select("Bstrand46", "resi 355-373 & chain B ")
cmd.color ("yellow", "Bstrand46")


cmd.select("Bstrand47", "resi 376-390 & chain B ")
cmd.color ("blue", "Bstrand47")


cmd.select("Bstrand48", "resi 438-452 & chain B ")
cmd.color ("red", "Bstrand48")


cmd.select("Bstrand49", "resi 455-469 & chain B ")
cmd.color ("green", "Bstrand49")


cmd.select("Bstrand50", "resi 475-492 & chain B ")
cmd.color ("orange", "Bstrand50")


cmd.select("Bstrand51", "resi 495-506 & chain B ")
cmd.color ("teal", "Bstrand51")


cmd.select("Bstrand52", "resi 522-525 & chain B ")
cmd.color ("yellow", "Bstrand52")


cmd.select("Bstrand53", "resi 532-544 & chain B ")
cmd.color ("blue", "Bstrand53")


cmd.select("Bstrand54", "resi 548-563 & chain B ")
cmd.color ("red", "Bstrand54")


cmd.select("Bstrand55", "resi 567-568 & chain B ")
cmd.color ("green", "Bstrand55")


cmd.select("Bstrand56", "resi 575-597 & chain B ")
cmd.color ("orange", "Bstrand56")


cmd.select("Bstrand57", "resi 600-609 & chain B ")
cmd.color ("teal", "Bstrand57")


cmd.select("Bstrand58", "resi 635-644 & chain B ")
cmd.color ("yellow", "Bstrand58")


cmd.select("Bstrand59", "resi 649-658 & chain B ")
cmd.color ("blue", "Bstrand59")


cmd.select("Bstrand60", "resi 661-662 & chain B ")
cmd.color ("red", "Bstrand60")


cmd.select("Bstrand61", "resi 681-682 & chain B ")
cmd.color ("green", "Bstrand61")


cmd.select("Bstrand62", "resi 685-694 & chain B ")
cmd.color ("orange", "Bstrand62")


cmd.select("Bstrand63", "resi 702-709 & chain B ")
cmd.color ("teal", "Bstrand63")


cmd.select("Bstrand64", "resi 733-741 & chain B ")
cmd.color ("yellow", "Bstrand64")


cmd.select("Cstrand65", "resi 67-72 & chain C ")
cmd.color ("blue", "Cstrand65")


cmd.select("Cstrand66", "resi 95-97 & chain C ")
cmd.color ("red", "Cstrand66")


cmd.select("Cstrand67", "resi 107-109 & chain C ")
cmd.color ("green", "Cstrand67")


cmd.select("Cstrand68", "resi 112-113 & chain C ")
cmd.color ("orange", "Cstrand68")


cmd.select("Cstrand69", "resi 118-121 & chain C ")
cmd.color ("teal", "Cstrand69")


cmd.select("Cstrand70", "resi 144-151 & chain C ")
cmd.color ("yellow", "Cstrand70")


cmd.select("Cstrand71", "resi 165-171 & chain C ")
cmd.color ("blue", "Cstrand71")


cmd.select("Cstrand72", "resi 185-194 & chain C ")
cmd.color ("red", "Cstrand72")


cmd.select("Cstrand73", "resi 198-209 & chain C ")
cmd.color ("green", "Cstrand73")


cmd.select("Cstrand74", "resi 212-223 & chain C ")
cmd.color ("orange", "Cstrand74")


cmd.select("Cstrand75", "resi 246-259 & chain C ")
cmd.color ("teal", "Cstrand75")


cmd.select("Cstrand76", "resi 264-279 & chain C ")
cmd.color ("yellow", "Cstrand76")


cmd.select("Cstrand77", "resi 302-320 & chain C ")
cmd.color ("blue", "Cstrand77")


cmd.select("Cstrand78", "resi 323-339 & chain C ")
cmd.color ("red", "Cstrand78")


cmd.select("Cstrand79", "resi 355-373 & chain C ")
cmd.color ("green", "Cstrand79")


cmd.select("Cstrand80", "resi 376-390 & chain C ")
cmd.color ("orange", "Cstrand80")


cmd.select("Cstrand81", "resi 438-452 & chain C ")
cmd.color ("teal", "Cstrand81")


cmd.select("Cstrand82", "resi 455-469 & chain C ")
cmd.color ("yellow", "Cstrand82")


cmd.select("Cstrand83", "resi 475-492 & chain C ")
cmd.color ("blue", "Cstrand83")


cmd.select("Cstrand84", "resi 495-506 & chain C ")
cmd.color ("red", "Cstrand84")


cmd.select("Cstrand85", "resi 523-525 & chain C ")
cmd.color ("green", "Cstrand85")


cmd.select("Cstrand86", "resi 532-544 & chain C ")
cmd.color ("orange", "Cstrand86")


cmd.select("Cstrand87", "resi 548-563 & chain C ")
cmd.color ("teal", "Cstrand87")


cmd.select("Cstrand88", "resi 576-597 & chain C ")
cmd.color ("yellow", "Cstrand88")


cmd.select("Cstrand89", "resi 600-609 & chain C ")
cmd.color ("blue", "Cstrand89")


cmd.select("Cstrand90", "resi 635-644 & chain C ")
cmd.color ("red", "Cstrand90")


cmd.select("Cstrand91", "resi 649-658 & chain C ")
cmd.color ("green", "Cstrand91")


cmd.select("Cstrand92", "resi 685-694 & chain C ")
cmd.color ("orange", "Cstrand92")


cmd.select("Cstrand93", "resi 702-709 & chain C ")
cmd.color ("teal", "Cstrand93")


cmd.select("Cstrand94", "resi 733-741 & chain C ")
cmd.color ("yellow", "Cstrand94")


cmd.select("barrel", "Astrand* or Bstrand* or Cstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
