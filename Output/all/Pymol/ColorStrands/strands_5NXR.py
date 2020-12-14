from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5NXR.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("5NXR_A_S0", "resi 10-22 & chain A & 5NXR ")
cmd.color ("red", "5NXR_A_S0")


cmd.select("5NXR_A_S1", "resi 35-50 & chain A & 5NXR ")
cmd.color ("yellow", "5NXR_A_S1")


cmd.select("5NXR_A_S2", "resi 54-64 & chain A & 5NXR ")
cmd.color ("green", "5NXR_A_S2")


cmd.select("5NXR_A_S3", "resi 76-86 & chain A & 5NXR ")
cmd.color ("cyan", "5NXR_A_S3")


cmd.select("5NXR_A_S4", "resi 90-99 & chain A & 5NXR ")
cmd.color ("blue", "5NXR_A_S4")


cmd.select("5NXR_A_S5", "resi 130-138 & chain A & 5NXR ")
cmd.color ("magenta", "5NXR_A_S5")


cmd.select("5NXR_A_S6", "resi 149-158 & chain A & 5NXR ")
cmd.color ("red", "5NXR_A_S6")


cmd.select("5NXR_A_S7", "resi 172-184 & chain A & 5NXR ")
cmd.color ("yellow", "5NXR_A_S7")


cmd.select("5NXR_A_S8", "resi 187-206 & chain A & 5NXR ")
cmd.color ("green", "5NXR_A_S8")


cmd.select("5NXR_A_S9", "resi 215-233 & chain A & 5NXR ")
cmd.color ("cyan", "5NXR_A_S9")


cmd.select("5NXR_A_S10", "resi 236-252 & chain A & 5NXR ")
cmd.color ("blue", "5NXR_A_S10")


cmd.select("5NXR_A_S11", "resi 257-272 & chain A & 5NXR ")
cmd.color ("magenta", "5NXR_A_S11")


cmd.select("5NXR_A_S12", "resi 278-289 & chain A & 5NXR ")
cmd.color ("red", "5NXR_A_S12")


cmd.select("5NXR_A_S13", "resi 298-312 & chain A & 5NXR ")
cmd.color ("yellow", "5NXR_A_S13")


cmd.select("5NXR_A_S14", "resi 315-326 & chain A & 5NXR ")
cmd.color ("green", "5NXR_A_S14")


cmd.select("5NXR_A_S15", "resi 343-351 & chain A & 5NXR ")
cmd.color ("cyan", "5NXR_A_S15")


cmd.select("5NXR_barrel", "5NXR_A_S*")
cmd.show("cartoon", "5NXR_barrel")
cmd.zoom("5NXR_barrel")
