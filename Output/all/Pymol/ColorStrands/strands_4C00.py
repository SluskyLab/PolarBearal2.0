from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4C00.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("4C00_A_S0", "resi 267-275 & chain A & 4C00 ")
cmd.color ("red", "4C00_A_S0")


cmd.select("4C00_A_S1", "resi 279-288 & chain A & 4C00 ")
cmd.color ("yellow", "4C00_A_S1")


cmd.select("4C00_A_S2", "resi 297-304 & chain A & 4C00 ")
cmd.color ("green", "4C00_A_S2")


cmd.select("4C00_A_S3", "resi 307-322 & chain A & 4C00 ")
cmd.color ("cyan", "4C00_A_S3")


cmd.select("4C00_A_S4", "resi 325-338 & chain A & 4C00 ")
cmd.color ("blue", "4C00_A_S4")


cmd.select("4C00_A_S5", "resi 343-357 & chain A & 4C00 ")
cmd.color ("magenta", "4C00_A_S5")


cmd.select("4C00_A_S6", "resi 361-375 & chain A & 4C00 ")
cmd.color ("red", "4C00_A_S6")


cmd.select("4C00_A_S7", "resi 381-398 & chain A & 4C00 ")
cmd.color ("yellow", "4C00_A_S7")


cmd.select("4C00_A_S8", "resi 405-416 & chain A & 4C00 ")
cmd.color ("green", "4C00_A_S8")


cmd.select("4C00_A_S9", "resi 426-439 & chain A & 4C00 ")
cmd.color ("cyan", "4C00_A_S9")


cmd.select("4C00_A_S10", "resi 443-455 & chain A & 4C00 ")
cmd.color ("blue", "4C00_A_S10")


cmd.select("4C00_A_S11", "resi 496-510 & chain A & 4C00 ")
cmd.color ("magenta", "4C00_A_S11")


cmd.select("4C00_A_S12", "resi 514-526 & chain A & 4C00 ")
cmd.color ("red", "4C00_A_S12")


cmd.select("4C00_A_S13", "resi 535-544 & chain A & 4C00 ")
cmd.color ("yellow", "4C00_A_S13")


cmd.select("4C00_A_S14", "resi 551-559 & chain A & 4C00 ")
cmd.color ("green", "4C00_A_S14")


cmd.select("4C00_A_S15", "resi 568-572 & chain A & 4C00 ")
cmd.color ("cyan", "4C00_A_S15")


cmd.select("4C00_barrel", "4C00_A_S*")
cmd.show("cartoon", "4C00_barrel")
cmd.zoom("4C00_barrel")
