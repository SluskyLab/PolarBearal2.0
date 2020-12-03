from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/6TZK.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 708-708 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 726-726 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 744-746 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 750-750 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 761-761 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 765-765 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 783-798 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 803-817 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 820-832 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 835-835 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 838-839 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 843-844 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 848-848 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 854-875 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 878-885 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 891-904 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 907-918 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 921-921 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("Astrand18", "resi 928-929 & chain A ")
cmd.color ("red", "Astrand18")


cmd.select("Astrand19", "resi 934-934 & chain A ")
cmd.color ("green", "Astrand19")


cmd.select("Astrand20", "resi 939-939 & chain A ")
cmd.color ("orange", "Astrand20")


cmd.select("Astrand21", "resi 943-953 & chain A ")
cmd.color ("teal", "Astrand21")


cmd.select("Astrand22", "resi 959-972 & chain A ")
cmd.color ("yellow", "Astrand22")


cmd.select("Astrand23", "resi 975-975 & chain A ")
cmd.color ("blue", "Astrand23")


cmd.select("Astrand24", "resi 978-994 & chain A ")
cmd.color ("red", "Astrand24")


cmd.select("Astrand25", "resi 997-1013 & chain A ")
cmd.color ("green", "Astrand25")


cmd.select("Astrand26", "resi 1021-1021 & chain A ")
cmd.color ("orange", "Astrand26")


cmd.select("Astrand27", "resi 1024-1026 & chain A ")
cmd.color ("teal", "Astrand27")


cmd.select("Astrand28", "resi 1029-1043 & chain A ")
cmd.color ("yellow", "Astrand28")


cmd.select("Astrand29", "resi 1046-1064 & chain A ")
cmd.color ("blue", "Astrand29")


cmd.select("Astrand30", "resi 1067-1069 & chain A ")
cmd.color ("red", "Astrand30")


cmd.select("Astrand31", "resi 1073-1073 & chain A ")
cmd.color ("green", "Astrand31")


cmd.select("Astrand32", "resi 1084-1086 & chain A ")
cmd.color ("orange", "Astrand32")


cmd.select("Astrand33", "resi 1089-1107 & chain A ")
cmd.color ("teal", "Astrand33")


cmd.select("Astrand34", "resi 1110-1119 & chain A ")
cmd.color ("yellow", "Astrand34")


cmd.select("Astrand35", "resi 1125-1136 & chain A ")
cmd.color ("blue", "Astrand35")


cmd.select("Astrand36", "resi 1140-1142 & chain A ")
cmd.color ("red", "Astrand36")


cmd.select("Astrand37", "resi 1146-1146 & chain A ")
cmd.color ("green", "Astrand37")


cmd.select("Astrand38", "resi 1149-1149 & chain A ")
cmd.color ("orange", "Astrand38")


cmd.select("Astrand39", "resi 1152-1152 & chain A ")
cmd.color ("teal", "Astrand39")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
