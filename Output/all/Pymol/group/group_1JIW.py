from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1JIW.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 13-19 & chain I, resi 25-35 & chain I, resi 40-45 & chain I, resi 60-64 & chain I, resi 67-71 & chain I, resi 77-85 & chain I, resi 88-92 & chain I, resi 98-103 & chain I, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[48.817740828902636,49.51346291436089,-31.96333348309552])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
