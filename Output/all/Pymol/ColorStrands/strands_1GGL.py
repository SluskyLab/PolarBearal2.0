from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1GGL.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("1GGL_A_S0", "resi 11-14 & chain A & 1GGL ")
cmd.color ("red", "1GGL_A_S0")


cmd.select("1GGL_A_S1", "resi 39-43 & chain A & 1GGL ")
cmd.color ("yellow", "1GGL_A_S1")


cmd.select("1GGL_A_S2", "resi 50-54 & chain A & 1GGL ")
cmd.color ("green", "1GGL_A_S2")


cmd.select("1GGL_A_S3", "resi 60-70 & chain A & 1GGL ")
cmd.color ("cyan", "1GGL_A_S3")


cmd.select("1GGL_A_S4", "resi 83-87 & chain A & 1GGL ")
cmd.color ("blue", "1GGL_A_S4")


cmd.select("1GGL_A_S5", "resi 93-98 & chain A & 1GGL ")
cmd.color ("magenta", "1GGL_A_S5")


cmd.select("1GGL_A_S6", "resi 105-109 & chain A & 1GGL ")
cmd.color ("red", "1GGL_A_S6")


cmd.select("1GGL_A_S7", "resi 115-120 & chain A & 1GGL ")
cmd.color ("yellow", "1GGL_A_S7")


cmd.select("1GGL_A_S8", "resi 126-133 & chain A & 1GGL ")
cmd.color ("green", "1GGL_A_S8")


cmd.select("1GGL_barrel", "1GGL_A_S*")
cmd.show("cartoon", "1GGL_barrel")
cmd.zoom("1GGL_barrel")
