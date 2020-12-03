from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3V8X.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 60-64 & chain A, resi 148-155 & chain A, resi 169-175 & chain A, resi 109-113 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[41.68891998291016,-51.54852005004883,44.43116012573242])
cmd.color ("white", "Centroid0")


cmd.select("Group1", "(resi 86-90 & chain A, resi 96-101 & chain A, )")
cmd.color ("red", "Group1")


cmd.pseudoatom ("Centroid1", pos=[33.83890862898393,-40.852636163884945,42.329363736239344])
cmd.color ("red", "Centroid1")


cmd.select("Group2", "(resi 188-197 & chain A, resi 202-213 & chain A, resi 216-228 & chain A, resi 305-314 & chain A, resi 317-319 & chain A, resi 325-341 & chain A, resi 394-415 & chain A, resi 425-447 & chain A, resi 465-488 & chain A, resi 494-527 & chain A, resi 547-560 & chain A, resi 257-260 & chain A, resi 277-284 & chain A, resi 246-250 & chain A, resi 575-592 & chain A, resi 596-610 & chain A, resi 620-632 & chain A, resi 638-649 & chain A, resi 673-686 & chain A, resi 689-712 & chain A, resi 717-742 & chain A, resi 756-771 & chain A, resi 775-779 & chain A, resi 790-798 & chain A, resi 804-813 & chain A, resi 822-826 & chain A, resi 832-836 & chain A, resi 845-855 & chain A, resi 860-867 & chain A, resi 906-914 & chain A, )")
cmd.color ("orange", "Group2")


cmd.pseudoatom ("Centroid2", pos=[35.08647638128286,-44.889496175428285,37.05835657490608])
cmd.color ("orange", "Centroid2")


cmd.select("Group3", "(resi 240-243 & chain A, resi 287-290 & chain A, )")
cmd.color ("purple", "Group3")


cmd.pseudoatom ("Centroid3", pos=[0.2553750015795231,-30.125624895095825,38.342124938964844])
cmd.color ("purple", "Centroid3")


cmd.select("Group4", "(resi 380-382 & chain A, resi 388-390 & chain A, )")
cmd.color ("yellow", "Group4")


cmd.pseudoatom ("Centroid4", pos=[4.639500002066295,-26.54633331298828,15.226333141326904])
cmd.color ("yellow", "Centroid4")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
