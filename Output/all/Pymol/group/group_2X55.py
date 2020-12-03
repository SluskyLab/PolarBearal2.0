from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2X55.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 14-32 & chain A, resi 39-62 & chain A, resi 65-74 & chain A, resi 97-122 & chain A, resi 126-144 & chain A, resi 164-185 & chain A, resi 188-208 & chain A, resi 213-236 & chain A, resi 239-250 & chain A, resi 275-292 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[-16.86019997956852,58.829769232334236,8.714989773738079])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
