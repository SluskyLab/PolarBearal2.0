from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4MT4.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("4MT4_A_S0", "resi 82-95 & chain A & 4MT4 ")
cmd.color ("red", "4MT4_A_S0")


cmd.select("4MT4_A_S1", "resi 323-332 & chain A & 4MT4 ")
cmd.color ("yellow", "4MT4_A_S1")


cmd.select("4MT4_B_S0", "resi 82-95 & chain B & 4MT4 ")
cmd.color ("red", "4MT4_B_S0")


cmd.select("4MT4_B_S1", "resi 323-332 & chain B & 4MT4 ")
cmd.color ("yellow", "4MT4_B_S1")


cmd.select("4MT4_C_S0", "resi 82-95 & chain C & 4MT4 ")
cmd.color ("red", "4MT4_C_S0")


cmd.select("4MT4_C_S1", "resi 323-332 & chain C & 4MT4 ")
cmd.color ("yellow", "4MT4_C_S1")


cmd.select("4MT4_barrel", "4MT4_A_S* or 4MT4_B_S* or 4MT4_C_S*")
cmd.show("cartoon", "4MT4_barrel")
cmd.zoom("4MT4_barrel")
