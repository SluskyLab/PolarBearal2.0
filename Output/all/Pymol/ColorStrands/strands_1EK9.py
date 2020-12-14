from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1EK9.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("1EK9_A_S0", "resi 39-52 & chain A & 1EK9 ")
cmd.color ("red", "1EK9_A_S0")


cmd.select("1EK9_A_S1", "resi 60-73 & chain A & 1EK9 ")
cmd.color ("yellow", "1EK9_A_S1")


cmd.select("1EK9_A_S2", "resi 246-262 & chain A & 1EK9 ")
cmd.color ("green", "1EK9_A_S2")


cmd.select("1EK9_A_S3", "resi 276-290 & chain A & 1EK9 ")
cmd.color ("cyan", "1EK9_A_S3")


cmd.select("1EK9_B_S0", "resi 39-52 & chain B & 1EK9 ")
cmd.color ("red", "1EK9_B_S0")


cmd.select("1EK9_B_S1", "resi 60-73 & chain B & 1EK9 ")
cmd.color ("yellow", "1EK9_B_S1")


cmd.select("1EK9_B_S2", "resi 246-262 & chain B & 1EK9 ")
cmd.color ("green", "1EK9_B_S2")


cmd.select("1EK9_B_S3", "resi 276-290 & chain B & 1EK9 ")
cmd.color ("cyan", "1EK9_B_S3")


cmd.select("1EK9_C_S0", "resi 39-52 & chain C & 1EK9 ")
cmd.color ("red", "1EK9_C_S0")


cmd.select("1EK9_C_S1", "resi 60-73 & chain C & 1EK9 ")
cmd.color ("yellow", "1EK9_C_S1")


cmd.select("1EK9_C_S2", "resi 246-262 & chain C & 1EK9 ")
cmd.color ("green", "1EK9_C_S2")


cmd.select("1EK9_C_S3", "resi 280-290 & chain C & 1EK9 ")
cmd.color ("cyan", "1EK9_C_S3")


cmd.select("1EK9_barrel", "1EK9_A_S* or 1EK9_B_S* or 1EK9_C_S*")
cmd.show("cartoon", "1EK9_barrel")
cmd.zoom("1EK9_barrel")
