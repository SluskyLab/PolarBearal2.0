from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2O62.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("2O62_A_S0", "resi 144-152 & chain A & 2O62 ")
cmd.color ("red", "2O62_A_S0")


cmd.select("2O62_A_S1", "resi 161-170 & chain A & 2O62 ")
cmd.color ("yellow", "2O62_A_S1")


cmd.select("2O62_A_S2", "resi 177-182 & chain A & 2O62 ")
cmd.color ("green", "2O62_A_S2")


cmd.select("2O62_A_S3", "resi 188-193 & chain A & 2O62 ")
cmd.color ("cyan", "2O62_A_S3")


cmd.select("2O62_A_S4", "resi 199-201 & chain A & 2O62 ")
cmd.color ("blue", "2O62_A_S4")


cmd.select("2O62_A_S5", "resi 208-214 & chain A & 2O62 ")
cmd.color ("magenta", "2O62_A_S5")


cmd.select("2O62_A_S6", "resi 218-224 & chain A & 2O62 ")
cmd.color ("red", "2O62_A_S6")


cmd.select("2O62_A_S7", "resi 232-240 & chain A & 2O62 ")
cmd.color ("yellow", "2O62_A_S7")


cmd.select("2O62_A_S8", "resi 244-252 & chain A & 2O62 ")
cmd.color ("green", "2O62_A_S8")


cmd.select("2O62_A_S9", "resi 259-266 & chain A & 2O62 ")
cmd.color ("cyan", "2O62_A_S9")


cmd.select("2O62_barrel", "2O62_A_S*")
cmd.show("cartoon", "2O62_barrel")
cmd.zoom("2O62_barrel")
