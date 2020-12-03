from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4K3C.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("4K3C_A_S0", "resi 422-431 & chain A & 4K3C ")
cmd.color ("red", "4K3C_A_S0")


cmd.select("4K3C_A_S1", "resi 434-443 & chain A & 4K3C ")
cmd.color ("yellow", "4K3C_A_S1")


cmd.select("4K3C_A_S2", "resi 452-459 & chain A & 4K3C ")
cmd.color ("green", "4K3C_A_S2")


cmd.select("4K3C_A_S3", "resi 462-472 & chain A & 4K3C ")
cmd.color ("cyan", "4K3C_A_S3")


cmd.select("4K3C_A_S4", "resi 481-492 & chain A & 4K3C ")
cmd.color ("blue", "4K3C_A_S4")


cmd.select("4K3C_A_S5", "resi 502-515 & chain A & 4K3C ")
cmd.color ("magenta", "4K3C_A_S5")


cmd.select("4K3C_A_S6", "resi 520-535 & chain A & 4K3C ")
cmd.color ("red", "4K3C_A_S6")


cmd.select("4K3C_A_S7", "resi 564-581 & chain A & 4K3C ")
cmd.color ("yellow", "4K3C_A_S7")


cmd.select("4K3C_A_S8", "resi 588-604 & chain A & 4K3C ")
cmd.color ("green", "4K3C_A_S8")


cmd.select("4K3C_A_S9", "resi 606-620 & chain A & 4K3C ")
cmd.color ("cyan", "4K3C_A_S9")


cmd.select("4K3C_A_S10", "resi 626-640 & chain A & 4K3C ")
cmd.color ("blue", "4K3C_A_S10")


cmd.select("4K3C_A_S11", "resi 690-701 & chain A & 4K3C ")
cmd.color ("magenta", "4K3C_A_S11")


cmd.select("4K3C_A_S12", "resi 715-726 & chain A & 4K3C ")
cmd.color ("red", "4K3C_A_S12")


cmd.select("4K3C_A_S13", "resi 750-759 & chain A & 4K3C ")
cmd.color ("yellow", "4K3C_A_S13")


cmd.select("4K3C_A_S14", "resi 766-775 & chain A & 4K3C ")
cmd.color ("green", "4K3C_A_S14")


cmd.select("4K3C_A_S15", "resi 784-793 & chain A & 4K3C ")
cmd.color ("cyan", "4K3C_A_S15")


cmd.select("4K3C_barrel", "4K3C_A_S*")
cmd.show("cartoon", "4K3C_barrel")
cmd.zoom("4K3C_barrel")
