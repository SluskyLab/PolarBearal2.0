from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1VPR.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand4", "resi 1028+1029+1030+1031+1032+1033+1034 & chain A ")


cmd.select("Astrand5", "resi 1071+1072+1073+1074+1075+1076+1077 & chain A ")


cmd.select("Astrand6", "resi 1080+1081+1082+1083+1084 & chain A ")


cmd.select("Astrand7", "resi 1094+1095+1096+1097+1098 & chain A ")


cmd.select("Astrand13", "resi 1162+1163+1164+1165+1166+1167+1168+1169+1170+1171+1172 & chain A ")


cmd.select("Astrand12", "resi 1150+1151+1152+1153+1154+1155+1156+1157+1158+1159 & chain A ")


cmd.select("Astrand11", "resi 1137+1138+1139+1140+1141+1142+1143+1144+1145+1146+1147 & chain A ")


cmd.select("Astrand10", "resi 1124+1125+1126+1127+1128+1129+1130+1131 & chain A ")


cmd.select("Astrand9", "resi 1112+1113+1114+1115+1116+1117+1118 & chain A ")


cmd.select("Astrand8", "resi 1102+1103+1104+1105+1106 & chain A ")


cmd.select("barrel", "Astrand*")
cmd.show("sticks", "barrel")
cmd.show("cartoon", "barrel")
cmd.set("cartoon_side_chain_helper", "on")
cmd.zoom("barrel")
cmd.color ("blue", "resi 1028 & chain A")

cmd.select ("Outward", "resi 1028 & chain A", merge=1)

cmd.color ("blue", "resi 1029 & chain A")

cmd.select ("Outward", "resi 1029 & chain A", merge=1)

cmd.color ("blue", "resi 1030 & chain A")

cmd.select ("Outward", "resi 1030 & chain A", merge=1)

cmd.color ("blue", "resi 1031 & chain A")

cmd.select ("Outward", "resi 1031 & chain A", merge=1)

cmd.color ("blue", "resi 1032 & chain A")

cmd.select ("Outward", "resi 1032 & chain A", merge=1)

cmd.color ("blue", "resi 1033 & chain A")

cmd.select ("Outward", "resi 1033 & chain A", merge=1)

cmd.color ("blue", "resi 1034 & chain A")

cmd.select ("Outward", "resi 1034 & chain A", merge=1)

cmd.color ("blue", "resi 1071 & chain A")

cmd.select ("Outward", "resi 1071 & chain A", merge=1)

cmd.color ("blue", "resi 1072 & chain A")

cmd.select ("Outward", "resi 1072 & chain A", merge=1)

cmd.color ("blue", "resi 1073 & chain A")

cmd.select ("Outward", "resi 1073 & chain A", merge=1)

cmd.color ("blue", "resi 1074 & chain A")

cmd.select ("Outward", "resi 1074 & chain A", merge=1)

cmd.color ("blue", "resi 1075 & chain A")

cmd.select ("Outward", "resi 1075 & chain A", merge=1)

cmd.color ("blue", "resi 1076 & chain A")

cmd.select ("Outward", "resi 1076 & chain A", merge=1)

cmd.color ("blue", "resi 1077 & chain A")

cmd.select ("Outward", "resi 1077 & chain A", merge=1)

cmd.color ("blue", "resi 1080 & chain A")

cmd.select ("Outward", "resi 1080 & chain A", merge=1)

cmd.color ("blue", "resi 1081 & chain A")

cmd.select ("Outward", "resi 1081 & chain A", merge=1)

cmd.color ("blue", "resi 1082 & chain A")

cmd.select ("Outward", "resi 1082 & chain A", merge=1)

cmd.color ("blue", "resi 1083 & chain A")

cmd.select ("Outward", "resi 1083 & chain A", merge=1)

cmd.color ("blue", "resi 1084 & chain A")

cmd.select ("Outward", "resi 1084 & chain A", merge=1)

cmd.color ("blue", "resi 1094 & chain A")

cmd.select ("Outward", "resi 1094 & chain A", merge=1)

cmd.color ("blue", "resi 1095 & chain A")

cmd.select ("Outward", "resi 1095 & chain A", merge=1)

cmd.color ("blue", "resi 1096 & chain A")

cmd.select ("Outward", "resi 1096 & chain A", merge=1)

cmd.color ("blue", "resi 1097 & chain A")

cmd.select ("Outward", "resi 1097 & chain A", merge=1)

cmd.color ("blue", "resi 1098 & chain A")

cmd.select ("Outward", "resi 1098 & chain A", merge=1)

cmd.color ("blue", "resi 1162 & chain A")

cmd.select ("Outward", "resi 1162 & chain A", merge=1)

cmd.color ("blue", "resi 1163 & chain A")

cmd.select ("Outward", "resi 1163 & chain A", merge=1)

cmd.color ("blue", "resi 1164 & chain A")

cmd.select ("Outward", "resi 1164 & chain A", merge=1)

cmd.color ("blue", "resi 1165 & chain A")

cmd.select ("Outward", "resi 1165 & chain A", merge=1)

cmd.color ("blue", "resi 1166 & chain A")

cmd.select ("Outward", "resi 1166 & chain A", merge=1)

cmd.color ("blue", "resi 1167 & chain A")

cmd.select ("Outward", "resi 1167 & chain A", merge=1)

cmd.color ("blue", "resi 1168 & chain A")

cmd.select ("Outward", "resi 1168 & chain A", merge=1)

cmd.color ("blue", "resi 1169 & chain A")

cmd.select ("Outward", "resi 1169 & chain A", merge=1)

cmd.color ("blue", "resi 1170 & chain A")

cmd.select ("Outward", "resi 1170 & chain A", merge=1)

cmd.color ("blue", "resi 1171 & chain A")

cmd.select ("Outward", "resi 1171 & chain A", merge=1)

cmd.color ("blue", "resi 1172 & chain A")

cmd.select ("Outward", "resi 1172 & chain A", merge=1)

cmd.color ("blue", "resi 1150 & chain A")

cmd.select ("Outward", "resi 1150 & chain A", merge=1)

cmd.color ("blue", "resi 1151 & chain A")

cmd.select ("Outward", "resi 1151 & chain A", merge=1)

cmd.color ("blue", "resi 1152 & chain A")

cmd.select ("Outward", "resi 1152 & chain A", merge=1)

cmd.color ("blue", "resi 1153 & chain A")

cmd.select ("Outward", "resi 1153 & chain A", merge=1)

cmd.color ("blue", "resi 1154 & chain A")

cmd.select ("Outward", "resi 1154 & chain A", merge=1)

cmd.color ("blue", "resi 1155 & chain A")

cmd.select ("Outward", "resi 1155 & chain A", merge=1)

cmd.color ("blue", "resi 1156 & chain A")

cmd.select ("Outward", "resi 1156 & chain A", merge=1)

cmd.color ("blue", "resi 1157 & chain A")

cmd.select ("Outward", "resi 1157 & chain A", merge=1)

cmd.color ("blue", "resi 1158 & chain A")

cmd.select ("Outward", "resi 1158 & chain A", merge=1)

cmd.color ("blue", "resi 1159 & chain A")

cmd.select ("Outward", "resi 1159 & chain A", merge=1)

cmd.color ("blue", "resi 1137 & chain A")

cmd.select ("Outward", "resi 1137 & chain A", merge=1)

cmd.color ("blue", "resi 1138 & chain A")

cmd.select ("Outward", "resi 1138 & chain A", merge=1)

cmd.color ("blue", "resi 1139 & chain A")

cmd.select ("Outward", "resi 1139 & chain A", merge=1)

cmd.color ("blue", "resi 1140 & chain A")

cmd.select ("Outward", "resi 1140 & chain A", merge=1)

cmd.color ("blue", "resi 1141 & chain A")

cmd.select ("Outward", "resi 1141 & chain A", merge=1)

cmd.color ("blue", "resi 1142 & chain A")

cmd.select ("Outward", "resi 1142 & chain A", merge=1)

cmd.color ("blue", "resi 1143 & chain A")

cmd.select ("Outward", "resi 1143 & chain A", merge=1)

cmd.color ("blue", "resi 1144 & chain A")

cmd.select ("Outward", "resi 1144 & chain A", merge=1)

cmd.color ("blue", "resi 1145 & chain A")

cmd.select ("Outward", "resi 1145 & chain A", merge=1)

cmd.color ("blue", "resi 1146 & chain A")

cmd.select ("Outward", "resi 1146 & chain A", merge=1)

cmd.color ("blue", "resi 1147 & chain A")

cmd.select ("Outward", "resi 1147 & chain A", merge=1)

cmd.color ("blue", "resi 1124 & chain A")

cmd.select ("Outward", "resi 1124 & chain A", merge=1)

cmd.color ("blue", "resi 1125 & chain A")

cmd.select ("Outward", "resi 1125 & chain A", merge=1)

cmd.color ("blue", "resi 1126 & chain A")

cmd.select ("Outward", "resi 1126 & chain A", merge=1)

cmd.color ("blue", "resi 1127 & chain A")

cmd.select ("Outward", "resi 1127 & chain A", merge=1)

cmd.color ("blue", "resi 1128 & chain A")

cmd.select ("Outward", "resi 1128 & chain A", merge=1)

cmd.color ("blue", "resi 1129 & chain A")

cmd.select ("Outward", "resi 1129 & chain A", merge=1)

cmd.color ("blue", "resi 1130 & chain A")

cmd.select ("Outward", "resi 1130 & chain A", merge=1)

cmd.color ("blue", "resi 1131 & chain A")

cmd.select ("Outward", "resi 1131 & chain A", merge=1)

cmd.color ("blue", "resi 1112 & chain A")

cmd.select ("Outward", "resi 1112 & chain A", merge=1)

cmd.color ("blue", "resi 1113 & chain A")

cmd.select ("Outward", "resi 1113 & chain A", merge=1)

cmd.color ("blue", "resi 1114 & chain A")

cmd.select ("Outward", "resi 1114 & chain A", merge=1)

cmd.color ("blue", "resi 1115 & chain A")

cmd.select ("Outward", "resi 1115 & chain A", merge=1)

cmd.color ("blue", "resi 1116 & chain A")

cmd.select ("Outward", "resi 1116 & chain A", merge=1)

cmd.color ("blue", "resi 1117 & chain A")

cmd.select ("Outward", "resi 1117 & chain A", merge=1)

cmd.color ("blue", "resi 1118 & chain A")

cmd.select ("Outward", "resi 1118 & chain A", merge=1)

cmd.color ("blue", "resi 1102 & chain A")

cmd.select ("Outward", "resi 1102 & chain A", merge=1)

cmd.color ("blue", "resi 1103 & chain A")

cmd.select ("Outward", "resi 1103 & chain A", merge=1)

cmd.color ("blue", "resi 1104 & chain A")

cmd.select ("Outward", "resi 1104 & chain A", merge=1)

cmd.color ("blue", "resi 1105 & chain A")

cmd.select ("Outward", "resi 1105 & chain A", merge=1)

cmd.color ("blue", "resi 1106 & chain A")

cmd.select ("Outward", "resi 1106 & chain A", merge=1)

cmd.load_cgo( [9.0, 47.416496,52.480377,46.065495, 41.91175, 69.37175, 48.5925, 1, 1,1,0,0,0,1], "axis" )
