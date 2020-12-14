from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2Y32.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("2Y32_A_S0", "resi 3-8 & chain A & 2Y32 ")
cmd.color ("red", "2Y32_A_S0")


cmd.select("2Y32_A_S1", "resi 14-21 & chain A & 2Y32 ")
cmd.color ("yellow", "2Y32_A_S1")


cmd.select("2Y32_A_S2", "resi 25-32 & chain A & 2Y32 ")
cmd.color ("green", "2Y32_A_S2")


cmd.select("2Y32_A_S3", "resi 45-52 & chain A & 2Y32 ")
cmd.color ("cyan", "2Y32_A_S3")


cmd.select("2Y32_A_S4", "resi 58-66 & chain A & 2Y32 ")
cmd.color ("blue", "2Y32_A_S4")


cmd.select("2Y32_A_S5", "resi 71-79 & chain A & 2Y32 ")
cmd.color ("magenta", "2Y32_A_S5")


cmd.select("2Y32_A_S6", "resi 85-92 & chain A & 2Y32 ")
cmd.color ("red", "2Y32_A_S6")


cmd.select("2Y32_A_S7", "resi 103-113 & chain A & 2Y32 ")
cmd.color ("yellow", "2Y32_A_S7")


cmd.select("2Y32_barrel", "2Y32_A_S*")
cmd.show("cartoon", "2Y32_barrel")
cmd.zoom("2Y32_barrel")
