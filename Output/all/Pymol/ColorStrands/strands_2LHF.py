from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2LHF.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("2LHF_A_S0", "resi 3-12 & chain A & 2LHF ")
cmd.color ("red", "2LHF_A_S0")


cmd.select("2LHF_A_S1", "resi 41-49 & chain A & 2LHF ")
cmd.color ("yellow", "2LHF_A_S1")


cmd.select("2LHF_A_S2", "resi 54-60 & chain A & 2LHF ")
cmd.color ("green", "2LHF_A_S2")


cmd.select("2LHF_A_S3", "resi 74-84 & chain A & 2LHF ")
cmd.color ("cyan", "2LHF_A_S3")


cmd.select("2LHF_A_S4", "resi 90-103 & chain A & 2LHF ")
cmd.color ("blue", "2LHF_A_S4")


cmd.select("2LHF_A_S5", "resi 120-130 & chain A & 2LHF ")
cmd.color ("magenta", "2LHF_A_S5")


cmd.select("2LHF_A_S6", "resi 136-145 & chain A & 2LHF ")
cmd.color ("red", "2LHF_A_S6")


cmd.select("2LHF_A_S7", "resi 170-177 & chain A & 2LHF ")
cmd.color ("yellow", "2LHF_A_S7")


cmd.select("2LHF_barrel", "2LHF_A_S*")
cmd.show("cartoon", "2LHF_barrel")
cmd.zoom("2LHF_barrel")
