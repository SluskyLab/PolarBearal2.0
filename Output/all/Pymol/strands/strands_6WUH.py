from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/6WUH.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 30-32 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 51-54 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 87-90 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 104-105 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Bstrand4", "resi 139-140 & chain B ")
cmd.color ("yellow", "Bstrand4")


cmd.select("Bstrand5", "resi 157-158 & chain B ")
cmd.color ("blue", "Bstrand5")


cmd.select("Bstrand6", "resi 179-182 & chain B ")
cmd.color ("red", "Bstrand6")


cmd.select("Bstrand7", "resi 206-210 & chain B ")
cmd.color ("green", "Bstrand7")


cmd.select("Bstrand8", "resi 215-217 & chain B ")
cmd.color ("orange", "Bstrand8")


cmd.select("Bstrand9", "resi 234-235 & chain B ")
cmd.color ("teal", "Bstrand9")


cmd.select("Bstrand10", "resi 273-277 & chain B ")
cmd.color ("yellow", "Bstrand10")


cmd.select("Bstrand11", "resi 290-297 & chain B ")
cmd.color ("blue", "Bstrand11")


cmd.select("Bstrand12", "resi 310-316 & chain B ")
cmd.color ("red", "Bstrand12")


cmd.select("Bstrand13", "resi 336-344 & chain B ")
cmd.color ("green", "Bstrand13")


cmd.select("Bstrand14", "resi 395-402 & chain B ")
cmd.color ("orange", "Bstrand14")


cmd.select("Bstrand15", "resi 416-417 & chain B ")
cmd.color ("teal", "Bstrand15")


cmd.select("Bstrand16", "resi 420-423 & chain B ")
cmd.color ("yellow", "Bstrand16")


cmd.select("Bstrand17", "resi 426-428 & chain B ")
cmd.color ("blue", "Bstrand17")


cmd.select("Bstrand18", "resi 469-477 & chain B ")
cmd.color ("red", "Bstrand18")


cmd.select("Bstrand19", "resi 482-483 & chain B ")
cmd.color ("green", "Bstrand19")


cmd.select("Bstrand20", "resi 486-489 & chain B ")
cmd.color ("orange", "Bstrand20")


cmd.select("Bstrand21", "resi 492-494 & chain B ")
cmd.color ("teal", "Bstrand21")


cmd.select("Cstrand22", "resi 6-7 & chain C ")
cmd.color ("yellow", "Cstrand22")


cmd.select("Cstrand23", "resi 40-41 & chain C ")
cmd.color ("blue", "Cstrand23")


cmd.select("Cstrand24", "resi 54-56 & chain C ")
cmd.color ("red", "Cstrand24")


cmd.select("Cstrand25", "resi 63-65 & chain C ")
cmd.color ("green", "Cstrand25")


cmd.select("barrel", "Astrand* or Bstrand* or Cstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
