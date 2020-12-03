from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4MEE.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 1005+1006+1007+1008+1009+1010+1011+1012+1013+1014+1015+1016+1017 & chain A ")


cmd.select("Astrand1", "resi 1023+1024+1025+1026+1027+1028+1029+1030+1031+1032+1033+1034+1035+1036+1037+1038+1039 & chain A ")


cmd.select("Astrand16", "resi 1274+1275+1276+1277+1278+1279+1280+1281+1282+1283+1284 & chain A ")


cmd.select("Astrand3", "resi 1047+1048+1049+1050+1051+1052+1053+1054+1055+1056+1057+1058+1059+1060+1061+1062+1063+1064+1065+1066 & chain A ")


cmd.select("Astrand4", "resi 1072+1073+1074+1075+1076+1077+1078+1079+1080+1081+1082+1083+1084+1085+1086+1087+1088+1089 & chain A ")


cmd.select("Astrand5", "resi 1097+1098+1099+1100+1101+1102+1103+1104+1105+1106+1107+1108+1109+1110+1111+1112+1113+1114+1115 & chain A ")


cmd.select("Astrand6", "resi 1120+1121+1122+1123+1124+1125+1126+1127+1128+1129+1130+1131+1132+1133+1134+1135+1136+1137+1138+1139+1140+1141+1142+1143+1144 & chain A ")


cmd.select("Astrand7", "resi 1150+1151+1152+1153+1154+1155+1156+1157+1158+1159+1160+1161+1162+1163+1164+1165+1166+1167+1168 & chain A ")


cmd.select("Astrand10", "resi 1187+1188+1189+1190+1191+1192+1193+1194+1195+1196+1197+1198+1199+1200 & chain A ")


cmd.select("Astrand11", "resi 1214+1215+1216+1217+1218+1219+1220+1221+1222 & chain A ")


cmd.select("Astrand14", "resi 1242+1243+1244+1245+1246+1247+1248+1249+1250+1251+1252+1253 & chain A ")


cmd.select("Astrand15", "resi 1258+1259+1260+1261+1262+1263+1264+1265+1266+1267+1268 & chain A ")


cmd.select("barrel", "Astrand*")
cmd.show("sticks", "barrel")
cmd.show("cartoon", "barrel")
cmd.set("cartoon_side_chain_helper", "on")
cmd.zoom("barrel")
cmd.color ("blue", "resi 1005 & chain A")

cmd.select ("Outward", "resi 1005 & chain A", merge=1)

cmd.color ("red", "resi 1006 & chain A")

cmd.select ("Inward", "resi 1006 & chain A", merge=1)

cmd.color ("blue", "resi 1007 & chain A")

cmd.select ("Outward", "resi 1007 & chain A", merge=1)

cmd.color ("red", "resi 1008 & chain A")

cmd.select ("Inward", "resi 1008 & chain A", merge=1)

cmd.color ("blue", "resi 1009 & chain A")

cmd.select ("Outward", "resi 1009 & chain A", merge=1)

cmd.color ("red", "resi 1010 & chain A")

cmd.select ("Inward", "resi 1010 & chain A", merge=1)

cmd.color ("blue", "resi 1011 & chain A")

cmd.select ("Outward", "resi 1011 & chain A", merge=1)

cmd.color ("red", "resi 1012 & chain A")

cmd.select ("Inward", "resi 1012 & chain A", merge=1)

cmd.color ("blue", "resi 1013 & chain A")

cmd.select ("Outward", "resi 1013 & chain A", merge=1)

cmd.color ("red", "resi 1014 & chain A")

cmd.select ("Inward", "resi 1014 & chain A", merge=1)

cmd.color ("blue", "resi 1015 & chain A")

cmd.select ("Outward", "resi 1015 & chain A", merge=1)

cmd.color ("red", "resi 1016 & chain A")

cmd.select ("Inward", "resi 1016 & chain A", merge=1)

cmd.color ("blue", "resi 1017 & chain A")

cmd.select ("Outward", "resi 1017 & chain A", merge=1)

cmd.color ("red", "resi 1023 & chain A")

cmd.select ("Inward", "resi 1023 & chain A", merge=1)

cmd.color ("blue", "resi 1024 & chain A")

cmd.select ("Outward", "resi 1024 & chain A", merge=1)

cmd.color ("red", "resi 1025 & chain A")

cmd.select ("Inward", "resi 1025 & chain A", merge=1)

cmd.color ("blue", "resi 1026 & chain A")

cmd.select ("Outward", "resi 1026 & chain A", merge=1)

cmd.color ("red", "resi 1027 & chain A")

cmd.select ("Inward", "resi 1027 & chain A", merge=1)

cmd.color ("blue", "resi 1028 & chain A")

cmd.select ("Outward", "resi 1028 & chain A", merge=1)

cmd.color ("red", "resi 1029 & chain A")

cmd.select ("Inward", "resi 1029 & chain A", merge=1)

cmd.color ("blue", "resi 1030 & chain A")

cmd.select ("Outward", "resi 1030 & chain A", merge=1)

cmd.color ("red", "resi 1031 & chain A")

cmd.select ("Inward", "resi 1031 & chain A", merge=1)

cmd.color ("blue", "resi 1032 & chain A")

cmd.select ("Outward", "resi 1032 & chain A", merge=1)

cmd.color ("red", "resi 1033 & chain A")

cmd.select ("Inward", "resi 1033 & chain A", merge=1)

cmd.color ("blue", "resi 1034 & chain A")

cmd.select ("Outward", "resi 1034 & chain A", merge=1)

cmd.color ("red", "resi 1035 & chain A")

cmd.select ("Inward", "resi 1035 & chain A", merge=1)

cmd.color ("blue", "resi 1036 & chain A")

cmd.select ("Outward", "resi 1036 & chain A", merge=1)

cmd.color ("blue", "resi 1037 & chain A")

cmd.select ("Outward", "resi 1037 & chain A", merge=1)

cmd.color ("red", "resi 1038 & chain A")

cmd.select ("Inward", "resi 1038 & chain A", merge=1)

cmd.color ("blue", "resi 1039 & chain A")

cmd.select ("Outward", "resi 1039 & chain A", merge=1)

cmd.color ("blue", "resi 1274 & chain A")

cmd.select ("Outward", "resi 1274 & chain A", merge=1)

cmd.color ("red", "resi 1275 & chain A")

cmd.select ("Inward", "resi 1275 & chain A", merge=1)

cmd.color ("blue", "resi 1276 & chain A")

cmd.select ("Outward", "resi 1276 & chain A", merge=1)

cmd.color ("red", "resi 1277 & chain A")

cmd.select ("Inward", "resi 1277 & chain A", merge=1)

cmd.color ("blue", "resi 1278 & chain A")

cmd.select ("Outward", "resi 1278 & chain A", merge=1)

cmd.color ("red", "resi 1279 & chain A")

cmd.select ("Inward", "resi 1279 & chain A", merge=1)

cmd.color ("blue", "resi 1280 & chain A")

cmd.select ("Outward", "resi 1280 & chain A", merge=1)

cmd.color ("red", "resi 1281 & chain A")

cmd.select ("Inward", "resi 1281 & chain A", merge=1)

cmd.color ("blue", "resi 1282 & chain A")

cmd.select ("Outward", "resi 1282 & chain A", merge=1)

cmd.color ("red", "resi 1283 & chain A")

cmd.select ("Inward", "resi 1283 & chain A", merge=1)

cmd.color ("blue", "resi 1284 & chain A")

cmd.select ("Outward", "resi 1284 & chain A", merge=1)

cmd.color ("blue", "resi 1047 & chain A")

cmd.select ("Outward", "resi 1047 & chain A", merge=1)

cmd.color ("red", "resi 1048 & chain A")

cmd.select ("Inward", "resi 1048 & chain A", merge=1)

cmd.color ("blue", "resi 1049 & chain A")

cmd.select ("Outward", "resi 1049 & chain A", merge=1)

cmd.color ("red", "resi 1050 & chain A")

cmd.select ("Inward", "resi 1050 & chain A", merge=1)

cmd.color ("blue", "resi 1051 & chain A")

cmd.select ("Outward", "resi 1051 & chain A", merge=1)

cmd.color ("red", "resi 1052 & chain A")

cmd.select ("Inward", "resi 1052 & chain A", merge=1)

cmd.color ("blue", "resi 1053 & chain A")

cmd.select ("Outward", "resi 1053 & chain A", merge=1)

cmd.color ("red", "resi 1054 & chain A")

cmd.select ("Inward", "resi 1054 & chain A", merge=1)

cmd.color ("blue", "resi 1055 & chain A")

cmd.select ("Outward", "resi 1055 & chain A", merge=1)

cmd.color ("red", "resi 1056 & chain A")

cmd.select ("Inward", "resi 1056 & chain A", merge=1)

cmd.color ("blue", "resi 1057 & chain A")

cmd.select ("Outward", "resi 1057 & chain A", merge=1)

cmd.color ("red", "resi 1058 & chain A")

cmd.select ("Inward", "resi 1058 & chain A", merge=1)

cmd.color ("blue", "resi 1059 & chain A")

cmd.select ("Outward", "resi 1059 & chain A", merge=1)

cmd.color ("red", "resi 1060 & chain A")

cmd.select ("Inward", "resi 1060 & chain A", merge=1)

cmd.color ("blue", "resi 1061 & chain A")

cmd.select ("Outward", "resi 1061 & chain A", merge=1)

cmd.color ("red", "resi 1062 & chain A")

cmd.select ("Inward", "resi 1062 & chain A", merge=1)

cmd.color ("blue", "resi 1063 & chain A")

cmd.select ("Outward", "resi 1063 & chain A", merge=1)

cmd.color ("red", "resi 1064 & chain A")

cmd.select ("Inward", "resi 1064 & chain A", merge=1)

cmd.color ("blue", "resi 1065 & chain A")

cmd.select ("Outward", "resi 1065 & chain A", merge=1)

cmd.color ("blue", "resi 1066 & chain A")

cmd.select ("Outward", "resi 1066 & chain A", merge=1)

cmd.color ("blue", "resi 1072 & chain A")

cmd.select ("Outward", "resi 1072 & chain A", merge=1)

cmd.color ("red", "resi 1073 & chain A")

cmd.select ("Inward", "resi 1073 & chain A", merge=1)

cmd.color ("blue", "resi 1074 & chain A")

cmd.select ("Outward", "resi 1074 & chain A", merge=1)

cmd.color ("red", "resi 1075 & chain A")

cmd.select ("Inward", "resi 1075 & chain A", merge=1)

cmd.color ("blue", "resi 1076 & chain A")

cmd.select ("Outward", "resi 1076 & chain A", merge=1)

cmd.color ("red", "resi 1077 & chain A")

cmd.select ("Inward", "resi 1077 & chain A", merge=1)

cmd.color ("blue", "resi 1078 & chain A")

cmd.select ("Outward", "resi 1078 & chain A", merge=1)

cmd.color ("red", "resi 1079 & chain A")

cmd.select ("Inward", "resi 1079 & chain A", merge=1)

cmd.color ("blue", "resi 1080 & chain A")

cmd.select ("Outward", "resi 1080 & chain A", merge=1)

cmd.color ("red", "resi 1081 & chain A")

cmd.select ("Inward", "resi 1081 & chain A", merge=1)

cmd.color ("blue", "resi 1082 & chain A")

cmd.select ("Outward", "resi 1082 & chain A", merge=1)

cmd.color ("red", "resi 1083 & chain A")

cmd.select ("Inward", "resi 1083 & chain A", merge=1)

cmd.color ("blue", "resi 1084 & chain A")

cmd.select ("Outward", "resi 1084 & chain A", merge=1)

cmd.color ("red", "resi 1085 & chain A")

cmd.select ("Inward", "resi 1085 & chain A", merge=1)

cmd.color ("blue", "resi 1086 & chain A")

cmd.select ("Outward", "resi 1086 & chain A", merge=1)

cmd.color ("red", "resi 1087 & chain A")

cmd.select ("Inward", "resi 1087 & chain A", merge=1)

cmd.color ("blue", "resi 1088 & chain A")

cmd.select ("Outward", "resi 1088 & chain A", merge=1)

cmd.color ("red", "resi 1089 & chain A")

cmd.select ("Inward", "resi 1089 & chain A", merge=1)

cmd.color ("red", "resi 1097 & chain A")

cmd.select ("Inward", "resi 1097 & chain A", merge=1)

cmd.color ("blue", "resi 1098 & chain A")

cmd.select ("Outward", "resi 1098 & chain A", merge=1)

cmd.color ("red", "resi 1099 & chain A")

cmd.select ("Inward", "resi 1099 & chain A", merge=1)

cmd.color ("blue", "resi 1100 & chain A")

cmd.select ("Outward", "resi 1100 & chain A", merge=1)

cmd.color ("red", "resi 1101 & chain A")

cmd.select ("Inward", "resi 1101 & chain A", merge=1)

cmd.color ("blue", "resi 1102 & chain A")

cmd.select ("Outward", "resi 1102 & chain A", merge=1)

cmd.color ("red", "resi 1103 & chain A")

cmd.select ("Inward", "resi 1103 & chain A", merge=1)

cmd.color ("blue", "resi 1104 & chain A")

cmd.select ("Outward", "resi 1104 & chain A", merge=1)

cmd.color ("red", "resi 1105 & chain A")

cmd.select ("Inward", "resi 1105 & chain A", merge=1)

cmd.color ("blue", "resi 1106 & chain A")

cmd.select ("Outward", "resi 1106 & chain A", merge=1)

cmd.color ("red", "resi 1107 & chain A")

cmd.select ("Inward", "resi 1107 & chain A", merge=1)

cmd.color ("blue", "resi 1108 & chain A")

cmd.select ("Outward", "resi 1108 & chain A", merge=1)

cmd.color ("red", "resi 1109 & chain A")

cmd.select ("Inward", "resi 1109 & chain A", merge=1)

cmd.color ("blue", "resi 1110 & chain A")

cmd.select ("Outward", "resi 1110 & chain A", merge=1)

cmd.color ("red", "resi 1111 & chain A")

cmd.select ("Inward", "resi 1111 & chain A", merge=1)

cmd.color ("blue", "resi 1112 & chain A")

cmd.select ("Outward", "resi 1112 & chain A", merge=1)

cmd.color ("red", "resi 1113 & chain A")

cmd.select ("Inward", "resi 1113 & chain A", merge=1)

cmd.color ("blue", "resi 1114 & chain A")

cmd.select ("Outward", "resi 1114 & chain A", merge=1)

cmd.color ("blue", "resi 1115 & chain A")

cmd.select ("Outward", "resi 1115 & chain A", merge=1)

cmd.color ("blue", "resi 1120 & chain A")

cmd.select ("Outward", "resi 1120 & chain A", merge=1)

cmd.color ("red", "resi 1121 & chain A")

cmd.select ("Inward", "resi 1121 & chain A", merge=1)

cmd.color ("blue", "resi 1122 & chain A")

cmd.select ("Outward", "resi 1122 & chain A", merge=1)

cmd.color ("red", "resi 1123 & chain A")

cmd.select ("Inward", "resi 1123 & chain A", merge=1)

cmd.color ("blue", "resi 1124 & chain A")

cmd.select ("Outward", "resi 1124 & chain A", merge=1)

cmd.color ("red", "resi 1125 & chain A")

cmd.select ("Inward", "resi 1125 & chain A", merge=1)

cmd.color ("blue", "resi 1126 & chain A")

cmd.select ("Outward", "resi 1126 & chain A", merge=1)

cmd.color ("red", "resi 1127 & chain A")

cmd.select ("Inward", "resi 1127 & chain A", merge=1)

cmd.color ("blue", "resi 1128 & chain A")

cmd.select ("Outward", "resi 1128 & chain A", merge=1)

cmd.color ("red", "resi 1129 & chain A")

cmd.select ("Inward", "resi 1129 & chain A", merge=1)

cmd.color ("blue", "resi 1130 & chain A")

cmd.select ("Outward", "resi 1130 & chain A", merge=1)

cmd.color ("red", "resi 1131 & chain A")

cmd.select ("Inward", "resi 1131 & chain A", merge=1)

cmd.color ("blue", "resi 1132 & chain A")

cmd.select ("Outward", "resi 1132 & chain A", merge=1)

cmd.color ("red", "resi 1133 & chain A")

cmd.select ("Inward", "resi 1133 & chain A", merge=1)

cmd.color ("blue", "resi 1134 & chain A")

cmd.select ("Outward", "resi 1134 & chain A", merge=1)

cmd.color ("red", "resi 1135 & chain A")

cmd.select ("Inward", "resi 1135 & chain A", merge=1)

cmd.color ("blue", "resi 1136 & chain A")

cmd.select ("Outward", "resi 1136 & chain A", merge=1)

cmd.color ("red", "resi 1137 & chain A")

cmd.select ("Inward", "resi 1137 & chain A", merge=1)

cmd.color ("red", "resi 1138 & chain A")

cmd.select ("Inward", "resi 1138 & chain A", merge=1)

cmd.color ("blue", "resi 1139 & chain A")

cmd.select ("Outward", "resi 1139 & chain A", merge=1)

cmd.color ("red", "resi 1140 & chain A")

cmd.select ("Inward", "resi 1140 & chain A", merge=1)

cmd.color ("blue", "resi 1141 & chain A")

cmd.select ("Outward", "resi 1141 & chain A", merge=1)

cmd.color ("blue", "resi 1142 & chain A")

cmd.select ("Outward", "resi 1142 & chain A", merge=1)

cmd.color ("red", "resi 1143 & chain A")

cmd.select ("Inward", "resi 1143 & chain A", merge=1)

cmd.color ("blue", "resi 1144 & chain A")

cmd.select ("Outward", "resi 1144 & chain A", merge=1)

cmd.color ("red", "resi 1150 & chain A")

cmd.select ("Inward", "resi 1150 & chain A", merge=1)

cmd.color ("blue", "resi 1151 & chain A")

cmd.select ("Outward", "resi 1151 & chain A", merge=1)

cmd.color ("red", "resi 1152 & chain A")

cmd.select ("Inward", "resi 1152 & chain A", merge=1)

cmd.color ("blue", "resi 1153 & chain A")

cmd.select ("Outward", "resi 1153 & chain A", merge=1)

cmd.color ("red", "resi 1154 & chain A")

cmd.select ("Inward", "resi 1154 & chain A", merge=1)

cmd.color ("blue", "resi 1155 & chain A")

cmd.select ("Outward", "resi 1155 & chain A", merge=1)

cmd.color ("red", "resi 1156 & chain A")

cmd.select ("Inward", "resi 1156 & chain A", merge=1)

cmd.color ("blue", "resi 1157 & chain A")

cmd.select ("Outward", "resi 1157 & chain A", merge=1)

cmd.color ("red", "resi 1158 & chain A")

cmd.select ("Inward", "resi 1158 & chain A", merge=1)

cmd.color ("blue", "resi 1159 & chain A")

cmd.select ("Outward", "resi 1159 & chain A", merge=1)

cmd.color ("red", "resi 1160 & chain A")

cmd.select ("Inward", "resi 1160 & chain A", merge=1)

cmd.color ("blue", "resi 1161 & chain A")

cmd.select ("Outward", "resi 1161 & chain A", merge=1)

cmd.color ("red", "resi 1162 & chain A")

cmd.select ("Inward", "resi 1162 & chain A", merge=1)

cmd.color ("blue", "resi 1163 & chain A")

cmd.select ("Outward", "resi 1163 & chain A", merge=1)

cmd.color ("red", "resi 1164 & chain A")

cmd.select ("Inward", "resi 1164 & chain A", merge=1)

cmd.color ("blue", "resi 1165 & chain A")

cmd.select ("Outward", "resi 1165 & chain A", merge=1)

cmd.color ("red", "resi 1166 & chain A")

cmd.select ("Inward", "resi 1166 & chain A", merge=1)

cmd.color ("blue", "resi 1167 & chain A")

cmd.select ("Outward", "resi 1167 & chain A", merge=1)

cmd.color ("red", "resi 1168 & chain A")

cmd.select ("Inward", "resi 1168 & chain A", merge=1)

cmd.color ("blue", "resi 1187 & chain A")

cmd.select ("Outward", "resi 1187 & chain A", merge=1)

cmd.color ("red", "resi 1188 & chain A")

cmd.select ("Inward", "resi 1188 & chain A", merge=1)

cmd.color ("blue", "resi 1189 & chain A")

cmd.select ("Outward", "resi 1189 & chain A", merge=1)

cmd.color ("red", "resi 1190 & chain A")

cmd.select ("Inward", "resi 1190 & chain A", merge=1)

cmd.color ("blue", "resi 1191 & chain A")

cmd.select ("Outward", "resi 1191 & chain A", merge=1)

cmd.color ("red", "resi 1192 & chain A")

cmd.select ("Inward", "resi 1192 & chain A", merge=1)

cmd.color ("blue", "resi 1193 & chain A")

cmd.select ("Outward", "resi 1193 & chain A", merge=1)

cmd.color ("red", "resi 1194 & chain A")

cmd.select ("Inward", "resi 1194 & chain A", merge=1)

cmd.color ("blue", "resi 1195 & chain A")

cmd.select ("Outward", "resi 1195 & chain A", merge=1)

cmd.color ("red", "resi 1196 & chain A")

cmd.select ("Inward", "resi 1196 & chain A", merge=1)

cmd.color ("blue", "resi 1197 & chain A")

cmd.select ("Outward", "resi 1197 & chain A", merge=1)

cmd.color ("blue", "resi 1198 & chain A")

cmd.select ("Outward", "resi 1198 & chain A", merge=1)

cmd.color ("red", "resi 1199 & chain A")

cmd.select ("Inward", "resi 1199 & chain A", merge=1)

cmd.color ("blue", "resi 1200 & chain A")

cmd.select ("Outward", "resi 1200 & chain A", merge=1)

cmd.color ("red", "resi 1214 & chain A")

cmd.select ("Inward", "resi 1214 & chain A", merge=1)

cmd.color ("blue", "resi 1215 & chain A")

cmd.select ("Outward", "resi 1215 & chain A", merge=1)

cmd.color ("red", "resi 1216 & chain A")

cmd.select ("Inward", "resi 1216 & chain A", merge=1)

cmd.color ("blue", "resi 1217 & chain A")

cmd.select ("Outward", "resi 1217 & chain A", merge=1)

cmd.color ("red", "resi 1218 & chain A")

cmd.select ("Inward", "resi 1218 & chain A", merge=1)

cmd.color ("blue", "resi 1219 & chain A")

cmd.select ("Outward", "resi 1219 & chain A", merge=1)

cmd.color ("red", "resi 1220 & chain A")

cmd.select ("Inward", "resi 1220 & chain A", merge=1)

cmd.color ("blue", "resi 1221 & chain A")

cmd.select ("Outward", "resi 1221 & chain A", merge=1)

cmd.color ("red", "resi 1222 & chain A")

cmd.select ("Inward", "resi 1222 & chain A", merge=1)

cmd.color ("blue", "resi 1242 & chain A")

cmd.select ("Outward", "resi 1242 & chain A", merge=1)

cmd.color ("red", "resi 1243 & chain A")

cmd.select ("Inward", "resi 1243 & chain A", merge=1)

cmd.color ("blue", "resi 1244 & chain A")

cmd.select ("Outward", "resi 1244 & chain A", merge=1)

cmd.color ("red", "resi 1245 & chain A")

cmd.select ("Inward", "resi 1245 & chain A", merge=1)

cmd.color ("blue", "resi 1246 & chain A")

cmd.select ("Outward", "resi 1246 & chain A", merge=1)

cmd.color ("red", "resi 1247 & chain A")

cmd.select ("Inward", "resi 1247 & chain A", merge=1)

cmd.color ("blue", "resi 1248 & chain A")

cmd.select ("Outward", "resi 1248 & chain A", merge=1)

cmd.color ("red", "resi 1249 & chain A")

cmd.select ("Inward", "resi 1249 & chain A", merge=1)

cmd.color ("blue", "resi 1250 & chain A")

cmd.select ("Outward", "resi 1250 & chain A", merge=1)

cmd.color ("red", "resi 1251 & chain A")

cmd.select ("Inward", "resi 1251 & chain A", merge=1)

cmd.color ("blue", "resi 1252 & chain A")

cmd.select ("Outward", "resi 1252 & chain A", merge=1)

cmd.color ("blue", "resi 1253 & chain A")

cmd.select ("Outward", "resi 1253 & chain A", merge=1)

cmd.color ("blue", "resi 1258 & chain A")

cmd.select ("Outward", "resi 1258 & chain A", merge=1)

cmd.color ("red", "resi 1259 & chain A")

cmd.select ("Inward", "resi 1259 & chain A", merge=1)

cmd.color ("blue", "resi 1260 & chain A")

cmd.select ("Outward", "resi 1260 & chain A", merge=1)

cmd.color ("red", "resi 1261 & chain A")

cmd.select ("Inward", "resi 1261 & chain A", merge=1)

cmd.color ("blue", "resi 1262 & chain A")

cmd.select ("Outward", "resi 1262 & chain A", merge=1)

cmd.color ("red", "resi 1263 & chain A")

cmd.select ("Inward", "resi 1263 & chain A", merge=1)

cmd.color ("blue", "resi 1264 & chain A")

cmd.select ("Outward", "resi 1264 & chain A", merge=1)

cmd.color ("red", "resi 1265 & chain A")

cmd.select ("Inward", "resi 1265 & chain A", merge=1)

cmd.color ("blue", "resi 1266 & chain A")

cmd.select ("Outward", "resi 1266 & chain A", merge=1)

cmd.color ("red", "resi 1267 & chain A")

cmd.select ("Inward", "resi 1267 & chain A", merge=1)

cmd.color ("blue", "resi 1268 & chain A")

cmd.select ("Outward", "resi 1268 & chain A", merge=1)

cmd.load_cgo( [9.0, -9.392417,20.6665,-13.616334, -9.392417, 20.6665, -13.616334, 1, 1,1,0,0,0,1], "axis" )
