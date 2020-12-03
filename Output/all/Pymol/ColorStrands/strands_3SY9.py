from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3SY9.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("3SY9_A_S0", "resi 14-27 & chain A & 3SY9 ")
cmd.color ("red", "3SY9_A_S0")


cmd.select("3SY9_A_S1", "resi 36-52 & chain A & 3SY9 ")
cmd.color ("yellow", "3SY9_A_S1")


cmd.select("3SY9_A_S2", "resi 57-68 & chain A & 3SY9 ")
cmd.color ("green", "3SY9_A_S2")


cmd.select("3SY9_A_S3", "resi 101-111 & chain A & 3SY9 ")
cmd.color ("cyan", "3SY9_A_S3")


cmd.select("3SY9_A_S4", "resi 116-120 & chain A & 3SY9 ")
cmd.color ("blue", "3SY9_A_S4")


cmd.select("3SY9_A_S5", "resi 142-148 & chain A & 3SY9 ")
cmd.color ("magenta", "3SY9_A_S5")


cmd.select("3SY9_A_S6", "resi 155-162 & chain A & 3SY9 ")
cmd.color ("red", "3SY9_A_S6")


cmd.select("3SY9_A_S7", "resi 189-198 & chain A & 3SY9 ")
cmd.color ("yellow", "3SY9_A_S7")


cmd.select("3SY9_A_S8", "resi 203-214 & chain A & 3SY9 ")
cmd.color ("green", "3SY9_A_S8")


cmd.select("3SY9_A_S9", "resi 216-230 & chain A & 3SY9 ")
cmd.color ("cyan", "3SY9_A_S9")


cmd.select("3SY9_A_S10", "resi 234-247 & chain A & 3SY9 ")
cmd.color ("blue", "3SY9_A_S10")


cmd.select("3SY9_A_S11", "resi 256-268 & chain A & 3SY9 ")
cmd.color ("magenta", "3SY9_A_S11")


cmd.select("3SY9_A_S12", "resi 271-283 & chain A & 3SY9 ")
cmd.color ("red", "3SY9_A_S12")


cmd.select("3SY9_A_S13", "resi 311-323 & chain A & 3SY9 ")
cmd.color ("yellow", "3SY9_A_S13")


cmd.select("3SY9_A_S14", "resi 328-342 & chain A & 3SY9 ")
cmd.color ("green", "3SY9_A_S14")


cmd.select("3SY9_A_S15", "resi 365-376 & chain A & 3SY9 ")
cmd.color ("cyan", "3SY9_A_S15")


cmd.select("3SY9_A_S16", "resi 387-398 & chain A & 3SY9 ")
cmd.color ("blue", "3SY9_A_S16")


cmd.select("3SY9_A_S17", "resi 405-421 & chain A & 3SY9 ")
cmd.color ("magenta", "3SY9_A_S17")


cmd.select("3SY9_barrel", "3SY9_A_S*")
cmd.show("cartoon", "3SY9_barrel")
cmd.zoom("3SY9_barrel")
