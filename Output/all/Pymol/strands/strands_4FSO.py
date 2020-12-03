from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4FSO.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 7-20 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 35-47 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 56-106 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 109-116 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 119-120 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 123-125 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 134-142 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 148-159 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 167-168 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 187-197 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 200-209 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 213-225 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 230-242 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 252-264 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 267-277 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 288-289 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 307-316 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 325-338 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("Astrand18", "resi 344-357 & chain A ")
cmd.color ("red", "Astrand18")


cmd.select("Astrand19", "resi 367-377 & chain A ")
cmd.color ("green", "Astrand19")


cmd.select("Astrand20", "resi 386-398 & chain A ")
cmd.color ("orange", "Astrand20")


cmd.select("Bstrand21", "resi 7-20 & chain B ")
cmd.color ("teal", "Bstrand21")


cmd.select("Bstrand22", "resi 36-47 & chain B ")
cmd.color ("yellow", "Bstrand22")


cmd.select("Bstrand23", "resi 55-65 & chain B ")
cmd.color ("blue", "Bstrand23")


cmd.select("Bstrand24", "resi 96-106 & chain B ")
cmd.color ("red", "Bstrand24")


cmd.select("Bstrand25", "resi 109-116 & chain B ")
cmd.color ("green", "Bstrand25")


cmd.select("Bstrand26", "resi 124-125 & chain B ")
cmd.color ("orange", "Bstrand26")


cmd.select("Bstrand27", "resi 135-142 & chain B ")
cmd.color ("teal", "Bstrand27")


cmd.select("Bstrand28", "resi 148-158 & chain B ")
cmd.color ("yellow", "Bstrand28")


cmd.select("Bstrand29", "resi 167-168 & chain B ")
cmd.color ("blue", "Bstrand29")


cmd.select("Bstrand30", "resi 187-197 & chain B ")
cmd.color ("red", "Bstrand30")


cmd.select("Bstrand31", "resi 200-209 & chain B ")
cmd.color ("green", "Bstrand31")


cmd.select("Bstrand32", "resi 213-226 & chain B ")
cmd.color ("orange", "Bstrand32")


cmd.select("Bstrand33", "resi 229-242 & chain B ")
cmd.color ("teal", "Bstrand33")


cmd.select("Bstrand34", "resi 252-264 & chain B ")
cmd.color ("yellow", "Bstrand34")


cmd.select("Bstrand35", "resi 267-277 & chain B ")
cmd.color ("blue", "Bstrand35")


cmd.select("Bstrand36", "resi 288-289 & chain B ")
cmd.color ("red", "Bstrand36")


cmd.select("Bstrand37", "resi 307-316 & chain B ")
cmd.color ("green", "Bstrand37")


cmd.select("Bstrand38", "resi 325-338 & chain B ")
cmd.color ("orange", "Bstrand38")


cmd.select("Bstrand39", "resi 344-357 & chain B ")
cmd.color ("teal", "Bstrand39")


cmd.select("Bstrand40", "resi 367-377 & chain B ")
cmd.color ("yellow", "Bstrand40")


cmd.select("Bstrand41", "resi 386-395 & chain B ")
cmd.color ("blue", "Bstrand41")


cmd.select("barrel", "Astrand* or Bstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
