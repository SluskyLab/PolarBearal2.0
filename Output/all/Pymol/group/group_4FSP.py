from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4FSP.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 8-22 & chain A, resi 31-43 & chain A, resi 51-64 & chain A, resi 89-100 & chain A, resi 103-110 & chain A, resi 129-136 & chain A, resi 142-152 & chain A, resi 181-191 & chain A, resi 194-203 & chain A, resi 207-219 & chain A, resi 224-236 & chain A, resi 246-257 & chain A, resi 262-272 & chain A, resi 302-311 & chain A, resi 320-330 & chain A, resi 342-352 & chain A, resi 362-372 & chain A, resi 378-390 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[-28.01925125674925,23.795072504863647,-2.5898985222053987])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
