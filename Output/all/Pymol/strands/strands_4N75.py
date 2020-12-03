from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4N75.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 427-433 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 437-446 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 455-462 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 466-475 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 484-495 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 505-520 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 523-537 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 564-579 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 590-600 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 608-620 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 628-640 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 662-663 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 710-720 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 733-745 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 767-778 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 781-792 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 799-809 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Bstrand17", "resi 427-433 & chain B ")
cmd.color ("blue", "Bstrand17")


cmd.select("Bstrand18", "resi 437-446 & chain B ")
cmd.color ("red", "Bstrand18")


cmd.select("Bstrand19", "resi 455-462 & chain B ")
cmd.color ("green", "Bstrand19")


cmd.select("Bstrand20", "resi 466-475 & chain B ")
cmd.color ("orange", "Bstrand20")


cmd.select("Bstrand21", "resi 484-495 & chain B ")
cmd.color ("teal", "Bstrand21")


cmd.select("Bstrand22", "resi 505-520 & chain B ")
cmd.color ("yellow", "Bstrand22")


cmd.select("Bstrand23", "resi 523-537 & chain B ")
cmd.color ("blue", "Bstrand23")


cmd.select("Bstrand24", "resi 564-579 & chain B ")
cmd.color ("red", "Bstrand24")


cmd.select("Bstrand25", "resi 590-600 & chain B ")
cmd.color ("green", "Bstrand25")


cmd.select("Bstrand26", "resi 608-620 & chain B ")
cmd.color ("orange", "Bstrand26")


cmd.select("Bstrand27", "resi 628-640 & chain B ")
cmd.color ("teal", "Bstrand27")


cmd.select("Bstrand28", "resi 662-663 & chain B ")
cmd.color ("yellow", "Bstrand28")


cmd.select("Bstrand29", "resi 671-674 & chain B ")
cmd.color ("blue", "Bstrand29")


cmd.select("Bstrand30", "resi 700-705 & chain B ")
cmd.color ("red", "Bstrand30")


cmd.select("Bstrand31", "resi 710-720 & chain B ")
cmd.color ("green", "Bstrand31")


cmd.select("Bstrand32", "resi 733-745 & chain B ")
cmd.color ("orange", "Bstrand32")


cmd.select("Bstrand33", "resi 767-778 & chain B ")
cmd.color ("teal", "Bstrand33")


cmd.select("Bstrand34", "resi 781-792 & chain B ")
cmd.color ("yellow", "Bstrand34")


cmd.select("Bstrand35", "resi 799-809 & chain B ")
cmd.color ("blue", "Bstrand35")


cmd.select("barrel", "Astrand* or Bstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
