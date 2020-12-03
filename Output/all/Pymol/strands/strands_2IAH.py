from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2IAH.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 46-50 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 53-54 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 69-72 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 81-82 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 85-89 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 105-109 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 112-116 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 168-173 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 196-201 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 204-209 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 212-213 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 217-219 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 222-223 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 243-251 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 263-270 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 278-286 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 290-300 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 307-319 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("Astrand18", "resi 326-341 & chain A ")
cmd.color ("red", "Astrand18")


cmd.select("Astrand19", "resi 344-358 & chain A ")
cmd.color ("green", "Astrand19")


cmd.select("Astrand20", "resi 366-367 & chain A ")
cmd.color ("orange", "Astrand20")


cmd.select("Astrand21", "resi 392-405 & chain A ")
cmd.color ("teal", "Astrand21")


cmd.select("Astrand22", "resi 411-430 & chain A ")
cmd.color ("yellow", "Astrand22")


cmd.select("Astrand23", "resi 441-466 & chain A ")
cmd.color ("blue", "Astrand23")


cmd.select("Astrand24", "resi 471-490 & chain A ")
cmd.color ("red", "Astrand24")


cmd.select("Astrand25", "resi 499-500 & chain A ")
cmd.color ("green", "Astrand25")


cmd.select("Astrand26", "resi 520-537 & chain A ")
cmd.color ("orange", "Astrand26")


cmd.select("Astrand27", "resi 543-558 & chain A ")
cmd.color ("teal", "Astrand27")


cmd.select("Astrand28", "resi 563-578 & chain A ")
cmd.color ("yellow", "Astrand28")


cmd.select("Astrand29", "resi 583-594 & chain A ")
cmd.color ("blue", "Astrand29")


cmd.select("Astrand30", "resi 611-624 & chain A ")
cmd.color ("red", "Astrand30")


cmd.select("Astrand31", "resi 629-645 & chain A ")
cmd.color ("green", "Astrand31")


cmd.select("Astrand32", "resi 664-682 & chain A ")
cmd.color ("orange", "Astrand32")


cmd.select("Astrand33", "resi 685-693 & chain A ")
cmd.color ("teal", "Astrand33")


cmd.select("Astrand34", "resi 696-697 & chain A ")
cmd.color ("yellow", "Astrand34")


cmd.select("Astrand35", "resi 711-720 & chain A ")
cmd.color ("blue", "Astrand35")


cmd.select("Astrand36", "resi 728-737 & chain A ")
cmd.color ("red", "Astrand36")


cmd.select("Astrand37", "resi 740-746 & chain A ")
cmd.color ("green", "Astrand37")


cmd.select("Astrand38", "resi 751-757 & chain A ")
cmd.color ("orange", "Astrand38")


cmd.select("Astrand39", "resi 760-770 & chain A ")
cmd.color ("teal", "Astrand39")


cmd.select("Astrand40", "resi 776-782 & chain A ")
cmd.color ("yellow", "Astrand40")


cmd.select("Astrand41", "resi 790-792 & chain A ")
cmd.color ("blue", "Astrand41")


cmd.select("Astrand42", "resi 798-801 & chain A ")
cmd.color ("red", "Astrand42")


cmd.select("Astrand43", "resi 806-812 & chain A ")
cmd.color ("green", "Astrand43")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
