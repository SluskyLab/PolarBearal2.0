from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4AFK.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 42-54 & chain A, resi 66-81 & chain A, resi 84-95 & chain A, resi 124-135 & chain A, resi 144-154 & chain A, resi 162-173 & chain A, resi 177-185 & chain A, resi 204-216 & chain A, resi 219-230 & chain A, resi 248-261 & chain A, resi 272-292 & chain A, resi 297-319 & chain A, resi 324-333 & chain A, resi 377-388 & chain A, resi 392-403 & chain A, resi 425-437 & chain A, resi 457-467 & chain A, resi 479-489 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[18.06577587647835,-4.131095414710737,30.97690044065234])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
