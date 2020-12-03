from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/6TZK.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand6", "resi 783+784+785+786+787+788+789+790+791+792+793+794+795+796+797+798 & chain A ")


cmd.select("Astrand35", "resi 1125+1126+1127+1128+1129+1130+1131+1132+1133+1134+1135+1136 & chain A ")


cmd.select("Astrand34", "resi 1110+1111+1112+1113+1114+1115+1116+1117+1118+1119 & chain A ")


cmd.select("Astrand33", "resi 1089+1090+1091+1092+1093+1094+1095+1096+1097+1098+1099+1100+1101+1102+1103+1104+1105+1106+1107 & chain A ")


cmd.select("Astrand28", "resi 1029+1030+1031+1032+1033+1034+1035+1036+1037+1038+1039+1040+1041+1042+1043 & chain A ")


cmd.select("Astrand29", "resi 1046+1047+1048+1049+1050+1051+1052+1053+1054+1055+1056+1057+1058+1059+1060+1061+1062+1063+1064 & chain A ")


cmd.select("Astrand24", "resi 978+979+980+981+982+983+984+985+986+987+988+989+990+991+992+993+994 & chain A ")


cmd.select("Astrand25", "resi 997+998+999+1000+1001+1002+1003+1004+1005+1006+1007+1008+1009+1010+1011+1012+1013 & chain A ")


cmd.select("Astrand22", "resi 959+960+961+962+963+964+965+966+967+968+969+970+971+972 & chain A ")


cmd.select("Astrand21", "resi 943+944+945+946+947+948+949+950+951+952+953 & chain A ")


cmd.select("Astrand16", "resi 907+908+909+910+911+912+913+914+915+916+917+918 & chain A ")


cmd.select("Astrand15", "resi 891+892+893+894+895+896+897+898+899+900+901+902+903+904 & chain A ")


cmd.select("Astrand14", "resi 878+879+880+881+882+883+884+885 & chain A ")


cmd.select("Astrand13", "resi 854+855+856+857+858+859+860+861+862+863+864+865+866+867+868+869+870+871+872+873+874+875 & chain A ")


cmd.select("Astrand8", "resi 820+821+822+823+824+825+826+827+828+829+830+831+832 & chain A ")


cmd.select("Astrand7", "resi 803+804+805+806+807+808+809+810+811+812+813+814+815+816+817 & chain A ")


cmd.select("barrel", "Astrand*")
cmd.show("sticks", "barrel")
cmd.show("cartoon", "barrel")
cmd.set("cartoon_side_chain_helper", "on")
cmd.zoom("barrel")
cmd.color ("red", "resi 783 & chain A")

cmd.select ("Inward", "resi 783 & chain A", merge=1)

cmd.color ("blue", "resi 784 & chain A")

cmd.select ("Outward", "resi 784 & chain A", merge=1)

cmd.color ("red", "resi 785 & chain A")

cmd.select ("Inward", "resi 785 & chain A", merge=1)

cmd.color ("blue", "resi 786 & chain A")

cmd.select ("Outward", "resi 786 & chain A", merge=1)

cmd.color ("red", "resi 787 & chain A")

cmd.select ("Inward", "resi 787 & chain A", merge=1)

cmd.color ("blue", "resi 788 & chain A")

cmd.select ("Outward", "resi 788 & chain A", merge=1)

cmd.color ("red", "resi 789 & chain A")

cmd.select ("Inward", "resi 789 & chain A", merge=1)

cmd.color ("blue", "resi 790 & chain A")

cmd.select ("Outward", "resi 790 & chain A", merge=1)

cmd.color ("red", "resi 791 & chain A")

cmd.select ("Inward", "resi 791 & chain A", merge=1)

cmd.color ("blue", "resi 792 & chain A")

cmd.select ("Outward", "resi 792 & chain A", merge=1)

cmd.color ("red", "resi 793 & chain A")

cmd.select ("Inward", "resi 793 & chain A", merge=1)

cmd.color ("blue", "resi 794 & chain A")

cmd.select ("Outward", "resi 794 & chain A", merge=1)

cmd.color ("red", "resi 795 & chain A")

cmd.select ("Inward", "resi 795 & chain A", merge=1)

cmd.color ("blue", "resi 796 & chain A")

cmd.select ("Outward", "resi 796 & chain A", merge=1)

cmd.color ("red", "resi 797 & chain A")

cmd.select ("Inward", "resi 797 & chain A", merge=1)

cmd.color ("blue", "resi 798 & chain A")

cmd.select ("Outward", "resi 798 & chain A", merge=1)

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

cmd.color ("red", "resi 1134 & chain A")

cmd.select ("Inward", "resi 1134 & chain A", merge=1)

cmd.color ("blue", "resi 1135 & chain A")

cmd.select ("Outward", "resi 1135 & chain A", merge=1)

cmd.color ("blue", "resi 1136 & chain A")

cmd.select ("Outward", "resi 1136 & chain A", merge=1)

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

cmd.color ("red", "resi 1115 & chain A")

cmd.select ("Inward", "resi 1115 & chain A", merge=1)

cmd.color ("blue", "resi 1116 & chain A")

cmd.select ("Outward", "resi 1116 & chain A", merge=1)

cmd.color ("red", "resi 1117 & chain A")

cmd.select ("Inward", "resi 1117 & chain A", merge=1)

cmd.color ("blue", "resi 1118 & chain A")

cmd.select ("Outward", "resi 1118 & chain A", merge=1)

cmd.color ("red", "resi 1119 & chain A")

cmd.select ("Inward", "resi 1119 & chain A", merge=1)

cmd.color ("red", "resi 1089 & chain A")

cmd.select ("Inward", "resi 1089 & chain A", merge=1)

cmd.color ("blue", "resi 1090 & chain A")

cmd.select ("Outward", "resi 1090 & chain A", merge=1)

cmd.color ("red", "resi 1091 & chain A")

cmd.select ("Inward", "resi 1091 & chain A", merge=1)

cmd.color ("blue", "resi 1092 & chain A")

cmd.select ("Outward", "resi 1092 & chain A", merge=1)

cmd.color ("red", "resi 1093 & chain A")

cmd.select ("Inward", "resi 1093 & chain A", merge=1)

cmd.color ("blue", "resi 1094 & chain A")

cmd.select ("Outward", "resi 1094 & chain A", merge=1)

cmd.color ("red", "resi 1095 & chain A")

cmd.select ("Inward", "resi 1095 & chain A", merge=1)

cmd.color ("blue", "resi 1096 & chain A")

cmd.select ("Outward", "resi 1096 & chain A", merge=1)

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

cmd.color ("blue", "resi 1105 & chain A")

cmd.select ("Outward", "resi 1105 & chain A", merge=1)

cmd.color ("red", "resi 1106 & chain A")

cmd.select ("Inward", "resi 1106 & chain A", merge=1)

cmd.color ("blue", "resi 1107 & chain A")

cmd.select ("Outward", "resi 1107 & chain A", merge=1)

cmd.color ("blue", "resi 1029 & chain A")

cmd.select ("Outward", "resi 1029 & chain A", merge=1)

cmd.color ("red", "resi 1030 & chain A")

cmd.select ("Inward", "resi 1030 & chain A", merge=1)

cmd.color ("blue", "resi 1031 & chain A")

cmd.select ("Outward", "resi 1031 & chain A", merge=1)

cmd.color ("red", "resi 1032 & chain A")

cmd.select ("Inward", "resi 1032 & chain A", merge=1)

cmd.color ("blue", "resi 1033 & chain A")

cmd.select ("Outward", "resi 1033 & chain A", merge=1)

cmd.color ("red", "resi 1034 & chain A")

cmd.select ("Inward", "resi 1034 & chain A", merge=1)

cmd.color ("blue", "resi 1035 & chain A")

cmd.select ("Outward", "resi 1035 & chain A", merge=1)

cmd.color ("red", "resi 1036 & chain A")

cmd.select ("Inward", "resi 1036 & chain A", merge=1)

cmd.color ("blue", "resi 1037 & chain A")

cmd.select ("Outward", "resi 1037 & chain A", merge=1)

cmd.color ("red", "resi 1038 & chain A")

cmd.select ("Inward", "resi 1038 & chain A", merge=1)

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

cmd.color ("blue", "resi 1046 & chain A")

cmd.select ("Outward", "resi 1046 & chain A", merge=1)

cmd.color ("red", "resi 1047 & chain A")

cmd.select ("Inward", "resi 1047 & chain A", merge=1)

cmd.color ("blue", "resi 1048 & chain A")

cmd.select ("Outward", "resi 1048 & chain A", merge=1)

cmd.color ("red", "resi 1049 & chain A")

cmd.select ("Inward", "resi 1049 & chain A", merge=1)

cmd.color ("blue", "resi 1050 & chain A")

cmd.select ("Outward", "resi 1050 & chain A", merge=1)

cmd.color ("red", "resi 1051 & chain A")

cmd.select ("Inward", "resi 1051 & chain A", merge=1)

cmd.color ("blue", "resi 1052 & chain A")

cmd.select ("Outward", "resi 1052 & chain A", merge=1)

cmd.color ("red", "resi 1053 & chain A")

cmd.select ("Inward", "resi 1053 & chain A", merge=1)

cmd.color ("blue", "resi 1054 & chain A")

cmd.select ("Outward", "resi 1054 & chain A", merge=1)

cmd.color ("red", "resi 1055 & chain A")

cmd.select ("Inward", "resi 1055 & chain A", merge=1)

cmd.color ("blue", "resi 1056 & chain A")

cmd.select ("Outward", "resi 1056 & chain A", merge=1)

cmd.color ("red", "resi 1057 & chain A")

cmd.select ("Inward", "resi 1057 & chain A", merge=1)

cmd.color ("blue", "resi 1058 & chain A")

cmd.select ("Outward", "resi 1058 & chain A", merge=1)

cmd.color ("red", "resi 1059 & chain A")

cmd.select ("Inward", "resi 1059 & chain A", merge=1)

cmd.color ("blue", "resi 1060 & chain A")

cmd.select ("Outward", "resi 1060 & chain A", merge=1)

cmd.color ("red", "resi 1061 & chain A")

cmd.select ("Inward", "resi 1061 & chain A", merge=1)

cmd.color ("blue", "resi 1062 & chain A")

cmd.select ("Outward", "resi 1062 & chain A", merge=1)

cmd.color ("blue", "resi 1063 & chain A")

cmd.select ("Outward", "resi 1063 & chain A", merge=1)

cmd.color ("red", "resi 1064 & chain A")

cmd.select ("Inward", "resi 1064 & chain A", merge=1)

cmd.color ("red", "resi 978 & chain A")

cmd.select ("Inward", "resi 978 & chain A", merge=1)

cmd.color ("blue", "resi 979 & chain A")

cmd.select ("Outward", "resi 979 & chain A", merge=1)

cmd.color ("red", "resi 980 & chain A")

cmd.select ("Inward", "resi 980 & chain A", merge=1)

cmd.color ("blue", "resi 981 & chain A")

cmd.select ("Outward", "resi 981 & chain A", merge=1)

cmd.color ("red", "resi 982 & chain A")

cmd.select ("Inward", "resi 982 & chain A", merge=1)

cmd.color ("blue", "resi 983 & chain A")

cmd.select ("Outward", "resi 983 & chain A", merge=1)

cmd.color ("red", "resi 984 & chain A")

cmd.select ("Inward", "resi 984 & chain A", merge=1)

cmd.color ("blue", "resi 985 & chain A")

cmd.select ("Outward", "resi 985 & chain A", merge=1)

cmd.color ("red", "resi 986 & chain A")

cmd.select ("Inward", "resi 986 & chain A", merge=1)

cmd.color ("blue", "resi 987 & chain A")

cmd.select ("Outward", "resi 987 & chain A", merge=1)

cmd.color ("red", "resi 988 & chain A")

cmd.select ("Inward", "resi 988 & chain A", merge=1)

cmd.color ("blue", "resi 989 & chain A")

cmd.select ("Outward", "resi 989 & chain A", merge=1)

cmd.color ("blue", "resi 990 & chain A")

cmd.select ("Outward", "resi 990 & chain A", merge=1)

cmd.color ("red", "resi 991 & chain A")

cmd.select ("Inward", "resi 991 & chain A", merge=1)

cmd.color ("blue", "resi 992 & chain A")

cmd.select ("Outward", "resi 992 & chain A", merge=1)

cmd.color ("red", "resi 993 & chain A")

cmd.select ("Inward", "resi 993 & chain A", merge=1)

cmd.color ("blue", "resi 994 & chain A")

cmd.select ("Outward", "resi 994 & chain A", merge=1)

cmd.color ("blue", "resi 997 & chain A")

cmd.select ("Outward", "resi 997 & chain A", merge=1)

cmd.color ("red", "resi 998 & chain A")

cmd.select ("Inward", "resi 998 & chain A", merge=1)

cmd.color ("blue", "resi 999 & chain A")

cmd.select ("Outward", "resi 999 & chain A", merge=1)

cmd.color ("red", "resi 1000 & chain A")

cmd.select ("Inward", "resi 1000 & chain A", merge=1)

cmd.color ("blue", "resi 1001 & chain A")

cmd.select ("Outward", "resi 1001 & chain A", merge=1)

cmd.color ("red", "resi 1002 & chain A")

cmd.select ("Inward", "resi 1002 & chain A", merge=1)

cmd.color ("blue", "resi 1003 & chain A")

cmd.select ("Outward", "resi 1003 & chain A", merge=1)

cmd.color ("red", "resi 1004 & chain A")

cmd.select ("Inward", "resi 1004 & chain A", merge=1)

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

cmd.color ("blue", "resi 1012 & chain A")

cmd.select ("Outward", "resi 1012 & chain A", merge=1)

cmd.color ("red", "resi 1013 & chain A")

cmd.select ("Inward", "resi 1013 & chain A", merge=1)

cmd.color ("blue", "resi 959 & chain A")

cmd.select ("Outward", "resi 959 & chain A", merge=1)

cmd.color ("red", "resi 960 & chain A")

cmd.select ("Inward", "resi 960 & chain A", merge=1)

cmd.color ("blue", "resi 961 & chain A")

cmd.select ("Outward", "resi 961 & chain A", merge=1)

cmd.color ("red", "resi 962 & chain A")

cmd.select ("Inward", "resi 962 & chain A", merge=1)

cmd.color ("blue", "resi 963 & chain A")

cmd.select ("Outward", "resi 963 & chain A", merge=1)

cmd.color ("red", "resi 964 & chain A")

cmd.select ("Inward", "resi 964 & chain A", merge=1)

cmd.color ("blue", "resi 965 & chain A")

cmd.select ("Outward", "resi 965 & chain A", merge=1)

cmd.color ("red", "resi 966 & chain A")

cmd.select ("Inward", "resi 966 & chain A", merge=1)

cmd.color ("blue", "resi 967 & chain A")

cmd.select ("Outward", "resi 967 & chain A", merge=1)

cmd.color ("red", "resi 968 & chain A")

cmd.select ("Inward", "resi 968 & chain A", merge=1)

cmd.color ("blue", "resi 969 & chain A")

cmd.select ("Outward", "resi 969 & chain A", merge=1)

cmd.color ("red", "resi 970 & chain A")

cmd.select ("Inward", "resi 970 & chain A", merge=1)

cmd.color ("blue", "resi 971 & chain A")

cmd.select ("Outward", "resi 971 & chain A", merge=1)

cmd.color ("red", "resi 972 & chain A")

cmd.select ("Inward", "resi 972 & chain A", merge=1)

cmd.color ("blue", "resi 943 & chain A")

cmd.select ("Outward", "resi 943 & chain A", merge=1)

cmd.color ("red", "resi 944 & chain A")

cmd.select ("Inward", "resi 944 & chain A", merge=1)

cmd.color ("blue", "resi 945 & chain A")

cmd.select ("Outward", "resi 945 & chain A", merge=1)

cmd.color ("red", "resi 946 & chain A")

cmd.select ("Inward", "resi 946 & chain A", merge=1)

cmd.color ("blue", "resi 947 & chain A")

cmd.select ("Outward", "resi 947 & chain A", merge=1)

cmd.color ("red", "resi 948 & chain A")

cmd.select ("Inward", "resi 948 & chain A", merge=1)

cmd.color ("blue", "resi 949 & chain A")

cmd.select ("Outward", "resi 949 & chain A", merge=1)

cmd.color ("red", "resi 950 & chain A")

cmd.select ("Inward", "resi 950 & chain A", merge=1)

cmd.color ("blue", "resi 951 & chain A")

cmd.select ("Outward", "resi 951 & chain A", merge=1)

cmd.color ("red", "resi 952 & chain A")

cmd.select ("Inward", "resi 952 & chain A", merge=1)

cmd.color ("blue", "resi 953 & chain A")

cmd.select ("Outward", "resi 953 & chain A", merge=1)

cmd.color ("blue", "resi 907 & chain A")

cmd.select ("Outward", "resi 907 & chain A", merge=1)

cmd.color ("red", "resi 908 & chain A")

cmd.select ("Inward", "resi 908 & chain A", merge=1)

cmd.color ("blue", "resi 909 & chain A")

cmd.select ("Outward", "resi 909 & chain A", merge=1)

cmd.color ("red", "resi 910 & chain A")

cmd.select ("Inward", "resi 910 & chain A", merge=1)

cmd.color ("blue", "resi 911 & chain A")

cmd.select ("Outward", "resi 911 & chain A", merge=1)

cmd.color ("red", "resi 912 & chain A")

cmd.select ("Inward", "resi 912 & chain A", merge=1)

cmd.color ("blue", "resi 913 & chain A")

cmd.select ("Outward", "resi 913 & chain A", merge=1)

cmd.color ("red", "resi 914 & chain A")

cmd.select ("Inward", "resi 914 & chain A", merge=1)

cmd.color ("blue", "resi 915 & chain A")

cmd.select ("Outward", "resi 915 & chain A", merge=1)

cmd.color ("red", "resi 916 & chain A")

cmd.select ("Inward", "resi 916 & chain A", merge=1)

cmd.color ("blue", "resi 917 & chain A")

cmd.select ("Outward", "resi 917 & chain A", merge=1)

cmd.color ("red", "resi 918 & chain A")

cmd.select ("Inward", "resi 918 & chain A", merge=1)

cmd.color ("red", "resi 891 & chain A")

cmd.select ("Inward", "resi 891 & chain A", merge=1)

cmd.color ("blue", "resi 892 & chain A")

cmd.select ("Outward", "resi 892 & chain A", merge=1)

cmd.color ("red", "resi 893 & chain A")

cmd.select ("Inward", "resi 893 & chain A", merge=1)

cmd.color ("blue", "resi 894 & chain A")

cmd.select ("Outward", "resi 894 & chain A", merge=1)

cmd.color ("red", "resi 895 & chain A")

cmd.select ("Inward", "resi 895 & chain A", merge=1)

cmd.color ("blue", "resi 896 & chain A")

cmd.select ("Outward", "resi 896 & chain A", merge=1)

cmd.color ("red", "resi 897 & chain A")

cmd.select ("Inward", "resi 897 & chain A", merge=1)

cmd.color ("blue", "resi 898 & chain A")

cmd.select ("Outward", "resi 898 & chain A", merge=1)

cmd.color ("red", "resi 899 & chain A")

cmd.select ("Inward", "resi 899 & chain A", merge=1)

cmd.color ("blue", "resi 900 & chain A")

cmd.select ("Outward", "resi 900 & chain A", merge=1)

cmd.color ("red", "resi 901 & chain A")

cmd.select ("Inward", "resi 901 & chain A", merge=1)

cmd.color ("blue", "resi 902 & chain A")

cmd.select ("Outward", "resi 902 & chain A", merge=1)

cmd.color ("blue", "resi 903 & chain A")

cmd.select ("Outward", "resi 903 & chain A", merge=1)

cmd.color ("red", "resi 904 & chain A")

cmd.select ("Inward", "resi 904 & chain A", merge=1)

cmd.color ("blue", "resi 878 & chain A")

cmd.select ("Outward", "resi 878 & chain A", merge=1)

cmd.color ("red", "resi 879 & chain A")

cmd.select ("Inward", "resi 879 & chain A", merge=1)

cmd.color ("blue", "resi 880 & chain A")

cmd.select ("Outward", "resi 880 & chain A", merge=1)

cmd.color ("red", "resi 881 & chain A")

cmd.select ("Inward", "resi 881 & chain A", merge=1)

cmd.color ("blue", "resi 882 & chain A")

cmd.select ("Outward", "resi 882 & chain A", merge=1)

cmd.color ("red", "resi 883 & chain A")

cmd.select ("Inward", "resi 883 & chain A", merge=1)

cmd.color ("blue", "resi 884 & chain A")

cmd.select ("Outward", "resi 884 & chain A", merge=1)

cmd.color ("red", "resi 885 & chain A")

cmd.select ("Inward", "resi 885 & chain A", merge=1)

cmd.color ("red", "resi 854 & chain A")

cmd.select ("Inward", "resi 854 & chain A", merge=1)

cmd.color ("blue", "resi 855 & chain A")

cmd.select ("Outward", "resi 855 & chain A", merge=1)

cmd.color ("blue", "resi 856 & chain A")

cmd.select ("Outward", "resi 856 & chain A", merge=1)

cmd.color ("red", "resi 857 & chain A")

cmd.select ("Inward", "resi 857 & chain A", merge=1)

cmd.color ("red", "resi 858 & chain A")

cmd.select ("Inward", "resi 858 & chain A", merge=1)

cmd.color ("blue", "resi 859 & chain A")

cmd.select ("Outward", "resi 859 & chain A", merge=1)

cmd.color ("red", "resi 860 & chain A")

cmd.select ("Inward", "resi 860 & chain A", merge=1)

cmd.color ("blue", "resi 861 & chain A")

cmd.select ("Outward", "resi 861 & chain A", merge=1)

cmd.color ("red", "resi 862 & chain A")

cmd.select ("Inward", "resi 862 & chain A", merge=1)

cmd.color ("blue", "resi 863 & chain A")

cmd.select ("Outward", "resi 863 & chain A", merge=1)

cmd.color ("red", "resi 864 & chain A")

cmd.select ("Inward", "resi 864 & chain A", merge=1)

cmd.color ("blue", "resi 865 & chain A")

cmd.select ("Outward", "resi 865 & chain A", merge=1)

cmd.color ("red", "resi 866 & chain A")

cmd.select ("Inward", "resi 866 & chain A", merge=1)

cmd.color ("blue", "resi 867 & chain A")

cmd.select ("Outward", "resi 867 & chain A", merge=1)

cmd.color ("red", "resi 868 & chain A")

cmd.select ("Inward", "resi 868 & chain A", merge=1)

cmd.color ("blue", "resi 869 & chain A")

cmd.select ("Outward", "resi 869 & chain A", merge=1)

cmd.color ("red", "resi 870 & chain A")

cmd.select ("Inward", "resi 870 & chain A", merge=1)

cmd.color ("blue", "resi 871 & chain A")

cmd.select ("Outward", "resi 871 & chain A", merge=1)

cmd.color ("red", "resi 872 & chain A")

cmd.select ("Inward", "resi 872 & chain A", merge=1)

cmd.color ("blue", "resi 873 & chain A")

cmd.select ("Outward", "resi 873 & chain A", merge=1)

cmd.color ("red", "resi 874 & chain A")

cmd.select ("Inward", "resi 874 & chain A", merge=1)

cmd.color ("blue", "resi 875 & chain A")

cmd.select ("Outward", "resi 875 & chain A", merge=1)

cmd.color ("blue", "resi 820 & chain A")

cmd.select ("Outward", "resi 820 & chain A", merge=1)

cmd.color ("red", "resi 821 & chain A")

cmd.select ("Inward", "resi 821 & chain A", merge=1)

cmd.color ("blue", "resi 822 & chain A")

cmd.select ("Outward", "resi 822 & chain A", merge=1)

cmd.color ("red", "resi 823 & chain A")

cmd.select ("Inward", "resi 823 & chain A", merge=1)

cmd.color ("blue", "resi 824 & chain A")

cmd.select ("Outward", "resi 824 & chain A", merge=1)

cmd.color ("red", "resi 825 & chain A")

cmd.select ("Inward", "resi 825 & chain A", merge=1)

cmd.color ("blue", "resi 826 & chain A")

cmd.select ("Outward", "resi 826 & chain A", merge=1)

cmd.color ("red", "resi 827 & chain A")

cmd.select ("Inward", "resi 827 & chain A", merge=1)

cmd.color ("blue", "resi 828 & chain A")

cmd.select ("Outward", "resi 828 & chain A", merge=1)

cmd.color ("red", "resi 829 & chain A")

cmd.select ("Inward", "resi 829 & chain A", merge=1)

cmd.color ("blue", "resi 830 & chain A")

cmd.select ("Outward", "resi 830 & chain A", merge=1)

cmd.color ("red", "resi 831 & chain A")

cmd.select ("Inward", "resi 831 & chain A", merge=1)

cmd.color ("blue", "resi 832 & chain A")

cmd.select ("Outward", "resi 832 & chain A", merge=1)

cmd.color ("red", "resi 803 & chain A")

cmd.select ("Inward", "resi 803 & chain A", merge=1)

cmd.color ("red", "resi 804 & chain A")

cmd.select ("Inward", "resi 804 & chain A", merge=1)

cmd.color ("blue", "resi 805 & chain A")

cmd.select ("Outward", "resi 805 & chain A", merge=1)

cmd.color ("red", "resi 806 & chain A")

cmd.select ("Inward", "resi 806 & chain A", merge=1)

cmd.color ("blue", "resi 807 & chain A")

cmd.select ("Outward", "resi 807 & chain A", merge=1)

cmd.color ("red", "resi 808 & chain A")

cmd.select ("Inward", "resi 808 & chain A", merge=1)

cmd.color ("blue", "resi 809 & chain A")

cmd.select ("Outward", "resi 809 & chain A", merge=1)

cmd.color ("red", "resi 810 & chain A")

cmd.select ("Inward", "resi 810 & chain A", merge=1)

cmd.color ("blue", "resi 811 & chain A")

cmd.select ("Outward", "resi 811 & chain A", merge=1)

cmd.color ("red", "resi 812 & chain A")

cmd.select ("Inward", "resi 812 & chain A", merge=1)

cmd.color ("blue", "resi 813 & chain A")

cmd.select ("Outward", "resi 813 & chain A", merge=1)

cmd.color ("red", "resi 814 & chain A")

cmd.select ("Inward", "resi 814 & chain A", merge=1)

cmd.color ("blue", "resi 815 & chain A")

cmd.select ("Outward", "resi 815 & chain A", merge=1)

cmd.color ("blue", "resi 816 & chain A")

cmd.select ("Outward", "resi 816 & chain A", merge=1)

cmd.color ("red", "resi 817 & chain A")

cmd.select ("Inward", "resi 817 & chain A", merge=1)

cmd.load_cgo( [9.0, 11.400375,17.290812,24.073751, 11.400375, 17.290812, 24.073751, 1, 1,1,0,0,0,1], "axis" )
