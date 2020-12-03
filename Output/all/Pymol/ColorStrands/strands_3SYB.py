from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3SYB.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("3SYB_A_S0", "resi 43-56 & chain A & 3SYB ")
cmd.color ("red", "3SYB_A_S0")


cmd.select("3SYB_A_S1", "resi 80-94 & chain A & 3SYB ")
cmd.color ("yellow", "3SYB_A_S1")


cmd.select("3SYB_A_S2", "resi 99-110 & chain A & 3SYB ")
cmd.color ("green", "3SYB_A_S2")


cmd.select("3SYB_A_S3", "resi 138-149 & chain A & 3SYB ")
cmd.color ("cyan", "3SYB_A_S3")


cmd.select("3SYB_A_S4", "resi 152-158 & chain A & 3SYB ")
cmd.color ("blue", "3SYB_A_S4")


cmd.select("3SYB_A_S5", "resi 180-187 & chain A & 3SYB ")
cmd.color ("magenta", "3SYB_A_S5")


cmd.select("3SYB_A_S6", "resi 191-200 & chain A & 3SYB ")
cmd.color ("red", "3SYB_A_S6")


cmd.select("3SYB_A_S7", "resi 226-235 & chain A & 3SYB ")
cmd.color ("yellow", "3SYB_A_S7")


cmd.select("3SYB_A_S8", "resi 239-250 & chain A & 3SYB ")
cmd.color ("green", "3SYB_A_S8")


cmd.select("3SYB_A_S9", "resi 253-264 & chain A & 3SYB ")
cmd.color ("cyan", "3SYB_A_S9")


cmd.select("3SYB_A_S10", "resi 272-284 & chain A & 3SYB ")
cmd.color ("blue", "3SYB_A_S10")


cmd.select("3SYB_A_S11", "resi 293-305 & chain A & 3SYB ")
cmd.color ("magenta", "3SYB_A_S11")


cmd.select("3SYB_A_S12", "resi 308-320 & chain A & 3SYB ")
cmd.color ("red", "3SYB_A_S12")


cmd.select("3SYB_A_S13", "resi 346-359 & chain A & 3SYB ")
cmd.color ("yellow", "3SYB_A_S13")


cmd.select("3SYB_A_S14", "resi 364-381 & chain A & 3SYB ")
cmd.color ("green", "3SYB_A_S14")


cmd.select("3SYB_A_S15", "resi 401-415 & chain A & 3SYB ")
cmd.color ("cyan", "3SYB_A_S15")


cmd.select("3SYB_A_S16", "resi 426-437 & chain A & 3SYB ")
cmd.color ("blue", "3SYB_A_S16")


cmd.select("3SYB_A_S17", "resi 445-458 & chain A & 3SYB ")
cmd.color ("magenta", "3SYB_A_S17")


cmd.select("3SYB_barrel", "3SYB_A_S*")
cmd.show("cartoon", "3SYB_barrel")
cmd.zoom("3SYB_barrel")
