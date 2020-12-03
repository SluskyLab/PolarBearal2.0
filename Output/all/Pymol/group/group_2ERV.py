from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2ERV.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 2-9 & chain A, resi 15-24 & chain A, resi 35-48 & chain A, resi 29-32 & chain A, resi 57-70 & chain A, resi 75-88 & chain A, resi 102-114 & chain A, resi 119-128 & chain A, resi 139-149 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[16.187673427620712,22.044255027965622,22.13253066856034])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
