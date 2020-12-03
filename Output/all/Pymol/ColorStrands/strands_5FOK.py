from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5FOK.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("5FOK_A_S0", "resi 157-165 & chain A & 5FOK ")
cmd.color ("red", "5FOK_A_S0")


cmd.select("5FOK_A_S1", "resi 169-180 & chain A & 5FOK ")
cmd.color ("yellow", "5FOK_A_S1")


cmd.select("5FOK_A_S2", "resi 184-197 & chain A & 5FOK ")
cmd.color ("green", "5FOK_A_S2")


cmd.select("5FOK_A_S3", "resi 203-216 & chain A & 5FOK ")
cmd.color ("cyan", "5FOK_A_S3")


cmd.select("5FOK_A_S4", "resi 223-236 & chain A & 5FOK ")
cmd.color ("blue", "5FOK_A_S4")


cmd.select("5FOK_A_S5", "resi 272-288 & chain A & 5FOK ")
cmd.color ("magenta", "5FOK_A_S5")


cmd.select("5FOK_A_S6", "resi 291-308 & chain A & 5FOK ")
cmd.color ("red", "5FOK_A_S6")


cmd.select("5FOK_A_S7", "resi 329-348 & chain A & 5FOK ")
cmd.color ("yellow", "5FOK_A_S7")


cmd.select("5FOK_A_S8", "resi 355-376 & chain A & 5FOK ")
cmd.color ("green", "5FOK_A_S8")


cmd.select("5FOK_A_S9", "resi 410-435 & chain A & 5FOK ")
cmd.color ("cyan", "5FOK_A_S9")


cmd.select("5FOK_A_S10", "resi 438-458 & chain A & 5FOK ")
cmd.color ("blue", "5FOK_A_S10")


cmd.select("5FOK_A_S11", "resi 467-487 & chain A & 5FOK ")
cmd.color ("magenta", "5FOK_A_S11")


cmd.select("5FOK_A_S12", "resi 491-502 & chain A & 5FOK ")
cmd.color ("red", "5FOK_A_S12")


cmd.select("5FOK_A_S13", "resi 528-539 & chain A & 5FOK ")
cmd.color ("yellow", "5FOK_A_S13")


cmd.select("5FOK_A_S14", "resi 543-556 & chain A & 5FOK ")
cmd.color ("green", "5FOK_A_S14")


cmd.select("5FOK_A_S15", "resi 573-588 & chain A & 5FOK ")
cmd.color ("cyan", "5FOK_A_S15")


cmd.select("5FOK_A_S16", "resi 592-607 & chain A & 5FOK ")
cmd.color ("blue", "5FOK_A_S16")


cmd.select("5FOK_A_S17", "resi 623-634 & chain A & 5FOK ")
cmd.color ("magenta", "5FOK_A_S17")


cmd.select("5FOK_A_S18", "resi 638-652 & chain A & 5FOK ")
cmd.color ("red", "5FOK_A_S18")


cmd.select("5FOK_A_S19", "resi 658-674 & chain A & 5FOK ")
cmd.color ("yellow", "5FOK_A_S19")


cmd.select("5FOK_A_S20", "resi 677-697 & chain A & 5FOK ")
cmd.color ("green", "5FOK_A_S20")


cmd.select("5FOK_A_S21", "resi 701-717 & chain A & 5FOK ")
cmd.color ("cyan", "5FOK_A_S21")


cmd.select("5FOK_barrel", "5FOK_A_S*")
cmd.show("cartoon", "5FOK_barrel")
cmd.zoom("5FOK_barrel")
