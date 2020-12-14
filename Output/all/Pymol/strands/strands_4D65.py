from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4D65.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 2-6 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 9-24 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 32-33 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 241-242 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 249-250 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Bstrand5", "resi 2-6 & chain B ")
cmd.color ("blue", "Bstrand5")


cmd.select("Bstrand6", "resi 9-23 & chain B ")
cmd.color ("red", "Bstrand6")


cmd.select("Bstrand7", "resi 32-33 & chain B ")
cmd.color ("green", "Bstrand7")


cmd.select("Bstrand8", "resi 241-242 & chain B ")
cmd.color ("orange", "Bstrand8")


cmd.select("Bstrand9", "resi 249-250 & chain B ")
cmd.color ("teal", "Bstrand9")


cmd.select("Cstrand10", "resi 2-6 & chain C ")
cmd.color ("yellow", "Cstrand10")


cmd.select("Cstrand11", "resi 9-23 & chain C ")
cmd.color ("blue", "Cstrand11")


cmd.select("Cstrand12", "resi 32-33 & chain C ")
cmd.color ("red", "Cstrand12")


cmd.select("Cstrand13", "resi 241-242 & chain C ")
cmd.color ("green", "Cstrand13")


cmd.select("Cstrand14", "resi 249-250 & chain C ")
cmd.color ("orange", "Cstrand14")


cmd.select("Dstrand15", "resi 2-6 & chain D ")
cmd.color ("teal", "Dstrand15")


cmd.select("Dstrand16", "resi 9-23 & chain D ")
cmd.color ("yellow", "Dstrand16")


cmd.select("Dstrand17", "resi 32-33 & chain D ")
cmd.color ("blue", "Dstrand17")


cmd.select("Dstrand18", "resi 241-242 & chain D ")
cmd.color ("red", "Dstrand18")


cmd.select("Dstrand19", "resi 249-250 & chain D ")
cmd.color ("green", "Dstrand19")


cmd.select("Estrand20", "resi 2-6 & chain E ")
cmd.color ("orange", "Estrand20")


cmd.select("Estrand21", "resi 9-24 & chain E ")
cmd.color ("teal", "Estrand21")


cmd.select("Estrand22", "resi 32-33 & chain E ")
cmd.color ("yellow", "Estrand22")


cmd.select("Estrand23", "resi 241-242 & chain E ")
cmd.color ("blue", "Estrand23")


cmd.select("Estrand24", "resi 249-250 & chain E ")
cmd.color ("red", "Estrand24")


cmd.select("Fstrand25", "resi 2-6 & chain F ")
cmd.color ("green", "Fstrand25")


cmd.select("Fstrand26", "resi 9-23 & chain F ")
cmd.color ("orange", "Fstrand26")


cmd.select("Fstrand27", "resi 32-33 & chain F ")
cmd.color ("teal", "Fstrand27")


cmd.select("Fstrand28", "resi 241-242 & chain F ")
cmd.color ("yellow", "Fstrand28")


cmd.select("Fstrand29", "resi 249-250 & chain F ")
cmd.color ("blue", "Fstrand29")


cmd.select("barrel", "Astrand* or Bstrand* or Cstrand* or Dstrand* or Estrand* or Fstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
