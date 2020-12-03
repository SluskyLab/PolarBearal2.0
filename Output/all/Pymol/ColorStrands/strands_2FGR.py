from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2FGR.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("2FGR_A_S0", "resi 3-20 & chain A & 2FGR ")
cmd.color ("red", "2FGR_A_S0")


cmd.select("2FGR_A_S1", "resi 24-45 & chain A & 2FGR ")
cmd.color ("yellow", "2FGR_A_S1")


cmd.select("2FGR_A_S2", "resi 52-62 & chain A & 2FGR ")
cmd.color ("green", "2FGR_A_S2")


cmd.select("2FGR_A_S3", "resi 67-82 & chain A & 2FGR ")
cmd.color ("cyan", "2FGR_A_S3")


cmd.select("2FGR_A_S4", "resi 87-92 & chain A & 2FGR ")
cmd.color ("blue", "2FGR_A_S4")


cmd.select("2FGR_A_S5", "resi 134-142 & chain A & 2FGR ")
cmd.color ("magenta", "2FGR_A_S5")


cmd.select("2FGR_A_S6", "resi 147-155 & chain A & 2FGR ")
cmd.color ("red", "2FGR_A_S6")


cmd.select("2FGR_A_S7", "resi 171-179 & chain A & 2FGR ")
cmd.color ("yellow", "2FGR_A_S7")


cmd.select("2FGR_A_S8", "resi 184-194 & chain A & 2FGR ")
cmd.color ("green", "2FGR_A_S8")


cmd.select("2FGR_A_S9", "resi 201-212 & chain A & 2FGR ")
cmd.color ("cyan", "2FGR_A_S9")


cmd.select("2FGR_A_S10", "resi 218-229 & chain A & 2FGR ")
cmd.color ("blue", "2FGR_A_S10")


cmd.select("2FGR_A_S11", "resi 236-249 & chain A & 2FGR ")
cmd.color ("magenta", "2FGR_A_S11")


cmd.select("2FGR_A_S12", "resi 253-265 & chain A & 2FGR ")
cmd.color ("red", "2FGR_A_S12")


cmd.select("2FGR_A_S13", "resi 269-282 & chain A & 2FGR ")
cmd.color ("yellow", "2FGR_A_S13")


cmd.select("2FGR_A_S14", "resi 286-298 & chain A & 2FGR ")
cmd.color ("green", "2FGR_A_S14")


cmd.select("2FGR_A_S15", "resi 315-332 & chain A & 2FGR ")
cmd.color ("cyan", "2FGR_A_S15")


cmd.select("2FGR_barrel", "2FGR_A_S*")
cmd.show("cartoon", "2FGR_barrel")
cmd.zoom("2FGR_barrel")
