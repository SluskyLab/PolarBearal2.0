from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2L5P.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 51-60 & chain A, resi 75-80 & chain A, resi 86-94 & chain A, resi 97-107 & chain A, resi 113-116 & chain A, resi 128-136 & chain A, resi 140-148 & chain A, resi 153-161 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[-0.1261940160349234,-2.796970150363979,-0.2137164001756195])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
