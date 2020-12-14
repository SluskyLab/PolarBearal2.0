from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5L8I.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("5L8I_A_S0", "resi 8-13 & chain A & 5L8I ")
cmd.color ("red", "5L8I_A_S0")


cmd.select("5L8I_A_S1", "resi 38-42 & chain A & 5L8I ")
cmd.color ("yellow", "5L8I_A_S1")


cmd.select("5L8I_A_S2", "resi 48-54 & chain A & 5L8I ")
cmd.color ("green", "5L8I_A_S2")


cmd.select("5L8I_A_S3", "resi 58-70 & chain A & 5L8I ")
cmd.color ("cyan", "5L8I_A_S3")


cmd.select("5L8I_A_S4", "resi 82-85 & chain A & 5L8I ")
cmd.color ("blue", "5L8I_A_S4")


cmd.select("5L8I_A_S5", "resi 91-93 & chain A & 5L8I ")
cmd.color ("magenta", "5L8I_A_S5")


cmd.select("5L8I_A_S6", "resi 99-103 & chain A & 5L8I ")
cmd.color ("red", "5L8I_A_S6")


cmd.select("5L8I_A_S7", "resi 109-114 & chain A & 5L8I ")
cmd.color ("yellow", "5L8I_A_S7")


cmd.select("5L8I_A_S8", "resi 120-127 & chain A & 5L8I ")
cmd.color ("green", "5L8I_A_S8")


cmd.select("5L8I_barrel", "5L8I_A_S*")
cmd.show("cartoon", "5L8I_barrel")
cmd.zoom("5L8I_barrel")
