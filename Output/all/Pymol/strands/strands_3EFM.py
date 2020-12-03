from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3EFM.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 54-57 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 81-83 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 91-94 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 97-98 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 101-104 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 107-110 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 127-134 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 148-154 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 162-170 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 174-184 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 191-202 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 211-225 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 228-241 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 261-275 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 281-297 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 302-323 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 326-347 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 368-387 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("Astrand18", "resi 390-407 & chain A ")
cmd.color ("red", "Astrand18")


cmd.select("Astrand19", "resi 410-429 & chain A ")
cmd.color ("green", "Astrand19")


cmd.select("Astrand20", "resi 434-445 & chain A ")
cmd.color ("orange", "Astrand20")


cmd.select("Astrand21", "resi 460-473 & chain A ")
cmd.color ("teal", "Astrand21")


cmd.select("Astrand22", "resi 478-495 & chain A ")
cmd.color ("yellow", "Astrand22")


cmd.select("Astrand23", "resi 510-513 & chain A ")
cmd.color ("blue", "Astrand23")


cmd.select("Astrand24", "resi 517-530 & chain A ")
cmd.color ("red", "Astrand24")


cmd.select("Astrand25", "resi 533-545 & chain A ")
cmd.color ("green", "Astrand25")


cmd.select("Astrand26", "resi 559-568 & chain A ")
cmd.color ("orange", "Astrand26")


cmd.select("Astrand27", "resi 576-586 & chain A ")
cmd.color ("teal", "Astrand27")


cmd.select("Astrand28", "resi 597-609 & chain A ")
cmd.color ("yellow", "Astrand28")


cmd.select("Astrand29", "resi 612-619 & chain A ")
cmd.color ("blue", "Astrand29")


cmd.select("Astrand30", "resi 643-651 & chain A ")
cmd.color ("red", "Astrand30")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
