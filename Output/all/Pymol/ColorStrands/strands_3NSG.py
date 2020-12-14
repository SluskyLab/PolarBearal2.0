from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3NSG.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("3NSG_A_S0", "resi 14-23 & chain A & 3NSG ")
cmd.color ("red", "3NSG_A_S0")


cmd.select("3NSG_A_S1", "resi 32-45 & chain A & 3NSG ")
cmd.color ("yellow", "3NSG_A_S1")


cmd.select("3NSG_A_S2", "resi 52-61 & chain A & 3NSG ")
cmd.color ("green", "3NSG_A_S2")


cmd.select("3NSG_A_S3", "resi 75-84 & chain A & 3NSG ")
cmd.color ("cyan", "3NSG_A_S3")


cmd.select("3NSG_A_S4", "resi 90-98 & chain A & 3NSG ")
cmd.color ("blue", "3NSG_A_S4")


cmd.select("3NSG_A_S5", "resi 131-139 & chain A & 3NSG ")
cmd.color ("magenta", "3NSG_A_S5")


cmd.select("3NSG_A_S6", "resi 148-159 & chain A & 3NSG ")
cmd.color ("red", "3NSG_A_S6")


cmd.select("3NSG_A_S7", "resi 169-180 & chain A & 3NSG ")
cmd.color ("yellow", "3NSG_A_S7")


cmd.select("3NSG_A_S8", "resi 183-193 & chain A & 3NSG ")
cmd.color ("green", "3NSG_A_S8")


cmd.select("3NSG_A_S9", "resi 209-219 & chain A & 3NSG ")
cmd.color ("cyan", "3NSG_A_S9")


cmd.select("3NSG_A_S10", "resi 222-238 & chain A & 3NSG ")
cmd.color ("blue", "3NSG_A_S10")


cmd.select("3NSG_A_S11", "resi 247-262 & chain A & 3NSG ")
cmd.color ("magenta", "3NSG_A_S11")


cmd.select("3NSG_A_S12", "resi 266-279 & chain A & 3NSG ")
cmd.color ("red", "3NSG_A_S12")


cmd.select("3NSG_A_S13", "resi 288-301 & chain A & 3NSG ")
cmd.color ("yellow", "3NSG_A_S13")


cmd.select("3NSG_A_S14", "resi 305-317 & chain A & 3NSG ")
cmd.color ("green", "3NSG_A_S14")


cmd.select("3NSG_A_S15", "resi 332-341 & chain A & 3NSG ")
cmd.color ("cyan", "3NSG_A_S15")


cmd.select("3NSG_barrel", "3NSG_A_S*")
cmd.show("cartoon", "3NSG_barrel")
cmd.zoom("3NSG_barrel")
