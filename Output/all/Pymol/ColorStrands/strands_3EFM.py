from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3EFM.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("3EFM_A_S0", "resi 162-170 & chain A & 3EFM ")
cmd.color ("red", "3EFM_A_S0")


cmd.select("3EFM_A_S1", "resi 174-186 & chain A & 3EFM ")
cmd.color ("yellow", "3EFM_A_S1")


cmd.select("3EFM_A_S2", "resi 191-202 & chain A & 3EFM ")
cmd.color ("green", "3EFM_A_S2")


cmd.select("3EFM_A_S3", "resi 210-224 & chain A & 3EFM ")
cmd.color ("cyan", "3EFM_A_S3")


cmd.select("3EFM_A_S4", "resi 227-242 & chain A & 3EFM ")
cmd.color ("blue", "3EFM_A_S4")


cmd.select("3EFM_A_S5", "resi 260-275 & chain A & 3EFM ")
cmd.color ("magenta", "3EFM_A_S5")


cmd.select("3EFM_A_S6", "resi 281-296 & chain A & 3EFM ")
cmd.color ("red", "3EFM_A_S6")


cmd.select("3EFM_A_S7", "resi 303-321 & chain A & 3EFM ")
cmd.color ("yellow", "3EFM_A_S7")


cmd.select("3EFM_A_S8", "resi 328-346 & chain A & 3EFM ")
cmd.color ("green", "3EFM_A_S8")


cmd.select("3EFM_A_S9", "resi 367-386 & chain A & 3EFM ")
cmd.color ("cyan", "3EFM_A_S9")


cmd.select("3EFM_A_S10", "resi 390-406 & chain A & 3EFM ")
cmd.color ("blue", "3EFM_A_S10")


cmd.select("3EFM_A_S11", "resi 412-428 & chain A & 3EFM ")
cmd.color ("magenta", "3EFM_A_S11")


cmd.select("3EFM_A_S12", "resi 433-449 & chain A & 3EFM ")
cmd.color ("red", "3EFM_A_S12")


cmd.select("3EFM_A_S13", "resi 457-473 & chain A & 3EFM ")
cmd.color ("yellow", "3EFM_A_S13")


cmd.select("3EFM_A_S14", "resi 477-496 & chain A & 3EFM ")
cmd.color ("green", "3EFM_A_S14")


cmd.select("3EFM_A_S15", "resi 509-528 & chain A & 3EFM ")
cmd.color ("cyan", "3EFM_A_S15")


cmd.select("3EFM_A_S16", "resi 533-546 & chain A & 3EFM ")
cmd.color ("blue", "3EFM_A_S16")


cmd.select("3EFM_A_S17", "resi 552-569 & chain A & 3EFM ")
cmd.color ("magenta", "3EFM_A_S17")


cmd.select("3EFM_A_S18", "resi 576-586 & chain A & 3EFM ")
cmd.color ("red", "3EFM_A_S18")


cmd.select("3EFM_A_S19", "resi 597-608 & chain A & 3EFM ")
cmd.color ("yellow", "3EFM_A_S19")


cmd.select("3EFM_A_S20", "resi 611-620 & chain A & 3EFM ")
cmd.color ("green", "3EFM_A_S20")


cmd.select("3EFM_A_S21", "resi 643-651 & chain A & 3EFM ")
cmd.color ("cyan", "3EFM_A_S21")


cmd.select("3EFM_barrel", "3EFM_A_S*")
cmd.show("cartoon", "3EFM_barrel")
cmd.zoom("3EFM_barrel")
