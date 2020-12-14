from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3PPT.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("3PPT_A_S0", "resi 12-15 & chain A & 3PPT ")
cmd.color ("red", "3PPT_A_S0")


cmd.select("3PPT_A_S1", "resi 40-43 & chain A & 3PPT ")
cmd.color ("yellow", "3PPT_A_S1")


cmd.select("3PPT_A_S2", "resi 51-55 & chain A & 3PPT ")
cmd.color ("green", "3PPT_A_S2")


cmd.select("3PPT_A_S3", "resi 61-71 & chain A & 3PPT ")
cmd.color ("cyan", "3PPT_A_S3")


cmd.select("3PPT_A_S4", "resi 82-85 & chain A & 3PPT ")
cmd.color ("blue", "3PPT_A_S4")


cmd.select("3PPT_A_S5", "resi 92-97 & chain A & 3PPT ")
cmd.color ("magenta", "3PPT_A_S5")


cmd.select("3PPT_A_S6", "resi 102-107 & chain A & 3PPT ")
cmd.color ("red", "3PPT_A_S6")


cmd.select("3PPT_A_S7", "resi 113-118 & chain A & 3PPT ")
cmd.color ("yellow", "3PPT_A_S7")


cmd.select("3PPT_A_S8", "resi 124-129 & chain A & 3PPT ")
cmd.color ("green", "3PPT_A_S8")


cmd.select("3PPT_barrel", "3PPT_A_S*")
cmd.show("cartoon", "3PPT_barrel")
cmd.zoom("3PPT_barrel")
