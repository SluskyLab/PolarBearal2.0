from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2VDF.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 9-23 & chain A, resi 26-43 & chain A, resi 48-65 & chain A, resi 85-103 & chain A, resi 106-122 & chain A, resi 131-150 & chain A, resi 153-171 & chain A, resi 182-185 & chain A, resi 188-200 & chain A, resi 206-218 & chain A, resi 240-252 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[11.852650910902481,-5.779065078620374,-31.3140592151845])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
