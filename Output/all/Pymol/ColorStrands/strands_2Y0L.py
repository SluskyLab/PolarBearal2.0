from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2Y0L.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("2Y0L_A_S0", "resi 19-32 & chain A & 2Y0L ")
cmd.color ("red", "2Y0L_A_S0")


cmd.select("2Y0L_A_S1", "resi 42-58 & chain A & 2Y0L ")
cmd.color ("yellow", "2Y0L_A_S1")


cmd.select("2Y0L_A_S2", "resi 63-76 & chain A & 2Y0L ")
cmd.color ("green", "2Y0L_A_S2")


cmd.select("2Y0L_A_S3", "resi 98-110 & chain A & 2Y0L ")
cmd.color ("cyan", "2Y0L_A_S3")


cmd.select("2Y0L_A_S4", "resi 115-119 & chain A & 2Y0L ")
cmd.color ("blue", "2Y0L_A_S4")


cmd.select("2Y0L_A_S5", "resi 141-147 & chain A & 2Y0L ")
cmd.color ("magenta", "2Y0L_A_S5")


cmd.select("2Y0L_A_S6", "resi 154-162 & chain A & 2Y0L ")
cmd.color ("red", "2Y0L_A_S6")


cmd.select("2Y0L_A_S7", "resi 190-200 & chain A & 2Y0L ")
cmd.color ("yellow", "2Y0L_A_S7")


cmd.select("2Y0L_A_S8", "resi 203-214 & chain A & 2Y0L ")
cmd.color ("green", "2Y0L_A_S8")


cmd.select("2Y0L_A_S9", "resi 216-228 & chain A & 2Y0L ")
cmd.color ("cyan", "2Y0L_A_S9")


cmd.select("2Y0L_A_S10", "resi 234-246 & chain A & 2Y0L ")
cmd.color ("blue", "2Y0L_A_S10")


cmd.select("2Y0L_A_S11", "resi 255-267 & chain A & 2Y0L ")
cmd.color ("magenta", "2Y0L_A_S11")


cmd.select("2Y0L_A_S12", "resi 270-284 & chain A & 2Y0L ")
cmd.color ("red", "2Y0L_A_S12")


cmd.select("2Y0L_A_S13", "resi 310-321 & chain A & 2Y0L ")
cmd.color ("yellow", "2Y0L_A_S13")


cmd.select("2Y0L_A_S14", "resi 326-343 & chain A & 2Y0L ")
cmd.color ("green", "2Y0L_A_S14")


cmd.select("2Y0L_A_S15", "resi 348-362 & chain A & 2Y0L ")
cmd.color ("cyan", "2Y0L_A_S15")


cmd.select("2Y0L_A_S16", "resi 372-383 & chain A & 2Y0L ")
cmd.color ("blue", "2Y0L_A_S16")


cmd.select("2Y0L_A_S17", "resi 388-402 & chain A & 2Y0L ")
cmd.color ("magenta", "2Y0L_A_S17")


cmd.select("2Y0L_barrel", "2Y0L_A_S*")
cmd.show("cartoon", "2Y0L_barrel")
cmd.zoom("2Y0L_barrel")
