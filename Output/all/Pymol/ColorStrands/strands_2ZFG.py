from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2ZFG.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("2ZFG_A_S0", "resi 10-22 & chain A & 2ZFG ")
cmd.color ("red", "2ZFG_A_S0")


cmd.select("2ZFG_A_S1", "resi 36-51 & chain A & 2ZFG ")
cmd.color ("yellow", "2ZFG_A_S1")


cmd.select("2ZFG_A_S2", "resi 55-65 & chain A & 2ZFG ")
cmd.color ("green", "2ZFG_A_S2")


cmd.select("2ZFG_A_S3", "resi 80-90 & chain A & 2ZFG ")
cmd.color ("cyan", "2ZFG_A_S3")


cmd.select("2ZFG_A_S4", "resi 94-103 & chain A & 2ZFG ")
cmd.color ("blue", "2ZFG_A_S4")


cmd.select("2ZFG_A_S5", "resi 133-143 & chain A & 2ZFG ")
cmd.color ("magenta", "2ZFG_A_S5")


cmd.select("2ZFG_A_S6", "resi 148-161 & chain A & 2ZFG ")
cmd.color ("red", "2ZFG_A_S6")


cmd.select("2ZFG_A_S7", "resi 170-181 & chain A & 2ZFG ")
cmd.color ("yellow", "2ZFG_A_S7")


cmd.select("2ZFG_A_S8", "resi 184-196 & chain A & 2ZFG ")
cmd.color ("green", "2ZFG_A_S8")


cmd.select("2ZFG_A_S9", "resi 209-221 & chain A & 2ZFG ")
cmd.color ("cyan", "2ZFG_A_S9")


cmd.select("2ZFG_A_S10", "resi 224-242 & chain A & 2ZFG ")
cmd.color ("blue", "2ZFG_A_S10")


cmd.select("2ZFG_A_S11", "resi 247-264 & chain A & 2ZFG ")
cmd.color ("magenta", "2ZFG_A_S11")


cmd.select("2ZFG_A_S12", "resi 270-281 & chain A & 2ZFG ")
cmd.color ("red", "2ZFG_A_S12")


cmd.select("2ZFG_A_S13", "resi 289-303 & chain A & 2ZFG ")
cmd.color ("yellow", "2ZFG_A_S13")


cmd.select("2ZFG_A_S14", "resi 306-317 & chain A & 2ZFG ")
cmd.color ("green", "2ZFG_A_S14")


cmd.select("2ZFG_A_S15", "resi 331-339 & chain A & 2ZFG ")
cmd.color ("cyan", "2ZFG_A_S15")


cmd.select("2ZFG_barrel", "2ZFG_A_S*")
cmd.show("cartoon", "2ZFG_barrel")
cmd.zoom("2ZFG_barrel")
