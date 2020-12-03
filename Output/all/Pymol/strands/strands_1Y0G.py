from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1Y0G.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 24-27 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 34-42 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 46-52 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 55-60 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 70-76 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 80-81 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 104-115 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 118-127 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 130-145 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 151-162 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 178-189 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Bstrand11", "resi 24-27 & chain B ")
cmd.color ("blue", "Bstrand11")


cmd.select("Bstrand12", "resi 34-42 & chain B ")
cmd.color ("red", "Bstrand12")


cmd.select("Bstrand13", "resi 46-52 & chain B ")
cmd.color ("green", "Bstrand13")


cmd.select("Bstrand14", "resi 55-60 & chain B ")
cmd.color ("orange", "Bstrand14")


cmd.select("Bstrand15", "resi 70-76 & chain B ")
cmd.color ("teal", "Bstrand15")


cmd.select("Bstrand16", "resi 80-81 & chain B ")
cmd.color ("yellow", "Bstrand16")


cmd.select("Bstrand17", "resi 104-115 & chain B ")
cmd.color ("blue", "Bstrand17")


cmd.select("Bstrand18", "resi 118-127 & chain B ")
cmd.color ("red", "Bstrand18")


cmd.select("Bstrand19", "resi 130-145 & chain B ")
cmd.color ("green", "Bstrand19")


cmd.select("Bstrand20", "resi 151-162 & chain B ")
cmd.color ("orange", "Bstrand20")


cmd.select("Bstrand21", "resi 178-189 & chain B ")
cmd.color ("teal", "Bstrand21")


cmd.select("Cstrand22", "resi 24-27 & chain C ")
cmd.color ("yellow", "Cstrand22")


cmd.select("Cstrand23", "resi 34-42 & chain C ")
cmd.color ("blue", "Cstrand23")


cmd.select("Cstrand24", "resi 46-52 & chain C ")
cmd.color ("red", "Cstrand24")


cmd.select("Cstrand25", "resi 55-60 & chain C ")
cmd.color ("green", "Cstrand25")


cmd.select("Cstrand26", "resi 70-76 & chain C ")
cmd.color ("orange", "Cstrand26")


cmd.select("Cstrand27", "resi 80-81 & chain C ")
cmd.color ("teal", "Cstrand27")


cmd.select("Cstrand28", "resi 104-114 & chain C ")
cmd.color ("yellow", "Cstrand28")


cmd.select("Cstrand29", "resi 119-127 & chain C ")
cmd.color ("blue", "Cstrand29")


cmd.select("Cstrand30", "resi 130-145 & chain C ")
cmd.color ("red", "Cstrand30")


cmd.select("Cstrand31", "resi 151-162 & chain C ")
cmd.color ("green", "Cstrand31")


cmd.select("Cstrand32", "resi 178-189 & chain C ")
cmd.color ("orange", "Cstrand32")


cmd.select("Dstrand33", "resi 24-27 & chain D ")
cmd.color ("teal", "Dstrand33")


cmd.select("Dstrand34", "resi 34-42 & chain D ")
cmd.color ("yellow", "Dstrand34")


cmd.select("Dstrand35", "resi 46-52 & chain D ")
cmd.color ("blue", "Dstrand35")


cmd.select("Dstrand36", "resi 55-60 & chain D ")
cmd.color ("red", "Dstrand36")


cmd.select("Dstrand37", "resi 72-76 & chain D ")
cmd.color ("green", "Dstrand37")


cmd.select("Dstrand38", "resi 80-81 & chain D ")
cmd.color ("orange", "Dstrand38")


cmd.select("Dstrand39", "resi 104-115 & chain D ")
cmd.color ("teal", "Dstrand39")


cmd.select("Dstrand40", "resi 118-127 & chain D ")
cmd.color ("yellow", "Dstrand40")


cmd.select("Dstrand41", "resi 130-145 & chain D ")
cmd.color ("blue", "Dstrand41")


cmd.select("Dstrand42", "resi 151-162 & chain D ")
cmd.color ("red", "Dstrand42")


cmd.select("Dstrand43", "resi 178-189 & chain D ")
cmd.color ("green", "Dstrand43")


cmd.select("barrel", "Astrand* or Bstrand* or Cstrand* or Dstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
