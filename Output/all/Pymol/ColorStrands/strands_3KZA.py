from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3KZA.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("3KZA_A_S0", "resi 44-49 & chain A & 3KZA ")
cmd.color ("red", "3KZA_A_S0")


cmd.select("3KZA_A_S1", "resi 53-58 & chain A & 3KZA ")
cmd.color ("yellow", "3KZA_A_S1")


cmd.select("3KZA_A_S2", "resi 69-74 & chain A & 3KZA ")
cmd.color ("green", "3KZA_A_S2")


cmd.select("3KZA_A_S3", "resi 82-84 & chain A & 3KZA ")
cmd.color ("cyan", "3KZA_A_S3")


cmd.select("3KZA_A_S4", "resi 90-98 & chain A & 3KZA ")
cmd.color ("blue", "3KZA_A_S4")


cmd.select("3KZA_A_S5", "resi 102-108 & chain A & 3KZA ")
cmd.color ("magenta", "3KZA_A_S5")


cmd.select("3KZA_barrel", "3KZA_A_S*")
cmd.show("cartoon", "3KZA_barrel")
cmd.zoom("3KZA_barrel")
