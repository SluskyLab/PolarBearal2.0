from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5AZP.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 25-26 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 81-95 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 99-117 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 253-254 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 292-303 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 315-325 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Bstrand6", "resi 25-26 & chain B ")
cmd.color ("red", "Bstrand6")


cmd.select("Bstrand7", "resi 81-95 & chain B ")
cmd.color ("green", "Bstrand7")


cmd.select("Bstrand8", "resi 99-118 & chain B ")
cmd.color ("orange", "Bstrand8")


cmd.select("Bstrand9", "resi 253-254 & chain B ")
cmd.color ("teal", "Bstrand9")


cmd.select("Bstrand10", "resi 292-303 & chain B ")
cmd.color ("yellow", "Bstrand10")


cmd.select("Bstrand11", "resi 315-325 & chain B ")
cmd.color ("blue", "Bstrand11")


cmd.select("Cstrand12", "resi 25-26 & chain C ")
cmd.color ("red", "Cstrand12")


cmd.select("Cstrand13", "resi 81-95 & chain C ")
cmd.color ("green", "Cstrand13")


cmd.select("Cstrand14", "resi 99-117 & chain C ")
cmd.color ("orange", "Cstrand14")


cmd.select("Cstrand15", "resi 253-254 & chain C ")
cmd.color ("teal", "Cstrand15")


cmd.select("Cstrand16", "resi 292-303 & chain C ")
cmd.color ("yellow", "Cstrand16")


cmd.select("Cstrand17", "resi 315-325 & chain C ")
cmd.color ("blue", "Cstrand17")


cmd.select("barrel", "Astrand* or Bstrand* or Cstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
