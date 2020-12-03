from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1GL4.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 367-367 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 371-376 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 379-383 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 388-389 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 394-396 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 400-414 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 419-433 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 438-446 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 485-494 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 497-497 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 500-507 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 510-511 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 515-525 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 534-547 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 550-562 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 566-566 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 573-584 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 590-590 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("Astrand18", "resi 594-594 & chain A ")
cmd.color ("red", "Astrand18")


cmd.select("Astrand19", "resi 600-613 & chain A ")
cmd.color ("green", "Astrand19")


cmd.select("Astrand20", "resi 618-628 & chain A ")
cmd.color ("orange", "Astrand20")


cmd.select("Bstrand21", "resi 1770-1774 & chain B ")
cmd.color ("teal", "Bstrand21")


cmd.select("Bstrand22", "resi 1779-1783 & chain B ")
cmd.color ("yellow", "Bstrand22")


cmd.select("Bstrand23", "resi 1787-1807 & chain B ")
cmd.color ("blue", "Bstrand23")


cmd.select("Bstrand24", "resi 1817-1820 & chain B ")
cmd.color ("red", "Bstrand24")


cmd.select("Bstrand25", "resi 1823-1827 & chain B ")
cmd.color ("green", "Bstrand25")


cmd.select("Bstrand26", "resi 1830-1830 & chain B ")
cmd.color ("orange", "Bstrand26")


cmd.select("Bstrand27", "resi 1836-1843 & chain B ")
cmd.color ("teal", "Bstrand27")


cmd.select("Bstrand28", "resi 1846-1856 & chain B ")
cmd.color ("yellow", "Bstrand28")


cmd.select("barrel", "Astrand* or Bstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
