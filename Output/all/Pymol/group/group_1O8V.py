from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1O8V.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 7-14 & chain A, resi 36-45 & chain A, resi 49-56 & chain A, resi 60-64 & chain A, resi 91-98 & chain A, resi 82-88 & chain A, resi 69-75 & chain A, resi 101-110 & chain A, resi 113-120 & chain A, resi 123-130 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[4.370705111286579,1.8621794885167708,10.449192323745825])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
