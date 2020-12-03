from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3SAO.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 10-18 & chain A, resi 34-41 & chain A, resi 45-52 & chain A, resi 59-66 & chain A, resi 74-77 & chain A, resi 82-89 & chain A, resi 94-103 & chain A, resi 106-115 & chain A, resi 142-144 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[-13.967102915267734,5.012676502002732,-18.810308821061078])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
