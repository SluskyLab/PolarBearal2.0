from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4QKY.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("4QKY_A_S0", "resi 212-219 & chain A & 4QKY ")
cmd.color ("red", "4QKY_A_S0")


cmd.select("4QKY_A_S1", "resi 231-238 & chain A & 4QKY ")
cmd.color ("yellow", "4QKY_A_S1")


cmd.select("4QKY_A_S2", "resi 247-259 & chain A & 4QKY ")
cmd.color ("green", "4QKY_A_S2")


cmd.select("4QKY_A_S3", "resi 263-274 & chain A & 4QKY ")
cmd.color ("cyan", "4QKY_A_S3")


cmd.select("4QKY_A_S4", "resi 280-291 & chain A & 4QKY ")
cmd.color ("blue", "4QKY_A_S4")


cmd.select("4QKY_A_S5", "resi 304-319 & chain A & 4QKY ")
cmd.color ("magenta", "4QKY_A_S5")


cmd.select("4QKY_A_S6", "resi 323-340 & chain A & 4QKY ")
cmd.color ("red", "4QKY_A_S6")


cmd.select("4QKY_A_S7", "resi 351-365 & chain A & 4QKY ")
cmd.color ("yellow", "4QKY_A_S7")


cmd.select("4QKY_A_S8", "resi 368-379 & chain A & 4QKY ")
cmd.color ("green", "4QKY_A_S8")


cmd.select("4QKY_A_S9", "resi 402-413 & chain A & 4QKY ")
cmd.color ("cyan", "4QKY_A_S9")


cmd.select("4QKY_A_S10", "resi 420-430 & chain A & 4QKY ")
cmd.color ("blue", "4QKY_A_S10")


cmd.select("4QKY_A_S11", "resi 460-474 & chain A & 4QKY ")
cmd.color ("magenta", "4QKY_A_S11")


cmd.select("4QKY_A_S12", "resi 484-497 & chain A & 4QKY ")
cmd.color ("red", "4QKY_A_S12")


cmd.select("4QKY_A_S13", "resi 506-518 & chain A & 4QKY ")
cmd.color ("yellow", "4QKY_A_S13")


cmd.select("4QKY_A_S14", "resi 521-532 & chain A & 4QKY ")
cmd.color ("green", "4QKY_A_S14")


cmd.select("4QKY_A_S15", "resi 545-554 & chain A & 4QKY ")
cmd.color ("cyan", "4QKY_A_S15")


cmd.select("4QKY_barrel", "4QKY_A_S*")
cmd.show("cartoon", "4QKY_barrel")
cmd.zoom("4QKY_barrel")
