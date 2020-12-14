from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1VYF.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("1VYF_A_S0", "resi 12-14 & chain A & 1VYF ")
cmd.color ("red", "1VYF_A_S0")


cmd.select("1VYF_A_S1", "resi 39-42 & chain A & 1VYF ")
cmd.color ("yellow", "1VYF_A_S1")


cmd.select("1VYF_A_S2", "resi 50-54 & chain A & 1VYF ")
cmd.color ("green", "1VYF_A_S2")


cmd.select("1VYF_A_S3", "resi 60-70 & chain A & 1VYF ")
cmd.color ("cyan", "1VYF_A_S3")


cmd.select("1VYF_A_S4", "resi 81-87 & chain A & 1VYF ")
cmd.color ("blue", "1VYF_A_S4")


cmd.select("1VYF_A_S5", "resi 90-97 & chain A & 1VYF ")
cmd.color ("magenta", "1VYF_A_S5")


cmd.select("1VYF_A_S6", "resi 103-109 & chain A & 1VYF ")
cmd.color ("red", "1VYF_A_S6")


cmd.select("1VYF_A_S7", "resi 114-119 & chain A & 1VYF ")
cmd.color ("yellow", "1VYF_A_S7")


cmd.select("1VYF_A_S8", "resi 125-132 & chain A & 1VYF ")
cmd.color ("green", "1VYF_A_S8")


cmd.select("1VYF_barrel", "1VYF_A_S*")
cmd.show("cartoon", "1VYF_barrel")
cmd.zoom("1VYF_barrel")
