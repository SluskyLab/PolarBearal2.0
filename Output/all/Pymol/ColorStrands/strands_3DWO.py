from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3DWO.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("3DWO_X_S0", "resi 44-61 & chain X & 3DWO ")
cmd.color ("red", "3DWO_X_S0")


cmd.select("3DWO_X_S1", "resi 91-106 & chain X & 3DWO ")
cmd.color ("yellow", "3DWO_X_S1")


cmd.select("3DWO_X_S2", "resi 110-125 & chain X & 3DWO ")
cmd.color ("green", "3DWO_X_S2")


cmd.select("3DWO_X_S3", "resi 137-154 & chain X & 3DWO ")
cmd.color ("cyan", "3DWO_X_S3")


cmd.select("3DWO_X_S4", "resi 157-177 & chain X & 3DWO ")
cmd.color ("blue", "3DWO_X_S4")


cmd.select("3DWO_X_S5", "resi 200-221 & chain X & 3DWO ")
cmd.color ("magenta", "3DWO_X_S5")


cmd.select("3DWO_X_S6", "resi 227-249 & chain X & 3DWO ")
cmd.color ("red", "3DWO_X_S6")


cmd.select("3DWO_X_S7", "resi 274-296 & chain X & 3DWO ")
cmd.color ("yellow", "3DWO_X_S7")


cmd.select("3DWO_X_S8", "resi 300-319 & chain X & 3DWO ")
cmd.color ("green", "3DWO_X_S8")


cmd.select("3DWO_X_S9", "resi 327-345 & chain X & 3DWO ")
cmd.color ("cyan", "3DWO_X_S9")


cmd.select("3DWO_X_S10", "resi 352-363 & chain X & 3DWO ")
cmd.color ("blue", "3DWO_X_S10")


cmd.select("3DWO_X_S11", "resi 378-389 & chain X & 3DWO ")
cmd.color ("magenta", "3DWO_X_S11")


cmd.select("3DWO_X_S12", "resi 395-413 & chain X & 3DWO ")
cmd.color ("red", "3DWO_X_S12")


cmd.select("3DWO_X_S13", "resi 425-441 & chain X & 3DWO ")
cmd.color ("yellow", "3DWO_X_S13")


cmd.select("3DWO_barrel", "3DWO_X_S*")
cmd.show("cartoon", "3DWO_barrel")
cmd.zoom("3DWO_barrel")
