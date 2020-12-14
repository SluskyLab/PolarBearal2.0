from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4FRX.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("4FRX_A_S0", "resi 8-21 & chain A & 4FRX ")
cmd.color ("red", "4FRX_A_S0")


cmd.select("4FRX_A_S1", "resi 32-48 & chain A & 4FRX ")
cmd.color ("yellow", "4FRX_A_S1")


cmd.select("4FRX_A_S2", "resi 53-66 & chain A & 4FRX ")
cmd.color ("green", "4FRX_A_S2")


cmd.select("4FRX_A_S3", "resi 97-107 & chain A & 4FRX ")
cmd.color ("cyan", "4FRX_A_S3")


cmd.select("4FRX_A_S4", "resi 112-116 & chain A & 4FRX ")
cmd.color ("blue", "4FRX_A_S4")


cmd.select("4FRX_A_S5", "resi 138-144 & chain A & 4FRX ")
cmd.color ("magenta", "4FRX_A_S5")


cmd.select("4FRX_A_S6", "resi 151-158 & chain A & 4FRX ")
cmd.color ("red", "4FRX_A_S6")


cmd.select("4FRX_A_S7", "resi 188-198 & chain A & 4FRX ")
cmd.color ("yellow", "4FRX_A_S7")


cmd.select("4FRX_A_S8", "resi 201-212 & chain A & 4FRX ")
cmd.color ("green", "4FRX_A_S8")


cmd.select("4FRX_A_S9", "resi 214-226 & chain A & 4FRX ")
cmd.color ("cyan", "4FRX_A_S9")


cmd.select("4FRX_A_S10", "resi 232-243 & chain A & 4FRX ")
cmd.color ("blue", "4FRX_A_S10")


cmd.select("4FRX_A_S11", "resi 274-285 & chain A & 4FRX ")
cmd.color ("magenta", "4FRX_A_S11")


cmd.select("4FRX_A_S12", "resi 290-302 & chain A & 4FRX ")
cmd.color ("red", "4FRX_A_S12")


cmd.select("4FRX_A_S13", "resi 333-344 & chain A & 4FRX ")
cmd.color ("yellow", "4FRX_A_S13")


cmd.select("4FRX_A_S14", "resi 349-364 & chain A & 4FRX ")
cmd.color ("green", "4FRX_A_S14")


cmd.select("4FRX_A_S15", "resi 371-383 & chain A & 4FRX ")
cmd.color ("cyan", "4FRX_A_S15")


cmd.select("4FRX_A_S16", "resi 393-402 & chain A & 4FRX ")
cmd.color ("blue", "4FRX_A_S16")


cmd.select("4FRX_A_S17", "resi 417-428 & chain A & 4FRX ")
cmd.color ("magenta", "4FRX_A_S17")


cmd.select("4FRX_barrel", "4FRX_A_S*")
cmd.show("cartoon", "4FRX_barrel")
cmd.zoom("4FRX_barrel")
