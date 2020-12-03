from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3SZH.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 11-14 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 20-26 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 31-37 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 50-57 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 60-68 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 73-85 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 92-101 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 111-119 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Bstrand8", "resi 11-14 & chain B ")
cmd.color ("orange", "Bstrand8")


cmd.select("Bstrand9", "resi 20-26 & chain B ")
cmd.color ("teal", "Bstrand9")


cmd.select("Bstrand10", "resi 31-37 & chain B ")
cmd.color ("yellow", "Bstrand10")


cmd.select("Bstrand11", "resi 50-57 & chain B ")
cmd.color ("blue", "Bstrand11")


cmd.select("Bstrand12", "resi 60-68 & chain B ")
cmd.color ("red", "Bstrand12")


cmd.select("Bstrand13", "resi 73-85 & chain B ")
cmd.color ("green", "Bstrand13")


cmd.select("Bstrand14", "resi 92-101 & chain B ")
cmd.color ("orange", "Bstrand14")


cmd.select("Bstrand15", "resi 111-119 & chain B ")
cmd.color ("teal", "Bstrand15")


cmd.select("Cstrand16", "resi 11-15 & chain C ")
cmd.color ("yellow", "Cstrand16")


cmd.select("Cstrand17", "resi 20-26 & chain C ")
cmd.color ("blue", "Cstrand17")


cmd.select("Cstrand18", "resi 31-37 & chain C ")
cmd.color ("red", "Cstrand18")


cmd.select("Cstrand19", "resi 50-57 & chain C ")
cmd.color ("green", "Cstrand19")


cmd.select("Cstrand20", "resi 60-68 & chain C ")
cmd.color ("orange", "Cstrand20")


cmd.select("Cstrand21", "resi 73-86 & chain C ")
cmd.color ("teal", "Cstrand21")


cmd.select("Cstrand22", "resi 91-101 & chain C ")
cmd.color ("yellow", "Cstrand22")


cmd.select("Cstrand23", "resi 111-119 & chain C ")
cmd.color ("blue", "Cstrand23")


cmd.select("Dstrand24", "resi 11-15 & chain D ")
cmd.color ("red", "Dstrand24")


cmd.select("Dstrand25", "resi 20-26 & chain D ")
cmd.color ("green", "Dstrand25")


cmd.select("Dstrand26", "resi 31-37 & chain D ")
cmd.color ("orange", "Dstrand26")


cmd.select("Dstrand27", "resi 49-57 & chain D ")
cmd.color ("teal", "Dstrand27")


cmd.select("Dstrand28", "resi 60-68 & chain D ")
cmd.color ("yellow", "Dstrand28")


cmd.select("Dstrand29", "resi 73-86 & chain D ")
cmd.color ("blue", "Dstrand29")


cmd.select("Dstrand30", "resi 91-101 & chain D ")
cmd.color ("red", "Dstrand30")


cmd.select("Dstrand31", "resi 111-119 & chain D ")
cmd.color ("green", "Dstrand31")


cmd.select("Estrand32", "resi 11-15 & chain E ")
cmd.color ("orange", "Estrand32")


cmd.select("Estrand33", "resi 20-26 & chain E ")
cmd.color ("teal", "Estrand33")


cmd.select("Estrand34", "resi 31-37 & chain E ")
cmd.color ("yellow", "Estrand34")


cmd.select("Estrand35", "resi 49-57 & chain E ")
cmd.color ("blue", "Estrand35")


cmd.select("Estrand36", "resi 60-68 & chain E ")
cmd.color ("red", "Estrand36")


cmd.select("Estrand37", "resi 73-87 & chain E ")
cmd.color ("green", "Estrand37")


cmd.select("Estrand38", "resi 90-101 & chain E ")
cmd.color ("orange", "Estrand38")


cmd.select("Estrand39", "resi 111-119 & chain E ")
cmd.color ("teal", "Estrand39")


cmd.select("Fstrand40", "resi 11-15 & chain F ")
cmd.color ("yellow", "Fstrand40")


cmd.select("Fstrand41", "resi 20-26 & chain F ")
cmd.color ("blue", "Fstrand41")


cmd.select("Fstrand42", "resi 31-37 & chain F ")
cmd.color ("red", "Fstrand42")


cmd.select("Fstrand43", "resi 50-57 & chain F ")
cmd.color ("green", "Fstrand43")


cmd.select("Fstrand44", "resi 60-68 & chain F ")
cmd.color ("orange", "Fstrand44")


cmd.select("Fstrand45", "resi 73-87 & chain F ")
cmd.color ("teal", "Fstrand45")


cmd.select("Fstrand46", "resi 90-101 & chain F ")
cmd.color ("yellow", "Fstrand46")


cmd.select("Fstrand47", "resi 111-119 & chain F ")
cmd.color ("blue", "Fstrand47")


cmd.select("barrel", "Astrand* or Bstrand* or Cstrand* or Dstrand* or Estrand* or Fstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
