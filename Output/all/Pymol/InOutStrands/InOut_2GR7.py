from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2GR7.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 1046+1047+1048+1049+1050+1051+1052+1053+1054+1055 & chain A ")


cmd.select("Astrand1", "resi 1058+1059+1060+1061+1062+1063+1064+1065+1066+1067+1068 & chain A ")


cmd.select("Astrand2", "resi 1074+1075+1076+1077+1078+1079+1080+1081+1082+1083 & chain A ")


cmd.select("Astrand3", "resi 1089+1090+1091+1092+1093+1094+1095+1096+1097 & chain A ")


cmd.select("Bstrand4", "resi 1046+1047+1048+1049+1050+1051+1052+1053+1054+1055 & chain B ")


cmd.select("Bstrand5", "resi 1058+1059+1060+1061+1062+1063+1064+1065+1066+1067+1068 & chain B ")


cmd.select("Bstrand6", "resi 1074+1075+1076+1077+1078+1079+1080+1081+1082+1083 & chain B ")


cmd.select("Bstrand7", "resi 1089+1090+1091+1092+1093+1094+1095+1096+1097 & chain B ")


cmd.select("Cstrand8", "resi 1046+1047+1048+1049+1050+1051+1052+1053+1054+1055 & chain C ")


cmd.select("Cstrand9", "resi 1058+1059+1060+1061+1062+1063+1064+1065+1066+1067+1068 & chain C ")


cmd.select("Cstrand10", "resi 1074+1075+1076+1077+1078+1079+1080+1081+1082+1083 & chain C ")


cmd.select("Cstrand11", "resi 1089+1090+1091+1092+1093+1094+1095+1096+1097 & chain C ")


cmd.select("barrel", "Astrand* or Bstrand* or Cstrand*")
cmd.show("sticks", "barrel")
cmd.show("cartoon", "barrel")
cmd.set("cartoon_side_chain_helper", "on")
cmd.zoom("barrel")
cmd.color ("blue", "resi 1046 & chain A")

cmd.select ("Outward", "resi 1046 & chain A", merge=1)

cmd.color ("blue", "resi 1047 & chain A")

cmd.select ("Outward", "resi 1047 & chain A", merge=1)

cmd.color ("blue", "resi 1048 & chain A")

cmd.select ("Outward", "resi 1048 & chain A", merge=1)

cmd.color ("blue", "resi 1049 & chain A")

cmd.select ("Outward", "resi 1049 & chain A", merge=1)

cmd.color ("blue", "resi 1050 & chain A")

cmd.select ("Outward", "resi 1050 & chain A", merge=1)

cmd.color ("blue", "resi 1051 & chain A")

cmd.select ("Outward", "resi 1051 & chain A", merge=1)

cmd.color ("blue", "resi 1052 & chain A")

cmd.select ("Outward", "resi 1052 & chain A", merge=1)

cmd.color ("blue", "resi 1053 & chain A")

cmd.select ("Outward", "resi 1053 & chain A", merge=1)

cmd.color ("blue", "resi 1054 & chain A")

cmd.select ("Outward", "resi 1054 & chain A", merge=1)

cmd.color ("blue", "resi 1055 & chain A")

cmd.select ("Outward", "resi 1055 & chain A", merge=1)

cmd.color ("blue", "resi 1058 & chain A")

cmd.select ("Outward", "resi 1058 & chain A", merge=1)

cmd.color ("blue", "resi 1059 & chain A")

cmd.select ("Outward", "resi 1059 & chain A", merge=1)

cmd.color ("blue", "resi 1060 & chain A")

cmd.select ("Outward", "resi 1060 & chain A", merge=1)

cmd.color ("blue", "resi 1061 & chain A")

cmd.select ("Outward", "resi 1061 & chain A", merge=1)

cmd.color ("blue", "resi 1062 & chain A")

cmd.select ("Outward", "resi 1062 & chain A", merge=1)

cmd.color ("blue", "resi 1063 & chain A")

cmd.select ("Outward", "resi 1063 & chain A", merge=1)

cmd.color ("blue", "resi 1064 & chain A")

cmd.select ("Outward", "resi 1064 & chain A", merge=1)

cmd.color ("blue", "resi 1065 & chain A")

cmd.select ("Outward", "resi 1065 & chain A", merge=1)

cmd.color ("blue", "resi 1066 & chain A")

cmd.select ("Outward", "resi 1066 & chain A", merge=1)

cmd.color ("blue", "resi 1067 & chain A")

cmd.select ("Outward", "resi 1067 & chain A", merge=1)

cmd.color ("blue", "resi 1068 & chain A")

cmd.select ("Outward", "resi 1068 & chain A", merge=1)

cmd.color ("blue", "resi 1074 & chain A")

cmd.select ("Outward", "resi 1074 & chain A", merge=1)

cmd.color ("blue", "resi 1075 & chain A")

cmd.select ("Outward", "resi 1075 & chain A", merge=1)

cmd.color ("blue", "resi 1076 & chain A")

cmd.select ("Outward", "resi 1076 & chain A", merge=1)

cmd.color ("blue", "resi 1077 & chain A")

cmd.select ("Outward", "resi 1077 & chain A", merge=1)

cmd.color ("blue", "resi 1078 & chain A")

cmd.select ("Outward", "resi 1078 & chain A", merge=1)

cmd.color ("blue", "resi 1079 & chain A")

cmd.select ("Outward", "resi 1079 & chain A", merge=1)

cmd.color ("blue", "resi 1080 & chain A")

cmd.select ("Outward", "resi 1080 & chain A", merge=1)

cmd.color ("blue", "resi 1081 & chain A")

cmd.select ("Outward", "resi 1081 & chain A", merge=1)

cmd.color ("blue", "resi 1082 & chain A")

cmd.select ("Outward", "resi 1082 & chain A", merge=1)

cmd.color ("blue", "resi 1083 & chain A")

cmd.select ("Outward", "resi 1083 & chain A", merge=1)

cmd.color ("blue", "resi 1089 & chain A")

cmd.select ("Outward", "resi 1089 & chain A", merge=1)

cmd.color ("blue", "resi 1090 & chain A")

cmd.select ("Outward", "resi 1090 & chain A", merge=1)

cmd.color ("blue", "resi 1091 & chain A")

cmd.select ("Outward", "resi 1091 & chain A", merge=1)

cmd.color ("blue", "resi 1092 & chain A")

cmd.select ("Outward", "resi 1092 & chain A", merge=1)

cmd.color ("blue", "resi 1093 & chain A")

cmd.select ("Outward", "resi 1093 & chain A", merge=1)

cmd.color ("blue", "resi 1094 & chain A")

cmd.select ("Outward", "resi 1094 & chain A", merge=1)

cmd.color ("blue", "resi 1095 & chain A")

cmd.select ("Outward", "resi 1095 & chain A", merge=1)

cmd.color ("blue", "resi 1096 & chain A")

cmd.select ("Outward", "resi 1096 & chain A", merge=1)

cmd.color ("blue", "resi 1097 & chain A")

cmd.select ("Outward", "resi 1097 & chain A", merge=1)

cmd.color ("blue", "resi 1046 & chain B")

cmd.select ("Outward", "resi 1046 & chain B", merge=1)

cmd.color ("blue", "resi 1047 & chain B")

cmd.select ("Outward", "resi 1047 & chain B", merge=1)

cmd.color ("blue", "resi 1048 & chain B")

cmd.select ("Outward", "resi 1048 & chain B", merge=1)

cmd.color ("blue", "resi 1049 & chain B")

cmd.select ("Outward", "resi 1049 & chain B", merge=1)

cmd.color ("blue", "resi 1050 & chain B")

cmd.select ("Outward", "resi 1050 & chain B", merge=1)

cmd.color ("blue", "resi 1051 & chain B")

cmd.select ("Outward", "resi 1051 & chain B", merge=1)

cmd.color ("blue", "resi 1052 & chain B")

cmd.select ("Outward", "resi 1052 & chain B", merge=1)

cmd.color ("blue", "resi 1053 & chain B")

cmd.select ("Outward", "resi 1053 & chain B", merge=1)

cmd.color ("blue", "resi 1054 & chain B")

cmd.select ("Outward", "resi 1054 & chain B", merge=1)

cmd.color ("blue", "resi 1055 & chain B")

cmd.select ("Outward", "resi 1055 & chain B", merge=1)

cmd.color ("blue", "resi 1058 & chain B")

cmd.select ("Outward", "resi 1058 & chain B", merge=1)

cmd.color ("blue", "resi 1059 & chain B")

cmd.select ("Outward", "resi 1059 & chain B", merge=1)

cmd.color ("blue", "resi 1060 & chain B")

cmd.select ("Outward", "resi 1060 & chain B", merge=1)

cmd.color ("blue", "resi 1061 & chain B")

cmd.select ("Outward", "resi 1061 & chain B", merge=1)

cmd.color ("blue", "resi 1062 & chain B")

cmd.select ("Outward", "resi 1062 & chain B", merge=1)

cmd.color ("blue", "resi 1063 & chain B")

cmd.select ("Outward", "resi 1063 & chain B", merge=1)

cmd.color ("blue", "resi 1064 & chain B")

cmd.select ("Outward", "resi 1064 & chain B", merge=1)

cmd.color ("blue", "resi 1065 & chain B")

cmd.select ("Outward", "resi 1065 & chain B", merge=1)

cmd.color ("blue", "resi 1066 & chain B")

cmd.select ("Outward", "resi 1066 & chain B", merge=1)

cmd.color ("blue", "resi 1067 & chain B")

cmd.select ("Outward", "resi 1067 & chain B", merge=1)

cmd.color ("blue", "resi 1068 & chain B")

cmd.select ("Outward", "resi 1068 & chain B", merge=1)

cmd.color ("blue", "resi 1074 & chain B")

cmd.select ("Outward", "resi 1074 & chain B", merge=1)

cmd.color ("blue", "resi 1075 & chain B")

cmd.select ("Outward", "resi 1075 & chain B", merge=1)

cmd.color ("blue", "resi 1076 & chain B")

cmd.select ("Outward", "resi 1076 & chain B", merge=1)

cmd.color ("blue", "resi 1077 & chain B")

cmd.select ("Outward", "resi 1077 & chain B", merge=1)

cmd.color ("blue", "resi 1078 & chain B")

cmd.select ("Outward", "resi 1078 & chain B", merge=1)

cmd.color ("blue", "resi 1079 & chain B")

cmd.select ("Outward", "resi 1079 & chain B", merge=1)

cmd.color ("blue", "resi 1080 & chain B")

cmd.select ("Outward", "resi 1080 & chain B", merge=1)

cmd.color ("blue", "resi 1081 & chain B")

cmd.select ("Outward", "resi 1081 & chain B", merge=1)

cmd.color ("blue", "resi 1082 & chain B")

cmd.select ("Outward", "resi 1082 & chain B", merge=1)

cmd.color ("blue", "resi 1083 & chain B")

cmd.select ("Outward", "resi 1083 & chain B", merge=1)

cmd.color ("blue", "resi 1089 & chain B")

cmd.select ("Outward", "resi 1089 & chain B", merge=1)

cmd.color ("blue", "resi 1090 & chain B")

cmd.select ("Outward", "resi 1090 & chain B", merge=1)

cmd.color ("blue", "resi 1091 & chain B")

cmd.select ("Outward", "resi 1091 & chain B", merge=1)

cmd.color ("blue", "resi 1092 & chain B")

cmd.select ("Outward", "resi 1092 & chain B", merge=1)

cmd.color ("blue", "resi 1093 & chain B")

cmd.select ("Outward", "resi 1093 & chain B", merge=1)

cmd.color ("blue", "resi 1094 & chain B")

cmd.select ("Outward", "resi 1094 & chain B", merge=1)

cmd.color ("blue", "resi 1095 & chain B")

cmd.select ("Outward", "resi 1095 & chain B", merge=1)

cmd.color ("blue", "resi 1096 & chain B")

cmd.select ("Outward", "resi 1096 & chain B", merge=1)

cmd.color ("blue", "resi 1097 & chain B")

cmd.select ("Outward", "resi 1097 & chain B", merge=1)

cmd.color ("blue", "resi 1046 & chain C")

cmd.select ("Outward", "resi 1046 & chain C", merge=1)

cmd.color ("blue", "resi 1047 & chain C")

cmd.select ("Outward", "resi 1047 & chain C", merge=1)

cmd.color ("blue", "resi 1048 & chain C")

cmd.select ("Outward", "resi 1048 & chain C", merge=1)

cmd.color ("blue", "resi 1049 & chain C")

cmd.select ("Outward", "resi 1049 & chain C", merge=1)

cmd.color ("blue", "resi 1050 & chain C")

cmd.select ("Outward", "resi 1050 & chain C", merge=1)

cmd.color ("blue", "resi 1051 & chain C")

cmd.select ("Outward", "resi 1051 & chain C", merge=1)

cmd.color ("blue", "resi 1052 & chain C")

cmd.select ("Outward", "resi 1052 & chain C", merge=1)

cmd.color ("blue", "resi 1053 & chain C")

cmd.select ("Outward", "resi 1053 & chain C", merge=1)

cmd.color ("blue", "resi 1054 & chain C")

cmd.select ("Outward", "resi 1054 & chain C", merge=1)

cmd.color ("blue", "resi 1055 & chain C")

cmd.select ("Outward", "resi 1055 & chain C", merge=1)

cmd.color ("blue", "resi 1058 & chain C")

cmd.select ("Outward", "resi 1058 & chain C", merge=1)

cmd.color ("blue", "resi 1059 & chain C")

cmd.select ("Outward", "resi 1059 & chain C", merge=1)

cmd.color ("blue", "resi 1060 & chain C")

cmd.select ("Outward", "resi 1060 & chain C", merge=1)

cmd.color ("blue", "resi 1061 & chain C")

cmd.select ("Outward", "resi 1061 & chain C", merge=1)

cmd.color ("blue", "resi 1062 & chain C")

cmd.select ("Outward", "resi 1062 & chain C", merge=1)

cmd.color ("blue", "resi 1063 & chain C")

cmd.select ("Outward", "resi 1063 & chain C", merge=1)

cmd.color ("blue", "resi 1064 & chain C")

cmd.select ("Outward", "resi 1064 & chain C", merge=1)

cmd.color ("blue", "resi 1065 & chain C")

cmd.select ("Outward", "resi 1065 & chain C", merge=1)

cmd.color ("blue", "resi 1066 & chain C")

cmd.select ("Outward", "resi 1066 & chain C", merge=1)

cmd.color ("blue", "resi 1067 & chain C")

cmd.select ("Outward", "resi 1067 & chain C", merge=1)

cmd.color ("blue", "resi 1068 & chain C")

cmd.select ("Outward", "resi 1068 & chain C", merge=1)

cmd.color ("blue", "resi 1074 & chain C")

cmd.select ("Outward", "resi 1074 & chain C", merge=1)

cmd.color ("blue", "resi 1075 & chain C")

cmd.select ("Outward", "resi 1075 & chain C", merge=1)

cmd.color ("blue", "resi 1076 & chain C")

cmd.select ("Outward", "resi 1076 & chain C", merge=1)

cmd.color ("blue", "resi 1077 & chain C")

cmd.select ("Outward", "resi 1077 & chain C", merge=1)

cmd.color ("blue", "resi 1078 & chain C")

cmd.select ("Outward", "resi 1078 & chain C", merge=1)

cmd.color ("blue", "resi 1079 & chain C")

cmd.select ("Outward", "resi 1079 & chain C", merge=1)

cmd.color ("blue", "resi 1080 & chain C")

cmd.select ("Outward", "resi 1080 & chain C", merge=1)

cmd.color ("blue", "resi 1081 & chain C")

cmd.select ("Outward", "resi 1081 & chain C", merge=1)

cmd.color ("blue", "resi 1082 & chain C")

cmd.select ("Outward", "resi 1082 & chain C", merge=1)

cmd.color ("blue", "resi 1083 & chain C")

cmd.select ("Outward", "resi 1083 & chain C", merge=1)

cmd.color ("blue", "resi 1089 & chain C")

cmd.select ("Outward", "resi 1089 & chain C", merge=1)

cmd.color ("blue", "resi 1090 & chain C")

cmd.select ("Outward", "resi 1090 & chain C", merge=1)

cmd.color ("blue", "resi 1091 & chain C")

cmd.select ("Outward", "resi 1091 & chain C", merge=1)

cmd.color ("blue", "resi 1092 & chain C")

cmd.select ("Outward", "resi 1092 & chain C", merge=1)

cmd.color ("blue", "resi 1093 & chain C")

cmd.select ("Outward", "resi 1093 & chain C", merge=1)

cmd.color ("blue", "resi 1094 & chain C")

cmd.select ("Outward", "resi 1094 & chain C", merge=1)

cmd.color ("blue", "resi 1095 & chain C")

cmd.select ("Outward", "resi 1095 & chain C", merge=1)

cmd.color ("blue", "resi 1096 & chain C")

cmd.select ("Outward", "resi 1096 & chain C", merge=1)

cmd.color ("blue", "resi 1097 & chain C")

cmd.select ("Outward", "resi 1097 & chain C", merge=1)

cmd.load_cgo( [9.0, 16.170252,19.043,70.0635, 16.198833, 19.040667, 45.04117, 1, 1,1,0,0,0,1], "axis" )
