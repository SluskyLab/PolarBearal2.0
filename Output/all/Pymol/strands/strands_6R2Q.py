from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/6R2Q.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Bstrand0", "resi 52-63 & chain B ")
cmd.color ("red", "Bstrand0")


cmd.select("Bstrand1", "resi 85-88 & chain B ")
cmd.color ("green", "Bstrand1")


cmd.select("Bstrand2", "resi 99-102 & chain B ")
cmd.color ("orange", "Bstrand2")


cmd.select("Bstrand3", "resi 110-113 & chain B ")
cmd.color ("teal", "Bstrand3")


cmd.select("Bstrand4", "resi 121-135 & chain B ")
cmd.color ("yellow", "Bstrand4")


cmd.select("Bstrand5", "resi 138-140 & chain B ")
cmd.color ("blue", "Bstrand5")


cmd.select("Bstrand6", "resi 173-191 & chain B ")
cmd.color ("red", "Bstrand6")


cmd.select("Bstrand7", "resi 196-216 & chain B ")
cmd.color ("green", "Bstrand7")


cmd.select("Bstrand8", "resi 221-242 & chain B ")
cmd.color ("orange", "Bstrand8")


cmd.select("Bstrand9", "resi 246-259 & chain B ")
cmd.color ("teal", "Bstrand9")


cmd.select("Bstrand10", "resi 263-267 & chain B ")
cmd.color ("yellow", "Bstrand10")


cmd.select("Bstrand11", "resi 279-283 & chain B ")
cmd.color ("blue", "Bstrand11")


cmd.select("Bstrand12", "resi 288-299 & chain B ")
cmd.color ("red", "Bstrand12")


cmd.select("Bstrand13", "resi 304-317 & chain B ")
cmd.color ("green", "Bstrand13")


cmd.select("Bstrand14", "resi 337-350 & chain B ")
cmd.color ("orange", "Bstrand14")


cmd.select("Bstrand15", "resi 356-369 & chain B ")
cmd.color ("teal", "Bstrand15")


cmd.select("Bstrand16", "resi 375-378 & chain B ")
cmd.color ("yellow", "Bstrand16")


cmd.select("Bstrand17", "resi 387-390 & chain B ")
cmd.color ("blue", "Bstrand17")


cmd.select("Bstrand18", "resi 396-407 & chain B ")
cmd.color ("red", "Bstrand18")


cmd.select("Bstrand19", "resi 413-425 & chain B ")
cmd.color ("green", "Bstrand19")


cmd.select("Bstrand20", "resi 433-445 & chain B ")
cmd.color ("orange", "Bstrand20")


cmd.select("Bstrand21", "resi 452-464 & chain B ")
cmd.color ("teal", "Bstrand21")


cmd.select("Bstrand22", "resi 489-500 & chain B ")
cmd.color ("yellow", "Bstrand22")


cmd.select("Bstrand23", "resi 506-518 & chain B ")
cmd.color ("blue", "Bstrand23")


cmd.select("Bstrand24", "resi 525-540 & chain B ")
cmd.color ("red", "Bstrand24")


cmd.select("Bstrand25", "resi 546-563 & chain B ")
cmd.color ("green", "Bstrand25")


cmd.select("Bstrand26", "resi 572-590 & chain B ")
cmd.color ("orange", "Bstrand26")


cmd.select("Bstrand27", "resi 598-621 & chain B ")
cmd.color ("teal", "Bstrand27")


cmd.select("Bstrand28", "resi 625-638 & chain B ")
cmd.color ("yellow", "Bstrand28")


cmd.select("Bstrand29", "resi 644-659 & chain B ")
cmd.color ("blue", "Bstrand29")


cmd.select("Bstrand30", "resi 680-694 & chain B ")
cmd.color ("red", "Bstrand30")


cmd.select("Cstrand31", "resi 50-59 & chain C ")
cmd.color ("green", "Cstrand31")


cmd.select("Cstrand32", "resi 62-70 & chain C ")
cmd.color ("orange", "Cstrand32")


cmd.select("Cstrand33", "resi 82-91 & chain C ")
cmd.color ("teal", "Cstrand33")


cmd.select("Cstrand34", "resi 103-113 & chain C ")
cmd.color ("yellow", "Cstrand34")


cmd.select("Cstrand35", "resi 121-124 & chain C ")
cmd.color ("blue", "Cstrand35")


cmd.select("Cstrand36", "resi 129-133 & chain C ")
cmd.color ("red", "Cstrand36")


cmd.select("Cstrand37", "resi 152-158 & chain C ")
cmd.color ("green", "Cstrand37")


cmd.select("Cstrand38", "resi 172-178 & chain C ")
cmd.color ("orange", "Cstrand38")


cmd.select("Cstrand39", "resi 331-338 & chain C ")
cmd.color ("teal", "Cstrand39")


cmd.select("Cstrand40", "resi 344-351 & chain C ")
cmd.color ("yellow", "Cstrand40")


cmd.select("Cstrand41", "resi 367-376 & chain C ")
cmd.color ("blue", "Cstrand41")


cmd.select("Cstrand42", "resi 396-402 & chain C ")
cmd.color ("red", "Cstrand42")


cmd.select("Cstrand43", "resi 411-413 & chain C ")
cmd.color ("green", "Cstrand43")


cmd.select("Cstrand44", "resi 416-420 & chain C ")
cmd.color ("orange", "Cstrand44")


cmd.select("Cstrand45", "resi 433-443 & chain C ")
cmd.color ("teal", "Cstrand45")


cmd.select("Cstrand46", "resi 458-460 & chain C ")
cmd.color ("yellow", "Cstrand46")


cmd.select("Cstrand47", "resi 464-469 & chain C ")
cmd.color ("blue", "Cstrand47")


cmd.select("Cstrand48", "resi 583-586 & chain C ")
cmd.color ("red", "Cstrand48")


cmd.select("Cstrand49", "resi 589-591 & chain C ")
cmd.color ("green", "Cstrand49")


cmd.select("barrel", "Bstrand* or Cstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
