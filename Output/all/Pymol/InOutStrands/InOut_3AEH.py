from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3AEH.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 1116+1117+1118+1119+1120+1121+1122+1123+1124+1125+1126+1127+1128 & chain A ")


cmd.select("Astrand1", "resi 1134+1135+1136+1137+1138+1139+1140+1141+1142+1143+1144+1145+1146+1147+1148+1149+1150 & chain A ")


cmd.select("Astrand2", "resi 1153+1154+1155+1156+1157+1158+1159+1160+1161+1162+1163+1164+1165+1166+1167+1168+1169+1170 & chain A ")


cmd.select("Astrand3", "resi 1173+1174+1175+1176+1177+1178+1179+1180+1181+1182+1183+1184+1185+1186+1187+1188+1189+1190 & chain A ")


cmd.select("Astrand4", "resi 1194+1195+1196+1197+1198+1199+1200+1201+1202+1203+1204+1205+1206+1207+1208+1209+1210+1211 & chain A ")


cmd.select("Astrand5", "resi 1217+1218+1219+1220+1221+1222+1223+1224+1225+1226+1227+1228+1229+1230+1231+1232+1233+1234+1235+1236+1237 & chain A ")


cmd.select("Astrand6", "resi 1242+1243+1244+1245+1246+1247+1248+1249+1250+1251+1252+1253+1254+1255+1256+1257 & chain A ")


cmd.select("Astrand8", "resi 1279+1280+1281+1282+1283+1284+1285+1286+1287+1288+1289+1290+1291+1292 & chain A ")


cmd.select("Astrand9", "resi 1296+1297+1298+1299+1300+1301+1302+1303+1304+1305+1306+1307+1308+1309+1310 & chain A ")


cmd.select("Astrand10", "resi 1331+1332+1333+1334+1335+1336+1337+1338+1339+1340+1341+1342+1343+1344+1345 & chain A ")


cmd.select("Astrand11", "resi 1349+1350+1351+1352+1353+1354+1355+1356+1357+1358+1359 & chain A ")


cmd.select("Astrand12", "resi 1364+1365+1366+1367+1368+1369+1370+1371+1372+1373+1374+1375+1376+1377 & chain A ")


cmd.select("barrel", "Astrand*")
cmd.show("sticks", "barrel")
cmd.show("cartoon", "barrel")
cmd.set("cartoon_side_chain_helper", "on")
cmd.zoom("barrel")
cmd.color ("blue", "resi 1116 & chain A")

cmd.select ("Outward", "resi 1116 & chain A", merge=1)

cmd.color ("red", "resi 1117 & chain A")

cmd.select ("Inward", "resi 1117 & chain A", merge=1)

cmd.color ("blue", "resi 1118 & chain A")

cmd.select ("Outward", "resi 1118 & chain A", merge=1)

cmd.color ("red", "resi 1119 & chain A")

cmd.select ("Inward", "resi 1119 & chain A", merge=1)

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

cmd.color ("blue", "resi 1134 & chain A")

cmd.select ("Outward", "resi 1134 & chain A", merge=1)

cmd.color ("red", "resi 1135 & chain A")

cmd.select ("Inward", "resi 1135 & chain A", merge=1)

cmd.color ("blue", "resi 1136 & chain A")

cmd.select ("Outward", "resi 1136 & chain A", merge=1)

cmd.color ("red", "resi 1137 & chain A")

cmd.select ("Inward", "resi 1137 & chain A", merge=1)

cmd.color ("blue", "resi 1138 & chain A")

cmd.select ("Outward", "resi 1138 & chain A", merge=1)

cmd.color ("red", "resi 1139 & chain A")

cmd.select ("Inward", "resi 1139 & chain A", merge=1)

cmd.color ("blue", "resi 1140 & chain A")

cmd.select ("Outward", "resi 1140 & chain A", merge=1)

cmd.color ("red", "resi 1141 & chain A")

cmd.select ("Inward", "resi 1141 & chain A", merge=1)

cmd.color ("blue", "resi 1142 & chain A")

cmd.select ("Outward", "resi 1142 & chain A", merge=1)

cmd.color ("red", "resi 1143 & chain A")

cmd.select ("Inward", "resi 1143 & chain A", merge=1)

cmd.color ("blue", "resi 1144 & chain A")

cmd.select ("Outward", "resi 1144 & chain A", merge=1)

cmd.color ("red", "resi 1145 & chain A")

cmd.select ("Inward", "resi 1145 & chain A", merge=1)

cmd.color ("blue", "resi 1146 & chain A")

cmd.select ("Outward", "resi 1146 & chain A", merge=1)

cmd.color ("red", "resi 1147 & chain A")

cmd.select ("Inward", "resi 1147 & chain A", merge=1)

cmd.color ("blue", "resi 1148 & chain A")

cmd.select ("Outward", "resi 1148 & chain A", merge=1)

cmd.color ("blue", "resi 1149 & chain A")

cmd.select ("Outward", "resi 1149 & chain A", merge=1)

cmd.color ("red", "resi 1150 & chain A")

cmd.select ("Inward", "resi 1150 & chain A", merge=1)

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

cmd.color ("blue", "resi 1169 & chain A")

cmd.select ("Outward", "resi 1169 & chain A", merge=1)

cmd.color ("red", "resi 1170 & chain A")

cmd.select ("Inward", "resi 1170 & chain A", merge=1)

cmd.color ("red", "resi 1173 & chain A")

cmd.select ("Inward", "resi 1173 & chain A", merge=1)

cmd.color ("blue", "resi 1174 & chain A")

cmd.select ("Outward", "resi 1174 & chain A", merge=1)

cmd.color ("red", "resi 1175 & chain A")

cmd.select ("Inward", "resi 1175 & chain A", merge=1)

cmd.color ("blue", "resi 1176 & chain A")

cmd.select ("Outward", "resi 1176 & chain A", merge=1)

cmd.color ("red", "resi 1177 & chain A")

cmd.select ("Inward", "resi 1177 & chain A", merge=1)

cmd.color ("blue", "resi 1178 & chain A")

cmd.select ("Outward", "resi 1178 & chain A", merge=1)

cmd.color ("red", "resi 1179 & chain A")

cmd.select ("Inward", "resi 1179 & chain A", merge=1)

cmd.color ("blue", "resi 1180 & chain A")

cmd.select ("Outward", "resi 1180 & chain A", merge=1)

cmd.color ("red", "resi 1181 & chain A")

cmd.select ("Inward", "resi 1181 & chain A", merge=1)

cmd.color ("blue", "resi 1182 & chain A")

cmd.select ("Outward", "resi 1182 & chain A", merge=1)

cmd.color ("red", "resi 1183 & chain A")

cmd.select ("Inward", "resi 1183 & chain A", merge=1)

cmd.color ("blue", "resi 1184 & chain A")

cmd.select ("Outward", "resi 1184 & chain A", merge=1)

cmd.color ("red", "resi 1185 & chain A")

cmd.select ("Inward", "resi 1185 & chain A", merge=1)

cmd.color ("blue", "resi 1186 & chain A")

cmd.select ("Outward", "resi 1186 & chain A", merge=1)

cmd.color ("red", "resi 1187 & chain A")

cmd.select ("Inward", "resi 1187 & chain A", merge=1)

cmd.color ("blue", "resi 1188 & chain A")

cmd.select ("Outward", "resi 1188 & chain A", merge=1)

cmd.color ("red", "resi 1189 & chain A")

cmd.select ("Inward", "resi 1189 & chain A", merge=1)

cmd.color ("red", "resi 1190 & chain A")

cmd.select ("Inward", "resi 1190 & chain A", merge=1)

cmd.color ("blue", "resi 1194 & chain A")

cmd.select ("Outward", "resi 1194 & chain A", merge=1)

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

cmd.color ("red", "resi 1217 & chain A")

cmd.select ("Inward", "resi 1217 & chain A", merge=1)

cmd.color ("blue", "resi 1218 & chain A")

cmd.select ("Outward", "resi 1218 & chain A", merge=1)

cmd.color ("red", "resi 1219 & chain A")

cmd.select ("Inward", "resi 1219 & chain A", merge=1)

cmd.color ("blue", "resi 1220 & chain A")

cmd.select ("Outward", "resi 1220 & chain A", merge=1)

cmd.color ("red", "resi 1221 & chain A")

cmd.select ("Inward", "resi 1221 & chain A", merge=1)

cmd.color ("blue", "resi 1222 & chain A")

cmd.select ("Outward", "resi 1222 & chain A", merge=1)

cmd.color ("red", "resi 1223 & chain A")

cmd.select ("Inward", "resi 1223 & chain A", merge=1)

cmd.color ("blue", "resi 1224 & chain A")

cmd.select ("Outward", "resi 1224 & chain A", merge=1)

cmd.color ("red", "resi 1225 & chain A")

cmd.select ("Inward", "resi 1225 & chain A", merge=1)

cmd.color ("blue", "resi 1226 & chain A")

cmd.select ("Outward", "resi 1226 & chain A", merge=1)

cmd.color ("red", "resi 1227 & chain A")

cmd.select ("Inward", "resi 1227 & chain A", merge=1)

cmd.color ("blue", "resi 1228 & chain A")

cmd.select ("Outward", "resi 1228 & chain A", merge=1)

cmd.color ("red", "resi 1229 & chain A")

cmd.select ("Inward", "resi 1229 & chain A", merge=1)

cmd.color ("blue", "resi 1230 & chain A")

cmd.select ("Outward", "resi 1230 & chain A", merge=1)

cmd.color ("red", "resi 1231 & chain A")

cmd.select ("Inward", "resi 1231 & chain A", merge=1)

cmd.color ("blue", "resi 1232 & chain A")

cmd.select ("Outward", "resi 1232 & chain A", merge=1)

cmd.color ("red", "resi 1233 & chain A")

cmd.select ("Inward", "resi 1233 & chain A", merge=1)

cmd.color ("blue", "resi 1234 & chain A")

cmd.select ("Outward", "resi 1234 & chain A", merge=1)

cmd.color ("red", "resi 1235 & chain A")

cmd.select ("Inward", "resi 1235 & chain A", merge=1)

cmd.color ("blue", "resi 1236 & chain A")

cmd.select ("Outward", "resi 1236 & chain A", merge=1)

cmd.color ("blue", "resi 1237 & chain A")

cmd.select ("Outward", "resi 1237 & chain A", merge=1)

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

cmd.color ("red", "resi 1253 & chain A")

cmd.select ("Inward", "resi 1253 & chain A", merge=1)

cmd.color ("blue", "resi 1254 & chain A")

cmd.select ("Outward", "resi 1254 & chain A", merge=1)

cmd.color ("red", "resi 1255 & chain A")

cmd.select ("Inward", "resi 1255 & chain A", merge=1)

cmd.color ("blue", "resi 1256 & chain A")

cmd.select ("Outward", "resi 1256 & chain A", merge=1)

cmd.color ("red", "resi 1257 & chain A")

cmd.select ("Inward", "resi 1257 & chain A", merge=1)

cmd.color ("blue", "resi 1279 & chain A")

cmd.select ("Outward", "resi 1279 & chain A", merge=1)

cmd.color ("red", "resi 1280 & chain A")

cmd.select ("Inward", "resi 1280 & chain A", merge=1)

cmd.color ("blue", "resi 1281 & chain A")

cmd.select ("Outward", "resi 1281 & chain A", merge=1)

cmd.color ("red", "resi 1282 & chain A")

cmd.select ("Inward", "resi 1282 & chain A", merge=1)

cmd.color ("blue", "resi 1283 & chain A")

cmd.select ("Outward", "resi 1283 & chain A", merge=1)

cmd.color ("red", "resi 1284 & chain A")

cmd.select ("Inward", "resi 1284 & chain A", merge=1)

cmd.color ("blue", "resi 1285 & chain A")

cmd.select ("Outward", "resi 1285 & chain A", merge=1)

cmd.color ("red", "resi 1286 & chain A")

cmd.select ("Inward", "resi 1286 & chain A", merge=1)

cmd.color ("blue", "resi 1287 & chain A")

cmd.select ("Outward", "resi 1287 & chain A", merge=1)

cmd.color ("red", "resi 1288 & chain A")

cmd.select ("Inward", "resi 1288 & chain A", merge=1)

cmd.color ("blue", "resi 1289 & chain A")

cmd.select ("Outward", "resi 1289 & chain A", merge=1)

cmd.color ("red", "resi 1290 & chain A")

cmd.select ("Inward", "resi 1290 & chain A", merge=1)

cmd.color ("red", "resi 1291 & chain A")

cmd.select ("Inward", "resi 1291 & chain A", merge=1)

cmd.color ("red", "resi 1292 & chain A")

cmd.select ("Inward", "resi 1292 & chain A", merge=1)

cmd.color ("blue", "resi 1296 & chain A")

cmd.select ("Outward", "resi 1296 & chain A", merge=1)

cmd.color ("red", "resi 1297 & chain A")

cmd.select ("Inward", "resi 1297 & chain A", merge=1)

cmd.color ("blue", "resi 1298 & chain A")

cmd.select ("Outward", "resi 1298 & chain A", merge=1)

cmd.color ("red", "resi 1299 & chain A")

cmd.select ("Inward", "resi 1299 & chain A", merge=1)

cmd.color ("blue", "resi 1300 & chain A")

cmd.select ("Outward", "resi 1300 & chain A", merge=1)

cmd.color ("red", "resi 1301 & chain A")

cmd.select ("Inward", "resi 1301 & chain A", merge=1)

cmd.color ("blue", "resi 1302 & chain A")

cmd.select ("Outward", "resi 1302 & chain A", merge=1)

cmd.color ("red", "resi 1303 & chain A")

cmd.select ("Inward", "resi 1303 & chain A", merge=1)

cmd.color ("blue", "resi 1304 & chain A")

cmd.select ("Outward", "resi 1304 & chain A", merge=1)

cmd.color ("red", "resi 1305 & chain A")

cmd.select ("Inward", "resi 1305 & chain A", merge=1)

cmd.color ("blue", "resi 1306 & chain A")

cmd.select ("Outward", "resi 1306 & chain A", merge=1)

cmd.color ("red", "resi 1307 & chain A")

cmd.select ("Inward", "resi 1307 & chain A", merge=1)

cmd.color ("blue", "resi 1308 & chain A")

cmd.select ("Outward", "resi 1308 & chain A", merge=1)

cmd.color ("red", "resi 1309 & chain A")

cmd.select ("Inward", "resi 1309 & chain A", merge=1)

cmd.color ("blue", "resi 1310 & chain A")

cmd.select ("Outward", "resi 1310 & chain A", merge=1)

cmd.color ("blue", "resi 1331 & chain A")

cmd.select ("Outward", "resi 1331 & chain A", merge=1)

cmd.color ("red", "resi 1332 & chain A")

cmd.select ("Inward", "resi 1332 & chain A", merge=1)

cmd.color ("blue", "resi 1333 & chain A")

cmd.select ("Outward", "resi 1333 & chain A", merge=1)

cmd.color ("red", "resi 1334 & chain A")

cmd.select ("Inward", "resi 1334 & chain A", merge=1)

cmd.color ("blue", "resi 1335 & chain A")

cmd.select ("Outward", "resi 1335 & chain A", merge=1)

cmd.color ("red", "resi 1336 & chain A")

cmd.select ("Inward", "resi 1336 & chain A", merge=1)

cmd.color ("blue", "resi 1337 & chain A")

cmd.select ("Outward", "resi 1337 & chain A", merge=1)

cmd.color ("red", "resi 1338 & chain A")

cmd.select ("Inward", "resi 1338 & chain A", merge=1)

cmd.color ("blue", "resi 1339 & chain A")

cmd.select ("Outward", "resi 1339 & chain A", merge=1)

cmd.color ("red", "resi 1340 & chain A")

cmd.select ("Inward", "resi 1340 & chain A", merge=1)

cmd.color ("blue", "resi 1341 & chain A")

cmd.select ("Outward", "resi 1341 & chain A", merge=1)

cmd.color ("red", "resi 1342 & chain A")

cmd.select ("Inward", "resi 1342 & chain A", merge=1)

cmd.color ("red", "resi 1343 & chain A")

cmd.select ("Inward", "resi 1343 & chain A", merge=1)

cmd.color ("blue", "resi 1344 & chain A")

cmd.select ("Outward", "resi 1344 & chain A", merge=1)

cmd.color ("red", "resi 1345 & chain A")

cmd.select ("Inward", "resi 1345 & chain A", merge=1)

cmd.color ("blue", "resi 1349 & chain A")

cmd.select ("Outward", "resi 1349 & chain A", merge=1)

cmd.color ("red", "resi 1350 & chain A")

cmd.select ("Inward", "resi 1350 & chain A", merge=1)

cmd.color ("blue", "resi 1351 & chain A")

cmd.select ("Outward", "resi 1351 & chain A", merge=1)

cmd.color ("red", "resi 1352 & chain A")

cmd.select ("Inward", "resi 1352 & chain A", merge=1)

cmd.color ("blue", "resi 1353 & chain A")

cmd.select ("Outward", "resi 1353 & chain A", merge=1)

cmd.color ("red", "resi 1354 & chain A")

cmd.select ("Inward", "resi 1354 & chain A", merge=1)

cmd.color ("blue", "resi 1355 & chain A")

cmd.select ("Outward", "resi 1355 & chain A", merge=1)

cmd.color ("red", "resi 1356 & chain A")

cmd.select ("Inward", "resi 1356 & chain A", merge=1)

cmd.color ("blue", "resi 1357 & chain A")

cmd.select ("Outward", "resi 1357 & chain A", merge=1)

cmd.color ("red", "resi 1358 & chain A")

cmd.select ("Inward", "resi 1358 & chain A", merge=1)

cmd.color ("blue", "resi 1359 & chain A")

cmd.select ("Outward", "resi 1359 & chain A", merge=1)

cmd.color ("blue", "resi 1364 & chain A")

cmd.select ("Outward", "resi 1364 & chain A", merge=1)

cmd.color ("blue", "resi 1365 & chain A")

cmd.select ("Outward", "resi 1365 & chain A", merge=1)

cmd.color ("red", "resi 1366 & chain A")

cmd.select ("Inward", "resi 1366 & chain A", merge=1)

cmd.color ("blue", "resi 1367 & chain A")

cmd.select ("Outward", "resi 1367 & chain A", merge=1)

cmd.color ("red", "resi 1368 & chain A")

cmd.select ("Inward", "resi 1368 & chain A", merge=1)

cmd.color ("blue", "resi 1369 & chain A")

cmd.select ("Outward", "resi 1369 & chain A", merge=1)

cmd.color ("red", "resi 1370 & chain A")

cmd.select ("Inward", "resi 1370 & chain A", merge=1)

cmd.color ("blue", "resi 1371 & chain A")

cmd.select ("Outward", "resi 1371 & chain A", merge=1)

cmd.color ("red", "resi 1372 & chain A")

cmd.select ("Inward", "resi 1372 & chain A", merge=1)

cmd.color ("blue", "resi 1373 & chain A")

cmd.select ("Outward", "resi 1373 & chain A", merge=1)

cmd.color ("red", "resi 1374 & chain A")

cmd.select ("Inward", "resi 1374 & chain A", merge=1)

cmd.color ("blue", "resi 1375 & chain A")

cmd.select ("Outward", "resi 1375 & chain A", merge=1)

cmd.color ("red", "resi 1376 & chain A")

cmd.select ("Inward", "resi 1376 & chain A", merge=1)

cmd.color ("blue", "resi 1377 & chain A")

cmd.select ("Outward", "resi 1377 & chain A", merge=1)

cmd.load_cgo( [9.0, 29.379248,-5.240083,19.08225, 29.379248, -5.240083, 19.08225, 1, 1,1,0,0,0,1], "axis" )
