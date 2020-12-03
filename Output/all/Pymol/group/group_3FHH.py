from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3FHH.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 11-13 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[0.14566667874654135,49.77466710408529,26.678333282470703])
cmd.color ("white", "Centroid0")


cmd.select("Group1", "(resi 18-26 & chain A, resi 97-104 & chain A, resi 89-93 & chain A, resi 118-126 & chain A, resi 71-75 & chain A, )")
cmd.color ("red", "Group1")


cmd.pseudoatom ("Centroid1", pos=[3.2014999836683273,40.75880575180054,37.717583391401504])
cmd.color ("red", "Centroid1")


cmd.select("Group2", "(resi 48-53 & chain A, resi 60-63 & chain A, )")
cmd.color ("orange", "Group2")


cmd.pseudoatom ("Centroid2", pos=[-1.676800012588501,32.29710025787354,48.52050018310547])
cmd.color ("orange", "Centroid2")


cmd.select("Group3", "(resi 135-146 & chain A, resi 151-162 & chain A, resi 165-181 & chain A, resi 185-202 & chain A, resi 208-223 & chain A, resi 240-256 & chain A, resi 263-278 & chain A, resi 287-303 & chain A, resi 307-326 & chain A, resi 341-359 & chain A, resi 362-379 & chain A, resi 385-401 & chain A, resi 404-415 & chain A, resi 446-464 & chain A, resi 470-483 & chain A, resi 496-518 & chain A, resi 435-442 & chain A, resi 429-432 & chain A, resi 487-491 & chain A, resi 521-533 & chain A, resi 539-545 & chain A, resi 548-557 & chain A, resi 562-571 & chain A, resi 587-599 & chain A, resi 605-612 & chain A, resi 630-639 & chain A, )")
cmd.color ("purple", "Group3")


cmd.pseudoatom ("Centroid3", pos=[2.162473262027955,37.332822561012186,38.26078589264775])
cmd.color ("purple", "Centroid3")


cmd.select("Group4", "(resi 574-584 & chain A, )")
cmd.color ("yellow", "Group4")


cmd.pseudoatom ("Centroid4", pos=[-12.906875014305115,28.73437476158142,57.95875024795532])
cmd.color ("yellow", "Centroid4")


cmd.select("Group5", "(resi 618-620 & chain A, resi 625-627 & chain A, )")
cmd.color ("green", "Group5")


cmd.pseudoatom ("Centroid5", pos=[-1.6020000154773395,33.95799986521403,62.25483385721842])
cmd.color ("green", "Centroid5")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
