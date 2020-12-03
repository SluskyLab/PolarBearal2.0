from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1AF6.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 2-14 & chain A, resi 40-53 & chain A, resi 56-68 & chain A, resi 80-89 & chain A, resi 99-105 & chain A, resi 124-132 & chain A, resi 138-148 & chain A, resi 167-179 & chain A, resi 186-196 & chain A, resi 211-223 & chain A, resi 226-236 & chain A, resi 267-280 & chain A, resi 284-296 & chain A, resi 303-316 & chain A, resi 320-333 & chain A, resi 339-352 & chain A, resi 362-373 & chain A, resi 408-420 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[19.746031925830668,42.89690421814244,82.12486308894745])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
