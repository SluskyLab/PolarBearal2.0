from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/6E4V.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 81-85 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 109-114 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 117-122 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 125-126 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 129-132 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 135-138 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 155-162 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 176-182 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 191-199 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 203-213 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 220-232 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 239-253 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 257-271 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 302-319 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 322-342 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 345-346 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 353-354 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 368-392 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("Astrand18", "resi 395-419 & chain A ")
cmd.color ("red", "Astrand18")


cmd.select("Astrand19", "resi 443-464 & chain A ")
cmd.color ("green", "Astrand19")


cmd.select("Astrand20", "resi 467-481 & chain A ")
cmd.color ("orange", "Astrand20")


cmd.select("Astrand21", "resi 486-501 & chain A ")
cmd.color ("teal", "Astrand21")


cmd.select("Astrand22", "resi 506-517 & chain A ")
cmd.color ("yellow", "Astrand22")


cmd.select("Astrand23", "resi 532-545 & chain A ")
cmd.color ("blue", "Astrand23")


cmd.select("Astrand24", "resi 550-571 & chain A ")
cmd.color ("red", "Astrand24")


cmd.select("Astrand25", "resi 579-584 & chain A ")
cmd.color ("green", "Astrand25")


cmd.select("Astrand26", "resi 588-601 & chain A ")
cmd.color ("orange", "Astrand26")


cmd.select("Astrand27", "resi 604-616 & chain A ")
cmd.color ("teal", "Astrand27")


cmd.select("Astrand28", "resi 630-639 & chain A ")
cmd.color ("yellow", "Astrand28")


cmd.select("Astrand29", "resi 646-655 & chain A ")
cmd.color ("blue", "Astrand29")


cmd.select("Astrand30", "resi 658-664 & chain A ")
cmd.color ("red", "Astrand30")


cmd.select("Astrand31", "resi 667-673 & chain A ")
cmd.color ("green", "Astrand31")


cmd.select("Astrand32", "resi 676-686 & chain A ")
cmd.color ("orange", "Astrand32")


cmd.select("Astrand33", "resi 691-698 & chain A ")
cmd.color ("teal", "Astrand33")


cmd.select("Astrand34", "resi 720-728 & chain A ")
cmd.color ("yellow", "Astrand34")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
