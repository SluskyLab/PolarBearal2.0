from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2K0L.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("2K0L_A_S0", "resi 19-26 & chain A & 2K0L ")
cmd.color ("red", "2K0L_A_S0")


cmd.select("2K0L_A_S1", "resi 53-60 & chain A & 2K0L ")
cmd.color ("yellow", "2K0L_A_S1")


cmd.select("2K0L_A_S2", "resi 67-74 & chain A & 2K0L ")
cmd.color ("green", "2K0L_A_S2")


cmd.select("2K0L_A_S3", "resi 94-104 & chain A & 2K0L ")
cmd.color ("cyan", "2K0L_A_S3")


cmd.select("2K0L_A_S4", "resi 108-119 & chain A & 2K0L ")
cmd.color ("blue", "2K0L_A_S4")


cmd.select("2K0L_A_S5", "resi 140-151 & chain A & 2K0L ")
cmd.color ("magenta", "2K0L_A_S5")


cmd.select("2K0L_A_S6", "resi 158-163 & chain A & 2K0L ")
cmd.color ("red", "2K0L_A_S6")


cmd.select("2K0L_A_S7", "resi 185-192 & chain A & 2K0L ")
cmd.color ("yellow", "2K0L_A_S7")


cmd.select("2K0L_barrel", "2K0L_A_S*")
cmd.show("cartoon", "2K0L_barrel")
cmd.zoom("2K0L_barrel")
