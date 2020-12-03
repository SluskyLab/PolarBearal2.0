from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2X9K.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("2X9K_A_S0", "resi 7-19 & chain A & 2X9K ")
cmd.color ("red", "2X9K_A_S0")


cmd.select("2X9K_A_S1", "resi 27-39 & chain A & 2X9K ")
cmd.color ("yellow", "2X9K_A_S1")


cmd.select("2X9K_A_S2", "resi 44-53 & chain A & 2X9K ")
cmd.color ("green", "2X9K_A_S2")


cmd.select("2X9K_A_S3", "resi 65-78 & chain A & 2X9K ")
cmd.color ("cyan", "2X9K_A_S3")


cmd.select("2X9K_A_S4", "resi 84-97 & chain A & 2X9K ")
cmd.color ("blue", "2X9K_A_S4")


cmd.select("2X9K_A_S5", "resi 107-122 & chain A & 2X9K ")
cmd.color ("magenta", "2X9K_A_S5")


cmd.select("2X9K_A_S6", "resi 125-138 & chain A & 2X9K ")
cmd.color ("red", "2X9K_A_S6")


cmd.select("2X9K_A_S7", "resi 148-161 & chain A & 2X9K ")
cmd.color ("yellow", "2X9K_A_S7")


cmd.select("2X9K_A_S8", "resi 164-177 & chain A & 2X9K ")
cmd.color ("green", "2X9K_A_S8")


cmd.select("2X9K_A_S9", "resi 187-200 & chain A & 2X9K ")
cmd.color ("cyan", "2X9K_A_S9")


cmd.select("2X9K_A_S10", "resi 203-219 & chain A & 2X9K ")
cmd.color ("blue", "2X9K_A_S10")


cmd.select("2X9K_A_S11", "resi 229-243 & chain A & 2X9K ")
cmd.color ("magenta", "2X9K_A_S11")


cmd.select("2X9K_A_S12", "resi 247-258 & chain A & 2X9K ")
cmd.color ("red", "2X9K_A_S12")


cmd.select("2X9K_A_S13", "resi 269-280 & chain A & 2X9K ")
cmd.color ("yellow", "2X9K_A_S13")


cmd.select("2X9K_barrel", "2X9K_A_S*")
cmd.show("cartoon", "2X9K_barrel")
cmd.zoom("2X9K_barrel")
