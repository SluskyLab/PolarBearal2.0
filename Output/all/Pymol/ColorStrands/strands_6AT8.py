from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/6AT8.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("6AT8_A_S0", "resi 11-14 & chain A & 6AT8 ")
cmd.color ("red", "6AT8_A_S0")


cmd.select("6AT8_A_S1", "resi 39-42 & chain A & 6AT8 ")
cmd.color ("yellow", "6AT8_A_S1")


cmd.select("6AT8_A_S2", "resi 50-54 & chain A & 6AT8 ")
cmd.color ("green", "6AT8_A_S2")


cmd.select("6AT8_A_S3", "resi 60-70 & chain A & 6AT8 ")
cmd.color ("cyan", "6AT8_A_S3")


cmd.select("6AT8_A_S4", "resi 83-86 & chain A & 6AT8 ")
cmd.color ("blue", "6AT8_A_S4")


cmd.select("6AT8_A_S5", "resi 93-98 & chain A & 6AT8 ")
cmd.color ("magenta", "6AT8_A_S5")


cmd.select("6AT8_A_S6", "resi 104-109 & chain A & 6AT8 ")
cmd.color ("red", "6AT8_A_S6")


cmd.select("6AT8_A_S7", "resi 115-120 & chain A & 6AT8 ")
cmd.color ("yellow", "6AT8_A_S7")


cmd.select("6AT8_A_S8", "resi 126-133 & chain A & 6AT8 ")
cmd.color ("green", "6AT8_A_S8")


cmd.select("6AT8_barrel", "6AT8_A_S*")
cmd.show("cartoon", "6AT8_barrel")
cmd.zoom("6AT8_barrel")
