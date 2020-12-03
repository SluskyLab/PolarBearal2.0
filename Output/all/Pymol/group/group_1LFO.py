from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1LFO.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 6-8 & chain A, resi 35-44 & chain A, resi 47-54 & chain A, resi 57-64 & chain A, resi 67-73 & chain A, resi 78-86 & chain A, resi 90-95 & chain A, resi 98-105 & chain A, resi 108-115 & chain A, resi 118-125 & chain A, resi 11-13 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[26.46694797664494,22.91802594568822,35.088610240391326])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
