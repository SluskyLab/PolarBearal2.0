from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2ICR.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 12-22 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 25-36 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 41-50 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 91-99 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 104-114 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 119-129 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 142-145 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 148-155 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 160-171 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 176-187 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 198-208 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 216-226 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Bstrand12", "resi 12-22 & chain B ")
cmd.color ("red", "Bstrand12")


cmd.select("Bstrand13", "resi 25-36 & chain B ")
cmd.color ("green", "Bstrand13")


cmd.select("Bstrand14", "resi 41-50 & chain B ")
cmd.color ("orange", "Bstrand14")


cmd.select("Bstrand15", "resi 91-99 & chain B ")
cmd.color ("teal", "Bstrand15")


cmd.select("Bstrand16", "resi 104-114 & chain B ")
cmd.color ("yellow", "Bstrand16")


cmd.select("Bstrand17", "resi 119-129 & chain B ")
cmd.color ("blue", "Bstrand17")


cmd.select("Bstrand18", "resi 142-145 & chain B ")
cmd.color ("red", "Bstrand18")


cmd.select("Bstrand19", "resi 148-155 & chain B ")
cmd.color ("green", "Bstrand19")


cmd.select("Bstrand20", "resi 160-171 & chain B ")
cmd.color ("orange", "Bstrand20")


cmd.select("Bstrand21", "resi 176-187 & chain B ")
cmd.color ("teal", "Bstrand21")


cmd.select("Bstrand22", "resi 198-208 & chain B ")
cmd.color ("yellow", "Bstrand22")


cmd.select("Bstrand23", "resi 216-226 & chain B ")
cmd.color ("blue", "Bstrand23")


cmd.select("Cstrand24", "resi 12-22 & chain C ")
cmd.color ("red", "Cstrand24")


cmd.select("Cstrand25", "resi 25-36 & chain C ")
cmd.color ("green", "Cstrand25")


cmd.select("Cstrand26", "resi 41-50 & chain C ")
cmd.color ("orange", "Cstrand26")


cmd.select("Cstrand27", "resi 91-99 & chain C ")
cmd.color ("teal", "Cstrand27")


cmd.select("Cstrand28", "resi 104-114 & chain C ")
cmd.color ("yellow", "Cstrand28")


cmd.select("Cstrand29", "resi 119-129 & chain C ")
cmd.color ("blue", "Cstrand29")


cmd.select("Cstrand30", "resi 142-145 & chain C ")
cmd.color ("red", "Cstrand30")


cmd.select("Cstrand31", "resi 148-155 & chain C ")
cmd.color ("green", "Cstrand31")


cmd.select("Cstrand32", "resi 160-171 & chain C ")
cmd.color ("orange", "Cstrand32")


cmd.select("Cstrand33", "resi 176-187 & chain C ")
cmd.color ("teal", "Cstrand33")


cmd.select("Cstrand34", "resi 198-208 & chain C ")
cmd.color ("yellow", "Cstrand34")


cmd.select("Cstrand35", "resi 216-226 & chain C ")
cmd.color ("blue", "Cstrand35")


cmd.select("Dstrand36", "resi 12-22 & chain D ")
cmd.color ("red", "Dstrand36")


cmd.select("Dstrand37", "resi 25-36 & chain D ")
cmd.color ("green", "Dstrand37")


cmd.select("Dstrand38", "resi 41-50 & chain D ")
cmd.color ("orange", "Dstrand38")


cmd.select("Dstrand39", "resi 91-99 & chain D ")
cmd.color ("teal", "Dstrand39")


cmd.select("Dstrand40", "resi 104-114 & chain D ")
cmd.color ("yellow", "Dstrand40")


cmd.select("Dstrand41", "resi 119-129 & chain D ")
cmd.color ("blue", "Dstrand41")


cmd.select("Dstrand42", "resi 142-145 & chain D ")
cmd.color ("red", "Dstrand42")


cmd.select("Dstrand43", "resi 148-155 & chain D ")
cmd.color ("green", "Dstrand43")


cmd.select("Dstrand44", "resi 160-171 & chain D ")
cmd.color ("orange", "Dstrand44")


cmd.select("Dstrand45", "resi 176-187 & chain D ")
cmd.color ("teal", "Dstrand45")


cmd.select("Dstrand46", "resi 198-208 & chain D ")
cmd.color ("yellow", "Dstrand46")


cmd.select("Dstrand47", "resi 215-226 & chain D ")
cmd.color ("blue", "Dstrand47")


cmd.select("barrel", "Astrand* or Bstrand* or Cstrand* or Dstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
