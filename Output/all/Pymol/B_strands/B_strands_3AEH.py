from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3AEH.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 1116+1117+1118+1119+1120+1121+1122+1123+1124+1125+1126+1127+1128 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 1134+1135+1136+1137+1138+1139+1140+1141+1142+1143+1144+1145+1146+1147+1148+1149+1150 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 1153+1154+1155+1156+1157+1158+1159+1160+1161+1162+1163+1164+1165+1166+1167+1168+1169+1170 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 1173+1174+1175+1176+1177+1178+1179+1180+1181+1182+1183+1184+1185+1186+1187+1188+1189+1190 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 1194+1195+1196+1197+1198+1199+1200+1201+1202+1203+1204+1205+1206+1207+1208+1209+1210+1211 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 1217+1218+1219+1220+1221+1222+1223+1224+1225+1226+1227+1228+1229+1230+1231+1232+1233+1234+1235+1236+1237 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 1242+1243+1244+1245+1246+1247+1248+1249+1250+1251+1252+1253+1254+1255+1256+1257 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 1279+1280+1281+1282+1283+1284+1285+1286+1287+1288+1289+1290+1291+1292 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 1296+1297+1298+1299+1300+1301+1302+1303+1304+1305+1306+1307+1308+1309+1310 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 1331+1332+1333+1334+1335+1336+1337+1338+1339+1340+1341+1342+1343+1344+1345 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 1349+1350+1351+1352+1353+1354+1355+1356+1357+1358+1359 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 1364+1365+1366+1367+1368+1369+1370+1371+1372+1373+1374+1375+1376+1377 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
