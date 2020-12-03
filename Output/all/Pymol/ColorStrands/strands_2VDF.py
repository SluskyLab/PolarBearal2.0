from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2VDF.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("2VDF_A_S0", "resi 9-22 & chain A & 2VDF ")
cmd.color ("red", "2VDF_A_S0")


cmd.select("2VDF_A_S1", "resi 27-42 & chain A & 2VDF ")
cmd.color ("yellow", "2VDF_A_S1")


cmd.select("2VDF_A_S2", "resi 47-70 & chain A & 2VDF ")
cmd.color ("green", "2VDF_A_S2")


cmd.select("2VDF_A_S3", "resi 76-100 & chain A & 2VDF ")
cmd.color ("cyan", "2VDF_A_S3")


cmd.select("2VDF_A_S4", "resi 106-122 & chain A & 2VDF ")
cmd.color ("blue", "2VDF_A_S4")


cmd.select("2VDF_A_S5", "resi 131-147 & chain A & 2VDF ")
cmd.color ("magenta", "2VDF_A_S5")


cmd.select("2VDF_A_S6", "resi 154-172 & chain A & 2VDF ")
cmd.color ("red", "2VDF_A_S6")


cmd.select("2VDF_A_S7", "resi 182-199 & chain A & 2VDF ")
cmd.color ("yellow", "2VDF_A_S7")


cmd.select("2VDF_A_S8", "resi 206-218 & chain A & 2VDF ")
cmd.color ("green", "2VDF_A_S8")


cmd.select("2VDF_A_S9", "resi 240-253 & chain A & 2VDF ")
cmd.color ("cyan", "2VDF_A_S9")


cmd.select("2VDF_barrel", "2VDF_A_S*")
cmd.show("cartoon", "2VDF_barrel")
cmd.zoom("2VDF_barrel")
