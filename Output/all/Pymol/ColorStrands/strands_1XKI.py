from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1XKI.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("1XKI_A_S0", "resi 15-24 & chain A & 1XKI ")
cmd.color ("red", "1XKI_A_S0")


cmd.select("1XKI_A_S1", "resi 39-44 & chain A & 1XKI ")
cmd.color ("yellow", "1XKI_A_S1")


cmd.select("1XKI_A_S2", "resi 48-55 & chain A & 1XKI ")
cmd.color ("green", "1XKI_A_S2")


cmd.select("1XKI_A_S3", "resi 62-71 & chain A & 1XKI ")
cmd.color ("cyan", "1XKI_A_S3")


cmd.select("1XKI_A_S4", "resi 75-79 & chain A & 1XKI ")
cmd.color ("blue", "1XKI_A_S4")


cmd.select("1XKI_A_S5", "resi 84-89 & chain A & 1XKI ")
cmd.color ("magenta", "1XKI_A_S5")


cmd.select("1XKI_A_S6", "resi 97-103 & chain A & 1XKI ")
cmd.color ("red", "1XKI_A_S6")


cmd.select("1XKI_A_S7", "resi 110-117 & chain A & 1XKI ")
cmd.color ("yellow", "1XKI_A_S7")


cmd.select("1XKI_barrel", "1XKI_A_S*")
cmd.show("cartoon", "1XKI_barrel")
cmd.zoom("1XKI_barrel")
