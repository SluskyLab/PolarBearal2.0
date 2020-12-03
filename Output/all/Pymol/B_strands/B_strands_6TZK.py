from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/6TZK.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 783+784+785+786+787+788+789+790+791+792+793+794+795+796+797+798 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 1125+1126+1127+1128+1129+1130+1131+1132+1133+1134+1135+1136 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 1110+1111+1112+1113+1114+1115+1116+1117+1118+1119 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 1089+1090+1091+1092+1093+1094+1095+1096+1097+1098+1099+1100+1101+1102+1103+1104+1105+1106+1107 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 1029+1030+1031+1032+1033+1034+1035+1036+1037+1038+1039+1040+1041+1042+1043 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 1046+1047+1048+1049+1050+1051+1052+1053+1054+1055+1056+1057+1058+1059+1060+1061+1062+1063+1064 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 978+979+980+981+982+983+984+985+986+987+988+989+990+991+992+993+994 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 997+998+999+1000+1001+1002+1003+1004+1005+1006+1007+1008+1009+1010+1011+1012+1013 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 959+960+961+962+963+964+965+966+967+968+969+970+971+972 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 943+944+945+946+947+948+949+950+951+952+953 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 907+908+909+910+911+912+913+914+915+916+917+918 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 891+892+893+894+895+896+897+898+899+900+901+902+903+904 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 878+879+880+881+882+883+884+885 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 854+855+856+857+858+859+860+861+862+863+864+865+866+867+868+869+870+871+872+873+874+875 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 820+821+822+823+824+825+826+827+828+829+830+831+832 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 803+804+805+806+807+808+809+810+811+812+813+814+815+816+817 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
