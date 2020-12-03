from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4FSO.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 7-20 & chain A, resi 35-47 & chain A, resi 56-106 & chain A, resi 109-116 & chain A, resi 134-142 & chain A, resi 148-159 & chain A, resi 187-197 & chain A, resi 200-209 & chain A, resi 213-225 & chain A, resi 230-242 & chain A, resi 252-264 & chain A, resi 267-277 & chain A, resi 307-316 & chain A, resi 325-338 & chain A, resi 344-357 & chain A, resi 367-377 & chain A, resi 386-398 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[26.881714912218467,13.683107483540184,45.11846734875831])
cmd.color ("white", "Centroid0")


cmd.select("Group1", "(resi 123-125 & chain A, )")
cmd.color ("red", "Group1")


cmd.pseudoatom ("Centroid1", pos=[28.80733299255371,12.629000027974447,50.50800069173177])
cmd.color ("red", "Centroid1")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
