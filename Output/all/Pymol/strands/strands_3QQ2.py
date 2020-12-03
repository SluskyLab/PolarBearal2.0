from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3QQ2.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 748-761 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 768-785 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 788-805 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 809-826 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 830-848 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 854-876 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 881-899 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 904-909 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 912-928 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 933-947 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 967-978 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 982-993 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 996-1008 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Bstrand13", "resi 748-761 & chain B ")
cmd.color ("green", "Bstrand13")


cmd.select("Bstrand14", "resi 768-785 & chain B ")
cmd.color ("orange", "Bstrand14")


cmd.select("Bstrand15", "resi 788-806 & chain B ")
cmd.color ("teal", "Bstrand15")


cmd.select("Bstrand16", "resi 810-826 & chain B ")
cmd.color ("yellow", "Bstrand16")


cmd.select("Bstrand17", "resi 831-849 & chain B ")
cmd.color ("blue", "Bstrand17")


cmd.select("Bstrand18", "resi 853-876 & chain B ")
cmd.color ("red", "Bstrand18")


cmd.select("Bstrand19", "resi 880-928 & chain B ")
cmd.color ("green", "Bstrand19")


cmd.select("Bstrand20", "resi 932-947 & chain B ")
cmd.color ("orange", "Bstrand20")


cmd.select("Bstrand21", "resi 964-977 & chain B ")
cmd.color ("teal", "Bstrand21")


cmd.select("Bstrand22", "resi 983-993 & chain B ")
cmd.color ("yellow", "Bstrand22")


cmd.select("Bstrand23", "resi 996-1007 & chain B ")
cmd.color ("blue", "Bstrand23")


cmd.select("Cstrand24", "resi 748-785 & chain C ")
cmd.color ("red", "Cstrand24")


cmd.select("Cstrand25", "resi 788-805 & chain C ")
cmd.color ("green", "Cstrand25")


cmd.select("Cstrand26", "resi 809-826 & chain C ")
cmd.color ("orange", "Cstrand26")


cmd.select("Cstrand27", "resi 831-848 & chain C ")
cmd.color ("teal", "Cstrand27")


cmd.select("Cstrand28", "resi 854-876 & chain C ")
cmd.color ("yellow", "Cstrand28")


cmd.select("Cstrand29", "resi 881-900 & chain C ")
cmd.color ("blue", "Cstrand29")


cmd.select("Cstrand30", "resi 903-928 & chain C ")
cmd.color ("red", "Cstrand30")


cmd.select("Cstrand31", "resi 933-947 & chain C ")
cmd.color ("green", "Cstrand31")


cmd.select("Cstrand32", "resi 965-977 & chain C ")
cmd.color ("orange", "Cstrand32")


cmd.select("Cstrand33", "resi 982-993 & chain C ")
cmd.color ("teal", "Cstrand33")


cmd.select("Cstrand34", "resi 996-1008 & chain C ")
cmd.color ("yellow", "Cstrand34")


cmd.select("barrel", "Astrand* or Bstrand* or Cstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
