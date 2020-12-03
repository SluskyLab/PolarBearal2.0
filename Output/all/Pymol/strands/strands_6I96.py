from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/6I96.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 154-155 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 158-162 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 170-171 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 179-183 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 205-206 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 220-221 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 232-234 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 237-238 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 256-263 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 277-283 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 291-299 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 304-313 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 320-332 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 339-354 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 357-371 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 404-419 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 424-447 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 454-481 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("Astrand18", "resi 484-512 & chain A ")
cmd.color ("red", "Astrand18")


cmd.select("Astrand19", "resi 524-525 & chain A ")
cmd.color ("green", "Astrand19")


cmd.select("Astrand20", "resi 529-548 & chain A ")
cmd.color ("orange", "Astrand20")


cmd.select("Astrand21", "resi 551-568 & chain A ")
cmd.color ("teal", "Astrand21")


cmd.select("Astrand22", "resi 574-590 & chain A ")
cmd.color ("yellow", "Astrand22")


cmd.select("Astrand23", "resi 596-607 & chain A ")
cmd.color ("blue", "Astrand23")


cmd.select("Astrand24", "resi 622-633 & chain A ")
cmd.color ("red", "Astrand24")


cmd.select("Astrand25", "resi 641-656 & chain A ")
cmd.color ("green", "Astrand25")


cmd.select("Astrand26", "resi 665-683 & chain A ")
cmd.color ("orange", "Astrand26")


cmd.select("Astrand27", "resi 687-702 & chain A ")
cmd.color ("teal", "Astrand27")


cmd.select("Astrand28", "resi 718-727 & chain A ")
cmd.color ("yellow", "Astrand28")


cmd.select("Astrand29", "resi 736-745 & chain A ")
cmd.color ("blue", "Astrand29")


cmd.select("Astrand30", "resi 748-749 & chain A ")
cmd.color ("red", "Astrand30")


cmd.select("Astrand31", "resi 757-758 & chain A ")
cmd.color ("green", "Astrand31")


cmd.select("Astrand32", "resi 761-771 & chain A ")
cmd.color ("orange", "Astrand32")


cmd.select("Astrand33", "resi 780-787 & chain A ")
cmd.color ("teal", "Astrand33")


cmd.select("Astrand34", "resi 795-800 & chain A ")
cmd.color ("yellow", "Astrand34")


cmd.select("Astrand35", "resi 803-806 & chain A ")
cmd.color ("blue", "Astrand35")


cmd.select("Astrand36", "resi 811-819 & chain A ")
cmd.color ("red", "Astrand36")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
