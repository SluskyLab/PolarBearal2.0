from pymol import cmd, stored
cmd.load("C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1XKW.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("1XKW_A_S0", "resi 188-196 & chain A & 1XKW ")
cmd.color ("red", "1XKW_A_S0")


cmd.select("1XKW_A_S1", "resi 198-209 & chain A & 1XKW ")
cmd.color ("yellow", "1XKW_A_S1")


cmd.select("1XKW_A_S2", "resi 217-229 & chain A & 1XKW ")
cmd.color ("green", "1XKW_A_S2")


cmd.select("1XKW_A_S3", "resi 236-250 & chain A & 1XKW ")
cmd.color ("cyan", "1XKW_A_S3")


cmd.select("1XKW_A_S4", "resi 254-268 & chain A & 1XKW ")
cmd.color ("blue", "1XKW_A_S4")


cmd.select("1XKW_A_S5", "resi 278-311 & chain A & 1XKW ")
cmd.color ("magenta", "1XKW_A_S5")


cmd.select("1XKW_A_S6", "resi 318-341 & chain A & 1XKW ")
cmd.color ("red", "1XKW_A_S6")


cmd.select("1XKW_A_S7", "resi 350-373 & chain A & 1XKW ")
cmd.color ("yellow", "1XKW_A_S7")


cmd.select("1XKW_A_S8", "resi 380-406 & chain A & 1XKW ")
cmd.color ("green", "1XKW_A_S8")


cmd.select("1XKW_A_S9", "resi 424-447 & chain A & 1XKW ")
cmd.color ("cyan", "1XKW_A_S9")


cmd.select("1XKW_A_S10", "resi 451-465 & chain A & 1XKW ")
cmd.color ("blue", "1XKW_A_S10")


cmd.select("1XKW_A_S11", "resi 476-485 & chain A & 1XKW ")
cmd.color ("magenta", "1XKW_A_S11")


cmd.select("1XKW_A_S12", "resi 490-502 & chain A & 1XKW ")
cmd.color ("red", "1XKW_A_S12")


cmd.select("1XKW_A_S13", "resi 518-531 & chain A & 1XKW ")
cmd.color ("yellow", "1XKW_A_S13")


cmd.select("1XKW_A_S14", "resi 535-552 & chain A & 1XKW ")
cmd.color ("green", "1XKW_A_S14")


cmd.select("1XKW_A_S15", "resi 567-584 & chain A & 1XKW ")
cmd.color ("cyan", "1XKW_A_S15")


cmd.select("1XKW_A_S16", "resi 589-604 & chain A & 1XKW ")
cmd.color ("blue", "1XKW_A_S16")


cmd.select("1XKW_A_S17", "resi 616-629 & chain A & 1XKW ")
cmd.color ("magenta", "1XKW_A_S17")


cmd.select("1XKW_A_S18", "resi 639-652 & chain A & 1XKW ")
cmd.color ("red", "1XKW_A_S18")


cmd.select("1XKW_A_S19", "resi 659-675 & chain A & 1XKW ")
cmd.color ("yellow", "1XKW_A_S19")


cmd.select("1XKW_A_S20", "resi 678-696 & chain A & 1XKW ")
cmd.color ("green", "1XKW_A_S20")


cmd.select("1XKW_A_S21", "resi 705-719 & chain A & 1XKW ")
cmd.color ("cyan", "1XKW_A_S21")


cmd.select("1XKW_barrel", "1XKW_A_S*")
cmd.show("cartoon", "1XKW_barrel")
cmd.zoom("1XKW_barrel")
