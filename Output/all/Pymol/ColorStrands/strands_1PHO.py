from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1PHO.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("1PHO_A_S0", "resi 12-23 & chain A & 1PHO ")
cmd.color ("red", "1PHO_A_S0")


cmd.select("1PHO_A_S1", "resi 36-51 & chain A & 1PHO ")
cmd.color ("yellow", "1PHO_A_S1")


cmd.select("1PHO_A_S2", "resi 55-65 & chain A & 1PHO ")
cmd.color ("green", "1PHO_A_S2")


cmd.select("1PHO_A_S3", "resi 80-89 & chain A & 1PHO ")
cmd.color ("cyan", "1PHO_A_S3")


cmd.select("1PHO_A_S4", "resi 95-103 & chain A & 1PHO ")
cmd.color ("blue", "1PHO_A_S4")


cmd.select("1PHO_A_S5", "resi 133-141 & chain A & 1PHO ")
cmd.color ("magenta", "1PHO_A_S5")


cmd.select("1PHO_A_S6", "resi 150-161 & chain A & 1PHO ")
cmd.color ("red", "1PHO_A_S6")


cmd.select("1PHO_A_S7", "resi 170-181 & chain A & 1PHO ")
cmd.color ("yellow", "1PHO_A_S7")


cmd.select("1PHO_A_S8", "resi 186-194 & chain A & 1PHO ")
cmd.color ("green", "1PHO_A_S8")


cmd.select("1PHO_A_S9", "resi 211-220 & chain A & 1PHO ")
cmd.color ("cyan", "1PHO_A_S9")


cmd.select("1PHO_A_S10", "resi 224-235 & chain A & 1PHO ")
cmd.color ("blue", "1PHO_A_S10")


cmd.select("1PHO_A_S11", "resi 253-264 & chain A & 1PHO ")
cmd.color ("magenta", "1PHO_A_S11")


cmd.select("1PHO_A_S12", "resi 270-281 & chain A & 1PHO ")
cmd.color ("red", "1PHO_A_S12")


cmd.select("1PHO_A_S13", "resi 291-301 & chain A & 1PHO ")
cmd.color ("yellow", "1PHO_A_S13")


cmd.select("1PHO_A_S14", "resi 306-317 & chain A & 1PHO ")
cmd.color ("green", "1PHO_A_S14")


cmd.select("1PHO_A_S15", "resi 331-340 & chain A & 1PHO ")
cmd.color ("cyan", "1PHO_A_S15")


cmd.select("1PHO_barrel", "1PHO_A_S*")
cmd.show("cartoon", "1PHO_barrel")
cmd.zoom("1PHO_barrel")
