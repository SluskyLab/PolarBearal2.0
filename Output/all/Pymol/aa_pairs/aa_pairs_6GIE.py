from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/6GIE.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.remove("hydrogens")
cmd.h_add("(name CA)")
cmd.select("Astrand0", "resi 0+1+2+3+4+5+6+7+8+9+10+11+12+13 & chain A ")


cmd.select("Astrand1", "resi 263+264+265+266+267+268+269+270+271+272+273 & chain A ")


cmd.select("Astrand2", "resi 244+245+246+247+248+249+250+251+252+253+254 & chain A ")


cmd.select("Astrand3", "resi 230+231+232+233+234+235+236+237+238+239+240+241 & chain A ")


cmd.select("Astrand4", "resi 212+213+214+215+216+217+218+219+220 & chain A ")


cmd.select("Astrand5", "resi 198+199+200+201+202+203+204+205+206+207+208+209 & chain A ")


cmd.select("Astrand6", "resi 185+186+187+188+189+190+191+192+193+194 & chain A ")


cmd.select("Astrand7", "resi 168+169+170+116+171+115+117+114+118+172+95+113+119+94+96+93+97+112+120+173+92+98+99+91+174+121+90+100+122+175+123+176+124+177+178 & chain A ")


cmd.select("Astrand8", "resi 72+73+74+75+76+77+135+78+134+79+133+80+132+131+81+130+129+82+128+127+83 & chain A ")


cmd.select("Astrand9", "resi 52+53+54+55+56+57+58+59+60+61 & chain A ")


cmd.select("Astrand10", "resi 21+22+23+24+25+26+27+28+29+30+31+32+33+34+35 & chain A ")


cmd.group("Strands", "*strand*")
cmd.select("barrel", "Astrand*")
cmd.pseudoatom ("PseudoH273A", pos=[1.5421784,158.49326,62.53242])
cmd.pseudoatom ("PseudoH4A", pos=[2.578947,158.63707,60.418224])
cmd.pseudoatom ("PseudoH271A", pos=[-2.740358,158.74083,57.24372])
cmd.pseudoatom ("PseudoH6A", pos=[-1.5656035,158.4755,55.3581])
cmd.pseudoatom ("PseudoH269A", pos=[-7.025857,159.97676,51.796474])
cmd.pseudoatom ("PseudoH8A", pos=[-5.9912457,159.26215,50.008785])
cmd.pseudoatom ("PseudoH267A", pos=[-10.445125,162.03638,46.392868])
cmd.pseudoatom ("PseudoH10A", pos=[-9.610964,160.88461,44.580242])
cmd.pseudoatom ("PseudoH265A", pos=[-11.373612,164.99811,40.825996])
cmd.pseudoatom ("PseudoH12A", pos=[-10.922388,163.93378,38.689255])
cmd.pseudoatom ("PseudoH263A", pos=[-12.683017,168.33223,34.611782])
cmd.pseudoatom ("PseudoH252A", pos=[-11.947886,171.14223,39.474598])
cmd.pseudoatom ("PseudoH264A", pos=[-12.583741,168.9977,39.165585])
cmd.pseudoatom ("PseudoH250A", pos=[-12.48761,168.00279,45.336884])
cmd.pseudoatom ("PseudoH266A", pos=[-12.889594,165.3911,45.00855])
cmd.pseudoatom ("PseudoH248A", pos=[-11.211803,164.32918,51.275932])
cmd.pseudoatom ("PseudoH268A", pos=[-10.658479,162.17575,50.874542])
cmd.pseudoatom ("PseudoH246A", pos=[-8.393008,161.1664,56.985203])
cmd.pseudoatom ("PseudoH270A", pos=[-6.8255625,160.02632,56.354855])
cmd.pseudoatom ("PseudoH244A", pos=[-4.9753265,158.72278,62.381763])
cmd.pseudoatom ("PseudoH239A", pos=[-7.638955,163.4403,62.897507])
cmd.pseudoatom ("PseudoH245A", pos=[-7.593742,162.15857,61.328453])
cmd.pseudoatom ("PseudoH237A", pos=[-9.38389,166.57532,56.97055])
cmd.pseudoatom ("PseudoH247A", pos=[-10.36023,164.77647,55.659676])
cmd.pseudoatom ("PseudoH235A", pos=[-10.151952,169.84926,51.1068])
cmd.pseudoatom ("PseudoH249A", pos=[-10.4246435,168.2998,49.277374])
cmd.pseudoatom ("PseudoH233A", pos=[-10.543839,173.1923,45.003128])
cmd.pseudoatom ("PseudoH251A", pos=[-10.337855,171.4202,43.55772])
cmd.pseudoatom ("PseudoH231A", pos=[-7.7572722,174.87172,39.09279])
cmd.pseudoatom ("PseudoH253A", pos=[-9.199998,173.98376,37.425003])
cmd.pseudoatom ("PseudoH230A", pos=[-5.584995,178.20596,36.968613])
cmd.pseudoatom ("PseudoH218A", pos=[-6.297007,177.78647,43.37815])
cmd.pseudoatom ("PseudoH232A", pos=[-8.062702,176.34183,43.28199])
cmd.pseudoatom ("PseudoH216A", pos=[-9.196811,175.59541,49.696175])
cmd.pseudoatom ("PseudoH234A", pos=[-10.658249,173.94968,49.490192])
cmd.pseudoatom ("PseudoH214A", pos=[-10.806554,172.73322,55.93865])
cmd.pseudoatom ("PseudoH236A", pos=[-10.734505,170.34656,55.48227])
cmd.pseudoatom ("PseudoH212A", pos=[-10.116698,169.38916,62.041897])
cmd.pseudoatom ("PseudoH207A", pos=[-7.752996,174.47147,61.69952])
cmd.pseudoatom ("PseudoH213A", pos=[-9.282473,173.25305,60.076176])
cmd.pseudoatom ("PseudoH205A", pos=[-6.650863,176.06082,55.62671])
cmd.pseudoatom ("PseudoH215A", pos=[-8.9255295,176.1564,54.20411])
cmd.pseudoatom ("PseudoH203A", pos=[-4.1164517,177.32997,49.519966])
cmd.pseudoatom ("PseudoH217A", pos=[-5.538553,177.48305,47.850044])
cmd.pseudoatom ("PseudoH201A", pos=[-0.9207232,179.0577,43.18886])
cmd.pseudoatom ("PseudoH219A", pos=[-2.3525403,178.63412,41.832115])
cmd.pseudoatom ("PseudoH199A", pos=[2.3474922,179.83719,37.155106])
cmd.pseudoatom ("PseudoH198A", pos=[6.522637,180.6858,35.744022])
cmd.pseudoatom ("PseudoH192A", pos=[5.2816505,180.17043,42.022713])
cmd.pseudoatom ("PseudoH200A", pos=[2.9730093,180.11702,41.511177])
cmd.pseudoatom ("PseudoH190A", pos=[1.7617059,179.78145,47.998093])
cmd.pseudoatom ("PseudoH202A", pos=[-0.38677084,179.21516,47.65626])
cmd.pseudoatom ("PseudoH188A", pos=[-1.3221484,179.4081,54.03178])
cmd.pseudoatom ("PseudoH204A", pos=[-3.7927809,178.82576,53.665665])
cmd.pseudoatom ("PseudoH186A", pos=[-4.802884,178.95663,60.17555])
cmd.pseudoatom ("PseudoH206A", pos=[-7.396838,178.26642,59.436264])
cmd.pseudoatom ("PseudoH185A", pos=[-4.361853,179.69122,64.49316])
cmd.pseudoatom ("PseudoH176A", pos=[0.74638987,178.7205,60.352406])
cmd.pseudoatom ("PseudoH187A", pos=[-0.71928686,178.68884,58.45536])
cmd.pseudoatom ("PseudoH174A", pos=[4.2945414,178.68575,54.09764])
cmd.pseudoatom ("PseudoH189A", pos=[2.6443677,178.71284,52.264805])
cmd.pseudoatom ("PseudoH172A", pos=[7.422177,179.74518,47.80893])
cmd.pseudoatom ("PseudoH191A", pos=[5.683028,178.70425,46.031906])
cmd.pseudoatom ("PseudoH170A", pos=[10.607626,178.21544,42.011395])
cmd.pseudoatom ("PseudoH193A", pos=[8.8034935,178.0271,40.177258])
cmd.pseudoatom ("PseudoH168A", pos=[13.13798,176.63109,36.1065])
cmd.pseudoatom ("PseudoH133A", pos=[14.537268,175.2433,41.237503])
cmd.pseudoatom ("PseudoH169A", pos=[14.5373,177.38904,40.40204])
cmd.pseudoatom ("PseudoH131A", pos=[13.351797,179.11987,46.559956])
cmd.pseudoatom ("PseudoH116A", pos=[14.661789,169.97597,42.597897])
cmd.pseudoatom ("PseudoH171A", pos=[11.275396,179.67624,46.238407])
cmd.pseudoatom ("PseudoH134A", pos=[14.652423,170.81767,40.399734])
cmd.pseudoatom ("PseudoH114A", pos=[13.258506,165.25558,37.514668])
cmd.pseudoatom ("PseudoH118A", pos=[15.912288,174.75993,47.36716])
cmd.pseudoatom ("PseudoH129A", pos=[10.221084,180.95454,52.56101])
cmd.pseudoatom ("PseudoH95A", pos=[13.712165,164.30911,47.150536])
cmd.pseudoatom ("PseudoH130A", pos=[13.895936,178.87697,51.03803])
cmd.pseudoatom ("PseudoH78A", pos=[12.873689,163.88213,49.13698])
cmd.pseudoatom ("PseudoH76A", pos=[10.506833,159.4012,44.351967])
cmd.pseudoatom ("PseudoH93A", pos=[15.343051,169.24689,51.813965])
cmd.pseudoatom ("PseudoH97A", pos=[10.535703,160.2173,42.326458])
cmd.pseudoatom ("PseudoH173A", pos=[7.9423666,180.24136,52.256207])
cmd.pseudoatom ("PseudoH80A", pos=[14.461611,168.5787,53.980366])
cmd.pseudoatom ("PseudoH74A", pos=[6.546822,157.0329,39.600735])
cmd.pseudoatom ("PseudoH99A", pos=[7.317498,157.14781,37.563576])
cmd.pseudoatom ("PseudoH91A", pos=[16.515789,173.83057,56.665997])
cmd.pseudoatom ("PseudoH127A", pos=[7.0128875,181.06352,58.445946])
cmd.pseudoatom ("PseudoH128A", pos=[10.823786,179.82562,56.77464])
cmd.pseudoatom ("PseudoH82A", pos=[16.198797,172.9809,59.00462])
cmd.pseudoatom ("PseudoH72A", pos=[2.3146253,155.02661,34.617134])
cmd.pseudoatom ("PseudoH122A", pos=[12.168866,180.73146,58.439358])
cmd.pseudoatom ("PseudoH59A", pos=[0.23202121,155.24344,39.96042])
cmd.pseudoatom ("PseudoH73A", pos=[2.6744697,154.92741,39.1426])
cmd.pseudoatom ("PseudoH57A", pos=[5.1155562,156.05531,44.82199])
cmd.pseudoatom ("PseudoH75A", pos=[7.494293,156.34038,43.9893])
cmd.pseudoatom ("PseudoH55A", pos=[9.716493,158.41136,49.798405])
cmd.pseudoatom ("PseudoH77A", pos=[11.233594,159.79196,48.8169])
cmd.pseudoatom ("PseudoH53A", pos=[13.016815,162.31612,54.35909])
cmd.pseudoatom ("PseudoH79A", pos=[13.748538,164.15662,53.54683])
cmd.pseudoatom ("PseudoH52A", pos=[13.280446,163.0606,58.915])
cmd.pseudoatom ("PseudoH28A", pos=[8.265331,159.69342,55.890285])
cmd.pseudoatom ("PseudoH54A", pos=[9.507723,159.82219,53.993004])
cmd.pseudoatom ("PseudoH26A", pos=[4.37599,157.36205,50.920204])
cmd.pseudoatom ("PseudoH56A", pos=[5.411208,157.45808,49.07947])
cmd.pseudoatom ("PseudoH24A", pos=[-0.056661487,157.46628,46.168312])
cmd.pseudoatom ("PseudoH58A", pos=[0.93449146,157.30492,43.849216])
cmd.pseudoatom ("PseudoH22A", pos=[-4.477324,157.7874,40.746925])
cmd.pseudoatom ("PseudoH60A", pos=[-3.4537134,157.20068,38.41814])
cmd.pseudoatom ("PseudoH21A", pos=[-8.94765,157.68773,39.716877])
cmd.pseudoatom ("PseudoH9A", pos=[-6.690525,157.83449,45.84505])
cmd.pseudoatom ("PseudoH23A", pos=[-4.4951115,157.16447,45.135284])
cmd.pseudoatom ("PseudoH7A", pos=[-2.2178447,157.06088,51.265057])
cmd.pseudoatom ("PseudoH25A", pos=[0.08567774,156.5258,50.535656])
cmd.pseudoatom ("PseudoH5A", pos=[2.5121017,157.2635,56.28923])
cmd.pseudoatom ("PseudoH27A", pos=[4.863852,157.12473,55.280052])
cmd.pseudoatom ("PseudoH3A", pos=[7.023104,158.38625,61.16229])
cmd.pseudoatom ("PseudoH29A", pos=[9.654317,158.63025,60.075417])
cmd.pseudoatom ("PseudoH33A", pos=[9.568718,161.88516,67.84836])
cmd.pseudoatom ("PseudoH0A", pos=[4.8448763,163.14738,69.91295])
cmd.group("Pseudo_Hydrogens", "PseudoH*")
cmd.pseudoatom ("PseudoR267A", pos=[-9.568881,163.47151,46.860897])
cmd.pseudoatom ("PseudoR247A", pos=[-8.886827,164.74873,54.774307])
cmd.pseudoatom ("PseudoR233A", pos=[-9.063031,172.86142,45.81351])
cmd.pseudoatom ("PseudoR234A", pos=[-12.310488,173.33315,49.19971])
cmd.pseudoatom ("PseudoR215A", pos=[-7.9102774,174.86937,53.662838])
cmd.pseudoatom ("PseudoR201A", pos=[0.056819655,177.76875,43.815487])
cmd.pseudoatom ("PseudoR192A", pos=[6.6174855,181.18019,42.579388])
cmd.pseudoatom ("PseudoR187A", pos=[-1.3912469,177.18837,57.864876])
cmd.pseudoatom ("PseudoR132A", pos=[15.077077,175.3366,45.344673])
cmd.pseudoatom ("PseudoR76A", pos=[9.078513,160.1252,45.067585])
cmd.pseudoatom ("PseudoR120A", pos=[15.0399685,178.80634,52.7216])
cmd.pseudoatom ("PseudoR79A", pos=[15.373964,164.37799,52.834393])
cmd.pseudoatom ("PseudoR23A", pos=[-3.834593,155.61867,44.61774])
cmd.pseudoatom ("PseudoR7A", pos=[-3.5498269,156.30211,52.102577])
cmd.pseudoatom ("PseudoR27A", pos=[6.178687,156.14726,54.58829])
cmd.group("Pseudo_RGroups", "PseudoR*")
cmd.distance("StrongHBond", "resi 5 & chain A & name O", "resi 272 & chain A & name N")
cmd.distance("StrongHBond", "resi 5 & chain A & name N", "resi 272 & chain A & name O")
cmd.distance("StrongHBond", "resi 7 & chain A & name O", "resi 270 & chain A & name N")
cmd.distance("StrongHBond", "resi 7 & chain A & name N", "resi 270 & chain A & name O")
cmd.distance("StrongHBond", "resi 9 & chain A & name O", "resi 268 & chain A & name N")
cmd.distance("StrongHBond", "resi 9 & chain A & name N", "resi 268 & chain A & name O")
cmd.distance("StrongHBond", "resi 11 & chain A & name O", "resi 266 & chain A & name N")
cmd.distance("StrongHBond", "resi 11 & chain A & name N", "resi 266 & chain A & name O")
cmd.distance("StrongHBond", "resi 13 & chain A & name O", "resi 264 & chain A & name N")
cmd.distance("StrongHBond", "resi 13 & chain A & name N", "resi 264 & chain A & name O")
cmd.distance("StrongHBond", "resi 263 & chain A & name O", "resi 253 & chain A & name N")
cmd.distance("StrongHBond", "resi 263 & chain A & name N", "resi 253 & chain A & name O")
cmd.distance("StrongHBond", "resi 265 & chain A & name O", "resi 251 & chain A & name N")
cmd.distance("StrongHBond", "resi 265 & chain A & name N", "resi 251 & chain A & name O")
cmd.distance("StrongHBond", "resi 267 & chain A & name O", "resi 249 & chain A & name N")
cmd.distance("StrongHBond", "resi 267 & chain A & name N", "resi 249 & chain A & name O")
cmd.distance("StrongHBond", "resi 269 & chain A & name O", "resi 247 & chain A & name N")
cmd.distance("StrongHBond", "resi 269 & chain A & name N", "resi 247 & chain A & name O")
cmd.distance("StrongHBond", "resi 271 & chain A & name O", "resi 245 & chain A & name N")
cmd.distance("StrongHBond", "resi 271 & chain A & name N", "resi 245 & chain A & name O")
cmd.distance("StrongHBond", "resi 244 & chain A & name O", "resi 241 & chain A & name N")
cmd.distance("StrongHBond", "resi 244 & chain A & name N", "resi 241 & chain A & name O")
cmd.distance("StrongHBond", "resi 246 & chain A & name O", "resi 238 & chain A & name N")
cmd.distance("StrongHBond", "resi 246 & chain A & name N", "resi 238 & chain A & name O")
cmd.distance("StrongHBond", "resi 248 & chain A & name O", "resi 236 & chain A & name N")
cmd.distance("StrongHBond", "resi 248 & chain A & name N", "resi 236 & chain A & name O")
cmd.distance("StrongHBond", "resi 250 & chain A & name O", "resi 234 & chain A & name N")
cmd.distance("StrongHBond", "resi 250 & chain A & name N", "resi 234 & chain A & name O")
cmd.distance("StrongHBond", "resi 252 & chain A & name O", "resi 232 & chain A & name N")
cmd.distance("StrongHBond", "resi 252 & chain A & name N", "resi 232 & chain A & name O")
cmd.distance("StrongHBond", "resi 254 & chain A & name O", "resi 230 & chain A & name N")
cmd.distance("StrongHBond", "resi 254 & chain A & name N", "resi 230 & chain A & name O")
cmd.distance("StrongHBond", "resi 231 & chain A & name O", "resi 219 & chain A & name N")
cmd.distance("StrongHBond", "resi 231 & chain A & name N", "resi 219 & chain A & name O")
cmd.distance("StrongHBond", "resi 233 & chain A & name O", "resi 217 & chain A & name N")
cmd.distance("StrongHBond", "resi 233 & chain A & name N", "resi 217 & chain A & name O")
cmd.distance("StrongHBond", "resi 235 & chain A & name O", "resi 215 & chain A & name N")
cmd.distance("StrongHBond", "resi 235 & chain A & name N", "resi 215 & chain A & name O")
cmd.distance("StrongHBond", "resi 237 & chain A & name O", "resi 213 & chain A & name N")
cmd.distance("StrongHBond", "resi 237 & chain A & name N", "resi 213 & chain A & name O")
cmd.distance("StrongHBond", "resi 212 & chain A & name O", "resi 209 & chain A & name N")
cmd.distance("StrongHBond", "resi 212 & chain A & name N", "resi 209 & chain A & name O")
cmd.distance("StrongHBond", "resi 214 & chain A & name O", "resi 206 & chain A & name N")
cmd.distance("StrongHBond", "resi 214 & chain A & name N", "resi 206 & chain A & name O")
cmd.distance("StrongHBond", "resi 216 & chain A & name O", "resi 204 & chain A & name N")
cmd.distance("StrongHBond", "resi 216 & chain A & name N", "resi 204 & chain A & name O")
cmd.distance("StrongHBond", "resi 218 & chain A & name O", "resi 202 & chain A & name N")
cmd.distance("StrongHBond", "resi 218 & chain A & name N", "resi 202 & chain A & name O")
cmd.distance("StrongHBond", "resi 220 & chain A & name O", "resi 200 & chain A & name N")
cmd.distance("StrongHBond", "resi 220 & chain A & name N", "resi 200 & chain A & name O")
cmd.distance("StrongHBond", "resi 199 & chain A & name O", "resi 193 & chain A & name N")
cmd.distance("StrongHBond", "resi 199 & chain A & name N", "resi 193 & chain A & name O")
cmd.distance("StrongHBond", "resi 201 & chain A & name O", "resi 191 & chain A & name N")
cmd.distance("StrongHBond", "resi 201 & chain A & name N", "resi 191 & chain A & name O")
cmd.distance("StrongHBond", "resi 203 & chain A & name O", "resi 189 & chain A & name N")
cmd.distance("StrongHBond", "resi 203 & chain A & name N", "resi 189 & chain A & name O")
cmd.distance("StrongHBond", "resi 205 & chain A & name O", "resi 187 & chain A & name N")
cmd.distance("StrongHBond", "resi 205 & chain A & name N", "resi 187 & chain A & name O")
cmd.distance("StrongHBond", "resi 207 & chain A & name O", "resi 185 & chain A & name N")
cmd.distance("StrongHBond", "resi 207 & chain A & name N", "resi 185 & chain A & name O")
cmd.distance("StrongHBond", "resi 186 & chain A & name O", "resi 177 & chain A & name N")
cmd.distance("StrongHBond", "resi 186 & chain A & name N", "resi 177 & chain A & name O")
cmd.distance("StrongHBond", "resi 188 & chain A & name O", "resi 175 & chain A & name N")
cmd.distance("StrongHBond", "resi 188 & chain A & name N", "resi 175 & chain A & name O")
cmd.distance("StrongHBond", "resi 190 & chain A & name O", "resi 173 & chain A & name N")
cmd.distance("StrongHBond", "resi 190 & chain A & name N", "resi 173 & chain A & name O")
cmd.distance("StrongHBond", "resi 192 & chain A & name O", "resi 171 & chain A & name N")
cmd.distance("StrongHBond", "resi 192 & chain A & name N", "resi 171 & chain A & name O")
cmd.distance("StrongHBond", "resi 194 & chain A & name O", "resi 169 & chain A & name N")
cmd.distance("StrongHBond", "resi 194 & chain A & name N", "resi 169 & chain A & name O")
cmd.distance("StrongHBond", "resi 168 & chain A & name O", "resi 134 & chain A & name N")
cmd.distance("StrongHBond", "resi 168 & chain A & name N", "resi 134 & chain A & name O")
cmd.distance("StrongHBond", "resi 170 & chain A & name O", "resi 132 & chain A & name N")
cmd.distance("StrongHBond", "resi 170 & chain A & name N", "resi 132 & chain A & name O")
cmd.distance("StrongHBond", "resi 115 & chain A & name O", "resi 135 & chain A & name N")
cmd.distance("StrongHBond", "resi 115 & chain A & name N", "resi 135 & chain A & name O")
cmd.distance("StrongHBond", "resi 117 & chain A & name O", "resi 133 & chain A & name N")
cmd.distance("StrongHBond", "resi 117 & chain A & name N", "resi 133 & chain A & name O")
cmd.distance("StrongHBond", "resi 172 & chain A & name O", "resi 130 & chain A & name N")
cmd.distance("StrongHBond", "resi 172 & chain A & name N", "resi 130 & chain A & name O")
cmd.distance("StrongHBond", "resi 119 & chain A & name O", "resi 131 & chain A & name N")
cmd.distance("StrongHBond", "resi 119 & chain A & name N", "resi 131 & chain A & name O")
cmd.distance("StrongHBond", "resi 94 & chain A & name O", "resi 79 & chain A & name N")
cmd.distance("StrongHBond", "resi 94 & chain A & name N", "resi 79 & chain A & name O")
cmd.distance("StrongHBond", "resi 96 & chain A & name O", "resi 77 & chain A & name N")
cmd.distance("StrongHBond", "resi 96 & chain A & name N", "resi 77 & chain A & name O")
cmd.distance("StrongHBond", "resi 92 & chain A & name O", "resi 81 & chain A & name N")
cmd.distance("StrongHBond", "resi 92 & chain A & name N", "resi 81 & chain A & name O")
cmd.distance("StrongHBond", "resi 98 & chain A & name O", "resi 75 & chain A & name N")
cmd.distance("StrongHBond", "resi 98 & chain A & name N", "resi 75 & chain A & name O")
cmd.distance("StrongHBond", "resi 174 & chain A & name O", "resi 128 & chain A & name N")
cmd.distance("StrongHBond", "resi 174 & chain A & name N", "resi 128 & chain A & name O")
cmd.distance("StrongHBond", "resi 121 & chain A & name O", "resi 129 & chain A & name N")
cmd.distance("StrongHBond", "resi 121 & chain A & name N", "resi 129 & chain A & name O")
cmd.distance("StrongHBond", "resi 90 & chain A & name O", "resi 83 & chain A & name N")
cmd.distance("StrongHBond", "resi 90 & chain A & name N", "resi 83 & chain A & name O")
cmd.distance("StrongHBond", "resi 100 & chain A & name O", "resi 73 & chain A & name N")
cmd.distance("StrongHBond", "resi 100 & chain A & name N", "resi 73 & chain A & name O")
cmd.distance("StrongHBond", "resi 72 & chain A & name O", "resi 60 & chain A & name N")
cmd.distance("StrongHBond", "resi 72 & chain A & name N", "resi 60 & chain A & name O")
cmd.distance("StrongHBond", "resi 74 & chain A & name O", "resi 58 & chain A & name N")
cmd.distance("StrongHBond", "resi 74 & chain A & name N", "resi 58 & chain A & name O")
cmd.distance("StrongHBond", "resi 76 & chain A & name O", "resi 56 & chain A & name N")
cmd.distance("StrongHBond", "resi 76 & chain A & name N", "resi 56 & chain A & name O")
cmd.distance("StrongHBond", "resi 78 & chain A & name O", "resi 54 & chain A & name N")
cmd.distance("StrongHBond", "resi 78 & chain A & name N", "resi 54 & chain A & name O")
cmd.distance("StrongHBond", "resi 80 & chain A & name O", "resi 52 & chain A & name N")
cmd.distance("StrongHBond", "resi 80 & chain A & name N", "resi 52 & chain A & name O")
cmd.distance("StrongHBond", "resi 53 & chain A & name O", "resi 29 & chain A & name N")
cmd.distance("StrongHBond", "resi 53 & chain A & name N", "resi 29 & chain A & name O")
cmd.distance("StrongHBond", "resi 55 & chain A & name O", "resi 27 & chain A & name N")
cmd.distance("StrongHBond", "resi 55 & chain A & name N", "resi 27 & chain A & name O")
cmd.distance("StrongHBond", "resi 57 & chain A & name O", "resi 25 & chain A & name N")
cmd.distance("StrongHBond", "resi 57 & chain A & name N", "resi 25 & chain A & name O")
cmd.distance("StrongHBond", "resi 59 & chain A & name O", "resi 23 & chain A & name N")
cmd.distance("StrongHBond", "resi 59 & chain A & name N", "resi 23 & chain A & name O")
cmd.distance("StrongHBond", "resi 61 & chain A & name O", "resi 21 & chain A & name N")
cmd.distance("StrongHBond", "resi 61 & chain A & name N", "resi 21 & chain A & name O")
cmd.distance("StrongHBond", "resi 22 & chain A & name O", "resi 10 & chain A & name N")
cmd.distance("StrongHBond", "resi 22 & chain A & name N", "resi 10 & chain A & name O")
cmd.distance("StrongHBond", "resi 24 & chain A & name O", "resi 8 & chain A & name N")
cmd.distance("StrongHBond", "resi 24 & chain A & name N", "resi 8 & chain A & name O")
cmd.distance("StrongHBond", "resi 26 & chain A & name O", "resi 6 & chain A & name N")
cmd.distance("StrongHBond", "resi 26 & chain A & name N", "resi 6 & chain A & name O")
cmd.distance("StrongHBond", "resi 28 & chain A & name O", "resi 4 & chain A & name N")
cmd.distance("StrongHBond", "resi 28 & chain A & name N", "resi 4 & chain A & name O")
cmd.distance("StrongHBond", "resi 34 & chain A & name O", "resi 1 & chain A & name N")
cmd.distance("StrongHBond", "resi 34 & chain A & name N", "resi 1 & chain A & name O")
cmd.distance("WeakHBond", "resi 3 & chain A & name O", "PseudoH273A")
cmd.distance("WeakHBond", "resi 272 & chain A & name O", "PseudoH4A")
cmd.distance("WeakHBond", "resi 5 & chain A & name O", "PseudoH271A")
cmd.distance("WeakHBond", "resi 270 & chain A & name O", "PseudoH6A")
cmd.distance("WeakHBond", "resi 7 & chain A & name O", "PseudoH269A")
cmd.distance("WeakHBond", "resi 268 & chain A & name O", "PseudoH8A")
cmd.distance("WeakHBond", "resi 9 & chain A & name O", "PseudoH267A")
cmd.distance("WeakHBond", "resi 266 & chain A & name O", "PseudoH10A")
cmd.distance("WeakHBond", "resi 11 & chain A & name O", "PseudoH265A")
cmd.distance("WeakHBond", "resi 264 & chain A & name O", "PseudoH12A")
cmd.distance("WeakHBond", "resi 13 & chain A & name O", "PseudoH263A")
cmd.distance("WeakHBond", "resi 263 & chain A & name O", "PseudoH252A")
cmd.distance("WeakHBond", "resi 251 & chain A & name O", "PseudoH264A")
cmd.distance("WeakHBond", "resi 265 & chain A & name O", "PseudoH250A")
cmd.distance("WeakHBond", "resi 249 & chain A & name O", "PseudoH266A")
cmd.distance("WeakHBond", "resi 267 & chain A & name O", "PseudoH248A")
cmd.distance("WeakHBond", "resi 247 & chain A & name O", "PseudoH268A")
cmd.distance("WeakHBond", "resi 269 & chain A & name O", "PseudoH246A")
cmd.distance("WeakHBond", "resi 245 & chain A & name O", "PseudoH270A")
cmd.distance("WeakHBond", "resi 271 & chain A & name O", "PseudoH244A")
cmd.distance("WeakHBond", "resi 244 & chain A & name O", "PseudoH239A")
cmd.distance("WeakHBond", "resi 238 & chain A & name O", "PseudoH245A")
cmd.distance("WeakHBond", "resi 246 & chain A & name O", "PseudoH237A")
cmd.distance("WeakHBond", "resi 236 & chain A & name O", "PseudoH247A")
cmd.distance("WeakHBond", "resi 248 & chain A & name O", "PseudoH235A")
cmd.distance("WeakHBond", "resi 234 & chain A & name O", "PseudoH249A")
cmd.distance("WeakHBond", "resi 250 & chain A & name O", "PseudoH233A")
cmd.distance("WeakHBond", "resi 232 & chain A & name O", "PseudoH251A")
cmd.distance("WeakHBond", "resi 252 & chain A & name O", "PseudoH231A")
cmd.distance("WeakHBond", "resi 230 & chain A & name O", "PseudoH253A")
cmd.distance("WeakHBond", "resi 219 & chain A & name O", "PseudoH230A")
cmd.distance("WeakHBond", "resi 231 & chain A & name O", "PseudoH218A")
cmd.distance("WeakHBond", "resi 217 & chain A & name O", "PseudoH232A")
cmd.distance("WeakHBond", "resi 233 & chain A & name O", "PseudoH216A")
cmd.distance("WeakHBond", "resi 215 & chain A & name O", "PseudoH234A")
cmd.distance("WeakHBond", "resi 235 & chain A & name O", "PseudoH214A")
cmd.distance("WeakHBond", "resi 213 & chain A & name O", "PseudoH236A")
cmd.distance("WeakHBond", "resi 237 & chain A & name O", "PseudoH212A")
cmd.distance("WeakHBond", "resi 212 & chain A & name O", "PseudoH207A")
cmd.distance("WeakHBond", "resi 206 & chain A & name O", "PseudoH213A")
cmd.distance("WeakHBond", "resi 214 & chain A & name O", "PseudoH205A")
cmd.distance("WeakHBond", "resi 204 & chain A & name O", "PseudoH215A")
cmd.distance("WeakHBond", "resi 216 & chain A & name O", "PseudoH203A")
cmd.distance("WeakHBond", "resi 202 & chain A & name O", "PseudoH217A")
cmd.distance("WeakHBond", "resi 218 & chain A & name O", "PseudoH201A")
cmd.distance("WeakHBond", "resi 200 & chain A & name O", "PseudoH219A")
cmd.distance("WeakHBond", "resi 220 & chain A & name O", "PseudoH199A")
cmd.distance("WeakHBond", "resi 193 & chain A & name O", "PseudoH198A")
cmd.distance("WeakHBond", "resi 199 & chain A & name O", "PseudoH192A")
cmd.distance("WeakHBond", "resi 191 & chain A & name O", "PseudoH200A")
cmd.distance("WeakHBond", "resi 201 & chain A & name O", "PseudoH190A")
cmd.distance("WeakHBond", "resi 189 & chain A & name O", "PseudoH202A")
cmd.distance("WeakHBond", "resi 203 & chain A & name O", "PseudoH188A")
cmd.distance("WeakHBond", "resi 187 & chain A & name O", "PseudoH204A")
cmd.distance("WeakHBond", "resi 205 & chain A & name O", "PseudoH186A")
cmd.distance("WeakHBond", "resi 185 & chain A & name O", "PseudoH206A")
cmd.distance("WeakHBond", "resi 177 & chain A & name O", "PseudoH185A")
cmd.distance("WeakHBond", "resi 186 & chain A & name O", "PseudoH176A")
cmd.distance("WeakHBond", "resi 175 & chain A & name O", "PseudoH187A")
cmd.distance("WeakHBond", "resi 188 & chain A & name O", "PseudoH174A")
cmd.distance("WeakHBond", "resi 173 & chain A & name O", "PseudoH189A")
cmd.distance("WeakHBond", "resi 190 & chain A & name O", "PseudoH172A")
cmd.distance("WeakHBond", "resi 171 & chain A & name O", "PseudoH191A")
cmd.distance("WeakHBond", "resi 192 & chain A & name O", "PseudoH170A")
cmd.distance("WeakHBond", "resi 169 & chain A & name O", "PseudoH193A")
cmd.distance("WeakHBond", "resi 194 & chain A & name O", "PseudoH168A")
cmd.distance("WeakHBond", "resi 168 & chain A & name O", "PseudoH133A")
cmd.distance("WeakHBond", "resi 132 & chain A & name O", "PseudoH169A")
cmd.distance("WeakHBond", "resi 170 & chain A & name O", "PseudoH131A")
cmd.distance("WeakHBond", "resi 133 & chain A & name O", "PseudoH116A")
cmd.distance("WeakHBond", "resi 130 & chain A & name O", "PseudoH171A")
cmd.distance("WeakHBond", "resi 115 & chain A & name O", "PseudoH134A")
cmd.distance("WeakHBond", "resi 135 & chain A & name O", "PseudoH114A")
cmd.distance("WeakHBond", "resi 131 & chain A & name O", "PseudoH118A")
cmd.distance("WeakHBond", "resi 172 & chain A & name O", "PseudoH129A")
cmd.distance("WeakHBond", "resi 77 & chain A & name O", "PseudoH95A")
cmd.distance("WeakHBond", "resi 119 & chain A & name O", "PseudoH130A")
cmd.distance("WeakHBond", "resi 94 & chain A & name O", "PseudoH78A")
cmd.distance("WeakHBond", "resi 96 & chain A & name O", "PseudoH76A")
cmd.distance("WeakHBond", "resi 79 & chain A & name O", "PseudoH93A")
cmd.distance("WeakHBond", "resi 75 & chain A & name O", "PseudoH97A")
cmd.distance("WeakHBond", "resi 128 & chain A & name O", "PseudoH173A")
cmd.distance("WeakHBond", "resi 92 & chain A & name O", "PseudoH80A")
cmd.distance("WeakHBond", "resi 98 & chain A & name O", "PseudoH74A")
cmd.distance("WeakHBond", "resi 73 & chain A & name O", "PseudoH99A")
cmd.distance("WeakHBond", "resi 81 & chain A & name O", "PseudoH91A")
cmd.distance("WeakHBond", "resi 174 & chain A & name O", "PseudoH127A")
cmd.distance("WeakHBond", "resi 121 & chain A & name O", "PseudoH128A")
cmd.distance("WeakHBond", "resi 90 & chain A & name O", "PseudoH82A")
cmd.distance("WeakHBond", "resi 100 & chain A & name O", "PseudoH72A")
cmd.distance("WeakHBond", "resi 127 & chain A & name O", "PseudoH122A")
cmd.distance("WeakHBond", "resi 72 & chain A & name O", "PseudoH59A")
cmd.distance("WeakHBond", "resi 58 & chain A & name O", "PseudoH73A")
cmd.distance("WeakHBond", "resi 74 & chain A & name O", "PseudoH57A")
cmd.distance("WeakHBond", "resi 56 & chain A & name O", "PseudoH75A")
cmd.distance("WeakHBond", "resi 76 & chain A & name O", "PseudoH55A")
cmd.distance("WeakHBond", "resi 54 & chain A & name O", "PseudoH77A")
cmd.distance("WeakHBond", "resi 78 & chain A & name O", "PseudoH53A")
cmd.distance("WeakHBond", "resi 52 & chain A & name O", "PseudoH79A")
cmd.distance("WeakHBond", "resi 29 & chain A & name O", "PseudoH52A")
cmd.distance("WeakHBond", "resi 53 & chain A & name O", "PseudoH28A")
cmd.distance("WeakHBond", "resi 27 & chain A & name O", "PseudoH54A")
cmd.distance("WeakHBond", "resi 55 & chain A & name O", "PseudoH26A")
cmd.distance("WeakHBond", "resi 25 & chain A & name O", "PseudoH56A")
cmd.distance("WeakHBond", "resi 57 & chain A & name O", "PseudoH24A")
cmd.distance("WeakHBond", "resi 23 & chain A & name O", "PseudoH58A")
cmd.distance("WeakHBond", "resi 59 & chain A & name O", "PseudoH22A")
cmd.distance("WeakHBond", "resi 21 & chain A & name O", "PseudoH60A")
cmd.distance("WeakHBond", "resi 10 & chain A & name O", "PseudoH21A")
cmd.distance("WeakHBond", "resi 22 & chain A & name O", "PseudoH9A")
cmd.distance("WeakHBond", "resi 8 & chain A & name O", "PseudoH23A")
cmd.distance("WeakHBond", "resi 24 & chain A & name O", "PseudoH7A")
cmd.distance("WeakHBond", "resi 6 & chain A & name O", "PseudoH25A")
cmd.distance("WeakHBond", "resi 26 & chain A & name O", "PseudoH5A")
cmd.distance("WeakHBond", "resi 4 & chain A & name O", "PseudoH27A")
cmd.distance("WeakHBond", "resi 28 & chain A & name O", "PseudoH3A")
cmd.distance("WeakHBond", "resi 2 & chain A & name O", "PseudoH29A")
cmd.distance("WeakHBond", "resi 1 & chain A & name O", "PseudoH33A")
cmd.distance("WeakHBond", "resi 34 & chain A & name O", "PseudoH0A")
cmd.distance("NonHBond", "resi 4 & chain A & name CB", "resi 273 & chain A & name CB")
cmd.distance("NonHBond", "resi 6 & chain A & name CB", "resi 271 & chain A & name CB")
cmd.distance("NonHBond", "resi 8 & chain A & name CB", "resi 269 & chain A & name CB")
cmd.distance("NonHBond", "resi 10 & chain A & name CB", "PseudoR267A")
cmd.distance("NonHBond", "resi 12 & chain A & name CB", "resi 265 & chain A & name CB")
cmd.distance("NonHBond", "resi 264 & chain A & name CB", "resi 252 & chain A & name CB")
cmd.distance("NonHBond", "resi 266 & chain A & name CB", "resi 250 & chain A & name CB")
cmd.distance("NonHBond", "resi 268 & chain A & name CB", "resi 248 & chain A & name CB")
cmd.distance("NonHBond", "resi 270 & chain A & name CB", "resi 246 & chain A & name CB")
cmd.distance("NonHBond", "resi 272 & chain A & name CB", "resi 244 & chain A & name CB")
cmd.distance("NonHBond", "resi 245 & chain A & name CB", "resi 239 & chain A & name CB")
cmd.distance("NonHBond", "PseudoR247A", "resi 237 & chain A & name CB")
cmd.distance("NonHBond", "resi 249 & chain A & name CB", "resi 235 & chain A & name CB")
cmd.distance("NonHBond", "resi 251 & chain A & name CB", "PseudoR233A")
cmd.distance("NonHBond", "resi 253 & chain A & name CB", "resi 231 & chain A & name CB")
cmd.distance("NonHBond", "resi 230 & chain A & name CB", "resi 220 & chain A & name CB")
cmd.distance("NonHBond", "resi 232 & chain A & name CB", "resi 218 & chain A & name CB")
cmd.distance("NonHBond", "PseudoR234A", "resi 216 & chain A & name CB")
cmd.distance("NonHBond", "resi 236 & chain A & name CB", "resi 214 & chain A & name CB")
cmd.distance("NonHBond", "resi 238 & chain A & name CB", "resi 212 & chain A & name CB")
cmd.distance("NonHBond", "resi 213 & chain A & name CB", "resi 207 & chain A & name CB")
cmd.distance("NonHBond", "PseudoR215A", "resi 205 & chain A & name CB")
cmd.distance("NonHBond", "resi 217 & chain A & name CB", "resi 203 & chain A & name CB")
cmd.distance("NonHBond", "resi 219 & chain A & name CB", "PseudoR201A")
cmd.distance("NonHBond", "resi 198 & chain A & name CB", "resi 194 & chain A & name CB")
cmd.distance("NonHBond", "resi 200 & chain A & name CB", "PseudoR192A")
cmd.distance("NonHBond", "resi 202 & chain A & name CB", "resi 190 & chain A & name CB")
cmd.distance("NonHBond", "resi 204 & chain A & name CB", "resi 188 & chain A & name CB")
cmd.distance("NonHBond", "resi 206 & chain A & name CB", "resi 186 & chain A & name CB")
cmd.distance("NonHBond", "resi 185 & chain A & name CB", "resi 178 & chain A & name CB")
cmd.distance("NonHBond", "PseudoR187A", "resi 176 & chain A & name CB")
cmd.distance("NonHBond", "resi 189 & chain A & name CB", "resi 174 & chain A & name CB")
cmd.distance("NonHBond", "resi 191 & chain A & name CB", "resi 172 & chain A & name CB")
cmd.distance("NonHBond", "resi 193 & chain A & name CB", "resi 170 & chain A & name CB")
cmd.distance("NonHBond", "resi 169 & chain A & name CB", "resi 133 & chain A & name CB")
cmd.distance("NonHBond", "resi 116 & chain A & name CB", "resi 134 & chain A & name CB")
cmd.distance("NonHBond", "resi 171 & chain A & name CB", "resi 131 & chain A & name CB")
cmd.distance("NonHBond", "resi 118 & chain A & name CB", "PseudoR132A")
cmd.distance("NonHBond", "resi 95 & chain A & name CB", "resi 78 & chain A & name CB")
cmd.distance("NonHBond", "resi 93 & chain A & name CB", "resi 80 & chain A & name CB")
cmd.distance("NonHBond", "resi 97 & chain A & name CB", "PseudoR76A")
cmd.distance("NonHBond", "PseudoR120A", "resi 130 & chain A & name CB")
cmd.distance("NonHBond", "resi 173 & chain A & name CB", "resi 129 & chain A & name CB")
cmd.distance("NonHBond", "resi 99 & chain A & name CB", "resi 74 & chain A & name CB")
cmd.distance("NonHBond", "resi 91 & chain A & name CB", "resi 82 & chain A & name CB")
cmd.distance("NonHBond", "resi 122 & chain A & name CB", "resi 128 & chain A & name CB")
cmd.distance("NonHBond", "resi 175 & chain A & name CB", "resi 127 & chain A & name CB")
cmd.distance("NonHBond", "resi 73 & chain A & name CB", "resi 59 & chain A & name CB")
cmd.distance("NonHBond", "resi 75 & chain A & name CB", "resi 57 & chain A & name CB")
cmd.distance("NonHBond", "resi 77 & chain A & name CB", "resi 55 & chain A & name CB")
cmd.distance("NonHBond", "PseudoR79A", "resi 53 & chain A & name CB")
cmd.distance("NonHBond", "resi 52 & chain A & name CB", "resi 30 & chain A & name CB")
cmd.distance("NonHBond", "resi 54 & chain A & name CB", "resi 28 & chain A & name CB")
cmd.distance("NonHBond", "resi 56 & chain A & name CB", "resi 26 & chain A & name CB")
cmd.distance("NonHBond", "resi 58 & chain A & name CB", "resi 24 & chain A & name CB")
cmd.distance("NonHBond", "resi 60 & chain A & name CB", "resi 22 & chain A & name CB")
cmd.distance("NonHBond", "resi 21 & chain A & name CB", "resi 11 & chain A & name CB")
cmd.distance("NonHBond", "PseudoR23A", "resi 9 & chain A & name CB")
cmd.distance("NonHBond", "resi 25 & chain A & name CB", "PseudoR7A")
cmd.distance("NonHBond", "PseudoR27A", "resi 5 & chain A & name CB")
cmd.distance("NonHBond", "resi 29 & chain A & name CB", "resi 3 & chain A & name CB")
cmd.distance("NonHBond", "resi 35 & chain A & name CB", "resi 0 & chain A & name CB")
cmd.show("stick", "barrel")
cmd.color("red","StrongHBond")
cmd.color("green","WeakHBond")
cmd.color("purpleblue","NonHBond")
cmd.color("magenta","PseudoR*")
cmd.color("green","name CA & barrel")
cmd.color("red","name O & barrel")
cmd.color("blue","name N & barrel")
cmd.hide("labels")
cmd.zoom("barrel")
