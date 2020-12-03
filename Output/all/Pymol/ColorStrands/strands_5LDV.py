from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5LDV.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("5LDV_A_S0", "resi 14-29 & chain A & 5LDV ")
cmd.color ("red", "5LDV_A_S0")


cmd.select("5LDV_A_S1", "resi 41-55 & chain A & 5LDV ")
cmd.color ("yellow", "5LDV_A_S1")


cmd.select("5LDV_A_S2", "resi 60-73 & chain A & 5LDV ")
cmd.color ("green", "5LDV_A_S2")


cmd.select("5LDV_A_S3", "resi 91-99 & chain A & 5LDV ")
cmd.color ("cyan", "5LDV_A_S3")


cmd.select("5LDV_A_S4", "resi 104-110 & chain A & 5LDV ")
cmd.color ("blue", "5LDV_A_S4")


cmd.select("5LDV_A_S5", "resi 127-134 & chain A & 5LDV ")
cmd.color ("magenta", "5LDV_A_S5")


cmd.select("5LDV_A_S6", "resi 139-149 & chain A & 5LDV ")
cmd.color ("red", "5LDV_A_S6")


cmd.select("5LDV_A_S7", "resi 182-193 & chain A & 5LDV ")
cmd.color ("yellow", "5LDV_A_S7")


cmd.select("5LDV_A_S8", "resi 197-210 & chain A & 5LDV ")
cmd.color ("green", "5LDV_A_S8")


cmd.select("5LDV_A_S9", "resi 213-225 & chain A & 5LDV ")
cmd.color ("cyan", "5LDV_A_S9")


cmd.select("5LDV_A_S10", "resi 231-242 & chain A & 5LDV ")
cmd.color ("blue", "5LDV_A_S10")


cmd.select("5LDV_A_S11", "resi 254-266 & chain A & 5LDV ")
cmd.color ("magenta", "5LDV_A_S11")


cmd.select("5LDV_A_S12", "resi 269-285 & chain A & 5LDV ")
cmd.color ("red", "5LDV_A_S12")


cmd.select("5LDV_A_S13", "resi 318-331 & chain A & 5LDV ")
cmd.color ("yellow", "5LDV_A_S13")


cmd.select("5LDV_A_S14", "resi 335-347 & chain A & 5LDV ")
cmd.color ("green", "5LDV_A_S14")


cmd.select("5LDV_A_S15", "resi 357-370 & chain A & 5LDV ")
cmd.color ("cyan", "5LDV_A_S15")


cmd.select("5LDV_A_S16", "resi 373-388 & chain A & 5LDV ")
cmd.color ("blue", "5LDV_A_S16")


cmd.select("5LDV_A_S17", "resi 393-408 & chain A & 5LDV ")
cmd.color ("magenta", "5LDV_A_S17")


cmd.select("5LDV_barrel", "5LDV_A_S*")
cmd.show("cartoon", "5LDV_barrel")
cmd.zoom("5LDV_barrel")
