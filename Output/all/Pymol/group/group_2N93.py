from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2N93.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 6-13 & chain A, resi 40-44 & chain A, resi 49-53 & chain A, resi 59-62 & chain A, resi 121-129 & chain A, resi 112-118 & chain A, resi 103-106 & chain A, resi 88-94 & chain A, resi 76-84 & chain A, resi 66-71 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[29.741109430789948,34.438906103372574,31.65810939669609])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
