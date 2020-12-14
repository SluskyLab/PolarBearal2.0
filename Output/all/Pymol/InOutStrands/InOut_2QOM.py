from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2QOM.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 1039+1040+1041+1042+1043+1044+1045+1046+1047+1048+1049+1050+1051 & chain A ")


cmd.select("Astrand1", "resi 1057+1058+1059+1060+1061+1062+1063+1064+1065+1066+1067+1068+1069 & chain A ")


cmd.select("Astrand2", "resi 1077+1078+1079+1080+1081+1082+1083+1084+1085+1086+1087+1088+1089+1090+1091+1092 & chain A ")


cmd.select("Astrand3", "resi 1097+1098+1099+1100+1101+1102+1103+1104+1105+1106+1107+1108+1109+1110+1111+1112 & chain A ")


cmd.select("Astrand4", "resi 1117+1118+1119+1120+1121+1122+1123+1124+1125+1126+1127+1128+1129+1130+1131+1132+1133 & chain A ")


cmd.select("Astrand5", "resi 1142+1143+1144+1145+1146+1147+1148+1149+1150+1151+1152+1153+1154+1155+1156+1157+1158+1159+1160 & chain A ")


cmd.select("Astrand6", "resi 1165+1166+1167+1168+1169+1170+1171+1172+1173+1174+1175+1176+1177+1178+1179+1180+1181+1182 & chain A ")


cmd.select("Astrand7", "resi 1195+1196+1197+1198+1199+1200+1201+1202+1203+1204+1205+1206+1207+1208+1209+1210+1211+1212+1213+1214+1215 & chain A ")


cmd.select("Astrand8", "resi 1219+1220+1221+1222+1223+1224+1225+1226+1227+1228+1229+1230+1231+1232+1233+1234+1235 & chain A ")


cmd.select("Astrand9", "resi 1254+1255+1256+1257+1258+1259+1260+1261+1262+1263+1264+1265+1266+1267+1268 & chain A ")


cmd.select("Astrand10", "resi 1272+1273+1274+1275+1276+1277+1278+1279+1280+1281+1282 & chain A ")


cmd.select("Astrand11", "resi 1287+1288+1289+1290+1291+1292+1293+1294+1297+1298+1299+1300 & chain A ")


cmd.select("barrel", "Astrand*")
cmd.show("sticks", "barrel")
cmd.show("cartoon", "barrel")
cmd.set("cartoon_side_chain_helper", "on")
cmd.zoom("barrel")
cmd.color ("blue", "resi 1039 & chain A")

cmd.select ("Outward", "resi 1039 & chain A", merge=1)

cmd.color ("red", "resi 1040 & chain A")

cmd.select ("Inward", "resi 1040 & chain A", merge=1)

cmd.color ("blue", "resi 1041 & chain A")

cmd.select ("Outward", "resi 1041 & chain A", merge=1)

cmd.color ("red", "resi 1042 & chain A")

cmd.select ("Inward", "resi 1042 & chain A", merge=1)

cmd.color ("blue", "resi 1043 & chain A")

cmd.select ("Outward", "resi 1043 & chain A", merge=1)

cmd.color ("red", "resi 1044 & chain A")

cmd.select ("Inward", "resi 1044 & chain A", merge=1)

cmd.color ("blue", "resi 1045 & chain A")

cmd.select ("Outward", "resi 1045 & chain A", merge=1)

cmd.color ("red", "resi 1046 & chain A")

cmd.select ("Inward", "resi 1046 & chain A", merge=1)

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

cmd.color ("red", "resi 1066 & chain A")

cmd.select ("Inward", "resi 1066 & chain A", merge=1)

cmd.color ("blue", "resi 1067 & chain A")

cmd.select ("Outward", "resi 1067 & chain A", merge=1)

cmd.color ("red", "resi 1068 & chain A")

cmd.select ("Inward", "resi 1068 & chain A", merge=1)

cmd.color ("blue", "resi 1069 & chain A")

cmd.select ("Outward", "resi 1069 & chain A", merge=1)

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

cmd.color ("blue", "resi 1090 & chain A")

cmd.select ("Outward", "resi 1090 & chain A", merge=1)

cmd.color ("red", "resi 1091 & chain A")

cmd.select ("Inward", "resi 1091 & chain A", merge=1)

cmd.color ("blue", "resi 1092 & chain A")

cmd.select ("Outward", "resi 1092 & chain A", merge=1)

cmd.color ("blue", "resi 1097 & chain A")

cmd.select ("Outward", "resi 1097 & chain A", merge=1)

cmd.color ("red", "resi 1098 & chain A")

cmd.select ("Inward", "resi 1098 & chain A", merge=1)

cmd.color ("blue", "resi 1099 & chain A")

cmd.select ("Outward", "resi 1099 & chain A", merge=1)

cmd.color ("red", "resi 1100 & chain A")

cmd.select ("Inward", "resi 1100 & chain A", merge=1)

cmd.color ("blue", "resi 1101 & chain A")

cmd.select ("Outward", "resi 1101 & chain A", merge=1)

cmd.color ("red", "resi 1102 & chain A")

cmd.select ("Inward", "resi 1102 & chain A", merge=1)

cmd.color ("blue", "resi 1103 & chain A")

cmd.select ("Outward", "resi 1103 & chain A", merge=1)

cmd.color ("red", "resi 1104 & chain A")

cmd.select ("Inward", "resi 1104 & chain A", merge=1)

cmd.color ("blue", "resi 1105 & chain A")

cmd.select ("Outward", "resi 1105 & chain A", merge=1)

cmd.color ("red", "resi 1106 & chain A")

cmd.select ("Inward", "resi 1106 & chain A", merge=1)

cmd.color ("blue", "resi 1107 & chain A")

cmd.select ("Outward", "resi 1107 & chain A", merge=1)

cmd.color ("red", "resi 1108 & chain A")

cmd.select ("Inward", "resi 1108 & chain A", merge=1)

cmd.color ("blue", "resi 1109 & chain A")

cmd.select ("Outward", "resi 1109 & chain A", merge=1)

cmd.color ("red", "resi 1110 & chain A")

cmd.select ("Inward", "resi 1110 & chain A", merge=1)

cmd.color ("blue", "resi 1111 & chain A")

cmd.select ("Outward", "resi 1111 & chain A", merge=1)

cmd.color ("red", "resi 1112 & chain A")

cmd.select ("Inward", "resi 1112 & chain A", merge=1)

cmd.color ("blue", "resi 1117 & chain A")

cmd.select ("Outward", "resi 1117 & chain A", merge=1)

cmd.color ("red", "resi 1118 & chain A")

cmd.select ("Inward", "resi 1118 & chain A", merge=1)

cmd.color ("blue", "resi 1119 & chain A")

cmd.select ("Outward", "resi 1119 & chain A", merge=1)

cmd.color ("red", "resi 1120 & chain A")

cmd.select ("Inward", "resi 1120 & chain A", merge=1)

cmd.color ("blue", "resi 1121 & chain A")

cmd.select ("Outward", "resi 1121 & chain A", merge=1)

cmd.color ("red", "resi 1122 & chain A")

cmd.select ("Inward", "resi 1122 & chain A", merge=1)

cmd.color ("blue", "resi 1123 & chain A")

cmd.select ("Outward", "resi 1123 & chain A", merge=1)

cmd.color ("red", "resi 1124 & chain A")

cmd.select ("Inward", "resi 1124 & chain A", merge=1)

cmd.color ("blue", "resi 1125 & chain A")

cmd.select ("Outward", "resi 1125 & chain A", merge=1)

cmd.color ("red", "resi 1126 & chain A")

cmd.select ("Inward", "resi 1126 & chain A", merge=1)

cmd.color ("blue", "resi 1127 & chain A")

cmd.select ("Outward", "resi 1127 & chain A", merge=1)

cmd.color ("red", "resi 1128 & chain A")

cmd.select ("Inward", "resi 1128 & chain A", merge=1)

cmd.color ("blue", "resi 1129 & chain A")

cmd.select ("Outward", "resi 1129 & chain A", merge=1)

cmd.color ("red", "resi 1130 & chain A")

cmd.select ("Inward", "resi 1130 & chain A", merge=1)

cmd.color ("blue", "resi 1131 & chain A")

cmd.select ("Outward", "resi 1131 & chain A", merge=1)

cmd.color ("red", "resi 1132 & chain A")

cmd.select ("Inward", "resi 1132 & chain A", merge=1)

cmd.color ("blue", "resi 1133 & chain A")

cmd.select ("Outward", "resi 1133 & chain A", merge=1)

cmd.color ("red", "resi 1142 & chain A")

cmd.select ("Inward", "resi 1142 & chain A", merge=1)

cmd.color ("blue", "resi 1143 & chain A")

cmd.select ("Outward", "resi 1143 & chain A", merge=1)

cmd.color ("red", "resi 1144 & chain A")

cmd.select ("Inward", "resi 1144 & chain A", merge=1)

cmd.color ("blue", "resi 1145 & chain A")

cmd.select ("Outward", "resi 1145 & chain A", merge=1)

cmd.color ("red", "resi 1146 & chain A")

cmd.select ("Inward", "resi 1146 & chain A", merge=1)

cmd.color ("blue", "resi 1147 & chain A")

cmd.select ("Outward", "resi 1147 & chain A", merge=1)

cmd.color ("red", "resi 1148 & chain A")

cmd.select ("Inward", "resi 1148 & chain A", merge=1)

cmd.color ("blue", "resi 1149 & chain A")

cmd.select ("Outward", "resi 1149 & chain A", merge=1)

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

cmd.color ("blue", "resi 1160 & chain A")

cmd.select ("Outward", "resi 1160 & chain A", merge=1)

cmd.color ("blue", "resi 1165 & chain A")

cmd.select ("Outward", "resi 1165 & chain A", merge=1)

cmd.color ("red", "resi 1166 & chain A")

cmd.select ("Inward", "resi 1166 & chain A", merge=1)

cmd.color ("blue", "resi 1167 & chain A")

cmd.select ("Outward", "resi 1167 & chain A", merge=1)

cmd.color ("red", "resi 1168 & chain A")

cmd.select ("Inward", "resi 1168 & chain A", merge=1)

cmd.color ("blue", "resi 1169 & chain A")

cmd.select ("Outward", "resi 1169 & chain A", merge=1)

cmd.color ("red", "resi 1170 & chain A")

cmd.select ("Inward", "resi 1170 & chain A", merge=1)

cmd.color ("blue", "resi 1171 & chain A")

cmd.select ("Outward", "resi 1171 & chain A", merge=1)

cmd.color ("red", "resi 1172 & chain A")

cmd.select ("Inward", "resi 1172 & chain A", merge=1)

cmd.color ("blue", "resi 1173 & chain A")

cmd.select ("Outward", "resi 1173 & chain A", merge=1)

cmd.color ("red", "resi 1174 & chain A")

cmd.select ("Inward", "resi 1174 & chain A", merge=1)

cmd.color ("blue", "resi 1175 & chain A")

cmd.select ("Outward", "resi 1175 & chain A", merge=1)

cmd.color ("red", "resi 1176 & chain A")

cmd.select ("Inward", "resi 1176 & chain A", merge=1)

cmd.color ("blue", "resi 1177 & chain A")

cmd.select ("Outward", "resi 1177 & chain A", merge=1)

cmd.color ("red", "resi 1178 & chain A")

cmd.select ("Inward", "resi 1178 & chain A", merge=1)

cmd.color ("blue", "resi 1179 & chain A")

cmd.select ("Outward", "resi 1179 & chain A", merge=1)

cmd.color ("red", "resi 1180 & chain A")

cmd.select ("Inward", "resi 1180 & chain A", merge=1)

cmd.color ("blue", "resi 1181 & chain A")

cmd.select ("Outward", "resi 1181 & chain A", merge=1)

cmd.color ("blue", "resi 1182 & chain A")

cmd.select ("Outward", "resi 1182 & chain A", merge=1)

cmd.color ("red", "resi 1195 & chain A")

cmd.select ("Inward", "resi 1195 & chain A", merge=1)

cmd.color ("blue", "resi 1196 & chain A")

cmd.select ("Outward", "resi 1196 & chain A", merge=1)

cmd.color ("red", "resi 1197 & chain A")

cmd.select ("Inward", "resi 1197 & chain A", merge=1)

cmd.color ("blue", "resi 1198 & chain A")

cmd.select ("Outward", "resi 1198 & chain A", merge=1)

cmd.color ("red", "resi 1199 & chain A")

cmd.select ("Inward", "resi 1199 & chain A", merge=1)

cmd.color ("blue", "resi 1200 & chain A")

cmd.select ("Outward", "resi 1200 & chain A", merge=1)

cmd.color ("red", "resi 1201 & chain A")

cmd.select ("Inward", "resi 1201 & chain A", merge=1)

cmd.color ("blue", "resi 1202 & chain A")

cmd.select ("Outward", "resi 1202 & chain A", merge=1)

cmd.color ("red", "resi 1203 & chain A")

cmd.select ("Inward", "resi 1203 & chain A", merge=1)

cmd.color ("blue", "resi 1204 & chain A")

cmd.select ("Outward", "resi 1204 & chain A", merge=1)

cmd.color ("red", "resi 1205 & chain A")

cmd.select ("Inward", "resi 1205 & chain A", merge=1)

cmd.color ("blue", "resi 1206 & chain A")

cmd.select ("Outward", "resi 1206 & chain A", merge=1)

cmd.color ("red", "resi 1207 & chain A")

cmd.select ("Inward", "resi 1207 & chain A", merge=1)

cmd.color ("blue", "resi 1208 & chain A")

cmd.select ("Outward", "resi 1208 & chain A", merge=1)

cmd.color ("red", "resi 1209 & chain A")

cmd.select ("Inward", "resi 1209 & chain A", merge=1)

cmd.color ("blue", "resi 1210 & chain A")

cmd.select ("Outward", "resi 1210 & chain A", merge=1)

cmd.color ("red", "resi 1211 & chain A")

cmd.select ("Inward", "resi 1211 & chain A", merge=1)

cmd.color ("blue", "resi 1212 & chain A")

cmd.select ("Outward", "resi 1212 & chain A", merge=1)

cmd.color ("red", "resi 1213 & chain A")

cmd.select ("Inward", "resi 1213 & chain A", merge=1)

cmd.color ("red", "resi 1214 & chain A")

cmd.select ("Inward", "resi 1214 & chain A", merge=1)

cmd.color ("red", "resi 1215 & chain A")

cmd.select ("Inward", "resi 1215 & chain A", merge=1)

cmd.color ("blue", "resi 1219 & chain A")

cmd.select ("Outward", "resi 1219 & chain A", merge=1)

cmd.color ("red", "resi 1220 & chain A")

cmd.select ("Inward", "resi 1220 & chain A", merge=1)

cmd.color ("blue", "resi 1221 & chain A")

cmd.select ("Outward", "resi 1221 & chain A", merge=1)

cmd.color ("red", "resi 1222 & chain A")

cmd.select ("Inward", "resi 1222 & chain A", merge=1)

cmd.color ("blue", "resi 1223 & chain A")

cmd.select ("Outward", "resi 1223 & chain A", merge=1)

cmd.color ("red", "resi 1224 & chain A")

cmd.select ("Inward", "resi 1224 & chain A", merge=1)

cmd.color ("blue", "resi 1225 & chain A")

cmd.select ("Outward", "resi 1225 & chain A", merge=1)

cmd.color ("red", "resi 1226 & chain A")

cmd.select ("Inward", "resi 1226 & chain A", merge=1)

cmd.color ("blue", "resi 1227 & chain A")

cmd.select ("Outward", "resi 1227 & chain A", merge=1)

cmd.color ("red", "resi 1228 & chain A")

cmd.select ("Inward", "resi 1228 & chain A", merge=1)

cmd.color ("blue", "resi 1229 & chain A")

cmd.select ("Outward", "resi 1229 & chain A", merge=1)

cmd.color ("red", "resi 1230 & chain A")

cmd.select ("Inward", "resi 1230 & chain A", merge=1)

cmd.color ("blue", "resi 1231 & chain A")

cmd.select ("Outward", "resi 1231 & chain A", merge=1)

cmd.color ("red", "resi 1232 & chain A")

cmd.select ("Inward", "resi 1232 & chain A", merge=1)

cmd.color ("blue", "resi 1233 & chain A")

cmd.select ("Outward", "resi 1233 & chain A", merge=1)

cmd.color ("red", "resi 1234 & chain A")

cmd.select ("Inward", "resi 1234 & chain A", merge=1)

cmd.color ("red", "resi 1235 & chain A")

cmd.select ("Inward", "resi 1235 & chain A", merge=1)

cmd.color ("blue", "resi 1254 & chain A")

cmd.select ("Outward", "resi 1254 & chain A", merge=1)

cmd.color ("red", "resi 1255 & chain A")

cmd.select ("Inward", "resi 1255 & chain A", merge=1)

cmd.color ("blue", "resi 1256 & chain A")

cmd.select ("Outward", "resi 1256 & chain A", merge=1)

cmd.color ("red", "resi 1257 & chain A")

cmd.select ("Inward", "resi 1257 & chain A", merge=1)

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

cmd.color ("red", "resi 1266 & chain A")

cmd.select ("Inward", "resi 1266 & chain A", merge=1)

cmd.color ("blue", "resi 1267 & chain A")

cmd.select ("Outward", "resi 1267 & chain A", merge=1)

cmd.color ("red", "resi 1268 & chain A")

cmd.select ("Inward", "resi 1268 & chain A", merge=1)

cmd.color ("blue", "resi 1272 & chain A")

cmd.select ("Outward", "resi 1272 & chain A", merge=1)

cmd.color ("red", "resi 1273 & chain A")

cmd.select ("Inward", "resi 1273 & chain A", merge=1)

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

cmd.color ("blue", "resi 1287 & chain A")

cmd.select ("Outward", "resi 1287 & chain A", merge=1)

cmd.color ("blue", "resi 1288 & chain A")

cmd.select ("Outward", "resi 1288 & chain A", merge=1)

cmd.color ("red", "resi 1289 & chain A")

cmd.select ("Inward", "resi 1289 & chain A", merge=1)

cmd.color ("blue", "resi 1290 & chain A")

cmd.select ("Outward", "resi 1290 & chain A", merge=1)

cmd.color ("red", "resi 1291 & chain A")

cmd.select ("Inward", "resi 1291 & chain A", merge=1)

cmd.color ("blue", "resi 1292 & chain A")

cmd.select ("Outward", "resi 1292 & chain A", merge=1)

cmd.color ("red", "resi 1293 & chain A")

cmd.select ("Inward", "resi 1293 & chain A", merge=1)

cmd.color ("blue", "resi 1294 & chain A")

cmd.select ("Outward", "resi 1294 & chain A", merge=1)

cmd.color ("red", "resi 1297 & chain A")

cmd.select ("Inward", "resi 1297 & chain A", merge=1)

cmd.color ("blue", "resi 1298 & chain A")

cmd.select ("Outward", "resi 1298 & chain A", merge=1)

cmd.color ("red", "resi 1299 & chain A")

cmd.select ("Inward", "resi 1299 & chain A", merge=1)

cmd.color ("blue", "resi 1300 & chain A")

cmd.select ("Outward", "resi 1300 & chain A", merge=1)

cmd.load_cgo( [9.0, 5.8988338,-6.2450004,25.378334, 5.8988338, -6.2450004, 25.378334, 1, 1,1,0,0,0,1], "axis" )
