from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1UYN.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Xstrand0", "resi 819+820+821+822+823+824+825+826+827+828+829+830+831+832+833 & chain X ")
cmd.color ("red", "Xstrand0")


cmd.select("Xstrand1", "resi 838+839+840+841+842+843+844+845+846+847+848+849+850+851+852+853+854+855 & chain X ")
cmd.color ("green", "Xstrand1")


cmd.select("Xstrand2", "resi 858+859+860+861+862+863+864+865+866+867+868+869+870+871+872+873 & chain X ")
cmd.color ("orange", "Xstrand2")


cmd.select("Xstrand3", "resi 876+877+878+879+880+881+882+883+884+885+886+887+888+889+890+891+892+893 & chain X ")
cmd.color ("teal", "Xstrand3")


cmd.select("Xstrand4", "resi 897+898+899+900+901+902+903+904+905+906+907+908+909+910+911+912+913+914+915 & chain X ")
cmd.color ("yellow", "Xstrand4")


cmd.select("Xstrand5", "resi 921+922+923+924+925+926+927+928+929+930+931+932+933+934+935+936+937+938+939 & chain X ")
cmd.color ("blue", "Xstrand5")


cmd.select("Xstrand6", "resi 948+949+950+951+952+953+954+955+956+957+958+959+960+961+962 & chain X ")
cmd.color ("red", "Xstrand6")


cmd.select("Xstrand7", "resi 979+980+981+982+983+984+985+986+987+988+989+990+991+992+993+994+995 & chain X ")
cmd.color ("green", "Xstrand7")


cmd.select("Xstrand8", "resi 1000+1001+1002+1003+1004+1005+1006+1007+1008+1009+1010+1011 & chain X ")
cmd.color ("orange", "Xstrand8")


cmd.select("Xstrand9", "resi 1041+1042+1043+1044+1045+1046+1047+1048+1049+1050+1051+1052+1053+1054 & chain X ")
cmd.color ("teal", "Xstrand9")


cmd.select("Xstrand10", "resi 1057+1058+1059+1060+1061+1062+1063+1064+1065+1066+1067+1068 & chain X ")
cmd.color ("yellow", "Xstrand10")


cmd.select("Xstrand11", "resi 1071+1072+1073+1074+1075+1076+1077+1078+1079+1080+1081+1082+1083 & chain X ")
cmd.color ("blue", "Xstrand11")


cmd.select("barrel", "Xstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
