from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1IFC.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 2-12 & chain A, resi 34-42 & chain A, resi 47-52 & chain A, resi 57-62 & chain A, resi 123-130 & chain A, resi 113-118 & chain A, resi 100-108 & chain A, resi 89-94 & chain A, resi 76-84 & chain A, resi 67-71 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[6.58519337669015,-0.857106636762619,7.665980026225249])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
