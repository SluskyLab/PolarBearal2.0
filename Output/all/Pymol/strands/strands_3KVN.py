from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3KVN.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 8-11 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 108-112 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 115-120 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 139-142 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 182-185 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 227-230 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 347-360 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 369-383 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 388-403 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 408-425 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 428-450 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 453-474 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 484-499 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 512-514 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 517-533 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 538-549 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 556-561 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 564-572 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("Astrand18", "resi 579-592 & chain A ")
cmd.color ("red", "Astrand18")


cmd.select("Astrand19", "resi 595-606 & chain A ")
cmd.color ("green", "Astrand19")


cmd.select("Astrand20", "resi 609-621 & chain A ")
cmd.color ("orange", "Astrand20")


cmd.select("Xstrand21", "resi 8-11 & chain X ")
cmd.color ("teal", "Xstrand21")


cmd.select("Xstrand22", "resi 108-112 & chain X ")
cmd.color ("yellow", "Xstrand22")


cmd.select("Xstrand23", "resi 115-120 & chain X ")
cmd.color ("blue", "Xstrand23")


cmd.select("Xstrand24", "resi 139-142 & chain X ")
cmd.color ("red", "Xstrand24")


cmd.select("Xstrand25", "resi 182-185 & chain X ")
cmd.color ("green", "Xstrand25")


cmd.select("Xstrand26", "resi 227-230 & chain X ")
cmd.color ("orange", "Xstrand26")


cmd.select("Xstrand27", "resi 348-360 & chain X ")
cmd.color ("teal", "Xstrand27")


cmd.select("Xstrand28", "resi 369-383 & chain X ")
cmd.color ("yellow", "Xstrand28")


cmd.select("Xstrand29", "resi 388-403 & chain X ")
cmd.color ("blue", "Xstrand29")


cmd.select("Xstrand30", "resi 408-425 & chain X ")
cmd.color ("red", "Xstrand30")


cmd.select("Xstrand31", "resi 428-450 & chain X ")
cmd.color ("green", "Xstrand31")


cmd.select("Xstrand32", "resi 453-474 & chain X ")
cmd.color ("orange", "Xstrand32")


cmd.select("Xstrand33", "resi 484-499 & chain X ")
cmd.color ("teal", "Xstrand33")


cmd.select("Xstrand34", "resi 512-514 & chain X ")
cmd.color ("yellow", "Xstrand34")


cmd.select("Xstrand35", "resi 517-533 & chain X ")
cmd.color ("blue", "Xstrand35")


cmd.select("Xstrand36", "resi 538-549 & chain X ")
cmd.color ("red", "Xstrand36")


cmd.select("Xstrand37", "resi 556-561 & chain X ")
cmd.color ("green", "Xstrand37")


cmd.select("Xstrand38", "resi 569-572 & chain X ")
cmd.color ("orange", "Xstrand38")


cmd.select("Xstrand39", "resi 579-592 & chain X ")
cmd.color ("teal", "Xstrand39")


cmd.select("Xstrand40", "resi 595-606 & chain X ")
cmd.color ("yellow", "Xstrand40")


cmd.select("Xstrand41", "resi 609-621 & chain X ")
cmd.color ("blue", "Xstrand41")


cmd.select("barrel", "Astrand* or Xstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
