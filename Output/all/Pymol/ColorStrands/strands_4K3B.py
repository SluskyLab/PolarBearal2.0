from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4K3B.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("4K3B_A_S0", "resi 425-433 & chain A & 4K3B ")
cmd.color ("red", "4K3B_A_S0")


cmd.select("4K3B_A_S1", "resi 437-449 & chain A & 4K3B ")
cmd.color ("yellow", "4K3B_A_S1")


cmd.select("4K3B_A_S2", "resi 454-462 & chain A & 4K3B ")
cmd.color ("green", "4K3B_A_S2")


cmd.select("4K3B_A_S3", "resi 465-475 & chain A & 4K3B ")
cmd.color ("cyan", "4K3B_A_S3")


cmd.select("4K3B_A_S4", "resi 485-495 & chain A & 4K3B ")
cmd.color ("blue", "4K3B_A_S4")


cmd.select("4K3B_A_S5", "resi 507-519 & chain A & 4K3B ")
cmd.color ("magenta", "4K3B_A_S5")


cmd.select("4K3B_A_S6", "resi 526-540 & chain A & 4K3B ")
cmd.color ("red", "4K3B_A_S6")


cmd.select("4K3B_A_S7", "resi 563-580 & chain A & 4K3B ")
cmd.color ("yellow", "4K3B_A_S7")


cmd.select("4K3B_A_S8", "resi 590-605 & chain A & 4K3B ")
cmd.color ("green", "4K3B_A_S8")


cmd.select("4K3B_A_S9", "resi 607-621 & chain A & 4K3B ")
cmd.color ("cyan", "4K3B_A_S9")


cmd.select("4K3B_A_S10", "resi 625-639 & chain A & 4K3B ")
cmd.color ("blue", "4K3B_A_S10")


cmd.select("4K3B_A_S11", "resi 684-695 & chain A & 4K3B ")
cmd.color ("magenta", "4K3B_A_S11")


cmd.select("4K3B_A_S12", "resi 705-718 & chain A & 4K3B ")
cmd.color ("red", "4K3B_A_S12")


cmd.select("4K3B_A_S13", "resi 749-759 & chain A & 4K3B ")
cmd.color ("yellow", "4K3B_A_S13")


cmd.select("4K3B_A_S14", "resi 765-773 & chain A & 4K3B ")
cmd.color ("green", "4K3B_A_S14")


cmd.select("4K3B_A_S15", "resi 783-788 & chain A & 4K3B ")
cmd.color ("cyan", "4K3B_A_S15")


cmd.select("4K3B_barrel", "4K3B_A_S*")
cmd.show("cartoon", "4K3B_barrel")
cmd.zoom("4K3B_barrel")
