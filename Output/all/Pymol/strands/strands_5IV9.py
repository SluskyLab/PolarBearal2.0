from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5IV9.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 29-31 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 34-36 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 42-53 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 56-66 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 79-89 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 93-103 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 108-118 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 124-133 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 138-147 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 157-166 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 171-180 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 185-195 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 208-212 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 216-220 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 223-228 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 231-240 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 245-256 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 259-268 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("Astrand18", "resi 286-297 & chain A ")
cmd.color ("red", "Astrand18")


cmd.select("Astrand19", "resi 301-310 & chain A ")
cmd.color ("green", "Astrand19")


cmd.select("Astrand20", "resi 330-340 & chain A ")
cmd.color ("orange", "Astrand20")


cmd.select("Astrand21", "resi 344-355 & chain A ")
cmd.color ("teal", "Astrand21")


cmd.select("Astrand22", "resi 364-379 & chain A ")
cmd.color ("yellow", "Astrand22")


cmd.select("Astrand23", "resi 382-395 & chain A ")
cmd.color ("blue", "Astrand23")


cmd.select("Astrand24", "resi 402-417 & chain A ")
cmd.color ("red", "Astrand24")


cmd.select("Astrand25", "resi 421-437 & chain A ")
cmd.color ("green", "Astrand25")


cmd.select("Astrand26", "resi 453-472 & chain A ")
cmd.color ("orange", "Astrand26")


cmd.select("Astrand27", "resi 478-489 & chain A ")
cmd.color ("teal", "Astrand27")


cmd.select("Astrand28", "resi 529-540 & chain A ")
cmd.color ("yellow", "Astrand28")


cmd.select("Astrand29", "resi 546-557 & chain A ")
cmd.color ("blue", "Astrand29")


cmd.select("Astrand30", "resi 577-587 & chain A ")
cmd.color ("red", "Astrand30")


cmd.select("Astrand31", "resi 595-602 & chain A ")
cmd.color ("green", "Astrand31")


cmd.select("Astrand32", "resi 607-617 & chain A ")
cmd.color ("orange", "Astrand32")


cmd.select("Astrand33", "resi 625-632 & chain A ")
cmd.color ("teal", "Astrand33")


cmd.select("Astrand34", "resi 654-661 & chain A ")
cmd.color ("yellow", "Astrand34")


cmd.select("Astrand35", "resi 672-678 & chain A ")
cmd.color ("blue", "Astrand35")


cmd.select("Astrand36", "resi 684-694 & chain A ")
cmd.color ("red", "Astrand36")


cmd.select("Astrand37", "resi 699-712 & chain A ")
cmd.color ("green", "Astrand37")


cmd.select("Astrand38", "resi 719-731 & chain A ")
cmd.color ("orange", "Astrand38")


cmd.select("Bstrand39", "resi 35-40 & chain B ")
cmd.color ("teal", "Bstrand39")


cmd.select("Bstrand40", "resi 61-62 & chain B ")
cmd.color ("yellow", "Bstrand40")


cmd.select("Bstrand41", "resi 74-89 & chain B ")
cmd.color ("blue", "Bstrand41")


cmd.select("Bstrand42", "resi 95-109 & chain B ")
cmd.color ("red", "Bstrand42")


cmd.select("Bstrand43", "resi 115-127 & chain B ")
cmd.color ("green", "Bstrand43")


cmd.select("barrel", "Astrand* or Bstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
