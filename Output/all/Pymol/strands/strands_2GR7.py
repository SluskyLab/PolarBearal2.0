from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2GR7.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 1046-1055 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 1058-1068 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 1074-1083 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 1089-1097 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Bstrand4", "resi 1046-1055 & chain B ")
cmd.color ("yellow", "Bstrand4")


cmd.select("Bstrand5", "resi 1058-1068 & chain B ")
cmd.color ("blue", "Bstrand5")


cmd.select("Bstrand6", "resi 1074-1083 & chain B ")
cmd.color ("red", "Bstrand6")


cmd.select("Bstrand7", "resi 1089-1097 & chain B ")
cmd.color ("green", "Bstrand7")


cmd.select("Cstrand8", "resi 1046-1055 & chain C ")
cmd.color ("orange", "Cstrand8")


cmd.select("Cstrand9", "resi 1058-1068 & chain C ")
cmd.color ("teal", "Cstrand9")


cmd.select("Cstrand10", "resi 1074-1083 & chain C ")
cmd.color ("yellow", "Cstrand10")


cmd.select("Cstrand11", "resi 1089-1097 & chain C ")
cmd.color ("blue", "Cstrand11")


cmd.select("Dstrand12", "resi 1046-1055 & chain D ")
cmd.color ("red", "Dstrand12")


cmd.select("Dstrand13", "resi 1058-1068 & chain D ")
cmd.color ("green", "Dstrand13")


cmd.select("Dstrand14", "resi 1074-1083 & chain D ")
cmd.color ("orange", "Dstrand14")


cmd.select("Dstrand15", "resi 1089-1097 & chain D ")
cmd.color ("teal", "Dstrand15")


cmd.select("Estrand16", "resi 1046-1055 & chain E ")
cmd.color ("yellow", "Estrand16")


cmd.select("Estrand17", "resi 1058-1068 & chain E ")
cmd.color ("blue", "Estrand17")


cmd.select("Estrand18", "resi 1074-1083 & chain E ")
cmd.color ("red", "Estrand18")


cmd.select("Estrand19", "resi 1089-1097 & chain E ")
cmd.color ("green", "Estrand19")


cmd.select("Fstrand20", "resi 1046-1055 & chain F ")
cmd.color ("orange", "Fstrand20")


cmd.select("Fstrand21", "resi 1058-1068 & chain F ")
cmd.color ("teal", "Fstrand21")


cmd.select("Fstrand22", "resi 1074-1083 & chain F ")
cmd.color ("yellow", "Fstrand22")


cmd.select("Fstrand23", "resi 1089-1097 & chain F ")
cmd.color ("blue", "Fstrand23")


cmd.select("barrel", "Astrand* or Bstrand* or Cstrand* or Dstrand* or Estrand* or Fstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
