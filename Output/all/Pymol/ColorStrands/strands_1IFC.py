from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1IFC.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("1IFC_A_S0", "resi 4-12 & chain A & 1IFC ")
cmd.color ("red", "1IFC_A_S0")


cmd.select("1IFC_A_S1", "resi 37-39 & chain A & 1IFC ")
cmd.color ("yellow", "1IFC_A_S1")


cmd.select("1IFC_A_S2", "resi 50-70 & chain A & 1IFC ")
cmd.color ("green", "1IFC_A_S2")


cmd.select("1IFC_A_S3", "resi 78-83 & chain A & 1IFC ")
cmd.color ("cyan", "1IFC_A_S3")


cmd.select("1IFC_A_S4", "resi 89-94 & chain A & 1IFC ")
cmd.color ("blue", "1IFC_A_S4")


cmd.select("1IFC_A_S5", "resi 102-107 & chain A & 1IFC ")
cmd.color ("magenta", "1IFC_A_S5")


cmd.select("1IFC_A_S6", "resi 113-118 & chain A & 1IFC ")
cmd.color ("red", "1IFC_A_S6")


cmd.select("1IFC_A_S7", "resi 124-131 & chain A & 1IFC ")
cmd.color ("yellow", "1IFC_A_S7")


cmd.select("1IFC_barrel", "1IFC_A_S*")
cmd.show("cartoon", "1IFC_barrel")
cmd.zoom("1IFC_barrel")
