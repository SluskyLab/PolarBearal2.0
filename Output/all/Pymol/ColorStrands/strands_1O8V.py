from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1O8V.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("1O8V_A_S0", "resi 11-14 & chain A & 1O8V ")
cmd.color ("red", "1O8V_A_S0")


cmd.select("1O8V_A_S1", "resi 39-42 & chain A & 1O8V ")
cmd.color ("yellow", "1O8V_A_S1")


cmd.select("1O8V_A_S2", "resi 51-55 & chain A & 1O8V ")
cmd.color ("green", "1O8V_A_S2")


cmd.select("1O8V_A_S3", "resi 61-71 & chain A & 1O8V ")
cmd.color ("cyan", "1O8V_A_S3")


cmd.select("1O8V_A_S4", "resi 82-86 & chain A & 1O8V ")
cmd.color ("blue", "1O8V_A_S4")


cmd.select("1O8V_A_S5", "resi 92-97 & chain A & 1O8V ")
cmd.color ("magenta", "1O8V_A_S5")


cmd.select("1O8V_A_S6", "resi 103-108 & chain A & 1O8V ")
cmd.color ("red", "1O8V_A_S6")


cmd.select("1O8V_A_S7", "resi 114-119 & chain A & 1O8V ")
cmd.color ("yellow", "1O8V_A_S7")


cmd.select("1O8V_A_S8", "resi 125-132 & chain A & 1O8V ")
cmd.color ("green", "1O8V_A_S8")


cmd.select("1O8V_barrel", "1O8V_A_S*")
cmd.show("cartoon", "1O8V_barrel")
cmd.zoom("1O8V_barrel")
