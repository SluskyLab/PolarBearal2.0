from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/6QWR.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("6QWR_A_S0", "resi 17-27 & chain A & 6QWR ")
cmd.color ("red", "6QWR_A_S0")


cmd.select("6QWR_A_S1", "resi 46-61 & chain A & 6QWR ")
cmd.color ("yellow", "6QWR_A_S1")


cmd.select("6QWR_A_S2", "resi 68-84 & chain A & 6QWR ")
cmd.color ("green", "6QWR_A_S2")


cmd.select("6QWR_A_S3", "resi 94-107 & chain A & 6QWR ")
cmd.color ("cyan", "6QWR_A_S3")


cmd.select("6QWR_A_S4", "resi 118-132 & chain A & 6QWR ")
cmd.color ("blue", "6QWR_A_S4")


cmd.select("6QWR_A_S5", "resi 139-155 & chain A & 6QWR ")
cmd.color ("magenta", "6QWR_A_S5")


cmd.select("6QWR_A_S6", "resi 162-177 & chain A & 6QWR ")
cmd.color ("red", "6QWR_A_S6")


cmd.select("6QWR_A_S7", "resi 187-204 & chain A & 6QWR ")
cmd.color ("yellow", "6QWR_A_S7")


cmd.select("6QWR_barrel", "6QWR_A_S*")
cmd.show("cartoon", "6QWR_barrel")
cmd.zoom("6QWR_barrel")
