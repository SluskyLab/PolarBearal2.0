from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5IXG.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 8-11 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 17-24 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 29-35 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 38-45 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 50-58 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 62-63 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 86-96 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 99-109 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 112-127 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 134-145 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 162-173 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Bstrand11", "resi 7-11 & chain B ")
cmd.color ("blue", "Bstrand11")


cmd.select("Bstrand12", "resi 17-24 & chain B ")
cmd.color ("red", "Bstrand12")


cmd.select("Bstrand13", "resi 29-35 & chain B ")
cmd.color ("green", "Bstrand13")


cmd.select("Bstrand14", "resi 38-45 & chain B ")
cmd.color ("orange", "Bstrand14")


cmd.select("Bstrand15", "resi 50-58 & chain B ")
cmd.color ("teal", "Bstrand15")


cmd.select("Bstrand16", "resi 62-63 & chain B ")
cmd.color ("yellow", "Bstrand16")


cmd.select("Bstrand17", "resi 86-96 & chain B ")
cmd.color ("blue", "Bstrand17")


cmd.select("Bstrand18", "resi 99-109 & chain B ")
cmd.color ("red", "Bstrand18")


cmd.select("Bstrand19", "resi 112-127 & chain B ")
cmd.color ("green", "Bstrand19")


cmd.select("Bstrand20", "resi 134-145 & chain B ")
cmd.color ("orange", "Bstrand20")


cmd.select("Bstrand21", "resi 162-173 & chain B ")
cmd.color ("teal", "Bstrand21")


cmd.select("Cstrand22", "resi 7-11 & chain C ")
cmd.color ("yellow", "Cstrand22")


cmd.select("Cstrand23", "resi 17-24 & chain C ")
cmd.color ("blue", "Cstrand23")


cmd.select("Cstrand24", "resi 29-35 & chain C ")
cmd.color ("red", "Cstrand24")


cmd.select("Cstrand25", "resi 38-45 & chain C ")
cmd.color ("green", "Cstrand25")


cmd.select("Cstrand26", "resi 50-58 & chain C ")
cmd.color ("orange", "Cstrand26")


cmd.select("Cstrand27", "resi 62-63 & chain C ")
cmd.color ("teal", "Cstrand27")


cmd.select("Cstrand28", "resi 86-96 & chain C ")
cmd.color ("yellow", "Cstrand28")


cmd.select("Cstrand29", "resi 99-109 & chain C ")
cmd.color ("blue", "Cstrand29")


cmd.select("Cstrand30", "resi 112-127 & chain C ")
cmd.color ("red", "Cstrand30")


cmd.select("Cstrand31", "resi 134-145 & chain C ")
cmd.color ("green", "Cstrand31")


cmd.select("Cstrand32", "resi 162-173 & chain C ")
cmd.color ("orange", "Cstrand32")


cmd.select("Dstrand33", "resi 7-11 & chain D ")
cmd.color ("teal", "Dstrand33")


cmd.select("Dstrand34", "resi 17-24 & chain D ")
cmd.color ("yellow", "Dstrand34")


cmd.select("Dstrand35", "resi 29-35 & chain D ")
cmd.color ("blue", "Dstrand35")


cmd.select("Dstrand36", "resi 38-45 & chain D ")
cmd.color ("red", "Dstrand36")


cmd.select("Dstrand37", "resi 50-58 & chain D ")
cmd.color ("green", "Dstrand37")


cmd.select("Dstrand38", "resi 62-63 & chain D ")
cmd.color ("orange", "Dstrand38")


cmd.select("Dstrand39", "resi 86-96 & chain D ")
cmd.color ("teal", "Dstrand39")


cmd.select("Dstrand40", "resi 99-109 & chain D ")
cmd.color ("yellow", "Dstrand40")


cmd.select("Dstrand41", "resi 112-127 & chain D ")
cmd.color ("blue", "Dstrand41")


cmd.select("Dstrand42", "resi 134-145 & chain D ")
cmd.color ("red", "Dstrand42")


cmd.select("Dstrand43", "resi 162-173 & chain D ")
cmd.color ("green", "Dstrand43")


cmd.select("barrel", "Astrand* or Bstrand* or Cstrand* or Dstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
