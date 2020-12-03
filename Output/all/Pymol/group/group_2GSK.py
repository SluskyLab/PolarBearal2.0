from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2GSK.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 6-11 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[28.048333168029785,-0.25349996487299603,23.414499918619793])
cmd.color ("white", "Centroid0")


cmd.select("Group1", "(resi 26-30 & chain A, resi 106-111 & chain A, resi 125-130 & chain A, resi 76-80 & chain A, )")
cmd.color ("red", "Group1")


cmd.pseudoatom ("Centroid1", pos=[29.391545555808328,4.3261363191360775,-6.643409143794667])
cmd.color ("red", "Centroid1")


cmd.select("Group2", "(resi 52-56 & chain A, resi 64-68 & chain A, )")
cmd.color ("orange", "Group2")


cmd.pseudoatom ("Centroid2", pos=[32.30459995269776,-2.995099937450141,-17.995699977874757])
cmd.color ("orange", "Centroid2")


cmd.select("Group3", "(resi 137-145 & chain A, resi 149-161 & chain A, resi 164-178 & chain A, resi 195-209 & chain A, resi 214-228 & chain A, resi 242-257 & chain A, resi 261-277 & chain A, resi 289-305 & chain A, resi 309-322 & chain A, resi 333-348 & chain A, resi 351-362 & chain A, resi 366-380 & chain A, resi 383-394 & chain A, resi 413-426 & chain A, resi 429-441 & chain A, resi 459-472 & chain A, resi 475-488 & chain A, resi 501-511 & chain A, resi 514-523 & chain A, resi 544-554 & chain A, resi 559-566 & chain A, resi 585-593 & chain A, )")
cmd.color ("purple", "Group3")


cmd.pseudoatom ("Centroid3", pos=[31.605096581886556,4.861634466026364,-6.727375893731569])
cmd.color ("purple", "Centroid3")


cmd.select("Group4", "(resi 444-447 & chain A, resi 452-455 & chain A, )")
cmd.color ("yellow", "Group4")


cmd.pseudoatom ("Centroid4", pos=[24.113250255584717,5.67550003528595,-34.20674991607666])
cmd.color ("yellow", "Centroid4")


cmd.select("Group5", "(resi 526-530 & chain A, resi 537-541 & chain A, )")
cmd.color ("green", "Group5")


cmd.pseudoatom ("Centroid5", pos=[31.3875,-11.72639994621277,-31.273600006103514])
cmd.color ("green", "Centroid5")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
