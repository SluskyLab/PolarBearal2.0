from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/6TZK.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("6TZK_A_S0", "resi 785-798 & chain A & 6TZK ")
cmd.color ("red", "6TZK_A_S0")


cmd.select("6TZK_A_S1", "resi 803-815 & chain A & 6TZK ")
cmd.color ("yellow", "6TZK_A_S1")


cmd.select("6TZK_A_S2", "resi 821-834 & chain A & 6TZK ")
cmd.color ("green", "6TZK_A_S2")


cmd.select("6TZK_A_S3", "resi 862-874 & chain A & 6TZK ")
cmd.color ("cyan", "6TZK_A_S3")


cmd.select("6TZK_A_S4", "resi 877-887 & chain A & 6TZK ")
cmd.color ("blue", "6TZK_A_S4")


cmd.select("6TZK_A_S5", "resi 891-902 & chain A & 6TZK ")
cmd.color ("magenta", "6TZK_A_S5")


cmd.select("6TZK_A_S6", "resi 908-928 & chain A & 6TZK ")
cmd.color ("red", "6TZK_A_S6")


cmd.select("6TZK_A_S7", "resi 939-953 & chain A & 6TZK ")
cmd.color ("yellow", "6TZK_A_S7")


cmd.select("6TZK_A_S8", "resi 960-971 & chain A & 6TZK ")
cmd.color ("green", "6TZK_A_S8")


cmd.select("6TZK_A_S9", "resi 978-992 & chain A & 6TZK ")
cmd.color ("cyan", "6TZK_A_S9")


cmd.select("6TZK_A_S10", "resi 996-1011 & chain A & 6TZK ")
cmd.color ("blue", "6TZK_A_S10")


cmd.select("6TZK_A_S11", "resi 1028-1042 & chain A & 6TZK ")
cmd.color ("magenta", "6TZK_A_S11")


cmd.select("6TZK_A_S12", "resi 1047-1066 & chain A & 6TZK ")
cmd.color ("red", "6TZK_A_S12")


cmd.select("6TZK_A_S13", "resi 1084-1106 & chain A & 6TZK ")
cmd.color ("yellow", "6TZK_A_S13")


cmd.select("6TZK_A_S14", "resi 1108-1120 & chain A & 6TZK ")
cmd.color ("green", "6TZK_A_S14")


cmd.select("6TZK_A_S15", "resi 1128-1140 & chain A & 6TZK ")
cmd.color ("cyan", "6TZK_A_S15")


cmd.select("6TZK_barrel", "6TZK_A_S*")
cmd.show("cartoon", "6TZK_barrel")
cmd.zoom("6TZK_barrel")
