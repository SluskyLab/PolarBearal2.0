from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4GGR.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("4GGR_A_S0", "resi 11-14 & chain A & 4GGR ")
cmd.color ("red", "4GGR_A_S0")


cmd.select("4GGR_A_S1", "resi 20-25 & chain A & 4GGR ")
cmd.color ("yellow", "4GGR_A_S1")


cmd.select("4GGR_A_S2", "resi 29-36 & chain A & 4GGR ")
cmd.color ("green", "4GGR_A_S2")


cmd.select("4GGR_A_S3", "resi 49-55 & chain A & 4GGR ")
cmd.color ("cyan", "4GGR_A_S3")


cmd.select("4GGR_A_S4", "resi 60-66 & chain A & 4GGR ")
cmd.color ("blue", "4GGR_A_S4")


cmd.select("4GGR_A_S5", "resi 71-78 & chain A & 4GGR ")
cmd.color ("magenta", "4GGR_A_S5")


cmd.select("4GGR_A_S6", "resi 84-92 & chain A & 4GGR ")
cmd.color ("red", "4GGR_A_S6")


cmd.select("4GGR_A_S7", "resi 100-109 & chain A & 4GGR ")
cmd.color ("yellow", "4GGR_A_S7")


cmd.select("4GGR_barrel", "4GGR_A_S*")
cmd.show("cartoon", "4GGR_barrel")
cmd.zoom("4GGR_barrel")
