from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/6GIE.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("6GIE_A_S0", "resi 1-13 & chain A & 6GIE ")
cmd.color ("red", "6GIE_A_S0")


cmd.select("6GIE_A_S1", "resi 21-34 & chain A & 6GIE ")
cmd.color ("yellow", "6GIE_A_S1")


cmd.select("6GIE_A_S2", "resi 52-61 & chain A & 6GIE ")
cmd.color ("green", "6GIE_A_S2")


cmd.select("6GIE_A_S3", "resi 72-83 & chain A & 6GIE ")
cmd.color ("cyan", "6GIE_A_S3")


cmd.select("6GIE_A_S4", "resi 90-100 & chain A & 6GIE ")
cmd.color ("blue", "6GIE_A_S4")


cmd.select("6GIE_A_S5", "resi 114-123 & chain A & 6GIE ")
cmd.color ("magenta", "6GIE_A_S5")


cmd.select("6GIE_A_S6", "resi 126-135 & chain A & 6GIE ")
cmd.color ("red", "6GIE_A_S6")


cmd.select("6GIE_A_S7", "resi 168-177 & chain A & 6GIE ")
cmd.color ("yellow", "6GIE_A_S7")


cmd.select("6GIE_A_S8", "resi 185-194 & chain A & 6GIE ")
cmd.color ("green", "6GIE_A_S8")


cmd.select("6GIE_A_S9", "resi 199-208 & chain A & 6GIE ")
cmd.color ("cyan", "6GIE_A_S9")


cmd.select("6GIE_A_S10", "resi 212-220 & chain A & 6GIE ")
cmd.color ("blue", "6GIE_A_S10")


cmd.select("6GIE_A_S11", "resi 229-240 & chain A & 6GIE ")
cmd.color ("magenta", "6GIE_A_S11")


cmd.select("6GIE_A_S12", "resi 243-254 & chain A & 6GIE ")
cmd.color ("red", "6GIE_A_S12")


cmd.select("6GIE_A_S13", "resi 263-274 & chain A & 6GIE ")
cmd.color ("yellow", "6GIE_A_S13")


cmd.select("6GIE_barrel", "6GIE_A_S*")
cmd.show("cartoon", "6GIE_barrel")
cmd.zoom("6GIE_barrel")
