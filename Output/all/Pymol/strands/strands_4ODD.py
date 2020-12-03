from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4ODD.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 13-22 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 36-44 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 49-57 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 62-71 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 77-80 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 84-92 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 96-104 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 110-118 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 145-147 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Bstrand9", "resi 13-22 & chain B ")
cmd.color ("teal", "Bstrand9")


cmd.select("Bstrand10", "resi 36-44 & chain B ")
cmd.color ("yellow", "Bstrand10")


cmd.select("Bstrand11", "resi 49-57 & chain B ")
cmd.color ("blue", "Bstrand11")


cmd.select("Bstrand12", "resi 62-71 & chain B ")
cmd.color ("red", "Bstrand12")


cmd.select("Bstrand13", "resi 77-80 & chain B ")
cmd.color ("green", "Bstrand13")


cmd.select("Bstrand14", "resi 84-92 & chain B ")
cmd.color ("orange", "Bstrand14")


cmd.select("Bstrand15", "resi 96-104 & chain B ")
cmd.color ("teal", "Bstrand15")


cmd.select("Bstrand16", "resi 110-118 & chain B ")
cmd.color ("yellow", "Bstrand16")


cmd.select("Bstrand17", "resi 145-147 & chain B ")
cmd.color ("blue", "Bstrand17")


cmd.select("Cstrand18", "resi 13-22 & chain C ")
cmd.color ("red", "Cstrand18")


cmd.select("Cstrand19", "resi 37-44 & chain C ")
cmd.color ("green", "Cstrand19")


cmd.select("Cstrand20", "resi 49-58 & chain C ")
cmd.color ("orange", "Cstrand20")


cmd.select("Cstrand21", "resi 61-71 & chain C ")
cmd.color ("teal", "Cstrand21")


cmd.select("Cstrand22", "resi 77-80 & chain C ")
cmd.color ("yellow", "Cstrand22")


cmd.select("Cstrand23", "resi 84-91 & chain C ")
cmd.color ("blue", "Cstrand23")


cmd.select("Cstrand24", "resi 96-104 & chain C ")
cmd.color ("red", "Cstrand24")


cmd.select("Cstrand25", "resi 110-118 & chain C ")
cmd.color ("green", "Cstrand25")


cmd.select("Cstrand26", "resi 145-147 & chain C ")
cmd.color ("orange", "Cstrand26")


cmd.select("barrel", "Astrand* or Bstrand* or Cstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
