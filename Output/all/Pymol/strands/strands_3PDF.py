from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3PDF.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 2-2 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 5-7 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 14-20 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 24-25 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 29-29 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 36-45 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 49-52 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 57-63 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 67-72 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 75-80 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 83-86 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 90-93 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 96-97 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 100-103 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 109-116 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 210-212 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 215-216 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 219-222 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("Astrand18", "resi 226-227 & chain A ")
cmd.color ("red", "Astrand18")


cmd.select("Astrand19", "resi 232-232 & chain A ")
cmd.color ("green", "Astrand19")


cmd.select("Astrand20", "resi 255-255 & chain A ")
cmd.color ("orange", "Astrand20")


cmd.select("Astrand21", "resi 258-260 & chain A ")
cmd.color ("teal", "Astrand21")


cmd.select("Astrand22", "resi 271-271 & chain A ")
cmd.color ("yellow", "Astrand22")


cmd.select("Astrand23", "resi 277-278 & chain A ")
cmd.color ("blue", "Astrand23")


cmd.select("Astrand24", "resi 292-294 & chain A ")
cmd.color ("red", "Astrand24")


cmd.select("Astrand25", "resi 298-298 & chain A ")
cmd.color ("green", "Astrand25")


cmd.select("Astrand26", "resi 303-304 & chain A ")
cmd.color ("orange", "Astrand26")


cmd.select("Astrand27", "resi 308-322 & chain A ")
cmd.color ("teal", "Astrand27")


cmd.select("Astrand28", "resi 327-327 & chain A ")
cmd.color ("yellow", "Astrand28")


cmd.select("Astrand29", "resi 332-332 & chain A ")
cmd.color ("blue", "Astrand29")


cmd.select("Astrand30", "resi 346-353 & chain A ")
cmd.color ("red", "Astrand30")


cmd.select("Astrand31", "resi 361-366 & chain A ")
cmd.color ("green", "Astrand31")


cmd.select("Astrand32", "resi 374-374 & chain A ")
cmd.color ("orange", "Astrand32")


cmd.select("Astrand33", "resi 377-384 & chain A ")
cmd.color ("teal", "Astrand33")


cmd.select("Astrand34", "resi 387-390 & chain A ")
cmd.color ("yellow", "Astrand34")


cmd.select("Astrand35", "resi 396-403 & chain A ")
cmd.color ("blue", "Astrand35")


cmd.select("Astrand36", "resi 411-411 & chain A ")
cmd.color ("red", "Astrand36")


cmd.select("Astrand37", "resi 414-419 & chain A ")
cmd.color ("green", "Astrand37")


cmd.select("Astrand38", "resi 431-436 & chain A ")
cmd.color ("orange", "Astrand38")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
