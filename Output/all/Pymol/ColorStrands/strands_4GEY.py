from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4GEY.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("4GEY_A_S0", "resi 28-42 & chain A & 4GEY ")
cmd.color ("red", "4GEY_A_S0")


cmd.select("4GEY_A_S1", "resi 52-65 & chain A & 4GEY ")
cmd.color ("yellow", "4GEY_A_S1")


cmd.select("4GEY_A_S2", "resi 73-86 & chain A & 4GEY ")
cmd.color ("green", "4GEY_A_S2")


cmd.select("4GEY_A_S3", "resi 113-125 & chain A & 4GEY ")
cmd.color ("cyan", "4GEY_A_S3")


cmd.select("4GEY_A_S4", "resi 129-136 & chain A & 4GEY ")
cmd.color ("blue", "4GEY_A_S4")


cmd.select("4GEY_A_S5", "resi 175-184 & chain A & 4GEY ")
cmd.color ("magenta", "4GEY_A_S5")


cmd.select("4GEY_A_S6", "resi 187-197 & chain A & 4GEY ")
cmd.color ("red", "4GEY_A_S6")


cmd.select("4GEY_A_S7", "resi 216-228 & chain A & 4GEY ")
cmd.color ("yellow", "4GEY_A_S7")


cmd.select("4GEY_A_S8", "resi 235-248 & chain A & 4GEY ")
cmd.color ("green", "4GEY_A_S8")


cmd.select("4GEY_A_S9", "resi 270-287 & chain A & 4GEY ")
cmd.color ("cyan", "4GEY_A_S9")


cmd.select("4GEY_A_S10", "resi 293-305 & chain A & 4GEY ")
cmd.color ("blue", "4GEY_A_S10")


cmd.select("4GEY_A_S11", "resi 312-321 & chain A & 4GEY ")
cmd.color ("magenta", "4GEY_A_S11")


cmd.select("4GEY_A_S12", "resi 332-341 & chain A & 4GEY ")
cmd.color ("red", "4GEY_A_S12")


cmd.select("4GEY_A_S13", "resi 374-385 & chain A & 4GEY ")
cmd.color ("yellow", "4GEY_A_S13")


cmd.select("4GEY_A_S14", "resi 388-399 & chain A & 4GEY ")
cmd.color ("green", "4GEY_A_S14")


cmd.select("4GEY_A_S15", "resi 410-420 & chain A & 4GEY ")
cmd.color ("cyan", "4GEY_A_S15")


cmd.select("4GEY_barrel", "4GEY_A_S*")
cmd.show("cartoon", "4GEY_barrel")
cmd.zoom("4GEY_barrel")
