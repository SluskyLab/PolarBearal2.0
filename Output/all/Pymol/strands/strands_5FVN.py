from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5FVN.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 2-6 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 9-23 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 31-32 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Bstrand3", "resi 2-6 & chain B ")
cmd.color ("teal", "Bstrand3")


cmd.select("Bstrand4", "resi 9-24 & chain B ")
cmd.color ("yellow", "Bstrand4")


cmd.select("Bstrand5", "resi 31-32 & chain B ")
cmd.color ("blue", "Bstrand5")


cmd.select("Cstrand6", "resi 2-6 & chain C ")
cmd.color ("red", "Cstrand6")


cmd.select("Cstrand7", "resi 9-23 & chain C ")
cmd.color ("green", "Cstrand7")


cmd.select("Cstrand8", "resi 31-32 & chain C ")
cmd.color ("orange", "Cstrand8")


cmd.select("Dstrand9", "resi 2-6 & chain D ")
cmd.color ("teal", "Dstrand9")


cmd.select("Dstrand10", "resi 9-24 & chain D ")
cmd.color ("yellow", "Dstrand10")


cmd.select("Dstrand11", "resi 31-32 & chain D ")
cmd.color ("blue", "Dstrand11")


cmd.select("Dstrand12", "resi 242-243 & chain D ")
cmd.color ("red", "Dstrand12")


cmd.select("Dstrand13", "resi 247-248 & chain D ")
cmd.color ("green", "Dstrand13")


cmd.select("Estrand14", "resi 2-6 & chain E ")
cmd.color ("orange", "Estrand14")


cmd.select("Estrand15", "resi 9-24 & chain E ")
cmd.color ("teal", "Estrand15")


cmd.select("Estrand16", "resi 31-32 & chain E ")
cmd.color ("yellow", "Estrand16")


cmd.select("Fstrand17", "resi 2-6 & chain F ")
cmd.color ("blue", "Fstrand17")


cmd.select("Fstrand18", "resi 9-24 & chain F ")
cmd.color ("red", "Fstrand18")


cmd.select("Fstrand19", "resi 31-32 & chain F ")
cmd.color ("green", "Fstrand19")


cmd.select("barrel", "Astrand* or Bstrand* or Cstrand* or Dstrand* or Estrand* or Fstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
