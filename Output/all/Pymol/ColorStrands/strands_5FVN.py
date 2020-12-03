from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5FVN.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("5FVN_A_S0", "resi 10-22 & chain A & 5FVN ")
cmd.color ("red", "5FVN_A_S0")


cmd.select("5FVN_A_S1", "resi 31-46 & chain A & 5FVN ")
cmd.color ("yellow", "5FVN_A_S1")


cmd.select("5FVN_A_S2", "resi 50-61 & chain A & 5FVN ")
cmd.color ("green", "5FVN_A_S2")


cmd.select("5FVN_A_S3", "resi 70-82 & chain A & 5FVN ")
cmd.color ("cyan", "5FVN_A_S3")


cmd.select("5FVN_A_S4", "resi 86-92 & chain A & 5FVN ")
cmd.color ("blue", "5FVN_A_S4")


cmd.select("5FVN_A_S5", "resi 125-135 & chain A & 5FVN ")
cmd.color ("magenta", "5FVN_A_S5")


cmd.select("5FVN_A_S6", "resi 140-155 & chain A & 5FVN ")
cmd.color ("red", "5FVN_A_S6")


cmd.select("5FVN_A_S7", "resi 166-182 & chain A & 5FVN ")
cmd.color ("yellow", "5FVN_A_S7")


cmd.select("5FVN_A_S8", "resi 187-197 & chain A & 5FVN ")
cmd.color ("green", "5FVN_A_S8")


cmd.select("5FVN_A_S9", "resi 214-224 & chain A & 5FVN ")
cmd.color ("cyan", "5FVN_A_S9")


cmd.select("5FVN_A_S10", "resi 227-243 & chain A & 5FVN ")
cmd.color ("blue", "5FVN_A_S10")


cmd.select("5FVN_A_S11", "resi 247-262 & chain A & 5FVN ")
cmd.color ("magenta", "5FVN_A_S11")


cmd.select("5FVN_A_S12", "resi 268-279 & chain A & 5FVN ")
cmd.color ("red", "5FVN_A_S12")


cmd.select("5FVN_A_S13", "resi 288-302 & chain A & 5FVN ")
cmd.color ("yellow", "5FVN_A_S13")


cmd.select("5FVN_A_S14", "resi 305-316 & chain A & 5FVN ")
cmd.color ("green", "5FVN_A_S14")


cmd.select("5FVN_A_S15", "resi 333-341 & chain A & 5FVN ")
cmd.color ("cyan", "5FVN_A_S15")


cmd.select("5FVN_barrel", "5FVN_A_S*")
cmd.show("cartoon", "5FVN_barrel")
cmd.zoom("5FVN_barrel")
