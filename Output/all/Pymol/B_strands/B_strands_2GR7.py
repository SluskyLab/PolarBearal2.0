from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2GR7.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 1046+1047+1048+1049+1050+1051+1052+1053+1054+1055 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Cstrand1", "resi 1089+1090+1091+1092+1093+1094+1095+1096+1097 & chain C ")
cmd.color ("green", "Cstrand1")


cmd.select("Cstrand2", "resi 1074+1075+1076+1077+1078+1079+1080+1081+1082+1083 & chain C ")
cmd.color ("orange", "Cstrand2")


cmd.select("Cstrand3", "resi 1058+1059+1060+1061+1062+1063+1064+1065+1066+1067+1068 & chain C ")
cmd.color ("teal", "Cstrand3")


cmd.select("Cstrand4", "resi 1046+1047+1048+1049+1050+1051+1052+1053+1054+1055 & chain C ")
cmd.color ("yellow", "Cstrand4")


cmd.select("Bstrand5", "resi 1089+1090+1091+1092+1093+1094+1095+1096+1097 & chain B ")
cmd.color ("blue", "Bstrand5")


cmd.select("Bstrand6", "resi 1074+1075+1076+1077+1078+1079+1080+1081+1082+1083 & chain B ")
cmd.color ("red", "Bstrand6")


cmd.select("Bstrand7", "resi 1058+1059+1060+1061+1062+1063+1064+1065+1066+1067+1068 & chain B ")
cmd.color ("green", "Bstrand7")


cmd.select("Bstrand8", "resi 1046+1047+1048+1049+1050+1051+1052+1053+1054+1055 & chain B ")
cmd.color ("orange", "Bstrand8")


cmd.select("Astrand9", "resi 1089+1090+1091+1092+1093+1094+1095+1096+1097 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 1074+1075+1076+1077+1078+1079+1080+1081+1082+1083 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 1058+1059+1060+1061+1062+1063+1064+1065+1066+1067+1068 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("barrel", "Astrand* or Cstrand* or Bstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
