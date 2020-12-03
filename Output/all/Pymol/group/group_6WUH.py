from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/6WUH.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 30-32 & chain A, resi 492-494 & chain B, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[70.8350003560384,85.84066645304362,112.86333338419597])
cmd.color ("white", "Centroid0")


cmd.select("Group1", "(resi 51-54 & chain A, resi 87-90 & chain A, )")
cmd.color ("red", "Group1")


cmd.pseudoatom ("Centroid1", pos=[101.94637680053711,84.15537452697754,131.5998773574829])
cmd.color ("red", "Centroid1")


cmd.select("Group2", "(resi 179-182 & chain B, resi 206-210 & chain B, resi 215-217 & chain B, )")
cmd.color ("orange", "Group2")


cmd.pseudoatom ("Centroid2", pos=[101.0274175008138,95.74600028991699,105.30841700236003])
cmd.color ("orange", "Centroid2")


cmd.select("Group3", "(resi 273-277 & chain B, resi 290-297 & chain B, resi 310-316 & chain B, resi 336-344 & chain B, resi 395-402 & chain B, resi 420-423 & chain B, resi 426-428 & chain B, resi 469-477 & chain B, resi 486-489 & chain B, )")
cmd.color ("purple", "Group3")


cmd.pseudoatom ("Centroid3", pos=[81.98559623852111,83.22636855276008,95.72189451518811])
cmd.color ("purple", "Centroid3")


cmd.select("Group4", "(resi 54-56 & chain C, resi 63-65 & chain C, )")
cmd.color ("yellow", "Group4")


cmd.pseudoatom ("Centroid4", pos=[142.42400105794272,108.52483240763347,127.04599889119466])
cmd.color ("yellow", "Centroid4")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
