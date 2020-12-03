from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4ZGV.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("4ZGV_A_S0", "resi 212-220 & chain A & 4ZGV ")
cmd.color ("red", "4ZGV_A_S0")


cmd.select("4ZGV_A_S1", "resi 247-260 & chain A & 4ZGV ")
cmd.color ("yellow", "4ZGV_A_S1")


cmd.select("4ZGV_A_S2", "resi 263-281 & chain A & 4ZGV ")
cmd.color ("green", "4ZGV_A_S2")


cmd.select("4ZGV_A_S3", "resi 286-304 & chain A & 4ZGV ")
cmd.color ("cyan", "4ZGV_A_S3")


cmd.select("4ZGV_A_S4", "resi 310-324 & chain A & 4ZGV ")
cmd.color ("blue", "4ZGV_A_S4")


cmd.select("4ZGV_A_S5", "resi 334-348 & chain A & 4ZGV ")
cmd.color ("magenta", "4ZGV_A_S5")


cmd.select("4ZGV_A_S6", "resi 355-382 & chain A & 4ZGV ")
cmd.color ("red", "4ZGV_A_S6")


cmd.select("4ZGV_A_S7", "resi 402-430 & chain A & 4ZGV ")
cmd.color ("yellow", "4ZGV_A_S7")


cmd.select("4ZGV_A_S8", "resi 437-460 & chain A & 4ZGV ")
cmd.color ("green", "4ZGV_A_S8")


cmd.select("4ZGV_A_S9", "resi 495-517 & chain A & 4ZGV ")
cmd.color ("cyan", "4ZGV_A_S9")


cmd.select("4ZGV_A_S10", "resi 521-533 & chain A & 4ZGV ")
cmd.color ("blue", "4ZGV_A_S10")


cmd.select("4ZGV_A_S11", "resi 538-550 & chain A & 4ZGV ")
cmd.color ("magenta", "4ZGV_A_S11")


cmd.select("4ZGV_A_S12", "resi 556-587 & chain A & 4ZGV ")
cmd.color ("red", "4ZGV_A_S12")


cmd.select("4ZGV_A_S13", "resi 596-626 & chain A & 4ZGV ")
cmd.color ("yellow", "4ZGV_A_S13")


cmd.select("4ZGV_A_S14", "resi 632-648 & chain A & 4ZGV ")
cmd.color ("green", "4ZGV_A_S14")


cmd.select("4ZGV_A_S15", "resi 659-675 & chain A & 4ZGV ")
cmd.color ("cyan", "4ZGV_A_S15")


cmd.select("4ZGV_A_S16", "resi 687-702 & chain A & 4ZGV ")
cmd.color ("blue", "4ZGV_A_S16")


cmd.select("4ZGV_A_S17", "resi 737-748 & chain A & 4ZGV ")
cmd.color ("magenta", "4ZGV_A_S17")


cmd.select("4ZGV_A_S18", "resi 752-775 & chain A & 4ZGV ")
cmd.color ("red", "4ZGV_A_S18")


cmd.select("4ZGV_A_S19", "resi 792-816 & chain A & 4ZGV ")
cmd.color ("yellow", "4ZGV_A_S19")


cmd.select("4ZGV_A_S20", "resi 822-843 & chain A & 4ZGV ")
cmd.color ("green", "4ZGV_A_S20")


cmd.select("4ZGV_A_S21", "resi 850-866 & chain A & 4ZGV ")
cmd.color ("cyan", "4ZGV_A_S21")


cmd.select("4ZGV_barrel", "4ZGV_A_S*")
cmd.show("cartoon", "4ZGV_barrel")
cmd.zoom("4ZGV_barrel")
