from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1YC9.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("1YC9_B_S0", "resi 113-127 & chain B & 1YC9 ")
cmd.color ("red", "1YC9_B_S0")


cmd.select("1YC9_B_S1", "resi 138-153 & chain B & 1YC9 ")
cmd.color ("yellow", "1YC9_B_S1")


cmd.select("1YC9_B_S2", "resi 326-339 & chain B & 1YC9 ")
cmd.color ("green", "1YC9_B_S2")


cmd.select("1YC9_B_S3", "resi 352-361 & chain B & 1YC9 ")
cmd.color ("cyan", "1YC9_B_S3")


cmd.select("1YC9_C_S0", "resi 113-127 & chain C & 1YC9 ")
cmd.color ("red", "1YC9_C_S0")


cmd.select("1YC9_C_S1", "resi 138-153 & chain C & 1YC9 ")
cmd.color ("yellow", "1YC9_C_S1")


cmd.select("1YC9_C_S2", "resi 326-339 & chain C & 1YC9 ")
cmd.color ("green", "1YC9_C_S2")


cmd.select("1YC9_C_S3", "resi 352-361 & chain C & 1YC9 ")
cmd.color ("cyan", "1YC9_C_S3")


cmd.select("1YC9_D_S0", "resi 113-127 & chain D & 1YC9 ")
cmd.color ("red", "1YC9_D_S0")


cmd.select("1YC9_D_S1", "resi 138-153 & chain D & 1YC9 ")
cmd.color ("yellow", "1YC9_D_S1")


cmd.select("1YC9_D_S2", "resi 326-339 & chain D & 1YC9 ")
cmd.color ("green", "1YC9_D_S2")


cmd.select("1YC9_D_S3", "resi 352-361 & chain D & 1YC9 ")
cmd.color ("cyan", "1YC9_D_S3")


cmd.select("1YC9_barrel", "1YC9_B_S* or 1YC9_C_S* or 1YC9_D_S*")
cmd.show("cartoon", "1YC9_barrel")
cmd.zoom("1YC9_barrel")
