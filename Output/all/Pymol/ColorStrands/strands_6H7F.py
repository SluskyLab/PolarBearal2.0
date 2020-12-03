from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/6H7F.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("6H7F_A_S0", "resi 170-178 & chain A & 6H7F ")
cmd.color ("red", "6H7F_A_S0")


cmd.select("6H7F_A_S1", "resi 182-193 & chain A & 6H7F ")
cmd.color ("yellow", "6H7F_A_S1")


cmd.select("6H7F_A_S2", "resi 198-210 & chain A & 6H7F ")
cmd.color ("green", "6H7F_A_S2")


cmd.select("6H7F_A_S3", "resi 217-231 & chain A & 6H7F ")
cmd.color ("cyan", "6H7F_A_S3")


cmd.select("6H7F_A_S4", "resi 236-249 & chain A & 6H7F ")
cmd.color ("blue", "6H7F_A_S4")


cmd.select("6H7F_A_S5", "resi 279-295 & chain A & 6H7F ")
cmd.color ("magenta", "6H7F_A_S5")


cmd.select("6H7F_A_S6", "resi 298-321 & chain A & 6H7F ")
cmd.color ("red", "6H7F_A_S6")


cmd.select("6H7F_A_S7", "resi 330-353 & chain A & 6H7F ")
cmd.color ("yellow", "6H7F_A_S7")


cmd.select("6H7F_A_S8", "resi 359-388 & chain A & 6H7F ")
cmd.color ("green", "6H7F_A_S8")


cmd.select("6H7F_A_S9", "resi 410-428 & chain A & 6H7F ")
cmd.color ("cyan", "6H7F_A_S9")


cmd.select("6H7F_A_S10", "resi 432-447 & chain A & 6H7F ")
cmd.color ("blue", "6H7F_A_S10")


cmd.select("6H7F_A_S11", "resi 458-471 & chain A & 6H7F ")
cmd.color ("magenta", "6H7F_A_S11")


cmd.select("6H7F_A_S12", "resi 474-486 & chain A & 6H7F ")
cmd.color ("red", "6H7F_A_S12")


cmd.select("6H7F_A_S13", "resi 505-517 & chain A & 6H7F ")
cmd.color ("yellow", "6H7F_A_S13")


cmd.select("6H7F_A_S14", "resi 520-538 & chain A & 6H7F ")
cmd.color ("green", "6H7F_A_S14")


cmd.select("6H7F_A_S15", "resi 548-567 & chain A & 6H7F ")
cmd.color ("cyan", "6H7F_A_S15")


cmd.select("6H7F_A_S16", "resi 571-587 & chain A & 6H7F ")
cmd.color ("blue", "6H7F_A_S16")


cmd.select("6H7F_A_S17", "resi 603-614 & chain A & 6H7F ")
cmd.color ("magenta", "6H7F_A_S17")


cmd.select("6H7F_A_S18", "resi 620-635 & chain A & 6H7F ")
cmd.color ("red", "6H7F_A_S18")


cmd.select("6H7F_A_S19", "resi 641-657 & chain A & 6H7F ")
cmd.color ("yellow", "6H7F_A_S19")


cmd.select("6H7F_A_S20", "resi 664-678 & chain A & 6H7F ")
cmd.color ("green", "6H7F_A_S20")


cmd.select("6H7F_A_S21", "resi 688-700 & chain A & 6H7F ")
cmd.color ("cyan", "6H7F_A_S21")


cmd.select("6H7F_barrel", "6H7F_A_S*")
cmd.show("cartoon", "6H7F_barrel")
cmd.zoom("6H7F_barrel")
