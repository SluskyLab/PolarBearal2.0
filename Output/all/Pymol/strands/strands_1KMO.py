from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1KMO.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 104-108 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 130-131 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 148-149 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 161-164 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 167-168 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 189-195 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 211-216 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 224-233 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 243-253 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 258-269 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 278-289 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 295-309 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 332-346 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 352-371 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 374-377 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 380-397 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 400-423 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 436-457 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("Astrand18", "resi 460-477 & chain A ")
cmd.color ("red", "Astrand18")


cmd.select("Astrand19", "resi 483-502 & chain A ")
cmd.color ("green", "Astrand19")


cmd.select("Astrand20", "resi 505-516 & chain A ")
cmd.color ("orange", "Astrand20")


cmd.select("Astrand21", "resi 535-547 & chain A ")
cmd.color ("teal", "Astrand21")


cmd.select("Astrand22", "resi 551-565 & chain A ")
cmd.color ("yellow", "Astrand22")


cmd.select("Astrand23", "resi 579-593 & chain A ")
cmd.color ("blue", "Astrand23")


cmd.select("Astrand24", "resi 604-617 & chain A ")
cmd.color ("red", "Astrand24")


cmd.select("Astrand25", "resi 634-642 & chain A ")
cmd.color ("green", "Astrand25")


cmd.select("Astrand26", "resi 647-656 & chain A ")
cmd.color ("orange", "Astrand26")


cmd.select("Astrand27", "resi 681-691 & chain A ")
cmd.color ("teal", "Astrand27")


cmd.select("Astrand28", "resi 700-706 & chain A ")
cmd.color ("yellow", "Astrand28")


cmd.select("Astrand29", "resi 714-717 & chain A ")
cmd.color ("blue", "Astrand29")


cmd.select("Astrand30", "resi 724-727 & chain A ")
cmd.color ("red", "Astrand30")


cmd.select("Astrand31", "resi 732-740 & chain A ")
cmd.color ("green", "Astrand31")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
