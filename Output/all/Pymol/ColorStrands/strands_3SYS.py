from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3SYS.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("3SYS_A_S0", "resi 10-23 & chain A & 3SYS ")
cmd.color ("red", "3SYS_A_S0")


cmd.select("3SYS_A_S1", "resi 34-50 & chain A & 3SYS ")
cmd.color ("yellow", "3SYS_A_S1")


cmd.select("3SYS_A_S2", "resi 55-68 & chain A & 3SYS ")
cmd.color ("green", "3SYS_A_S2")


cmd.select("3SYS_A_S3", "resi 92-102 & chain A & 3SYS ")
cmd.color ("cyan", "3SYS_A_S3")


cmd.select("3SYS_A_S4", "resi 105-111 & chain A & 3SYS ")
cmd.color ("blue", "3SYS_A_S4")


cmd.select("3SYS_A_S5", "resi 133-140 & chain A & 3SYS ")
cmd.color ("magenta", "3SYS_A_S5")


cmd.select("3SYS_A_S6", "resi 144-153 & chain A & 3SYS ")
cmd.color ("red", "3SYS_A_S6")


cmd.select("3SYS_A_S7", "resi 178-188 & chain A & 3SYS ")
cmd.color ("yellow", "3SYS_A_S7")


cmd.select("3SYS_A_S8", "resi 192-203 & chain A & 3SYS ")
cmd.color ("green", "3SYS_A_S8")


cmd.select("3SYS_A_S9", "resi 205-217 & chain A & 3SYS ")
cmd.color ("cyan", "3SYS_A_S9")


cmd.select("3SYS_A_S10", "resi 223-235 & chain A & 3SYS ")
cmd.color ("blue", "3SYS_A_S10")


cmd.select("3SYS_A_S11", "resi 244-256 & chain A & 3SYS ")
cmd.color ("magenta", "3SYS_A_S11")


cmd.select("3SYS_A_S12", "resi 261-272 & chain A & 3SYS ")
cmd.color ("red", "3SYS_A_S12")


cmd.select("3SYS_A_S13", "resi 298-311 & chain A & 3SYS ")
cmd.color ("yellow", "3SYS_A_S13")


cmd.select("3SYS_A_S14", "resi 318-332 & chain A & 3SYS ")
cmd.color ("green", "3SYS_A_S14")


cmd.select("3SYS_A_S15", "resi 340-351 & chain A & 3SYS ")
cmd.color ("cyan", "3SYS_A_S15")


cmd.select("3SYS_A_S16", "resi 361-372 & chain A & 3SYS ")
cmd.color ("blue", "3SYS_A_S16")


cmd.select("3SYS_A_S17", "resi 377-390 & chain A & 3SYS ")
cmd.color ("magenta", "3SYS_A_S17")


cmd.select("3SYS_barrel", "3SYS_A_S*")
cmd.show("cartoon", "3SYS_barrel")
cmd.zoom("3SYS_barrel")
