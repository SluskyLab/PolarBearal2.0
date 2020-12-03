from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1EK9.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 41-53 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 61-76 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 192-196 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 247-257 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 260-262 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 280-294 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 419-424 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Bstrand7", "resi 41-53 & chain B ")
cmd.color ("green", "Bstrand7")


cmd.select("Bstrand8", "resi 61-76 & chain B ")
cmd.color ("orange", "Bstrand8")


cmd.select("Bstrand9", "resi 192-196 & chain B ")
cmd.color ("teal", "Bstrand9")


cmd.select("Bstrand10", "resi 247-257 & chain B ")
cmd.color ("yellow", "Bstrand10")


cmd.select("Bstrand11", "resi 260-262 & chain B ")
cmd.color ("blue", "Bstrand11")


cmd.select("Bstrand12", "resi 280-294 & chain B ")
cmd.color ("red", "Bstrand12")


cmd.select("Bstrand13", "resi 419-424 & chain B ")
cmd.color ("green", "Bstrand13")


cmd.select("Cstrand14", "resi 41-53 & chain C ")
cmd.color ("orange", "Cstrand14")


cmd.select("Cstrand15", "resi 61-76 & chain C ")
cmd.color ("teal", "Cstrand15")


cmd.select("Cstrand16", "resi 192-196 & chain C ")
cmd.color ("yellow", "Cstrand16")


cmd.select("Cstrand17", "resi 247-257 & chain C ")
cmd.color ("blue", "Cstrand17")


cmd.select("Cstrand18", "resi 260-262 & chain C ")
cmd.color ("red", "Cstrand18")


cmd.select("Cstrand19", "resi 280-294 & chain C ")
cmd.color ("green", "Cstrand19")


cmd.select("Cstrand20", "resi 419-424 & chain C ")
cmd.color ("orange", "Cstrand20")


cmd.select("barrel", "Astrand* or Bstrand* or Cstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
