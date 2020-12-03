from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5DL5.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("5DL5_A_S0", "resi 14-27 & chain A & 5DL5 ")
cmd.color ("red", "5DL5_A_S0")


cmd.select("5DL5_A_S1", "resi 35-51 & chain A & 5DL5 ")
cmd.color ("yellow", "5DL5_A_S1")


cmd.select("5DL5_A_S2", "resi 56-74 & chain A & 5DL5 ")
cmd.color ("green", "5DL5_A_S2")


cmd.select("5DL5_A_S3", "resi 92-102 & chain A & 5DL5 ")
cmd.color ("cyan", "5DL5_A_S3")


cmd.select("5DL5_A_S4", "resi 107-111 & chain A & 5DL5 ")
cmd.color ("blue", "5DL5_A_S4")


cmd.select("5DL5_A_S5", "resi 133-139 & chain A & 5DL5 ")
cmd.color ("magenta", "5DL5_A_S5")


cmd.select("5DL5_A_S6", "resi 146-153 & chain A & 5DL5 ")
cmd.color ("red", "5DL5_A_S6")


cmd.select("5DL5_A_S7", "resi 174-184 & chain A & 5DL5 ")
cmd.color ("yellow", "5DL5_A_S7")


cmd.select("5DL5_A_S8", "resi 187-198 & chain A & 5DL5 ")
cmd.color ("green", "5DL5_A_S8")


cmd.select("5DL5_A_S9", "resi 201-214 & chain A & 5DL5 ")
cmd.color ("cyan", "5DL5_A_S9")


cmd.select("5DL5_A_S10", "resi 218-231 & chain A & 5DL5 ")
cmd.color ("blue", "5DL5_A_S10")


cmd.select("5DL5_A_S11", "resi 258-270 & chain A & 5DL5 ")
cmd.color ("magenta", "5DL5_A_S11")


cmd.select("5DL5_A_S12", "resi 275-286 & chain A & 5DL5 ")
cmd.color ("red", "5DL5_A_S12")


cmd.select("5DL5_A_S13", "resi 316-327 & chain A & 5DL5 ")
cmd.color ("yellow", "5DL5_A_S13")


cmd.select("5DL5_A_S14", "resi 335-350 & chain A & 5DL5 ")
cmd.color ("green", "5DL5_A_S14")


cmd.select("5DL5_A_S15", "resi 354-369 & chain A & 5DL5 ")
cmd.color ("cyan", "5DL5_A_S15")


cmd.select("5DL5_A_S16", "resi 379-390 & chain A & 5DL5 ")
cmd.color ("blue", "5DL5_A_S16")


cmd.select("5DL5_A_S17", "resi 401-415 & chain A & 5DL5 ")
cmd.color ("magenta", "5DL5_A_S17")


cmd.select("5DL5_barrel", "5DL5_A_S*")
cmd.show("cartoon", "5DL5_barrel")
cmd.zoom("5DL5_barrel")
