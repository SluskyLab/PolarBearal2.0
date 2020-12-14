from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5GGE.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("5GGE_A_S0", "resi 11-14 & chain A & 5GGE ")
cmd.color ("red", "5GGE_A_S0")


cmd.select("5GGE_A_S1", "resi 39-42 & chain A & 5GGE ")
cmd.color ("yellow", "5GGE_A_S1")


cmd.select("5GGE_A_S2", "resi 51-54 & chain A & 5GGE ")
cmd.color ("green", "5GGE_A_S2")


cmd.select("5GGE_A_S3", "resi 60-70 & chain A & 5GGE ")
cmd.color ("cyan", "5GGE_A_S3")


cmd.select("5GGE_A_S4", "resi 80-85 & chain A & 5GGE ")
cmd.color ("blue", "5GGE_A_S4")


cmd.select("5GGE_A_S5", "resi 91-95 & chain A & 5GGE ")
cmd.color ("magenta", "5GGE_A_S5")


cmd.select("5GGE_A_S6", "resi 101-106 & chain A & 5GGE ")
cmd.color ("red", "5GGE_A_S6")


cmd.select("5GGE_A_S7", "resi 112-117 & chain A & 5GGE ")
cmd.color ("yellow", "5GGE_A_S7")


cmd.select("5GGE_A_S8", "resi 123-130 & chain A & 5GGE ")
cmd.color ("green", "5GGE_A_S8")


cmd.select("5GGE_barrel", "5GGE_A_S*")
cmd.show("cartoon", "5GGE_barrel")
cmd.zoom("5GGE_barrel")
