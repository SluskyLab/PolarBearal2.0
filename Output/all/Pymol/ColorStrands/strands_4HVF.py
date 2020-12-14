from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4HVF.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("4HVF_A_S0", "resi 35-91 & chain A & 4HVF ")
cmd.color ("red", "4HVF_A_S0")


cmd.select("4HVF_A_S1", "resi 98-106 & chain A & 4HVF ")
cmd.color ("yellow", "4HVF_A_S1")


cmd.select("4HVF_A_S2", "resi 113-145 & chain A & 4HVF ")
cmd.color ("green", "4HVF_A_S2")


cmd.select("4HVF_A_S3", "resi 153-161 & chain A & 4HVF ")
cmd.color ("cyan", "4HVF_A_S3")


cmd.select("4HVF_A_S4", "resi 176-195 & chain A & 4HVF ")
cmd.color ("blue", "4HVF_A_S4")


cmd.select("4HVF_A_S5", "resi 209-214 & chain A & 4HVF ")
cmd.color ("magenta", "4HVF_A_S5")


cmd.select("4HVF_barrel", "4HVF_A_S*")
cmd.show("cartoon", "4HVF_barrel")
cmd.zoom("4HVF_barrel")
