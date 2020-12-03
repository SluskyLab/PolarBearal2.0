from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2YNK.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("2YNK_A_S0", "resi 93-100 & chain A & 2YNK ")
cmd.color ("red", "2YNK_A_S0")


cmd.select("2YNK_A_S1", "resi 116-123 & chain A & 2YNK ")
cmd.color ("yellow", "2YNK_A_S1")


cmd.select("2YNK_A_S2", "resi 129-140 & chain A & 2YNK ")
cmd.color ("green", "2YNK_A_S2")


cmd.select("2YNK_A_S3", "resi 149-160 & chain A & 2YNK ")
cmd.color ("cyan", "2YNK_A_S3")


cmd.select("2YNK_A_S4", "resi 165-170 & chain A & 2YNK ")
cmd.color ("blue", "2YNK_A_S4")


cmd.select("2YNK_A_S5", "resi 193-198 & chain A & 2YNK ")
cmd.color ("magenta", "2YNK_A_S5")


cmd.select("2YNK_A_S6", "resi 215-224 & chain A & 2YNK ")
cmd.color ("red", "2YNK_A_S6")


cmd.select("2YNK_A_S7", "resi 235-244 & chain A & 2YNK ")
cmd.color ("yellow", "2YNK_A_S7")


cmd.select("2YNK_A_S8", "resi 250-259 & chain A & 2YNK ")
cmd.color ("green", "2YNK_A_S8")


cmd.select("2YNK_A_S9", "resi 289-300 & chain A & 2YNK ")
cmd.color ("cyan", "2YNK_A_S9")


cmd.select("2YNK_A_S10", "resi 307-317 & chain A & 2YNK ")
cmd.color ("blue", "2YNK_A_S10")


cmd.select("2YNK_A_S11", "resi 328-337 & chain A & 2YNK ")
cmd.color ("magenta", "2YNK_A_S11")


cmd.select("2YNK_A_S12", "resi 343-352 & chain A & 2YNK ")
cmd.color ("red", "2YNK_A_S12")


cmd.select("2YNK_A_S13", "resi 389-398 & chain A & 2YNK ")
cmd.color ("yellow", "2YNK_A_S13")


cmd.select("2YNK_A_S14", "resi 404-414 & chain A & 2YNK ")
cmd.color ("green", "2YNK_A_S14")


cmd.select("2YNK_A_S15", "resi 429-440 & chain A & 2YNK ")
cmd.color ("cyan", "2YNK_A_S15")


cmd.select("2YNK_A_S16", "resi 447-456 & chain A & 2YNK ")
cmd.color ("blue", "2YNK_A_S16")


cmd.select("2YNK_A_S17", "resi 464-472 & chain A & 2YNK ")
cmd.color ("magenta", "2YNK_A_S17")


cmd.select("2YNK_barrel", "2YNK_A_S*")
cmd.show("cartoon", "2YNK_barrel")
cmd.zoom("2YNK_barrel")
