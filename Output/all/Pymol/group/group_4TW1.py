from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4TW1.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 19-29 & chain A, resi 34-44 & chain A, resi 51-62 & chain A, resi 231-237 & chain A, resi 97-103 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[-61.4331251780192,53.59510429700216,17.245687504609425])
cmd.color ("white", "Centroid0")


cmd.select("Group1", "(resi 75-90 & chain A, resi 165-172 & chain A, resi 139-157 & chain A, resi 111-123 & chain A, resi 244-265 & chain A, resi 268-272 & chain A, resi 275-291 & chain A, resi 297-302 & chain A, resi 136-148 & chain B, resi 159-180 & chain B, resi 188-200 & chain B, resi 103-118 & chain B, resi 92-95 & chain B, resi 203-206 & chain B, resi 259-275 & chain B, resi 285-302 & chain B, resi 307-316 & chain B, resi 110-125 & chain C, resi 135-149 & chain C, resi 138-152 & chain D, resi 158-173 & chain D, resi 111-128 & chain E, resi 131-149 & chain E, resi 138-149 & chain F, resi 159-180 & chain F, resi 188-200 & chain F, resi 103-118 & chain F, resi 92-95 & chain F, resi 203-206 & chain F, resi 259-275 & chain F, resi 285-302 & chain F, resi 307-316 & chain F, resi 110-127 & chain G, resi 132-137 & chain G, resi 138-152 & chain H, resi 157-173 & chain H, )")
cmd.color ("red", "Group1")


cmd.pseudoatom ("Centroid1", pos=[-46.24649399205258,39.340433182865986,-16.382374459432686])
cmd.color ("red", "Centroid1")


cmd.select("Group2", "(resi 175-177 & chain A, resi 180-182 & chain A, )")
cmd.color ("orange", "Group2")


cmd.pseudoatom ("Centroid2", pos=[-35.71483357747396,54.93866729736328,-7.731333414713542])
cmd.color ("orange", "Centroid2")


cmd.select("Group3", "(resi 45-55 & chain B, resi 60-70 & chain B, resi 77-88 & chain B, resi 247-253 & chain B, resi 123-129 & chain B, )")
cmd.color ("purple", "Group3")


cmd.pseudoatom ("Centroid3", pos=[-74.78552103042603,63.575312534968056,-0.9948124955408275])
cmd.color ("purple", "Centroid3")


cmd.select("Group4", "(resi 19-29 & chain C, resi 34-44 & chain C, resi 51-62 & chain C, resi 231-237 & chain C, resi 97-103 & chain C, )")
cmd.color ("yellow", "Group4")


cmd.pseudoatom ("Centroid4", pos=[-87.28189579645793,55.099000215530396,-20.431458443403244])
cmd.color ("yellow", "Centroid4")


cmd.select("Group5", "(resi 75-90 & chain C, resi 165-172 & chain C, resi 153-157 & chain C, resi 244-263 & chain C, resi 270-280 & chain C, resi 283-291 & chain C, resi 297-303 & chain C, )")
cmd.color ("green", "Group5")


cmd.pseudoatom ("Centroid5", pos=[-77.09565815172698,60.4781840474982,-35.76963153638338])
cmd.color ("green", "Centroid5")


cmd.select("Group6", "(resi 175-177 & chain C, resi 180-182 & chain C, )")
cmd.color ("cyan", "Group6")


cmd.pseudoatom ("Centroid6", pos=[-56.78800010681152,51.880833307902016,-39.13083267211914])
cmd.color ("cyan", "Centroid6")


cmd.select("Group7", "(resi 48-55 & chain D, resi 60-69 & chain D, resi 77-83 & chain D, resi 247-253 & chain D, resi 123-129 & chain D, )")
cmd.color ("blue", "Group7")


cmd.pseudoatom ("Centroid7", pos=[-91.7459744184445,33.58076917208158,-30.10487194550343])
cmd.color ("blue", "Centroid7")


cmd.select("Group8", "(resi 92-95 & chain D, resi 103-106 & chain D, resi 259-275 & chain D, resi 110-117 & chain D, resi 188-200 & chain D, resi 176-180 & chain D, resi 203-206 & chain D, resi 285-302 & chain D, resi 307-316 & chain D, )")
cmd.color ("purple", "Group8")


cmd.pseudoatom ("Centroid8", pos=[-81.49816866955125,31.027469749910285,-44.73114461783903])
cmd.color ("purple", "Centroid8")


cmd.select("Group9", "(resi 19-29 & chain E, resi 34-44 & chain E, resi 51-62 & chain E, resi 231-237 & chain E, resi 97-103 & chain E, )")
cmd.color ("red", "Group9")


cmd.pseudoatom ("Centroid9", pos=[-85.17443752288818,9.468000092854103,-23.547291616598766])
cmd.color ("red", "Centroid9")


cmd.select("Group10", "(resi 75-90 & chain E, resi 165-172 & chain E, resi 153-158 & chain E, resi 244-263 & chain E, resi 270-276 & chain E, resi 281-291 & chain E, resi 296-303 & chain E, )")
cmd.color ("orange", "Group10")


cmd.pseudoatom ("Centroid10", pos=[-73.16938174398322,3.9745657816529274,-36.157236977627406])
cmd.color ("orange", "Centroid10")


cmd.select("Group11", "(resi 175-177 & chain E, resi 180-182 & chain E, )")
cmd.color ("yellow", "Group11")


cmd.pseudoatom ("Centroid11", pos=[-52.67099952697754,13.888000011444092,-37.679500579833984])
cmd.color ("yellow", "Centroid11")


cmd.select("Group12", "(resi 45-47 & chain F, resi 60-70 & chain F, resi 50-55 & chain F, resi 77-88 & chain F, resi 247-253 & chain F, resi 123-129 & chain F, )")
cmd.color ("green", "Group12")


cmd.pseudoatom ("Centroid12", pos=[-71.70502165089484,-0.465760862738218,-5.557869581262702])
cmd.color ("green", "Centroid12")


cmd.select("Group13", "(resi 19-29 & chain G, resi 34-44 & chain G, resi 51-57 & chain G, resi 60-62 & chain G, resi 231-237 & chain G, resi 97-103 & chain G, )")
cmd.color ("cyan", "Group13")


cmd.pseudoatom ("Centroid13", pos=[-59.706717449685804,7.8427391572167044,14.38665216902028])
cmd.color ("cyan", "Centroid13")


cmd.select("Group14", "(resi 75-90 & chain G, resi 165-172 & chain G, resi 153-157 & chain G, resi 244-265 & chain G, resi 268-291 & chain G, resi 296-303 & chain G, )")
cmd.color ("blue", "Group14")


cmd.pseudoatom ("Centroid14", pos=[-39.43314453492682,5.590180732399585,9.899795277201267])
cmd.color ("blue", "Centroid14")


cmd.select("Group15", "(resi 175-177 & chain G, resi 180-182 & chain G, )")
cmd.color ("purple", "Group15")


cmd.pseudoatom ("Centroid15", pos=[-31.316500345865887,16.649666627248127,-5.9746666351954145])
cmd.color ("purple", "Centroid15")


cmd.select("Group16", "(resi 45-55 & chain H, resi 60-70 & chain H, resi 77-88 & chain H, resi 247-253 & chain H, resi 123-129 & chain H, )")
cmd.color ("red", "Group16")


cmd.pseudoatom ("Centroid16", pos=[-54.93149995803833,30.61914587020874,23.381708244482677])
cmd.color ("red", "Centroid16")


cmd.select("Group17", "(resi 92-95 & chain H, resi 103-118 & chain H, resi 188-200 & chain H, resi 176-180 & chain H, resi 203-206 & chain H, resi 259-275 & chain H, resi 285-302 & chain H, resi 307-316 & chain H, )")
cmd.color ("orange", "Group17")


cmd.pseudoatom ("Centroid17", pos=[-37.743793092924975,34.807333299483375,20.08274706615799])
cmd.color ("orange", "Centroid17")


cmd.select("Group18", "(resi 19-29 & chain I, resi 34-44 & chain I, resi 51-62 & chain I, resi 231-237 & chain I, resi 97-103 & chain I, )")
cmd.color ("yellow", "Group18")


cmd.pseudoatom ("Centroid18", pos=[27.795666615168255,67.19872879981995,-72.58558320999146])
cmd.color ("yellow", "Centroid18")


cmd.select("Group19", "(resi 75-90 & chain I, resi 165-172 & chain I, resi 135-157 & chain I, resi 110-123 & chain I, resi 244-265 & chain I, resi 268-291 & chain I, resi 296-303 & chain I, resi 131-147 & chain J, resi 154-168 & chain J, resi 111-125 & chain K, resi 136-157 & chain K, resi 165-172 & chain K, resi 75-90 & chain K, resi 244-263 & chain K, resi 270-291 & chain K, resi 297-303 & chain K, resi 136-151 & chain L, resi 157-173 & chain L, resi 111-127 & chain M, resi 133-157 & chain M, resi 165-172 & chain M, resi 75-90 & chain M, resi 244-265 & chain M, resi 268-291 & chain M, resi 296-302 & chain M, resi 136-152 & chain N, resi 156-173 & chain N, resi 111-126 & chain O, resi 134-157 & chain O, resi 165-172 & chain O, resi 75-90 & chain O, resi 244-265 & chain O, resi 268-291 & chain O, resi 296-302 & chain O, resi 136-151 & chain P, resi 157-180 & chain P, resi 188-200 & chain P, resi 103-117 & chain P, resi 92-95 & chain P, resi 203-206 & chain P, resi 259-275 & chain P, resi 285-302 & chain P, resi 307-316 & chain P, )")
cmd.color ("green", "Group19")


cmd.pseudoatom ("Centroid19", pos=[-5.074522026396655,46.206215547184705,-82.18715237592322])
cmd.color ("green", "Centroid19")


cmd.select("Group20", "(resi 175-177 & chain I, resi 180-182 & chain I, )")
cmd.color ("cyan", "Group20")


cmd.pseudoatom ("Centroid20", pos=[-4.39133336643378,58.31716664632162,-59.459999084472656])
cmd.color ("cyan", "Centroid20")


cmd.select("Group21", "(resi 40-50 & chain J, resi 55-65 & chain J, resi 72-81 & chain J, resi 242-248 & chain J, resi 118-124 & chain J, )")
cmd.color ("blue", "Group21")


cmd.pseudoatom ("Centroid21", pos=[33.83236955559772,45.27541322293489,-64.53117370605469])
cmd.color ("blue", "Centroid21")


cmd.select("Group22", "(resi 88-90 & chain J, resi 98-100 & chain J, resi 254-270 & chain J, resi 103-113 & chain J, resi 183-195 & chain J, resi 171-175 & chain J, resi 198-201 & chain J, resi 280-297 & chain J, resi 302-311 & chain J, )")
cmd.color ("purple", "Group22")


cmd.pseudoatom ("Centroid22", pos=[21.665404789593246,40.685273851667134,-51.67326182410831])
cmd.color ("purple", "Centroid22")


cmd.select("Group23", "(resi 19-29 & chain K, resi 34-44 & chain K, resi 51-62 & chain K, resi 231-237 & chain K, resi 97-103 & chain K, )")
cmd.color ("red", "Group23")


cmd.pseudoatom ("Centroid23", pos=[32.06787500778834,21.688187445203464,-73.04612469673157])
cmd.color ("red", "Centroid23")


cmd.select("Group24", "(resi 175-177 & chain K, resi 180-182 & chain K, )")
cmd.color ("orange", "Group24")


cmd.pseudoatom ("Centroid24", pos=[-2.72816667954127,20.082833290100098,-64.97400093078613])
cmd.color ("orange", "Centroid24")


cmd.select("Group25", "(resi 45-55 & chain L, resi 60-70 & chain L, resi 77-88 & chain L, resi 247-253 & chain L, resi 123-129 & chain L, )")
cmd.color ("yellow", "Group25")


cmd.pseudoatom ("Centroid25", pos=[24.229500045379,11.689708355814219,-94.20327075322469])
cmd.color ("yellow", "Centroid25")


cmd.select("Group26", "(resi 92-95 & chain L, resi 103-118 & chain L, resi 188-200 & chain L, resi 176-180 & chain L, resi 203-206 & chain L, resi 259-275 & chain L, resi 285-302 & chain L, resi 307-316 & chain L, )")
cmd.color ("green", "Group26")


cmd.pseudoatom ("Centroid26", pos=[8.787379312874942,3.086724104509614,-90.79593070896192])
cmd.color ("green", "Centroid26")


cmd.select("Group27", "(resi 19-29 & chain M, resi 34-44 & chain M, resi 51-57 & chain M, resi 60-62 & chain M, resi 231-237 & chain M, resi 97-103 & chain M, )")
cmd.color ("cyan", "Group27")


cmd.pseudoatom ("Centroid27", pos=[14.762673914108587,20.029956568842348,-115.0749340886655])
cmd.color ("cyan", "Centroid27")


cmd.select("Group28", "(resi 175-177 & chain M, resi 180-182 & chain M, )")
cmd.color ("blue", "Group28")


cmd.pseudoatom ("Centroid28", pos=[-17.947500228881836,22.640166600545246,-99.74083455403645])
cmd.color ("blue", "Centroid28")


cmd.select("Group29", "(resi 45-55 & chain N, resi 60-70 & chain N, resi 77-88 & chain N, resi 248-253 & chain N, resi 123-129 & chain N, )")
cmd.color ("purple", "Group29")


cmd.pseudoatom ("Centroid29", pos=[8.35612765652068,42.707191548448925,-123.46872402759308])
cmd.color ("purple", "Centroid29")


cmd.select("Group30", "(resi 92-95 & chain N, resi 103-118 & chain N, resi 188-200 & chain N, resi 176-180 & chain N, resi 203-206 & chain N, resi 259-275 & chain N, resi 285-302 & chain N, resi 307-316 & chain N, )")
cmd.color ("red", "Group30")


cmd.pseudoatom ("Centroid30", pos=[-9.753758609594627,44.03195403088098,-123.16663246593257])
cmd.color ("red", "Centroid30")


cmd.select("Group31", "(resi 19-29 & chain O, resi 34-44 & chain O, resi 51-62 & chain O, resi 231-237 & chain O, resi 97-103 & chain O, )")
cmd.color ("orange", "Group31")


cmd.pseudoatom ("Centroid31", pos=[9.622812476630012,65.83700029055278,-114.64804188410442])
cmd.color ("orange", "Centroid31")


cmd.select("Group32", "(resi 175-177 & chain O, resi 180-182 & chain O, )")
cmd.color ("yellow", "Group32")


cmd.pseudoatom ("Centroid32", pos=[-19.745166142781574,60.68649991353353,-94.93816757202148])
cmd.color ("yellow", "Centroid32")


cmd.select("Group33", "(resi 45-55 & chain P, resi 60-70 & chain P, resi 77-88 & chain P, resi 247-253 & chain P, resi 123-129 & chain P, )")
cmd.color ("green", "Group33")


cmd.pseudoatom ("Centroid33", pos=[17.80908332268397,75.72487529118855,-93.54635397593181])
cmd.color ("green", "Centroid33")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
