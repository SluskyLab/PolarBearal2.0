from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4MEE.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 1005-1017 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 1023-1039 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 1042-1043 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 1047-1066 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 1072-1089 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 1097-1115 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 1120-1144 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 1150-1168 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 1171-1172 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 1178-1182 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 1187-1200 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 1214-1222 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 1227-1230 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 1235-1237 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 1242-1253 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 1258-1268 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 1274-1284 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
