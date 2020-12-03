from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/6UCU.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 83-93 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 97-106 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 114-121 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 125-132 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 137-143 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 150-157 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 164-172 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 176-187 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 193-203 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 209-219 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 227-237 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 243-249 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 255-264 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 267-275 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 299-308 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 312-319 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 323-331 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 337-345 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("Astrand18", "resi 350-362 & chain A ")
cmd.color ("red", "Astrand18")


cmd.select("Istrand19", "resi 83-93 & chain I ")
cmd.color ("green", "Istrand19")


cmd.select("Istrand20", "resi 97-106 & chain I ")
cmd.color ("orange", "Istrand20")


cmd.select("Istrand21", "resi 114-121 & chain I ")
cmd.color ("teal", "Istrand21")


cmd.select("Istrand22", "resi 125-132 & chain I ")
cmd.color ("yellow", "Istrand22")


cmd.select("Istrand23", "resi 137-143 & chain I ")
cmd.color ("blue", "Istrand23")


cmd.select("Istrand24", "resi 150-157 & chain I ")
cmd.color ("red", "Istrand24")


cmd.select("Istrand25", "resi 164-172 & chain I ")
cmd.color ("green", "Istrand25")


cmd.select("Istrand26", "resi 176-187 & chain I ")
cmd.color ("orange", "Istrand26")


cmd.select("Istrand27", "resi 193-203 & chain I ")
cmd.color ("teal", "Istrand27")


cmd.select("Istrand28", "resi 209-219 & chain I ")
cmd.color ("yellow", "Istrand28")


cmd.select("Istrand29", "resi 227-237 & chain I ")
cmd.color ("blue", "Istrand29")


cmd.select("Istrand30", "resi 243-249 & chain I ")
cmd.color ("red", "Istrand30")


cmd.select("Istrand31", "resi 255-264 & chain I ")
cmd.color ("green", "Istrand31")


cmd.select("Istrand32", "resi 267-275 & chain I ")
cmd.color ("orange", "Istrand32")


cmd.select("Istrand33", "resi 299-308 & chain I ")
cmd.color ("teal", "Istrand33")


cmd.select("Istrand34", "resi 312-319 & chain I ")
cmd.color ("yellow", "Istrand34")


cmd.select("Istrand35", "resi 323-331 & chain I ")
cmd.color ("blue", "Istrand35")


cmd.select("Istrand36", "resi 337-345 & chain I ")
cmd.color ("red", "Istrand36")


cmd.select("Istrand37", "resi 350-362 & chain I ")
cmd.color ("green", "Istrand37")


cmd.select("barrel", "Astrand* or Istrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
