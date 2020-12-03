from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3AEH.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 1116-1128 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 1134-1150 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 1153-1170 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 1173-1190 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 1194-1211 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 1217-1237 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 1242-1257 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 1275-1276 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 1279-1292 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 1296-1310 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 1331-1345 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 1349-1359 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 1364-1377 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Bstrand13", "resi 1116-1128 & chain B ")
cmd.color ("green", "Bstrand13")


cmd.select("Bstrand14", "resi 1134-1150 & chain B ")
cmd.color ("orange", "Bstrand14")


cmd.select("Bstrand15", "resi 1153-1170 & chain B ")
cmd.color ("teal", "Bstrand15")


cmd.select("Bstrand16", "resi 1173-1190 & chain B ")
cmd.color ("yellow", "Bstrand16")


cmd.select("Bstrand17", "resi 1194-1211 & chain B ")
cmd.color ("blue", "Bstrand17")


cmd.select("Bstrand18", "resi 1217-1239 & chain B ")
cmd.color ("red", "Bstrand18")


cmd.select("Bstrand19", "resi 1242-1257 & chain B ")
cmd.color ("green", "Bstrand19")


cmd.select("Bstrand20", "resi 1275-1276 & chain B ")
cmd.color ("orange", "Bstrand20")


cmd.select("Bstrand21", "resi 1279-1292 & chain B ")
cmd.color ("teal", "Bstrand21")


cmd.select("Bstrand22", "resi 1296-1310 & chain B ")
cmd.color ("yellow", "Bstrand22")


cmd.select("Bstrand23", "resi 1331-1345 & chain B ")
cmd.color ("blue", "Bstrand23")


cmd.select("Bstrand24", "resi 1349-1359 & chain B ")
cmd.color ("red", "Bstrand24")


cmd.select("Bstrand25", "resi 1364-1377 & chain B ")
cmd.color ("green", "Bstrand25")


cmd.select("barrel", "Astrand* or Bstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
