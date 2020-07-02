from pymol import cmd, stored
cmd.load("/Users/ryan/Desktop/gitLab/polarbearel/DB/mono/1A0T.pdb")
cmd.hide("everything", "all")
cmd.color("grey50","all")
cmd.select("1A0T_P_S0", "resi 4-15 & chain P & 1A0T ")
cmd.color ("red", "1A0T_P_S0")


cmd.select("1A0T_P_S1", "resi 48-57 & chain P & 1A0T ")
cmd.color ("yellow", "1A0T_P_S1")


cmd.select("1A0T_P_S2", "resi 64-75 & chain P & 1A0T ")
cmd.color ("green", "1A0T_P_S2")


cmd.select("1A0T_P_S3", "resi 89-98 & chain P & 1A0T ")
cmd.color ("cyan", "1A0T_P_S3")


cmd.select("1A0T_P_S4", "resi 111-125 & chain P & 1A0T ")
cmd.color ("blue", "1A0T_P_S4")


cmd.select("1A0T_P_S5", "resi 130-147 & chain P & 1A0T ")
cmd.color ("magenta", "1A0T_P_S5")


cmd.select("1A0T_P_S6", "resi 151-162 & chain P & 1A0T ")
cmd.color ("red", "1A0T_P_S6")


cmd.select("1A0T_P_S7", "resi 172-182 & chain P & 1A0T ")
cmd.color ("yellow", "1A0T_P_S7")


cmd.select("1A0T_P_S8", "resi 185-195 & chain P & 1A0T ")
cmd.color ("green", "1A0T_P_S8")


cmd.select("1A0T_P_S9", "resi 215-226 & chain P & 1A0T ")
cmd.color ("cyan", "1A0T_P_S9")


cmd.select("1A0T_P_S10", "resi 233-245 & chain P & 1A0T ")
cmd.color ("blue", "1A0T_P_S10")


cmd.select("1A0T_P_S11", "resi 265-277 & chain P & 1A0T ")
cmd.color ("magenta", "1A0T_P_S11")


cmd.select("1A0T_P_S12", "resi 281-293 & chain P & 1A0T ")
cmd.color ("red", "1A0T_P_S12")


cmd.select("1A0T_P_S13", "resi 301-315 & chain P & 1A0T ")
cmd.color ("yellow", "1A0T_P_S13")


cmd.select("1A0T_P_S14", "resi 318-333 & chain P & 1A0T ")
cmd.color ("green", "1A0T_P_S14")


cmd.select("1A0T_P_S15", "resi 343-357 & chain P & 1A0T ")
cmd.color ("cyan", "1A0T_P_S15")


cmd.select("1A0T_P_S16", "resi 369-380 & chain P & 1A0T ")
cmd.color ("blue", "1A0T_P_S16")


cmd.select("1A0T_P_S17", "resi 402-413 & chain P & 1A0T ")
cmd.color ("magenta", "1A0T_P_S17")


cmd.select("1A0T_barrel", "1A0T_P_S*")
cmd.show("cartoon", "1A0T_barrel")
cmd.zoom("1A0T_barrel")
