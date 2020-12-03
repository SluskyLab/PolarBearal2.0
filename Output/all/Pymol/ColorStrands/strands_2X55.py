from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2X55.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("2X55_A_S0", "resi 14-31 & chain A & 2X55 ")
cmd.color ("red", "2X55_A_S0")


cmd.select("2X55_A_S1", "resi 40-59 & chain A & 2X55 ")
cmd.color ("yellow", "2X55_A_S1")


cmd.select("2X55_A_S2", "resi 66-87 & chain A & 2X55 ")
cmd.color ("green", "2X55_A_S2")


cmd.select("2X55_A_S3", "resi 96-121 & chain A & 2X55 ")
cmd.color ("cyan", "2X55_A_S3")


cmd.select("2X55_A_S4", "resi 125-150 & chain A & 2X55 ")
cmd.color ("blue", "2X55_A_S4")


cmd.select("2X55_A_S5", "resi 155-184 & chain A & 2X55 ")
cmd.color ("magenta", "2X55_A_S5")


cmd.select("2X55_A_S6", "resi 189-208 & chain A & 2X55 ")
cmd.color ("red", "2X55_A_S6")


cmd.select("2X55_A_S7", "resi 213-235 & chain A & 2X55 ")
cmd.color ("yellow", "2X55_A_S7")


cmd.select("2X55_A_S8", "resi 238-270 & chain A & 2X55 ")
cmd.color ("green", "2X55_A_S8")


cmd.select("2X55_A_S9", "resi 276-292 & chain A & 2X55 ")
cmd.color ("cyan", "2X55_A_S9")


cmd.select("2X55_barrel", "2X55_A_S*")
cmd.show("cartoon", "2X55_barrel")
cmd.zoom("2X55_barrel")
