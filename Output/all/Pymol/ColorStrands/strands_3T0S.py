from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3T0S.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("3T0S_A_S0", "resi 7-20 & chain A & 3T0S ")
cmd.color ("red", "3T0S_A_S0")


cmd.select("3T0S_A_S1", "resi 31-47 & chain A & 3T0S ")
cmd.color ("yellow", "3T0S_A_S1")


cmd.select("3T0S_A_S2", "resi 52-65 & chain A & 3T0S ")
cmd.color ("green", "3T0S_A_S2")


cmd.select("3T0S_A_S3", "resi 89-100 & chain A & 3T0S ")
cmd.color ("cyan", "3T0S_A_S3")


cmd.select("3T0S_A_S4", "resi 105-109 & chain A & 3T0S ")
cmd.color ("blue", "3T0S_A_S4")


cmd.select("3T0S_A_S5", "resi 131-137 & chain A & 3T0S ")
cmd.color ("magenta", "3T0S_A_S5")


cmd.select("3T0S_A_S6", "resi 144-152 & chain A & 3T0S ")
cmd.color ("red", "3T0S_A_S6")


cmd.select("3T0S_A_S7", "resi 177-187 & chain A & 3T0S ")
cmd.color ("yellow", "3T0S_A_S7")


cmd.select("3T0S_A_S8", "resi 190-201 & chain A & 3T0S ")
cmd.color ("green", "3T0S_A_S8")


cmd.select("3T0S_A_S9", "resi 203-217 & chain A & 3T0S ")
cmd.color ("cyan", "3T0S_A_S9")


cmd.select("3T0S_A_S10", "resi 221-233 & chain A & 3T0S ")
cmd.color ("blue", "3T0S_A_S10")


cmd.select("3T0S_A_S11", "resi 244-255 & chain A & 3T0S ")
cmd.color ("magenta", "3T0S_A_S11")


cmd.select("3T0S_A_S12", "resi 260-272 & chain A & 3T0S ")
cmd.color ("red", "3T0S_A_S12")


cmd.select("3T0S_A_S13", "resi 300-310 & chain A & 3T0S ")
cmd.color ("yellow", "3T0S_A_S13")


cmd.select("3T0S_A_S14", "resi 315-328 & chain A & 3T0S ")
cmd.color ("green", "3T0S_A_S14")


cmd.select("3T0S_A_S15", "resi 340-350 & chain A & 3T0S ")
cmd.color ("cyan", "3T0S_A_S15")


cmd.select("3T0S_A_S16", "resi 361-372 & chain A & 3T0S ")
cmd.color ("blue", "3T0S_A_S16")


cmd.select("3T0S_A_S17", "resi 377-391 & chain A & 3T0S ")
cmd.color ("magenta", "3T0S_A_S17")


cmd.select("3T0S_barrel", "3T0S_A_S*")
cmd.show("cartoon", "3T0S_barrel")
cmd.zoom("3T0S_barrel")
