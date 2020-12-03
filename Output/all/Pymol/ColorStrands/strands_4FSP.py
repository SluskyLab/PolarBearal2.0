from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4FSP.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("4FSP_A_S0", "resi 8-21 & chain A & 4FSP ")
cmd.color ("red", "4FSP_A_S0")


cmd.select("4FSP_A_S1", "resi 31-47 & chain A & 4FSP ")
cmd.color ("yellow", "4FSP_A_S1")


cmd.select("4FSP_A_S2", "resi 52-65 & chain A & 4FSP ")
cmd.color ("green", "4FSP_A_S2")


cmd.select("4FSP_A_S3", "resi 89-99 & chain A & 4FSP ")
cmd.color ("cyan", "4FSP_A_S3")


cmd.select("4FSP_A_S4", "resi 104-108 & chain A & 4FSP ")
cmd.color ("blue", "4FSP_A_S4")


cmd.select("4FSP_A_S5", "resi 130-136 & chain A & 4FSP ")
cmd.color ("magenta", "4FSP_A_S5")


cmd.select("4FSP_A_S6", "resi 143-150 & chain A & 4FSP ")
cmd.color ("red", "4FSP_A_S6")


cmd.select("4FSP_A_S7", "resi 180-190 & chain A & 4FSP ")
cmd.color ("yellow", "4FSP_A_S7")


cmd.select("4FSP_A_S8", "resi 193-204 & chain A & 4FSP ")
cmd.color ("green", "4FSP_A_S8")


cmd.select("4FSP_A_S9", "resi 206-218 & chain A & 4FSP ")
cmd.color ("cyan", "4FSP_A_S9")


cmd.select("4FSP_A_S10", "resi 224-236 & chain A & 4FSP ")
cmd.color ("blue", "4FSP_A_S10")


cmd.select("4FSP_A_S11", "resi 245-257 & chain A & 4FSP ")
cmd.color ("magenta", "4FSP_A_S11")


cmd.select("4FSP_A_S12", "resi 261-275 & chain A & 4FSP ")
cmd.color ("red", "4FSP_A_S12")


cmd.select("4FSP_A_S13", "resi 299-312 & chain A & 4FSP ")
cmd.color ("yellow", "4FSP_A_S13")


cmd.select("4FSP_A_S14", "resi 317-333 & chain A & 4FSP ")
cmd.color ("green", "4FSP_A_S14")


cmd.select("4FSP_A_S15", "resi 341-352 & chain A & 4FSP ")
cmd.color ("cyan", "4FSP_A_S15")


cmd.select("4FSP_A_S16", "resi 362-373 & chain A & 4FSP ")
cmd.color ("blue", "4FSP_A_S16")


cmd.select("4FSP_A_S17", "resi 378-392 & chain A & 4FSP ")
cmd.color ("magenta", "4FSP_A_S17")


cmd.select("4FSP_barrel", "4FSP_A_S*")
cmd.show("cartoon", "4FSP_barrel")
cmd.zoom("4FSP_barrel")
