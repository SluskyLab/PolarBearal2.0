from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1UYN.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Xstrand0", "resi 819+820+821+822+823+824+825+826+827+828+829+830+831+832+833 & chain X ")


cmd.select("Xstrand1", "resi 838+839+840+841+842+843+844+845+846+847+848+849+850+851+852+853+854+855 & chain X ")


cmd.select("Xstrand2", "resi 858+859+860+861+862+863+864+865+866+867+868+869+870+871+872+873 & chain X ")


cmd.select("Xstrand3", "resi 876+877+878+879+880+881+882+883+884+885+886+887+888+889+890+891+892+893 & chain X ")


cmd.select("Xstrand4", "resi 897+898+899+900+901+902+903+904+905+906+907+908+909+910+911+912+913+914+915 & chain X ")


cmd.select("Xstrand5", "resi 921+922+923+924+925+926+927+928+929+930+931+932+933+934+935+936+937+938+939 & chain X ")


cmd.select("Xstrand6", "resi 948+949+950+951+952+953+954+955+956+957+958+959+960+961+962 & chain X ")


cmd.select("Xstrand7", "resi 979+980+981+982+983+984+985+986+987+988+989+990+991+992+993+994+995 & chain X ")


cmd.select("Xstrand8", "resi 1000+1001+1002+1003+1004+1005+1006+1007+1008+1009+1010+1011 & chain X ")


cmd.select("Xstrand9", "resi 1041+1042+1043+1044+1045+1046+1047+1048+1049+1050+1051+1052+1053+1054 & chain X ")


cmd.select("Xstrand10", "resi 1057+1058+1059+1060+1061+1062+1063+1064+1065+1066+1067+1068 & chain X ")


cmd.select("Xstrand11", "resi 1071+1072+1073+1074+1075+1076+1077+1078+1079+1080+1081+1082+1083 & chain X ")


cmd.select("barrel", "Xstrand*")
cmd.show("sticks", "barrel")
cmd.show("cartoon", "barrel")
cmd.set("cartoon_side_chain_helper", "on")
cmd.zoom("barrel")
cmd.color ("blue", "resi 819 & chain X")

cmd.select ("Outward", "resi 819 & chain X", merge=1)

cmd.color ("red", "resi 820 & chain X")

cmd.select ("Inward", "resi 820 & chain X", merge=1)

cmd.color ("blue", "resi 821 & chain X")

cmd.select ("Outward", "resi 821 & chain X", merge=1)

cmd.color ("red", "resi 822 & chain X")

cmd.select ("Inward", "resi 822 & chain X", merge=1)

cmd.color ("blue", "resi 823 & chain X")

cmd.select ("Outward", "resi 823 & chain X", merge=1)

cmd.color ("red", "resi 824 & chain X")

cmd.select ("Inward", "resi 824 & chain X", merge=1)

cmd.color ("blue", "resi 825 & chain X")

cmd.select ("Outward", "resi 825 & chain X", merge=1)

cmd.color ("red", "resi 826 & chain X")

cmd.select ("Inward", "resi 826 & chain X", merge=1)

cmd.color ("blue", "resi 827 & chain X")

cmd.select ("Outward", "resi 827 & chain X", merge=1)

cmd.color ("red", "resi 828 & chain X")

cmd.select ("Inward", "resi 828 & chain X", merge=1)

cmd.color ("blue", "resi 829 & chain X")

cmd.select ("Outward", "resi 829 & chain X", merge=1)

cmd.color ("red", "resi 830 & chain X")

cmd.select ("Inward", "resi 830 & chain X", merge=1)

cmd.color ("blue", "resi 831 & chain X")

cmd.select ("Outward", "resi 831 & chain X", merge=1)

cmd.color ("red", "resi 832 & chain X")

cmd.select ("Inward", "resi 832 & chain X", merge=1)

cmd.color ("blue", "resi 833 & chain X")

cmd.select ("Outward", "resi 833 & chain X", merge=1)

cmd.color ("blue", "resi 838 & chain X")

cmd.select ("Outward", "resi 838 & chain X", merge=1)

cmd.color ("red", "resi 839 & chain X")

cmd.select ("Inward", "resi 839 & chain X", merge=1)

cmd.color ("blue", "resi 840 & chain X")

cmd.select ("Outward", "resi 840 & chain X", merge=1)

cmd.color ("red", "resi 841 & chain X")

cmd.select ("Inward", "resi 841 & chain X", merge=1)

cmd.color ("blue", "resi 842 & chain X")

cmd.select ("Outward", "resi 842 & chain X", merge=1)

cmd.color ("red", "resi 843 & chain X")

cmd.select ("Inward", "resi 843 & chain X", merge=1)

cmd.color ("blue", "resi 844 & chain X")

cmd.select ("Outward", "resi 844 & chain X", merge=1)

cmd.color ("red", "resi 845 & chain X")

cmd.select ("Inward", "resi 845 & chain X", merge=1)

cmd.color ("blue", "resi 846 & chain X")

cmd.select ("Outward", "resi 846 & chain X", merge=1)

cmd.color ("red", "resi 847 & chain X")

cmd.select ("Inward", "resi 847 & chain X", merge=1)

cmd.color ("blue", "resi 848 & chain X")

cmd.select ("Outward", "resi 848 & chain X", merge=1)

cmd.color ("red", "resi 849 & chain X")

cmd.select ("Inward", "resi 849 & chain X", merge=1)

cmd.color ("blue", "resi 850 & chain X")

cmd.select ("Outward", "resi 850 & chain X", merge=1)

cmd.color ("red", "resi 851 & chain X")

cmd.select ("Inward", "resi 851 & chain X", merge=1)

cmd.color ("blue", "resi 852 & chain X")

cmd.select ("Outward", "resi 852 & chain X", merge=1)

cmd.color ("blue", "resi 853 & chain X")

cmd.select ("Outward", "resi 853 & chain X", merge=1)

cmd.color ("red", "resi 854 & chain X")

cmd.select ("Inward", "resi 854 & chain X", merge=1)

cmd.color ("blue", "resi 855 & chain X")

cmd.select ("Outward", "resi 855 & chain X", merge=1)

cmd.color ("blue", "resi 858 & chain X")

cmd.select ("Outward", "resi 858 & chain X", merge=1)

cmd.color ("red", "resi 859 & chain X")

cmd.select ("Inward", "resi 859 & chain X", merge=1)

cmd.color ("blue", "resi 860 & chain X")

cmd.select ("Outward", "resi 860 & chain X", merge=1)

cmd.color ("red", "resi 861 & chain X")

cmd.select ("Inward", "resi 861 & chain X", merge=1)

cmd.color ("blue", "resi 862 & chain X")

cmd.select ("Outward", "resi 862 & chain X", merge=1)

cmd.color ("red", "resi 863 & chain X")

cmd.select ("Inward", "resi 863 & chain X", merge=1)

cmd.color ("blue", "resi 864 & chain X")

cmd.select ("Outward", "resi 864 & chain X", merge=1)

cmd.color ("red", "resi 865 & chain X")

cmd.select ("Inward", "resi 865 & chain X", merge=1)

cmd.color ("blue", "resi 866 & chain X")

cmd.select ("Outward", "resi 866 & chain X", merge=1)

cmd.color ("red", "resi 867 & chain X")

cmd.select ("Inward", "resi 867 & chain X", merge=1)

cmd.color ("blue", "resi 868 & chain X")

cmd.select ("Outward", "resi 868 & chain X", merge=1)

cmd.color ("red", "resi 869 & chain X")

cmd.select ("Inward", "resi 869 & chain X", merge=1)

cmd.color ("blue", "resi 870 & chain X")

cmd.select ("Outward", "resi 870 & chain X", merge=1)

cmd.color ("red", "resi 871 & chain X")

cmd.select ("Inward", "resi 871 & chain X", merge=1)

cmd.color ("blue", "resi 872 & chain X")

cmd.select ("Outward", "resi 872 & chain X", merge=1)

cmd.color ("red", "resi 873 & chain X")

cmd.select ("Inward", "resi 873 & chain X", merge=1)

cmd.color ("red", "resi 876 & chain X")

cmd.select ("Inward", "resi 876 & chain X", merge=1)

cmd.color ("blue", "resi 877 & chain X")

cmd.select ("Outward", "resi 877 & chain X", merge=1)

cmd.color ("red", "resi 878 & chain X")

cmd.select ("Inward", "resi 878 & chain X", merge=1)

cmd.color ("blue", "resi 879 & chain X")

cmd.select ("Outward", "resi 879 & chain X", merge=1)

cmd.color ("red", "resi 880 & chain X")

cmd.select ("Inward", "resi 880 & chain X", merge=1)

cmd.color ("blue", "resi 881 & chain X")

cmd.select ("Outward", "resi 881 & chain X", merge=1)

cmd.color ("red", "resi 882 & chain X")

cmd.select ("Inward", "resi 882 & chain X", merge=1)

cmd.color ("blue", "resi 883 & chain X")

cmd.select ("Outward", "resi 883 & chain X", merge=1)

cmd.color ("red", "resi 884 & chain X")

cmd.select ("Inward", "resi 884 & chain X", merge=1)

cmd.color ("blue", "resi 885 & chain X")

cmd.select ("Outward", "resi 885 & chain X", merge=1)

cmd.color ("red", "resi 886 & chain X")

cmd.select ("Inward", "resi 886 & chain X", merge=1)

cmd.color ("blue", "resi 887 & chain X")

cmd.select ("Outward", "resi 887 & chain X", merge=1)

cmd.color ("red", "resi 888 & chain X")

cmd.select ("Inward", "resi 888 & chain X", merge=1)

cmd.color ("blue", "resi 889 & chain X")

cmd.select ("Outward", "resi 889 & chain X", merge=1)

cmd.color ("red", "resi 890 & chain X")

cmd.select ("Inward", "resi 890 & chain X", merge=1)

cmd.color ("blue", "resi 891 & chain X")

cmd.select ("Outward", "resi 891 & chain X", merge=1)

cmd.color ("blue", "resi 892 & chain X")

cmd.select ("Outward", "resi 892 & chain X", merge=1)

cmd.color ("red", "resi 893 & chain X")

cmd.select ("Inward", "resi 893 & chain X", merge=1)

cmd.color ("blue", "resi 897 & chain X")

cmd.select ("Outward", "resi 897 & chain X", merge=1)

cmd.color ("red", "resi 898 & chain X")

cmd.select ("Inward", "resi 898 & chain X", merge=1)

cmd.color ("blue", "resi 899 & chain X")

cmd.select ("Outward", "resi 899 & chain X", merge=1)

cmd.color ("red", "resi 900 & chain X")

cmd.select ("Inward", "resi 900 & chain X", merge=1)

cmd.color ("blue", "resi 901 & chain X")

cmd.select ("Outward", "resi 901 & chain X", merge=1)

cmd.color ("red", "resi 902 & chain X")

cmd.select ("Inward", "resi 902 & chain X", merge=1)

cmd.color ("blue", "resi 903 & chain X")

cmd.select ("Outward", "resi 903 & chain X", merge=1)

cmd.color ("red", "resi 904 & chain X")

cmd.select ("Inward", "resi 904 & chain X", merge=1)

cmd.color ("blue", "resi 905 & chain X")

cmd.select ("Outward", "resi 905 & chain X", merge=1)

cmd.color ("red", "resi 906 & chain X")

cmd.select ("Inward", "resi 906 & chain X", merge=1)

cmd.color ("blue", "resi 907 & chain X")

cmd.select ("Outward", "resi 907 & chain X", merge=1)

cmd.color ("red", "resi 908 & chain X")

cmd.select ("Inward", "resi 908 & chain X", merge=1)

cmd.color ("blue", "resi 909 & chain X")

cmd.select ("Outward", "resi 909 & chain X", merge=1)

cmd.color ("red", "resi 910 & chain X")

cmd.select ("Inward", "resi 910 & chain X", merge=1)

cmd.color ("blue", "resi 911 & chain X")

cmd.select ("Outward", "resi 911 & chain X", merge=1)

cmd.color ("red", "resi 912 & chain X")

cmd.select ("Inward", "resi 912 & chain X", merge=1)

cmd.color ("blue", "resi 913 & chain X")

cmd.select ("Outward", "resi 913 & chain X", merge=1)

cmd.color ("red", "resi 914 & chain X")

cmd.select ("Inward", "resi 914 & chain X", merge=1)

cmd.color ("blue", "resi 915 & chain X")

cmd.select ("Outward", "resi 915 & chain X", merge=1)

cmd.color ("blue", "resi 921 & chain X")

cmd.select ("Outward", "resi 921 & chain X", merge=1)

cmd.color ("red", "resi 922 & chain X")

cmd.select ("Inward", "resi 922 & chain X", merge=1)

cmd.color ("blue", "resi 923 & chain X")

cmd.select ("Outward", "resi 923 & chain X", merge=1)

cmd.color ("red", "resi 924 & chain X")

cmd.select ("Inward", "resi 924 & chain X", merge=1)

cmd.color ("blue", "resi 925 & chain X")

cmd.select ("Outward", "resi 925 & chain X", merge=1)

cmd.color ("red", "resi 926 & chain X")

cmd.select ("Inward", "resi 926 & chain X", merge=1)

cmd.color ("blue", "resi 927 & chain X")

cmd.select ("Outward", "resi 927 & chain X", merge=1)

cmd.color ("red", "resi 928 & chain X")

cmd.select ("Inward", "resi 928 & chain X", merge=1)

cmd.color ("blue", "resi 929 & chain X")

cmd.select ("Outward", "resi 929 & chain X", merge=1)

cmd.color ("red", "resi 930 & chain X")

cmd.select ("Inward", "resi 930 & chain X", merge=1)

cmd.color ("blue", "resi 931 & chain X")

cmd.select ("Outward", "resi 931 & chain X", merge=1)

cmd.color ("red", "resi 932 & chain X")

cmd.select ("Inward", "resi 932 & chain X", merge=1)

cmd.color ("blue", "resi 933 & chain X")

cmd.select ("Outward", "resi 933 & chain X", merge=1)

cmd.color ("red", "resi 934 & chain X")

cmd.select ("Inward", "resi 934 & chain X", merge=1)

cmd.color ("blue", "resi 935 & chain X")

cmd.select ("Outward", "resi 935 & chain X", merge=1)

cmd.color ("red", "resi 936 & chain X")

cmd.select ("Inward", "resi 936 & chain X", merge=1)

cmd.color ("blue", "resi 937 & chain X")

cmd.select ("Outward", "resi 937 & chain X", merge=1)

cmd.color ("red", "resi 938 & chain X")

cmd.select ("Inward", "resi 938 & chain X", merge=1)

cmd.color ("blue", "resi 939 & chain X")

cmd.select ("Outward", "resi 939 & chain X", merge=1)

cmd.color ("red", "resi 948 & chain X")

cmd.select ("Inward", "resi 948 & chain X", merge=1)

cmd.color ("blue", "resi 949 & chain X")

cmd.select ("Outward", "resi 949 & chain X", merge=1)

cmd.color ("red", "resi 950 & chain X")

cmd.select ("Inward", "resi 950 & chain X", merge=1)

cmd.color ("blue", "resi 951 & chain X")

cmd.select ("Outward", "resi 951 & chain X", merge=1)

cmd.color ("red", "resi 952 & chain X")

cmd.select ("Inward", "resi 952 & chain X", merge=1)

cmd.color ("blue", "resi 953 & chain X")

cmd.select ("Outward", "resi 953 & chain X", merge=1)

cmd.color ("red", "resi 954 & chain X")

cmd.select ("Inward", "resi 954 & chain X", merge=1)

cmd.color ("blue", "resi 955 & chain X")

cmd.select ("Outward", "resi 955 & chain X", merge=1)

cmd.color ("red", "resi 956 & chain X")

cmd.select ("Inward", "resi 956 & chain X", merge=1)

cmd.color ("blue", "resi 957 & chain X")

cmd.select ("Outward", "resi 957 & chain X", merge=1)

cmd.color ("red", "resi 958 & chain X")

cmd.select ("Inward", "resi 958 & chain X", merge=1)

cmd.color ("blue", "resi 959 & chain X")

cmd.select ("Outward", "resi 959 & chain X", merge=1)

cmd.color ("red", "resi 960 & chain X")

cmd.select ("Inward", "resi 960 & chain X", merge=1)

cmd.color ("blue", "resi 961 & chain X")

cmd.select ("Outward", "resi 961 & chain X", merge=1)

cmd.color ("red", "resi 962 & chain X")

cmd.select ("Inward", "resi 962 & chain X", merge=1)

cmd.color ("red", "resi 979 & chain X")

cmd.select ("Inward", "resi 979 & chain X", merge=1)

cmd.color ("blue", "resi 980 & chain X")

cmd.select ("Outward", "resi 980 & chain X", merge=1)

cmd.color ("red", "resi 981 & chain X")

cmd.select ("Inward", "resi 981 & chain X", merge=1)

cmd.color ("blue", "resi 982 & chain X")

cmd.select ("Outward", "resi 982 & chain X", merge=1)

cmd.color ("red", "resi 983 & chain X")

cmd.select ("Inward", "resi 983 & chain X", merge=1)

cmd.color ("blue", "resi 984 & chain X")

cmd.select ("Outward", "resi 984 & chain X", merge=1)

cmd.color ("red", "resi 985 & chain X")

cmd.select ("Inward", "resi 985 & chain X", merge=1)

cmd.color ("blue", "resi 986 & chain X")

cmd.select ("Outward", "resi 986 & chain X", merge=1)

cmd.color ("red", "resi 987 & chain X")

cmd.select ("Inward", "resi 987 & chain X", merge=1)

cmd.color ("blue", "resi 988 & chain X")

cmd.select ("Outward", "resi 988 & chain X", merge=1)

cmd.color ("red", "resi 989 & chain X")

cmd.select ("Inward", "resi 989 & chain X", merge=1)

cmd.color ("blue", "resi 990 & chain X")

cmd.select ("Outward", "resi 990 & chain X", merge=1)

cmd.color ("red", "resi 991 & chain X")

cmd.select ("Inward", "resi 991 & chain X", merge=1)

cmd.color ("blue", "resi 992 & chain X")

cmd.select ("Outward", "resi 992 & chain X", merge=1)

cmd.color ("blue", "resi 993 & chain X")

cmd.select ("Outward", "resi 993 & chain X", merge=1)

cmd.color ("blue", "resi 994 & chain X")

cmd.select ("Outward", "resi 994 & chain X", merge=1)

cmd.color ("blue", "resi 995 & chain X")

cmd.select ("Outward", "resi 995 & chain X", merge=1)

cmd.color ("blue", "resi 1000 & chain X")

cmd.select ("Outward", "resi 1000 & chain X", merge=1)

cmd.color ("red", "resi 1001 & chain X")

cmd.select ("Inward", "resi 1001 & chain X", merge=1)

cmd.color ("blue", "resi 1002 & chain X")

cmd.select ("Outward", "resi 1002 & chain X", merge=1)

cmd.color ("red", "resi 1003 & chain X")

cmd.select ("Inward", "resi 1003 & chain X", merge=1)

cmd.color ("blue", "resi 1004 & chain X")

cmd.select ("Outward", "resi 1004 & chain X", merge=1)

cmd.color ("red", "resi 1005 & chain X")

cmd.select ("Inward", "resi 1005 & chain X", merge=1)

cmd.color ("blue", "resi 1006 & chain X")

cmd.select ("Outward", "resi 1006 & chain X", merge=1)

cmd.color ("red", "resi 1007 & chain X")

cmd.select ("Inward", "resi 1007 & chain X", merge=1)

cmd.color ("blue", "resi 1008 & chain X")

cmd.select ("Outward", "resi 1008 & chain X", merge=1)

cmd.color ("red", "resi 1009 & chain X")

cmd.select ("Inward", "resi 1009 & chain X", merge=1)

cmd.color ("blue", "resi 1010 & chain X")

cmd.select ("Outward", "resi 1010 & chain X", merge=1)

cmd.color ("red", "resi 1011 & chain X")

cmd.select ("Inward", "resi 1011 & chain X", merge=1)

cmd.color ("blue", "resi 1041 & chain X")

cmd.select ("Outward", "resi 1041 & chain X", merge=1)

cmd.color ("red", "resi 1042 & chain X")

cmd.select ("Inward", "resi 1042 & chain X", merge=1)

cmd.color ("blue", "resi 1043 & chain X")

cmd.select ("Outward", "resi 1043 & chain X", merge=1)

cmd.color ("red", "resi 1044 & chain X")

cmd.select ("Inward", "resi 1044 & chain X", merge=1)

cmd.color ("blue", "resi 1045 & chain X")

cmd.select ("Outward", "resi 1045 & chain X", merge=1)

cmd.color ("red", "resi 1046 & chain X")

cmd.select ("Inward", "resi 1046 & chain X", merge=1)

cmd.color ("blue", "resi 1047 & chain X")

cmd.select ("Outward", "resi 1047 & chain X", merge=1)

cmd.color ("red", "resi 1048 & chain X")

cmd.select ("Inward", "resi 1048 & chain X", merge=1)

cmd.color ("blue", "resi 1049 & chain X")

cmd.select ("Outward", "resi 1049 & chain X", merge=1)

cmd.color ("blue", "resi 1050 & chain X")

cmd.select ("Outward", "resi 1050 & chain X", merge=1)

cmd.color ("blue", "resi 1051 & chain X")

cmd.select ("Outward", "resi 1051 & chain X", merge=1)

cmd.color ("blue", "resi 1052 & chain X")

cmd.select ("Outward", "resi 1052 & chain X", merge=1)

cmd.color ("red", "resi 1053 & chain X")

cmd.select ("Inward", "resi 1053 & chain X", merge=1)

cmd.color ("blue", "resi 1054 & chain X")

cmd.select ("Outward", "resi 1054 & chain X", merge=1)

cmd.color ("blue", "resi 1057 & chain X")

cmd.select ("Outward", "resi 1057 & chain X", merge=1)

cmd.color ("red", "resi 1058 & chain X")

cmd.select ("Inward", "resi 1058 & chain X", merge=1)

cmd.color ("blue", "resi 1059 & chain X")

cmd.select ("Outward", "resi 1059 & chain X", merge=1)

cmd.color ("red", "resi 1060 & chain X")

cmd.select ("Inward", "resi 1060 & chain X", merge=1)

cmd.color ("blue", "resi 1061 & chain X")

cmd.select ("Outward", "resi 1061 & chain X", merge=1)

cmd.color ("red", "resi 1062 & chain X")

cmd.select ("Inward", "resi 1062 & chain X", merge=1)

cmd.color ("blue", "resi 1063 & chain X")

cmd.select ("Outward", "resi 1063 & chain X", merge=1)

cmd.color ("red", "resi 1064 & chain X")

cmd.select ("Inward", "resi 1064 & chain X", merge=1)

cmd.color ("blue", "resi 1065 & chain X")

cmd.select ("Outward", "resi 1065 & chain X", merge=1)

cmd.color ("red", "resi 1066 & chain X")

cmd.select ("Inward", "resi 1066 & chain X", merge=1)

cmd.color ("blue", "resi 1067 & chain X")

cmd.select ("Outward", "resi 1067 & chain X", merge=1)

cmd.color ("red", "resi 1068 & chain X")

cmd.select ("Inward", "resi 1068 & chain X", merge=1)

cmd.color ("red", "resi 1071 & chain X")

cmd.select ("Inward", "resi 1071 & chain X", merge=1)

cmd.color ("blue", "resi 1072 & chain X")

cmd.select ("Outward", "resi 1072 & chain X", merge=1)

cmd.color ("red", "resi 1073 & chain X")

cmd.select ("Inward", "resi 1073 & chain X", merge=1)

cmd.color ("blue", "resi 1074 & chain X")

cmd.select ("Outward", "resi 1074 & chain X", merge=1)

cmd.color ("red", "resi 1075 & chain X")

cmd.select ("Inward", "resi 1075 & chain X", merge=1)

cmd.color ("blue", "resi 1076 & chain X")

cmd.select ("Outward", "resi 1076 & chain X", merge=1)

cmd.color ("red", "resi 1077 & chain X")

cmd.select ("Inward", "resi 1077 & chain X", merge=1)

cmd.color ("blue", "resi 1078 & chain X")

cmd.select ("Outward", "resi 1078 & chain X", merge=1)

cmd.color ("red", "resi 1079 & chain X")

cmd.select ("Inward", "resi 1079 & chain X", merge=1)

cmd.color ("blue", "resi 1080 & chain X")

cmd.select ("Outward", "resi 1080 & chain X", merge=1)

cmd.color ("red", "resi 1081 & chain X")

cmd.select ("Inward", "resi 1081 & chain X", merge=1)

cmd.color ("blue", "resi 1082 & chain X")

cmd.select ("Outward", "resi 1082 & chain X", merge=1)

cmd.color ("blue", "resi 1083 & chain X")

cmd.select ("Outward", "resi 1083 & chain X", merge=1)

cmd.load_cgo( [9.0, 12.164584,17.93775,197.62059, 12.164584, 17.93775, 197.62059, 1, 1,1,0,0,0,1], "axis" )
