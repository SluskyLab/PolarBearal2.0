from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4D65.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("4D65_A_S0", "resi 10-22 & chain A & 4D65 ")
cmd.color ("red", "4D65_A_S0")


cmd.select("4D65_A_S1", "resi 32-47 & chain A & 4D65 ")
cmd.color ("yellow", "4D65_A_S1")


cmd.select("4D65_A_S2", "resi 51-61 & chain A & 4D65 ")
cmd.color ("green", "4D65_A_S2")


cmd.select("4D65_A_S3", "resi 73-83 & chain A & 4D65 ")
cmd.color ("cyan", "4D65_A_S3")


cmd.select("4D65_A_S4", "resi 87-96 & chain A & 4D65 ")
cmd.color ("blue", "4D65_A_S4")


cmd.select("4D65_A_S5", "resi 127-135 & chain A & 4D65 ")
cmd.color ("magenta", "4D65_A_S5")


cmd.select("4D65_A_S6", "resi 146-155 & chain A & 4D65 ")
cmd.color ("red", "4D65_A_S6")


cmd.select("4D65_A_S7", "resi 170-180 & chain A & 4D65 ")
cmd.color ("yellow", "4D65_A_S7")


cmd.select("4D65_A_S8", "resi 185-195 & chain A & 4D65 ")
cmd.color ("green", "4D65_A_S8")


cmd.select("4D65_A_S9", "resi 213-223 & chain A & 4D65 ")
cmd.color ("cyan", "4D65_A_S9")


cmd.select("4D65_A_S10", "resi 228-242 & chain A & 4D65 ")
cmd.color ("blue", "4D65_A_S10")


cmd.select("4D65_A_S11", "resi 249-263 & chain A & 4D65 ")
cmd.color ("magenta", "4D65_A_S11")


cmd.select("4D65_A_S12", "resi 270-281 & chain A & 4D65 ")
cmd.color ("red", "4D65_A_S12")


cmd.select("4D65_A_S13", "resi 289-303 & chain A & 4D65 ")
cmd.color ("yellow", "4D65_A_S13")


cmd.select("4D65_A_S14", "resi 306-317 & chain A & 4D65 ")
cmd.color ("green", "4D65_A_S14")


cmd.select("4D65_A_S15", "resi 334-342 & chain A & 4D65 ")
cmd.color ("cyan", "4D65_A_S15")


cmd.select("4D65_barrel", "4D65_A_S*")
cmd.show("cartoon", "4D65_barrel")
cmd.zoom("4D65_barrel")
