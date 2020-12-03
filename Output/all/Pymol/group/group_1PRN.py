from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1PRN.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 2-16 & chain A, resi 25-41 & chain A, resi 45-56 & chain A, resi 69-75 & chain A, resi 78-84 & chain A, resi 131-139 & chain A, resi 142-150 & chain A, resi 163-172 & chain A, resi 175-183 & chain A, resi 193-201 & chain A, resi 206-214 & chain A, resi 222-245 & chain A, resi 252-261 & chain A, resi 265-274 & chain A, resi 278-288 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[2.729273812934047,35.84302379971459,32.56968451681591])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
