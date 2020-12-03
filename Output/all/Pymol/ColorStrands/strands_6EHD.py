from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/6EHD.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("6EHD_A_S0", "resi 10-22 & chain A & 6EHD ")
cmd.color ("red", "6EHD_A_S0")


cmd.select("6EHD_A_S1", "resi 30-46 & chain A & 6EHD ")
cmd.color ("yellow", "6EHD_A_S1")


cmd.select("6EHD_A_S2", "resi 50-59 & chain A & 6EHD ")
cmd.color ("green", "6EHD_A_S2")


cmd.select("6EHD_A_S3", "resi 67-76 & chain A & 6EHD ")
cmd.color ("cyan", "6EHD_A_S3")


cmd.select("6EHD_A_S4", "resi 81-86 & chain A & 6EHD ")
cmd.color ("blue", "6EHD_A_S4")


cmd.select("6EHD_A_S5", "resi 120-126 & chain A & 6EHD ")
cmd.color ("magenta", "6EHD_A_S5")


cmd.select("6EHD_A_S6", "resi 132-139 & chain A & 6EHD ")
cmd.color ("red", "6EHD_A_S6")


cmd.select("6EHD_A_S7", "resi 147-155 & chain A & 6EHD ")
cmd.color ("yellow", "6EHD_A_S7")


cmd.select("6EHD_A_S8", "resi 161-179 & chain A & 6EHD ")
cmd.color ("green", "6EHD_A_S8")


cmd.select("6EHD_A_S9", "resi 186-203 & chain A & 6EHD ")
cmd.color ("cyan", "6EHD_A_S9")


cmd.select("6EHD_A_S10", "resi 209-221 & chain A & 6EHD ")
cmd.color ("blue", "6EHD_A_S10")


cmd.select("6EHD_A_S11", "resi 226-241 & chain A & 6EHD ")
cmd.color ("magenta", "6EHD_A_S11")


cmd.select("6EHD_A_S12", "resi 244-259 & chain A & 6EHD ")
cmd.color ("red", "6EHD_A_S12")


cmd.select("6EHD_A_S13", "resi 264-277 & chain A & 6EHD ")
cmd.color ("yellow", "6EHD_A_S13")


cmd.select("6EHD_A_S14", "resi 280-292 & chain A & 6EHD ")
cmd.color ("green", "6EHD_A_S14")


cmd.select("6EHD_A_S15", "resi 311-324 & chain A & 6EHD ")
cmd.color ("cyan", "6EHD_A_S15")


cmd.select("6EHD_barrel", "6EHD_A_S*")
cmd.show("cartoon", "6EHD_barrel")
cmd.zoom("6EHD_barrel")
