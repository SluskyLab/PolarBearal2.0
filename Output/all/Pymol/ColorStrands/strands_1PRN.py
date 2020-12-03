from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1PRN.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("1PRN_A_S0", "resi 3-15 & chain A & 1PRN ")
cmd.color ("red", "1PRN_A_S0")


cmd.select("1PRN_A_S1", "resi 24-39 & chain A & 1PRN ")
cmd.color ("yellow", "1PRN_A_S1")


cmd.select("1PRN_A_S2", "resi 46-57 & chain A & 1PRN ")
cmd.color ("green", "1PRN_A_S2")


cmd.select("1PRN_A_S3", "resi 67-74 & chain A & 1PRN ")
cmd.color ("cyan", "1PRN_A_S3")


cmd.select("1PRN_A_S4", "resi 77-83 & chain A & 1PRN ")
cmd.color ("blue", "1PRN_A_S4")


cmd.select("1PRN_A_S5", "resi 131-138 & chain A & 1PRN ")
cmd.color ("magenta", "1PRN_A_S5")


cmd.select("1PRN_A_S6", "resi 141-150 & chain A & 1PRN ")
cmd.color ("red", "1PRN_A_S6")


cmd.select("1PRN_A_S7", "resi 163-171 & chain A & 1PRN ")
cmd.color ("yellow", "1PRN_A_S7")


cmd.select("1PRN_A_S8", "resi 176-183 & chain A & 1PRN ")
cmd.color ("green", "1PRN_A_S8")


cmd.select("1PRN_A_S9", "resi 193-200 & chain A & 1PRN ")
cmd.color ("cyan", "1PRN_A_S9")


cmd.select("1PRN_A_S10", "resi 205-214 & chain A & 1PRN ")
cmd.color ("blue", "1PRN_A_S10")


cmd.select("1PRN_A_S11", "resi 223-231 & chain A & 1PRN ")
cmd.color ("magenta", "1PRN_A_S11")


cmd.select("1PRN_A_S12", "resi 236-243 & chain A & 1PRN ")
cmd.color ("red", "1PRN_A_S12")


cmd.select("1PRN_A_S13", "resi 252-261 & chain A & 1PRN ")
cmd.color ("yellow", "1PRN_A_S13")


cmd.select("1PRN_A_S14", "resi 265-273 & chain A & 1PRN ")
cmd.color ("green", "1PRN_A_S14")


cmd.select("1PRN_A_S15", "resi 280-289 & chain A & 1PRN ")
cmd.color ("cyan", "1PRN_A_S15")


cmd.select("1PRN_barrel", "1PRN_A_S*")
cmd.show("cartoon", "1PRN_barrel")
cmd.zoom("1PRN_barrel")
