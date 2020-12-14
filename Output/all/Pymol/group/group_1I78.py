from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1I78.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 12-31 & chain A, resi 37-58 & chain A, resi 64-73 & chain A, resi 77-85 & chain A, resi 97-122 & chain A, resi 126-144 & chain A, resi 147-149 & chain A, resi 169-189 & chain A, resi 192-213 & chain A, resi 219-242 & chain A, resi 245-267 & chain A, resi 272-296 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[25.93373657124383,56.52446873698916,12.985330390411296])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
