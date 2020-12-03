from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4Y25.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 518-530 & chain A, resi 540-547 & chain A, resi 555-565 & chain A, resi 575-586 & chain A, resi 589-599 & chain A, resi 604-615 & chain A, resi 620-628 & chain A, resi 644-654 & chain A, resi 659-670 & chain A, resi 675-689 & chain A, resi 693-697 & chain A, resi 700-705 & chain A, resi 718-735 & chain A, resi 738-753 & chain A, resi 757-772 & chain A, resi 776-788 & chain A, resi 793-807 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[-185.59997024911965,288.66444885554574,192.43084754380098])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
