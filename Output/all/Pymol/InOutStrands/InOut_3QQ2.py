from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3QQ2.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 748+749+750+751+752+753+754+755+756+757+758+759+760+761 & chain A ")


cmd.select("Astrand12", "resi 996+997+998+999+1000+1001+1002+1003+1004+1005+1006+1007+1008 & chain A ")


cmd.select("Astrand11", "resi 982+983+984+985+986+987+988+989+990+991+992+993 & chain A ")


cmd.select("Astrand10", "resi 967+968+969+970+971+972+973+974+975+976+977+978 & chain A ")


cmd.select("Astrand9", "resi 933+934+935+936+937+938+939+940+941+942+943+944+945+946+947 & chain A ")


cmd.select("Astrand7", "resi 904+905+906+907+908+909+912+913+914+915+916+917+918+919+920+921+922+923+924+925+926+927+928 & chain A ")


cmd.select("Astrand6", "resi 881+882+883+884+885+886+887+888+889+890+891+892+893+894+895+896+897+898+899 & chain A ")


cmd.select("Astrand5", "resi 854+855+856+857+858+859+860+861+862+863+864+865+866+867+868+869+870+871+872+873+874+875+876 & chain A ")


cmd.select("Astrand4", "resi 830+831+832+833+834+835+836+837+838+839+840+841+842+843+844+845+846+847+848 & chain A ")


cmd.select("Astrand3", "resi 809+810+811+812+813+814+815+816+817+818+819+820+821+822+823+824+825+826 & chain A ")


cmd.select("Astrand2", "resi 788+789+790+791+792+793+794+795+796+797+798+799+800+801+802+803+804+805 & chain A ")


cmd.select("Astrand1", "resi 768+769+770+771+772+773+774+775+776+777+778+779+780+781+782+783+784+785 & chain A ")


cmd.select("barrel", "Astrand*")
cmd.show("sticks", "barrel")
cmd.show("cartoon", "barrel")
cmd.set("cartoon_side_chain_helper", "on")
cmd.zoom("barrel")
cmd.color ("red", "resi 748 & chain A")

cmd.select ("Inward", "resi 748 & chain A", merge=1)

cmd.color ("blue", "resi 749 & chain A")

cmd.select ("Outward", "resi 749 & chain A", merge=1)

cmd.color ("red", "resi 750 & chain A")

cmd.select ("Inward", "resi 750 & chain A", merge=1)

cmd.color ("blue", "resi 751 & chain A")

cmd.select ("Outward", "resi 751 & chain A", merge=1)

cmd.color ("red", "resi 752 & chain A")

cmd.select ("Inward", "resi 752 & chain A", merge=1)

cmd.color ("blue", "resi 753 & chain A")

cmd.select ("Outward", "resi 753 & chain A", merge=1)

cmd.color ("red", "resi 754 & chain A")

cmd.select ("Inward", "resi 754 & chain A", merge=1)

cmd.color ("blue", "resi 755 & chain A")

cmd.select ("Outward", "resi 755 & chain A", merge=1)

cmd.color ("red", "resi 756 & chain A")

cmd.select ("Inward", "resi 756 & chain A", merge=1)

cmd.color ("blue", "resi 757 & chain A")

cmd.select ("Outward", "resi 757 & chain A", merge=1)

cmd.color ("red", "resi 758 & chain A")

cmd.select ("Inward", "resi 758 & chain A", merge=1)

cmd.color ("blue", "resi 759 & chain A")

cmd.select ("Outward", "resi 759 & chain A", merge=1)

cmd.color ("red", "resi 760 & chain A")

cmd.select ("Inward", "resi 760 & chain A", merge=1)

cmd.color ("blue", "resi 761 & chain A")

cmd.select ("Outward", "resi 761 & chain A", merge=1)

cmd.color ("blue", "resi 996 & chain A")

cmd.select ("Outward", "resi 996 & chain A", merge=1)

cmd.color ("red", "resi 997 & chain A")

cmd.select ("Inward", "resi 997 & chain A", merge=1)

cmd.color ("blue", "resi 998 & chain A")

cmd.select ("Outward", "resi 998 & chain A", merge=1)

cmd.color ("red", "resi 999 & chain A")

cmd.select ("Inward", "resi 999 & chain A", merge=1)

cmd.color ("blue", "resi 1000 & chain A")

cmd.select ("Outward", "resi 1000 & chain A", merge=1)

cmd.color ("red", "resi 1001 & chain A")

cmd.select ("Inward", "resi 1001 & chain A", merge=1)

cmd.color ("blue", "resi 1002 & chain A")

cmd.select ("Outward", "resi 1002 & chain A", merge=1)

cmd.color ("red", "resi 1003 & chain A")

cmd.select ("Inward", "resi 1003 & chain A", merge=1)

cmd.color ("blue", "resi 1004 & chain A")

cmd.select ("Outward", "resi 1004 & chain A", merge=1)

cmd.color ("red", "resi 1005 & chain A")

cmd.select ("Inward", "resi 1005 & chain A", merge=1)

cmd.color ("blue", "resi 1006 & chain A")

cmd.select ("Outward", "resi 1006 & chain A", merge=1)

cmd.color ("red", "resi 1007 & chain A")

cmd.select ("Inward", "resi 1007 & chain A", merge=1)

cmd.color ("blue", "resi 1008 & chain A")

cmd.select ("Outward", "resi 1008 & chain A", merge=1)

cmd.color ("blue", "resi 982 & chain A")

cmd.select ("Outward", "resi 982 & chain A", merge=1)

cmd.color ("red", "resi 983 & chain A")

cmd.select ("Inward", "resi 983 & chain A", merge=1)

cmd.color ("blue", "resi 984 & chain A")

cmd.select ("Outward", "resi 984 & chain A", merge=1)

cmd.color ("red", "resi 985 & chain A")

cmd.select ("Inward", "resi 985 & chain A", merge=1)

cmd.color ("blue", "resi 986 & chain A")

cmd.select ("Outward", "resi 986 & chain A", merge=1)

cmd.color ("red", "resi 987 & chain A")

cmd.select ("Inward", "resi 987 & chain A", merge=1)

cmd.color ("blue", "resi 988 & chain A")

cmd.select ("Outward", "resi 988 & chain A", merge=1)

cmd.color ("red", "resi 989 & chain A")

cmd.select ("Inward", "resi 989 & chain A", merge=1)

cmd.color ("blue", "resi 990 & chain A")

cmd.select ("Outward", "resi 990 & chain A", merge=1)

cmd.color ("red", "resi 991 & chain A")

cmd.select ("Inward", "resi 991 & chain A", merge=1)

cmd.color ("blue", "resi 992 & chain A")

cmd.select ("Outward", "resi 992 & chain A", merge=1)

cmd.color ("red", "resi 993 & chain A")

cmd.select ("Inward", "resi 993 & chain A", merge=1)

cmd.color ("red", "resi 967 & chain A")

cmd.select ("Inward", "resi 967 & chain A", merge=1)

cmd.color ("blue", "resi 968 & chain A")

cmd.select ("Outward", "resi 968 & chain A", merge=1)

cmd.color ("red", "resi 969 & chain A")

cmd.select ("Inward", "resi 969 & chain A", merge=1)

cmd.color ("blue", "resi 970 & chain A")

cmd.select ("Outward", "resi 970 & chain A", merge=1)

cmd.color ("red", "resi 971 & chain A")

cmd.select ("Inward", "resi 971 & chain A", merge=1)

cmd.color ("blue", "resi 972 & chain A")

cmd.select ("Outward", "resi 972 & chain A", merge=1)

cmd.color ("red", "resi 973 & chain A")

cmd.select ("Inward", "resi 973 & chain A", merge=1)

cmd.color ("blue", "resi 974 & chain A")

cmd.select ("Outward", "resi 974 & chain A", merge=1)

cmd.color ("red", "resi 975 & chain A")

cmd.select ("Inward", "resi 975 & chain A", merge=1)

cmd.color ("blue", "resi 976 & chain A")

cmd.select ("Outward", "resi 976 & chain A", merge=1)

cmd.color ("blue", "resi 977 & chain A")

cmd.select ("Outward", "resi 977 & chain A", merge=1)

cmd.color ("red", "resi 978 & chain A")

cmd.select ("Inward", "resi 978 & chain A", merge=1)

cmd.color ("red", "resi 933 & chain A")

cmd.select ("Inward", "resi 933 & chain A", merge=1)

cmd.color ("blue", "resi 934 & chain A")

cmd.select ("Outward", "resi 934 & chain A", merge=1)

cmd.color ("red", "resi 935 & chain A")

cmd.select ("Inward", "resi 935 & chain A", merge=1)

cmd.color ("blue", "resi 936 & chain A")

cmd.select ("Outward", "resi 936 & chain A", merge=1)

cmd.color ("red", "resi 937 & chain A")

cmd.select ("Inward", "resi 937 & chain A", merge=1)

cmd.color ("blue", "resi 938 & chain A")

cmd.select ("Outward", "resi 938 & chain A", merge=1)

cmd.color ("red", "resi 939 & chain A")

cmd.select ("Inward", "resi 939 & chain A", merge=1)

cmd.color ("blue", "resi 940 & chain A")

cmd.select ("Outward", "resi 940 & chain A", merge=1)

cmd.color ("red", "resi 941 & chain A")

cmd.select ("Inward", "resi 941 & chain A", merge=1)

cmd.color ("blue", "resi 942 & chain A")

cmd.select ("Outward", "resi 942 & chain A", merge=1)

cmd.color ("red", "resi 943 & chain A")

cmd.select ("Inward", "resi 943 & chain A", merge=1)

cmd.color ("blue", "resi 944 & chain A")

cmd.select ("Outward", "resi 944 & chain A", merge=1)

cmd.color ("red", "resi 945 & chain A")

cmd.select ("Inward", "resi 945 & chain A", merge=1)

cmd.color ("blue", "resi 946 & chain A")

cmd.select ("Outward", "resi 946 & chain A", merge=1)

cmd.color ("red", "resi 947 & chain A")

cmd.select ("Inward", "resi 947 & chain A", merge=1)

cmd.color ("red", "resi 904 & chain A")

cmd.select ("Inward", "resi 904 & chain A", merge=1)

cmd.color ("blue", "resi 905 & chain A")

cmd.select ("Outward", "resi 905 & chain A", merge=1)

cmd.color ("blue", "resi 906 & chain A")

cmd.select ("Outward", "resi 906 & chain A", merge=1)

cmd.color ("blue", "resi 907 & chain A")

cmd.select ("Outward", "resi 907 & chain A", merge=1)

cmd.color ("blue", "resi 908 & chain A")

cmd.select ("Outward", "resi 908 & chain A", merge=1)

cmd.color ("red", "resi 909 & chain A")

cmd.select ("Inward", "resi 909 & chain A", merge=1)

cmd.color ("blue", "resi 912 & chain A")

cmd.select ("Outward", "resi 912 & chain A", merge=1)

cmd.color ("red", "resi 913 & chain A")

cmd.select ("Inward", "resi 913 & chain A", merge=1)

cmd.color ("blue", "resi 914 & chain A")

cmd.select ("Outward", "resi 914 & chain A", merge=1)

cmd.color ("red", "resi 915 & chain A")

cmd.select ("Inward", "resi 915 & chain A", merge=1)

cmd.color ("blue", "resi 916 & chain A")

cmd.select ("Outward", "resi 916 & chain A", merge=1)

cmd.color ("red", "resi 917 & chain A")

cmd.select ("Inward", "resi 917 & chain A", merge=1)

cmd.color ("blue", "resi 918 & chain A")

cmd.select ("Outward", "resi 918 & chain A", merge=1)

cmd.color ("red", "resi 919 & chain A")

cmd.select ("Inward", "resi 919 & chain A", merge=1)

cmd.color ("blue", "resi 920 & chain A")

cmd.select ("Outward", "resi 920 & chain A", merge=1)

cmd.color ("red", "resi 921 & chain A")

cmd.select ("Inward", "resi 921 & chain A", merge=1)

cmd.color ("blue", "resi 922 & chain A")

cmd.select ("Outward", "resi 922 & chain A", merge=1)

cmd.color ("red", "resi 923 & chain A")

cmd.select ("Inward", "resi 923 & chain A", merge=1)

cmd.color ("blue", "resi 924 & chain A")

cmd.select ("Outward", "resi 924 & chain A", merge=1)

cmd.color ("blue", "resi 925 & chain A")

cmd.select ("Outward", "resi 925 & chain A", merge=1)

cmd.color ("red", "resi 926 & chain A")

cmd.select ("Inward", "resi 926 & chain A", merge=1)

cmd.color ("blue", "resi 927 & chain A")

cmd.select ("Outward", "resi 927 & chain A", merge=1)

cmd.color ("red", "resi 928 & chain A")

cmd.select ("Inward", "resi 928 & chain A", merge=1)

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

cmd.color ("blue", "resi 886 & chain A")

cmd.select ("Outward", "resi 886 & chain A", merge=1)

cmd.color ("red", "resi 887 & chain A")

cmd.select ("Inward", "resi 887 & chain A", merge=1)

cmd.color ("blue", "resi 888 & chain A")

cmd.select ("Outward", "resi 888 & chain A", merge=1)

cmd.color ("red", "resi 889 & chain A")

cmd.select ("Inward", "resi 889 & chain A", merge=1)

cmd.color ("blue", "resi 890 & chain A")

cmd.select ("Outward", "resi 890 & chain A", merge=1)

cmd.color ("red", "resi 891 & chain A")

cmd.select ("Inward", "resi 891 & chain A", merge=1)

cmd.color ("blue", "resi 892 & chain A")

cmd.select ("Outward", "resi 892 & chain A", merge=1)

cmd.color ("red", "resi 893 & chain A")

cmd.select ("Inward", "resi 893 & chain A", merge=1)

cmd.color ("red", "resi 894 & chain A")

cmd.select ("Inward", "resi 894 & chain A", merge=1)

cmd.color ("blue", "resi 895 & chain A")

cmd.select ("Outward", "resi 895 & chain A", merge=1)

cmd.color ("red", "resi 896 & chain A")

cmd.select ("Inward", "resi 896 & chain A", merge=1)

cmd.color ("blue", "resi 897 & chain A")

cmd.select ("Outward", "resi 897 & chain A", merge=1)

cmd.color ("red", "resi 898 & chain A")

cmd.select ("Inward", "resi 898 & chain A", merge=1)

cmd.color ("blue", "resi 899 & chain A")

cmd.select ("Outward", "resi 899 & chain A", merge=1)

cmd.color ("blue", "resi 854 & chain A")

cmd.select ("Outward", "resi 854 & chain A", merge=1)

cmd.color ("red", "resi 855 & chain A")

cmd.select ("Inward", "resi 855 & chain A", merge=1)

cmd.color ("blue", "resi 856 & chain A")

cmd.select ("Outward", "resi 856 & chain A", merge=1)

cmd.color ("red", "resi 857 & chain A")

cmd.select ("Inward", "resi 857 & chain A", merge=1)

cmd.color ("blue", "resi 858 & chain A")

cmd.select ("Outward", "resi 858 & chain A", merge=1)

cmd.color ("red", "resi 859 & chain A")

cmd.select ("Inward", "resi 859 & chain A", merge=1)

cmd.color ("blue", "resi 860 & chain A")

cmd.select ("Outward", "resi 860 & chain A", merge=1)

cmd.color ("red", "resi 861 & chain A")

cmd.select ("Inward", "resi 861 & chain A", merge=1)

cmd.color ("blue", "resi 862 & chain A")

cmd.select ("Outward", "resi 862 & chain A", merge=1)

cmd.color ("red", "resi 863 & chain A")

cmd.select ("Inward", "resi 863 & chain A", merge=1)

cmd.color ("blue", "resi 864 & chain A")

cmd.select ("Outward", "resi 864 & chain A", merge=1)

cmd.color ("red", "resi 865 & chain A")

cmd.select ("Inward", "resi 865 & chain A", merge=1)

cmd.color ("blue", "resi 866 & chain A")

cmd.select ("Outward", "resi 866 & chain A", merge=1)

cmd.color ("red", "resi 867 & chain A")

cmd.select ("Inward", "resi 867 & chain A", merge=1)

cmd.color ("blue", "resi 868 & chain A")

cmd.select ("Outward", "resi 868 & chain A", merge=1)

cmd.color ("red", "resi 869 & chain A")

cmd.select ("Inward", "resi 869 & chain A", merge=1)

cmd.color ("blue", "resi 870 & chain A")

cmd.select ("Outward", "resi 870 & chain A", merge=1)

cmd.color ("red", "resi 871 & chain A")

cmd.select ("Inward", "resi 871 & chain A", merge=1)

cmd.color ("blue", "resi 872 & chain A")

cmd.select ("Outward", "resi 872 & chain A", merge=1)

cmd.color ("red", "resi 873 & chain A")

cmd.select ("Inward", "resi 873 & chain A", merge=1)

cmd.color ("blue", "resi 874 & chain A")

cmd.select ("Outward", "resi 874 & chain A", merge=1)

cmd.color ("blue", "resi 875 & chain A")

cmd.select ("Outward", "resi 875 & chain A", merge=1)

cmd.color ("red", "resi 876 & chain A")

cmd.select ("Inward", "resi 876 & chain A", merge=1)

cmd.color ("blue", "resi 830 & chain A")

cmd.select ("Outward", "resi 830 & chain A", merge=1)

cmd.color ("red", "resi 831 & chain A")

cmd.select ("Inward", "resi 831 & chain A", merge=1)

cmd.color ("blue", "resi 832 & chain A")

cmd.select ("Outward", "resi 832 & chain A", merge=1)

cmd.color ("red", "resi 833 & chain A")

cmd.select ("Inward", "resi 833 & chain A", merge=1)

cmd.color ("blue", "resi 834 & chain A")

cmd.select ("Outward", "resi 834 & chain A", merge=1)

cmd.color ("red", "resi 835 & chain A")

cmd.select ("Inward", "resi 835 & chain A", merge=1)

cmd.color ("blue", "resi 836 & chain A")

cmd.select ("Outward", "resi 836 & chain A", merge=1)

cmd.color ("red", "resi 837 & chain A")

cmd.select ("Inward", "resi 837 & chain A", merge=1)

cmd.color ("blue", "resi 838 & chain A")

cmd.select ("Outward", "resi 838 & chain A", merge=1)

cmd.color ("red", "resi 839 & chain A")

cmd.select ("Inward", "resi 839 & chain A", merge=1)

cmd.color ("blue", "resi 840 & chain A")

cmd.select ("Outward", "resi 840 & chain A", merge=1)

cmd.color ("red", "resi 841 & chain A")

cmd.select ("Inward", "resi 841 & chain A", merge=1)

cmd.color ("blue", "resi 842 & chain A")

cmd.select ("Outward", "resi 842 & chain A", merge=1)

cmd.color ("red", "resi 843 & chain A")

cmd.select ("Inward", "resi 843 & chain A", merge=1)

cmd.color ("blue", "resi 844 & chain A")

cmd.select ("Outward", "resi 844 & chain A", merge=1)

cmd.color ("red", "resi 845 & chain A")

cmd.select ("Inward", "resi 845 & chain A", merge=1)

cmd.color ("blue", "resi 846 & chain A")

cmd.select ("Outward", "resi 846 & chain A", merge=1)

cmd.color ("red", "resi 847 & chain A")

cmd.select ("Inward", "resi 847 & chain A", merge=1)

cmd.color ("blue", "resi 848 & chain A")

cmd.select ("Outward", "resi 848 & chain A", merge=1)

cmd.color ("red", "resi 809 & chain A")

cmd.select ("Inward", "resi 809 & chain A", merge=1)

cmd.color ("blue", "resi 810 & chain A")

cmd.select ("Outward", "resi 810 & chain A", merge=1)

cmd.color ("red", "resi 811 & chain A")

cmd.select ("Inward", "resi 811 & chain A", merge=1)

cmd.color ("blue", "resi 812 & chain A")

cmd.select ("Outward", "resi 812 & chain A", merge=1)

cmd.color ("red", "resi 813 & chain A")

cmd.select ("Inward", "resi 813 & chain A", merge=1)

cmd.color ("blue", "resi 814 & chain A")

cmd.select ("Outward", "resi 814 & chain A", merge=1)

cmd.color ("red", "resi 815 & chain A")

cmd.select ("Inward", "resi 815 & chain A", merge=1)

cmd.color ("blue", "resi 816 & chain A")

cmd.select ("Outward", "resi 816 & chain A", merge=1)

cmd.color ("red", "resi 817 & chain A")

cmd.select ("Inward", "resi 817 & chain A", merge=1)

cmd.color ("blue", "resi 818 & chain A")

cmd.select ("Outward", "resi 818 & chain A", merge=1)

cmd.color ("red", "resi 819 & chain A")

cmd.select ("Inward", "resi 819 & chain A", merge=1)

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

cmd.color ("red", "resi 799 & chain A")

cmd.select ("Inward", "resi 799 & chain A", merge=1)

cmd.color ("blue", "resi 800 & chain A")

cmd.select ("Outward", "resi 800 & chain A", merge=1)

cmd.color ("red", "resi 801 & chain A")

cmd.select ("Inward", "resi 801 & chain A", merge=1)

cmd.color ("blue", "resi 802 & chain A")

cmd.select ("Outward", "resi 802 & chain A", merge=1)

cmd.color ("red", "resi 803 & chain A")

cmd.select ("Inward", "resi 803 & chain A", merge=1)

cmd.color ("blue", "resi 804 & chain A")

cmd.select ("Outward", "resi 804 & chain A", merge=1)

cmd.color ("red", "resi 805 & chain A")

cmd.select ("Inward", "resi 805 & chain A", merge=1)

cmd.color ("red", "resi 768 & chain A")

cmd.select ("Inward", "resi 768 & chain A", merge=1)

cmd.color ("blue", "resi 769 & chain A")

cmd.select ("Outward", "resi 769 & chain A", merge=1)

cmd.color ("red", "resi 770 & chain A")

cmd.select ("Inward", "resi 770 & chain A", merge=1)

cmd.color ("blue", "resi 771 & chain A")

cmd.select ("Outward", "resi 771 & chain A", merge=1)

cmd.color ("red", "resi 772 & chain A")

cmd.select ("Inward", "resi 772 & chain A", merge=1)

cmd.color ("blue", "resi 773 & chain A")

cmd.select ("Outward", "resi 773 & chain A", merge=1)

cmd.color ("red", "resi 774 & chain A")

cmd.select ("Inward", "resi 774 & chain A", merge=1)

cmd.color ("blue", "resi 775 & chain A")

cmd.select ("Outward", "resi 775 & chain A", merge=1)

cmd.color ("red", "resi 776 & chain A")

cmd.select ("Inward", "resi 776 & chain A", merge=1)

cmd.color ("blue", "resi 777 & chain A")

cmd.select ("Outward", "resi 777 & chain A", merge=1)

cmd.color ("red", "resi 778 & chain A")

cmd.select ("Inward", "resi 778 & chain A", merge=1)

cmd.color ("blue", "resi 779 & chain A")

cmd.select ("Outward", "resi 779 & chain A", merge=1)

cmd.color ("red", "resi 780 & chain A")

cmd.select ("Inward", "resi 780 & chain A", merge=1)

cmd.color ("blue", "resi 781 & chain A")

cmd.select ("Outward", "resi 781 & chain A", merge=1)

cmd.color ("red", "resi 782 & chain A")

cmd.select ("Inward", "resi 782 & chain A", merge=1)

cmd.color ("blue", "resi 783 & chain A")

cmd.select ("Outward", "resi 783 & chain A", merge=1)

cmd.color ("blue", "resi 784 & chain A")

cmd.select ("Outward", "resi 784 & chain A", merge=1)

cmd.color ("red", "resi 785 & chain A")

cmd.select ("Inward", "resi 785 & chain A", merge=1)

cmd.load_cgo( [9.0, 15.660167,-10.816167,8.603917, 15.660167, -10.816167, 8.603917, 1, 1,1,0,0,0,1], "axis" )
