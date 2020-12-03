from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/6H3I.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("6H3I_A_S0", "resi 138-152 & chain A & 6H3I ")
cmd.color ("red", "6H3I_A_S0")


cmd.select("6H3I_A_S1", "resi 166-180 & chain A & 6H3I ")
cmd.color ("yellow", "6H3I_A_S1")


cmd.select("6H3I_A_S2", "resi 188-193 & chain A & 6H3I ")
cmd.color ("green", "6H3I_A_S2")


cmd.select("6H3I_A_S3", "resi 204-208 & chain A & 6H3I ")
cmd.color ("cyan", "6H3I_A_S3")


cmd.select("6H3I_A_S4", "resi 218-223 & chain A & 6H3I ")
cmd.color ("blue", "6H3I_A_S4")


cmd.select("6H3I_A_S5", "resi 242-246 & chain A & 6H3I ")
cmd.color ("magenta", "6H3I_A_S5")


cmd.select("6H3I_barrel", "6H3I_A_S*")
cmd.show("cartoon", "6H3I_barrel")
cmd.zoom("6H3I_barrel")
