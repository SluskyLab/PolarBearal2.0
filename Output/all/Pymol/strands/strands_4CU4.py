from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4CU4.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 32-33 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 41-42 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 50-54 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 76-77 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 91-92 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 104-106 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 109-110 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 126-133 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 147-153 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 161-169 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 173-183 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 190-202 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 209-224 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 227-238 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 274-289 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 294-317 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 340-367 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 370-401 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("Astrand18", "resi 431-453 & chain A ")
cmd.color ("red", "Astrand18")


cmd.select("Astrand19", "resi 456-473 & chain A ")
cmd.color ("green", "Astrand19")


cmd.select("Astrand20", "resi 478-495 & chain A ")
cmd.color ("orange", "Astrand20")


cmd.select("Astrand21", "resi 501-512 & chain A ")
cmd.color ("teal", "Astrand21")


cmd.select("Astrand22", "resi 527-538 & chain A ")
cmd.color ("yellow", "Astrand22")


cmd.select("Astrand23", "resi 545-562 & chain A ")
cmd.color ("blue", "Astrand23")


cmd.select("Astrand24", "resi 570-588 & chain A ")
cmd.color ("red", "Astrand24")


cmd.select("Astrand25", "resi 593-608 & chain A ")
cmd.color ("green", "Astrand25")


cmd.select("Astrand26", "resi 623-633 & chain A ")
cmd.color ("orange", "Astrand26")


cmd.select("Astrand27", "resi 641-650 & chain A ")
cmd.color ("teal", "Astrand27")


cmd.select("Astrand28", "resi 653-654 & chain A ")
cmd.color ("yellow", "Astrand28")


cmd.select("Astrand29", "resi 662-663 & chain A ")
cmd.color ("blue", "Astrand29")


cmd.select("Astrand30", "resi 666-676 & chain A ")
cmd.color ("red", "Astrand30")


cmd.select("Astrand31", "resi 686-692 & chain A ")
cmd.color ("green", "Astrand31")


cmd.select("Astrand32", "resi 700-705 & chain A ")
cmd.color ("orange", "Astrand32")


cmd.select("Astrand33", "resi 708-711 & chain A ")
cmd.color ("teal", "Astrand33")


cmd.select("Astrand34", "resi 716-724 & chain A ")
cmd.color ("yellow", "Astrand34")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
