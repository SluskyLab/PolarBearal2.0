from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2R73.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 29-35 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 50-57 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 60-69 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 72-82 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 88-92 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 96-102 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 109-118 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 121-130 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 157-159 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Bstrand9", "resi 29-35 & chain B ")
cmd.color ("teal", "Bstrand9")


cmd.select("Bstrand10", "resi 50-57 & chain B ")
cmd.color ("yellow", "Bstrand10")


cmd.select("Bstrand11", "resi 60-68 & chain B ")
cmd.color ("blue", "Bstrand11")


cmd.select("Bstrand12", "resi 73-82 & chain B ")
cmd.color ("red", "Bstrand12")


cmd.select("Bstrand13", "resi 88-92 & chain B ")
cmd.color ("green", "Bstrand13")


cmd.select("Bstrand14", "resi 96-102 & chain B ")
cmd.color ("orange", "Bstrand14")


cmd.select("Bstrand15", "resi 109-118 & chain B ")
cmd.color ("teal", "Bstrand15")


cmd.select("Bstrand16", "resi 121-130 & chain B ")
cmd.color ("yellow", "Bstrand16")


cmd.select("Bstrand17", "resi 157-159 & chain B ")
cmd.color ("blue", "Bstrand17")


cmd.select("Cstrand18", "resi 29-35 & chain C ")
cmd.color ("red", "Cstrand18")


cmd.select("Cstrand19", "resi 49-57 & chain C ")
cmd.color ("green", "Cstrand19")


cmd.select("Cstrand20", "resi 60-69 & chain C ")
cmd.color ("orange", "Cstrand20")


cmd.select("Cstrand21", "resi 72-82 & chain C ")
cmd.color ("teal", "Cstrand21")


cmd.select("Cstrand22", "resi 88-92 & chain C ")
cmd.color ("yellow", "Cstrand22")


cmd.select("Cstrand23", "resi 96-102 & chain C ")
cmd.color ("blue", "Cstrand23")


cmd.select("Cstrand24", "resi 109-118 & chain C ")
cmd.color ("red", "Cstrand24")


cmd.select("Cstrand25", "resi 121-130 & chain C ")
cmd.color ("green", "Cstrand25")


cmd.select("Cstrand26", "resi 157-159 & chain C ")
cmd.color ("orange", "Cstrand26")


cmd.select("Dstrand27", "resi 29-35 & chain D ")
cmd.color ("teal", "Dstrand27")


cmd.select("Dstrand28", "resi 49-57 & chain D ")
cmd.color ("yellow", "Dstrand28")


cmd.select("Dstrand29", "resi 60-69 & chain D ")
cmd.color ("blue", "Dstrand29")


cmd.select("Dstrand30", "resi 72-82 & chain D ")
cmd.color ("red", "Dstrand30")


cmd.select("Dstrand31", "resi 88-92 & chain D ")
cmd.color ("green", "Dstrand31")


cmd.select("Dstrand32", "resi 96-102 & chain D ")
cmd.color ("orange", "Dstrand32")


cmd.select("Dstrand33", "resi 109-118 & chain D ")
cmd.color ("teal", "Dstrand33")


cmd.select("Dstrand34", "resi 121-130 & chain D ")
cmd.color ("yellow", "Dstrand34")


cmd.select("Dstrand35", "resi 157-159 & chain D ")
cmd.color ("blue", "Dstrand35")


cmd.select("barrel", "Astrand* or Bstrand* or Cstrand* or Dstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
