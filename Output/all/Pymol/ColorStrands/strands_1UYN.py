from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1UYN.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("1UYN_X_S0", "resi 819-832 & chain X & 1UYN ")
cmd.color ("red", "1UYN_X_S0")


cmd.select("1UYN_X_S1", "resi 839-854 & chain X & 1UYN ")
cmd.color ("yellow", "1UYN_X_S1")


cmd.select("1UYN_X_S2", "resi 858-872 & chain X & 1UYN ")
cmd.color ("green", "1UYN_X_S2")


cmd.select("1UYN_X_S3", "resi 877-891 & chain X & 1UYN ")
cmd.color ("cyan", "1UYN_X_S3")


cmd.select("1UYN_X_S4", "resi 898-916 & chain X & 1UYN ")
cmd.color ("blue", "1UYN_X_S4")


cmd.select("1UYN_X_S5", "resi 920-939 & chain X & 1UYN ")
cmd.color ("magenta", "1UYN_X_S5")


cmd.select("1UYN_X_S6", "resi 948-968 & chain X & 1UYN ")
cmd.color ("red", "1UYN_X_S6")


cmd.select("1UYN_X_S7", "resi 974-996 & chain X & 1UYN ")
cmd.color ("yellow", "1UYN_X_S7")


cmd.select("1UYN_X_S8", "resi 1000-1010 & chain X & 1UYN ")
cmd.color ("green", "1UYN_X_S8")


cmd.select("1UYN_X_S9", "resi 1042-1051 & chain X & 1UYN ")
cmd.color ("cyan", "1UYN_X_S9")


cmd.select("1UYN_X_S10", "resi 1058-1067 & chain X & 1UYN ")
cmd.color ("blue", "1UYN_X_S10")


cmd.select("1UYN_X_S11", "resi 1073-1084 & chain X & 1UYN ")
cmd.color ("magenta", "1UYN_X_S11")


cmd.select("1UYN_barrel", "1UYN_X_S*")
cmd.show("cartoon", "1UYN_barrel")
cmd.zoom("1UYN_barrel")
