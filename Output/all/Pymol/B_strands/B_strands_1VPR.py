from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1VPR.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 1028+1029+1030+1031+1032+1033+1034 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 1071+1072+1073+1074+1075+1076+1077 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 1080+1081+1082+1083+1084 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 1094+1095+1096+1097+1098 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 1102+1103+1104+1105+1106 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 1124+1125+1126+1127+1128+1129+1130+1131 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 1112+1113+1114+1115+1116+1117+1118 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 1137+1138+1139+1140+1141+1142+1143+1144+1145+1146+1147 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 1150+1151+1152+1153+1154+1155+1156+1157+1158+1159 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 1162+1163+1164+1165+1166+1167+1168+1169+1170+1171+1172 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
