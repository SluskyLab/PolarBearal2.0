from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4XMC.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("4XMC_A_S0", "resi 25-27 & chain A & 4XMC ")
cmd.color ("red", "4XMC_A_S0")


cmd.select("4XMC_A_S1", "resi 42-48 & chain A & 4XMC ")
cmd.color ("yellow", "4XMC_A_S1")


cmd.select("4XMC_A_S2", "resi 54-62 & chain A & 4XMC ")
cmd.color ("green", "4XMC_A_S2")


cmd.select("4XMC_A_S3", "resi 67-78 & chain A & 4XMC ")
cmd.color ("cyan", "4XMC_A_S3")


cmd.select("4XMC_A_S4", "resi 83-90 & chain A & 4XMC ")
cmd.color ("blue", "4XMC_A_S4")


cmd.select("4XMC_A_S5", "resi 99-113 & chain A & 4XMC ")
cmd.color ("magenta", "4XMC_A_S5")


cmd.select("4XMC_A_S6", "resi 119-125 & chain A & 4XMC ")
cmd.color ("red", "4XMC_A_S6")


cmd.select("4XMC_A_S7", "resi 133-138 & chain A & 4XMC ")
cmd.color ("yellow", "4XMC_A_S7")


cmd.select("4XMC_barrel", "4XMC_A_S*")
cmd.show("cartoon", "4XMC_barrel")
cmd.zoom("4XMC_barrel")
