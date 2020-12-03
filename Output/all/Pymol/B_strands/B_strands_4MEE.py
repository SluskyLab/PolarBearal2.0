from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4MEE.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 1005+1006+1007+1008+1009+1010+1011+1012+1013+1014+1015+1016+1017 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 1023+1024+1025+1026+1027+1028+1029+1030+1031+1032+1033+1034+1035+1036+1037+1038+1039 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 1274+1275+1276+1277+1278+1279+1280+1281+1282+1283+1284 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 1047+1048+1049+1050+1051+1052+1053+1054+1055+1056+1057+1058+1059+1060+1061+1062+1063+1064+1065+1066 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 1072+1073+1074+1075+1076+1077+1078+1079+1080+1081+1082+1083+1084+1085+1086+1087+1088+1089 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 1097+1098+1099+1100+1101+1102+1103+1104+1105+1106+1107+1108+1109+1110+1111+1112+1113+1114+1115 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 1120+1121+1122+1123+1124+1125+1126+1127+1128+1129+1130+1131+1132+1133+1134+1135+1136+1137+1138+1139+1140+1141+1142+1143+1144 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 1150+1151+1152+1153+1154+1155+1156+1157+1158+1159+1160+1161+1162+1163+1164+1165+1166+1167+1168 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 1187+1188+1189+1190+1191+1192+1193+1194+1195+1196+1197+1198+1199+1200 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 1214+1215+1216+1217+1218+1219+1220+1221+1222 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 1242+1243+1244+1245+1246+1247+1248+1249+1250+1251+1252+1253 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 1258+1259+1260+1261+1262+1263+1264+1265+1266+1267+1268 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
