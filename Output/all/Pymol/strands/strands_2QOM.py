from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2QOM.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 1039-1051 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 1057-1069 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 1077-1092 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 1097-1112 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 1117-1133 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 1142-1160 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 1165-1182 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 1195-1215 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 1219-1235 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 1254-1268 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 1272-1282 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 1287-1294 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 1297-1300 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Bstrand13", "resi 1039-1051 & chain B ")
cmd.color ("green", "Bstrand13")


cmd.select("Bstrand14", "resi 1057-1072 & chain B ")
cmd.color ("orange", "Bstrand14")


cmd.select("Bstrand15", "resi 1076-1092 & chain B ")
cmd.color ("teal", "Bstrand15")


cmd.select("Bstrand16", "resi 1096-1113 & chain B ")
cmd.color ("yellow", "Bstrand16")


cmd.select("Bstrand17", "resi 1117-1134 & chain B ")
cmd.color ("blue", "Bstrand17")


cmd.select("Bstrand18", "resi 1143-1162 & chain B ")
cmd.color ("red", "Bstrand18")


cmd.select("Bstrand19", "resi 1165-1182 & chain B ")
cmd.color ("green", "Bstrand19")


cmd.select("Bstrand20", "resi 1195-1215 & chain B ")
cmd.color ("orange", "Bstrand20")


cmd.select("Bstrand21", "resi 1220-1235 & chain B ")
cmd.color ("teal", "Bstrand21")


cmd.select("Bstrand22", "resi 1254-1268 & chain B ")
cmd.color ("yellow", "Bstrand22")


cmd.select("Bstrand23", "resi 1272-1275 & chain B ")
cmd.color ("blue", "Bstrand23")


cmd.select("Bstrand24", "resi 1278-1282 & chain B ")
cmd.color ("red", "Bstrand24")


cmd.select("Bstrand25", "resi 1287-1294 & chain B ")
cmd.color ("green", "Bstrand25")


cmd.select("Bstrand26", "resi 1297-1300 & chain B ")
cmd.color ("orange", "Bstrand26")


cmd.select("barrel", "Astrand* or Bstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
