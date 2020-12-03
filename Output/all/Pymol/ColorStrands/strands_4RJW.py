from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4RJW.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("4RJW_A_S0", "resi 28-42 & chain A & 4RJW ")
cmd.color ("red", "4RJW_A_S0")


cmd.select("4RJW_A_S1", "resi 53-69 & chain A & 4RJW ")
cmd.color ("yellow", "4RJW_A_S1")


cmd.select("4RJW_A_S2", "resi 73-80 & chain A & 4RJW ")
cmd.color ("green", "4RJW_A_S2")


cmd.select("4RJW_A_S3", "resi 92-100 & chain A & 4RJW ")
cmd.color ("cyan", "4RJW_A_S3")


cmd.select("4RJW_A_S4", "resi 107-112 & chain A & 4RJW ")
cmd.color ("blue", "4RJW_A_S4")


cmd.select("4RJW_A_S5", "resi 150-158 & chain A & 4RJW ")
cmd.color ("magenta", "4RJW_A_S5")


cmd.select("4RJW_A_S6", "resi 161-173 & chain A & 4RJW ")
cmd.color ("red", "4RJW_A_S6")


cmd.select("4RJW_A_S7", "resi 181-191 & chain A & 4RJW ")
cmd.color ("yellow", "4RJW_A_S7")


cmd.select("4RJW_A_S8", "resi 199-216 & chain A & 4RJW ")
cmd.color ("green", "4RJW_A_S8")


cmd.select("4RJW_A_S9", "resi 252-270 & chain A & 4RJW ")
cmd.color ("cyan", "4RJW_A_S9")


cmd.select("4RJW_A_S10", "resi 275-286 & chain A & 4RJW ")
cmd.color ("blue", "4RJW_A_S10")


cmd.select("4RJW_A_S11", "resi 295-308 & chain A & 4RJW ")
cmd.color ("magenta", "4RJW_A_S11")


cmd.select("4RJW_A_S12", "resi 334-347 & chain A & 4RJW ")
cmd.color ("red", "4RJW_A_S12")


cmd.select("4RJW_A_S13", "resi 363-376 & chain A & 4RJW ")
cmd.color ("yellow", "4RJW_A_S13")


cmd.select("4RJW_A_S14", "resi 379-392 & chain A & 4RJW ")
cmd.color ("green", "4RJW_A_S14")


cmd.select("4RJW_A_S15", "resi 401-413 & chain A & 4RJW ")
cmd.color ("cyan", "4RJW_A_S15")


cmd.select("4RJW_barrel", "4RJW_A_S*")
cmd.show("cartoon", "4RJW_barrel")
cmd.zoom("4RJW_barrel")
