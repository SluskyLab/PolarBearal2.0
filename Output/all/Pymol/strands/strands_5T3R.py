from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5T3R.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 58-61 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 213-214 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 224-225 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 267-271 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 301-304 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 313-314 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 336-337 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 345-346 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 351-352 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 355-359 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 377-378 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 390-392 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 396-398 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 402-406 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 457-458 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Dstrand15", "resi 212-224 & chain D ")
cmd.color ("teal", "Dstrand15")


cmd.select("Dstrand16", "resi 260-265 & chain D ")
cmd.color ("yellow", "Dstrand16")


cmd.select("Dstrand17", "resi 271-277 & chain D ")
cmd.color ("blue", "Dstrand17")


cmd.select("Dstrand18", "resi 303-315 & chain D ")
cmd.color ("red", "Dstrand18")


cmd.select("Dstrand19", "resi 319-331 & chain D ")
cmd.color ("green", "Dstrand19")


cmd.select("Dstrand20", "resi 339-353 & chain D ")
cmd.color ("orange", "Dstrand20")


cmd.select("Dstrand21", "resi 357-371 & chain D ")
cmd.color ("teal", "Dstrand21")


cmd.select("Dstrand22", "resi 421-435 & chain D ")
cmd.color ("yellow", "Dstrand22")


cmd.select("Dstrand23", "resi 441-460 & chain D ")
cmd.color ("blue", "Dstrand23")


cmd.select("Dstrand24", "resi 464-465 & chain D ")
cmd.color ("red", "Dstrand24")


cmd.select("Dstrand25", "resi 468-469 & chain D ")
cmd.color ("green", "Dstrand25")


cmd.select("Dstrand26", "resi 475-494 & chain D ")
cmd.color ("orange", "Dstrand26")


cmd.select("Dstrand27", "resi 502-524 & chain D ")
cmd.color ("teal", "Dstrand27")


cmd.select("Dstrand28", "resi 543-564 & chain D ")
cmd.color ("yellow", "Dstrand28")


cmd.select("Dstrand29", "resi 569-580 & chain D ")
cmd.color ("blue", "Dstrand29")


cmd.select("Dstrand30", "resi 591-599 & chain D ")
cmd.color ("red", "Dstrand30")


cmd.select("Dstrand31", "resi 615-616 & chain D ")
cmd.color ("green", "Dstrand31")


cmd.select("Dstrand32", "resi 620-627 & chain D ")
cmd.color ("orange", "Dstrand32")


cmd.select("Dstrand33", "resi 639-640 & chain D ")
cmd.color ("teal", "Dstrand33")


cmd.select("Dstrand34", "resi 674-675 & chain D ")
cmd.color ("yellow", "Dstrand34")


cmd.select("Dstrand35", "resi 686-693 & chain D ")
cmd.color ("blue", "Dstrand35")


cmd.select("Dstrand36", "resi 696-698 & chain D ")
cmd.color ("red", "Dstrand36")


cmd.select("Dstrand37", "resi 704-716 & chain D ")
cmd.color ("green", "Dstrand37")


cmd.select("Dstrand38", "resi 719-723 & chain D ")
cmd.color ("orange", "Dstrand38")


cmd.select("Dstrand39", "resi 733-737 & chain D ")
cmd.color ("teal", "Dstrand39")


cmd.select("Dstrand40", "resi 740-754 & chain D ")
cmd.color ("yellow", "Dstrand40")


cmd.select("Dstrand41", "resi 761-777 & chain D ")
cmd.color ("blue", "Dstrand41")


cmd.select("Dstrand42", "resi 804-806 & chain D ")
cmd.color ("red", "Dstrand42")


cmd.select("Dstrand43", "resi 809-812 & chain D ")
cmd.color ("green", "Dstrand43")


cmd.select("Dstrand44", "resi 833-835 & chain D ")
cmd.color ("orange", "Dstrand44")


cmd.select("Dstrand45", "resi 850-853 & chain D ")
cmd.color ("teal", "Dstrand45")


cmd.select("Dstrand46", "resi 859-869 & chain D ")
cmd.color ("yellow", "Dstrand46")


cmd.select("Dstrand47", "resi 872-882 & chain D ")
cmd.color ("blue", "Dstrand47")


cmd.select("Dstrand48", "resi 885-887 & chain D ")
cmd.color ("red", "Dstrand48")


cmd.select("Dstrand49", "resi 943-945 & chain D ")
cmd.color ("green", "Dstrand49")


cmd.select("Dstrand50", "resi 948-959 & chain D ")
cmd.color ("orange", "Dstrand50")


cmd.select("Dstrand51", "resi 972-980 & chain D ")
cmd.color ("teal", "Dstrand51")


cmd.select("Dstrand52", "resi 984-986 & chain D ")
cmd.color ("yellow", "Dstrand52")


cmd.select("Dstrand53", "resi 1006-1015 & chain D ")
cmd.color ("blue", "Dstrand53")


cmd.select("barrel", "Astrand* or Dstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
