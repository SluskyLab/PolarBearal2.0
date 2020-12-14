from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4FT6.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 8-22 & chain A, resi 31-44 & chain A, resi 52-67 & chain A, resi 89-101 & chain A, resi 104-111 & chain A, resi 129-137 & chain A, resi 143-154 & chain A, resi 177-186 & chain A, resi 191-200 & chain A, resi 204-217 & chain A, resi 220-233 & chain A, resi 243-255 & chain A, resi 258-268 & chain A, resi 298-307 & chain A, resi 316-328 & chain A, resi 336-348 & chain A, resi 358-368 & chain A, resi 374-386 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[-55.61025105654921,15.042584495320725,-30.893931445465785])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
