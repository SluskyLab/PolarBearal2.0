from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1FEP.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 28-32 & chain A, resi 121-126 & chain A, resi 140-145 & chain A, resi 82-86 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[35.83763651414351,33.072818062522195,59.67531845786355])
cmd.color ("white", "Centroid0")


cmd.select("Group1", "(resi 55-59 & chain A, resi 70-74 & chain A, )")
cmd.color ("red", "Group1")


cmd.pseudoatom ("Centroid1", pos=[34.033800506591795,32.84889965057373,46.09909934997559])
cmd.color ("red", "Centroid1")


cmd.select("Group2", "(resi 154-161 & chain A, resi 172-182 & chain A, resi 187-198 & chain A, resi 227-239 & chain A, resi 245-259 & chain A, resi 282-296 & chain A, resi 302-316 & chain A, resi 338-345 & chain A, resi 348-356 & chain A, resi 360-373 & chain A, resi 407-417 & chain A, resi 424-435 & chain A, resi 439-450 & chain A, resi 456-459 & chain A, resi 462-467 & chain A, resi 505-518 & chain A, resi 521-538 & chain A, resi 552-571 & chain A, resi 495-497 & chain A, resi 479-481 & chain A, resi 581-592 & chain A, resi 606-611 & chain A, resi 623-628 & chain A, resi 654-664 & chain A, resi 669-676 & chain A, resi 715-717 & chain A, resi 720-723 & chain A, )")
cmd.color ("orange", "Group2")


cmd.pseudoatom ("Centroid2", pos=[35.57717947558169,29.238783962123996,58.57108420068091])
cmd.color ("orange", "Centroid2")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
