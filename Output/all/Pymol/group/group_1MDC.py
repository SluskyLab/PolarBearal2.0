from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1MDC.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 7-13 & chain A, resi 37-43 & chain A, resi 48-53 & chain A, resi 58-63 & chain A, resi 124-130 & chain A, resi 112-117 & chain A, resi 100-107 & chain A, resi 90-95 & chain A, resi 77-85 & chain A, resi 68-72 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[15.067029416561127,22.247102905722226,3.1089411710991577])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
