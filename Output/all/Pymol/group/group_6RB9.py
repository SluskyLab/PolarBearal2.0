from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/6RB9.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 57-60 & chain A, resi 202-204 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[81.49657113211495,109.42128535679409,117.29414367675781])
cmd.color ("white", "Centroid0")


cmd.select("Group1", "(resi 68-71 & chain A, resi 192-198 & chain A, resi 236-242 & chain A, )")
cmd.color ("red", "Group1")


cmd.pseudoatom ("Centroid1", pos=[81.44111039903429,113.87038972642686,96.80722215440538])
cmd.color ("red", "Centroid1")


cmd.select("Group2", "(resi 87-93 & chain A, resi 176-188 & chain A, resi 247-257 & chain A, resi 247-257 & chain B, resi 176-188 & chain B, resi 87-93 & chain B, resi 247-257 & chain C, resi 176-188 & chain C, resi 87-93 & chain C, resi 247-257 & chain D, resi 176-188 & chain D, resi 87-93 & chain D, resi 247-257 & chain E, resi 176-188 & chain E, resi 87-93 & chain E, resi 247-257 & chain F, resi 176-188 & chain F, resi 87-93 & chain F, resi 87-93 & chain G, resi 176-188 & chain G, resi 247-257 & chain G, )")
cmd.color ("orange", "Group2")


cmd.pseudoatom ("Centroid2", pos=[117.70003238801033,117.69995827389202,96.60161295244771])
cmd.color ("orange", "Centroid2")


cmd.select("Group3", "(resi 97-132 & chain A, resi 136-171 & chain A, resi 136-171 & chain B, resi 97-132 & chain B, resi 136-171 & chain C, resi 97-132 & chain C, resi 136-171 & chain D, resi 97-132 & chain D, resi 136-171 & chain E, resi 97-132 & chain E, resi 136-171 & chain F, resi 97-132 & chain F, resi 97-132 & chain G, resi 136-171 & chain G, )")
cmd.color ("purple", "Group3")


cmd.pseudoatom ("Centroid3", pos=[117.70001983642578,117.6999919376676,129.84498617384168])
cmd.color ("purple", "Centroid3")


cmd.select("Group4", "(resi 57-60 & chain B, resi 202-204 & chain B, )")
cmd.color ("yellow", "Group4")


cmd.pseudoatom ("Centroid4", pos=[88.65514264787946,140.84300013950892,117.29414367675781])
cmd.color ("yellow", "Centroid4")


cmd.select("Group5", "(resi 68-71 & chain B, resi 192-198 & chain B, resi 236-242 & chain B, )")
cmd.color ("green", "Group5")


cmd.pseudoatom ("Centroid5", pos=[92.09894349839952,143.66066657172308,96.80722215440538])
cmd.color ("green", "Centroid5")


cmd.select("Group6", "(resi 57-60 & chain C, resi 202-204 & chain C, )")
cmd.color ("cyan", "Group6")


cmd.pseudoatom ("Centroid6", pos=[117.68485695975167,154.83785792759485,117.29414367675781])
cmd.color ("cyan", "Centroid6")


cmd.select("Group7", "(resi 68-71 & chain C, resi 192-198 & chain C, resi 236-242 & chain C, )")
cmd.color ("blue", "Group7")


cmd.pseudoatom ("Centroid7", pos=[122.0347785949707,153.90183342827692,96.80722215440538])
cmd.color ("blue", "Centroid7")


cmd.select("Group8", "(resi 57-60 & chain D, resi 202-204 & chain D, )")
cmd.color ("purple", "Group8")


cmd.pseudoatom ("Centroid8", pos=[146.72614179338728,140.86671665736608,117.29414367675781])
cmd.color ("purple", "Centroid8")


cmd.select("Group9", "(resi 68-71 & chain D, resi 192-198 & chain D, resi 236-242 & chain D, )")
cmd.color ("red", "Group9")


cmd.pseudoatom ("Centroid9", pos=[148.70655568440756,136.88233396742078,96.80722215440538])
cmd.color ("red", "Centroid9")


cmd.select("Group10", "(resi 57-60 & chain E, resi 202-204 & chain E, )")
cmd.color ("orange", "Group10")


cmd.pseudoatom ("Centroid10", pos=[153.91000148228235,109.45071520124164,117.29414367675781])
cmd.color ("orange", "Centroid10")


cmd.select("Group11", "(resi 68-71 & chain E, resi 192-198 & chain E, resi 236-242 & chain E, )")
cmd.color ("yellow", "Group11")


cmd.pseudoatom ("Centroid11", pos=[152.02972073025174,105.41827816433377,96.80722215440538])
cmd.color ("yellow", "Centroid11")


cmd.select("Group12", "(resi 57-60 & chain F, resi 202-204 & chain F, )")
cmd.color ("green", "Group12")


cmd.pseudoatom ("Centroid12", pos=[133.82728576660156,84.24657222202846,117.29414367675781])
cmd.color ("green", "Centroid12")


cmd.select("Group13", "(resi 68-71 & chain F, resi 192-198 & chain F, resi 236-242 & chain F, )")
cmd.color ("cyan", "Group13")


cmd.pseudoatom ("Centroid13", pos=[129.50177764892578,83.20238918728299,96.80722215440538])
cmd.color ("cyan", "Centroid13")


cmd.select("Group14", "(resi 57-60 & chain G, resi 202-204 & chain G, )")
cmd.color ("blue", "Group14")


cmd.pseudoatom ("Centroid14", pos=[101.60028730119977,84.23328508649554,117.29414367675781])
cmd.color ("blue", "Centroid14")


cmd.select("Group15", "(resi 68-71 & chain G, resi 192-198 & chain G, resi 236-242 & chain G, )")
cmd.color ("purple", "Group15")


cmd.pseudoatom ("Centroid15", pos=[98.08711073133681,86.96399985419379,96.80722215440538])
cmd.color ("purple", "Centroid15")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
