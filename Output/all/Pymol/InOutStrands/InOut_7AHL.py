from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/7AHL.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand1", "resi 111+112+113+114+115+116+117+118+119+120+121+122 & chain A ")


cmd.select("Bstrand12", "resi 132+133+134+135+136+137+138+139+140+141+142+143+144+145+146+147 & chain B ")


cmd.select("Bstrand11", "resi 111+112+113+114+115+116+117+118+119+120+121+122+123+124+125+126 & chain B ")


cmd.select("Cstrand22", "resi 135+136+137+138+139+140+141+142+143+144+145+146+147 & chain C ")


cmd.select("Cstrand21", "resi 111+112+113+114+115+116+117+118+119+120+121+122+123 & chain C ")


cmd.select("Dstrand32", "resi 136+137+138+139+140+141+142+143+144+145+146+147 & chain D ")


cmd.select("Dstrand31", "resi 111+112+113+114+115+116+117+118+119+120+121+122 & chain D ")


cmd.select("Estrand42", "resi 136+137+138+139+140+141+142+143+144+145+146+147 & chain E ")


cmd.select("Estrand41", "resi 111+112+113+114+115+116+117+118+119+120+121+122 & chain E ")


cmd.select("Fstrand52", "resi 132+133+134+135+136+137+138+139+140+141+142+143+144+145+146+147 & chain F ")


cmd.select("Fstrand51", "resi 111+112+113+114+115+116+117+118+119+120+121+122+123+124+125+126 & chain F ")


cmd.select("Gstrand62", "resi 132+133+134+135+136+137+138+139+140+141+142+143+144+145+146+147 & chain G ")


cmd.select("Gstrand61", "resi 111+112+113+114+115+116+117+118+119+120+121+122+123+124+125+126 & chain G ")


cmd.select("Astrand2", "resi 136+137+138+139+140+141+142+143+144+145+146+147 & chain A ")


cmd.select("barrel", "Astrand* or Bstrand* or Cstrand* or Dstrand* or Estrand* or Fstrand* or Gstrand*")
cmd.show("sticks", "barrel")
cmd.show("cartoon", "barrel")
cmd.set("cartoon_side_chain_helper", "on")
cmd.zoom("barrel")
cmd.color ("blue", "resi 111 & chain A")

cmd.select ("Outward", "resi 111 & chain A", merge=1)

cmd.color ("blue", "resi 112 & chain A")

cmd.select ("Outward", "resi 112 & chain A", merge=1)

cmd.color ("blue", "resi 113 & chain A")

cmd.select ("Outward", "resi 113 & chain A", merge=1)

cmd.color ("blue", "resi 114 & chain A")

cmd.select ("Outward", "resi 114 & chain A", merge=1)

cmd.color ("blue", "resi 115 & chain A")

cmd.select ("Outward", "resi 115 & chain A", merge=1)

cmd.color ("blue", "resi 116 & chain A")

cmd.select ("Outward", "resi 116 & chain A", merge=1)

cmd.color ("blue", "resi 117 & chain A")

cmd.select ("Outward", "resi 117 & chain A", merge=1)

cmd.color ("blue", "resi 118 & chain A")

cmd.select ("Outward", "resi 118 & chain A", merge=1)

cmd.color ("blue", "resi 119 & chain A")

cmd.select ("Outward", "resi 119 & chain A", merge=1)

cmd.color ("blue", "resi 120 & chain A")

cmd.select ("Outward", "resi 120 & chain A", merge=1)

cmd.color ("blue", "resi 121 & chain A")

cmd.select ("Outward", "resi 121 & chain A", merge=1)

cmd.color ("blue", "resi 122 & chain A")

cmd.select ("Outward", "resi 122 & chain A", merge=1)

cmd.color ("blue", "resi 132 & chain B")

cmd.select ("Outward", "resi 132 & chain B", merge=1)

cmd.color ("blue", "resi 133 & chain B")

cmd.select ("Outward", "resi 133 & chain B", merge=1)

cmd.color ("blue", "resi 134 & chain B")

cmd.select ("Outward", "resi 134 & chain B", merge=1)

cmd.color ("blue", "resi 135 & chain B")

cmd.select ("Outward", "resi 135 & chain B", merge=1)

cmd.color ("blue", "resi 136 & chain B")

cmd.select ("Outward", "resi 136 & chain B", merge=1)

cmd.color ("blue", "resi 137 & chain B")

cmd.select ("Outward", "resi 137 & chain B", merge=1)

cmd.color ("blue", "resi 138 & chain B")

cmd.select ("Outward", "resi 138 & chain B", merge=1)

cmd.color ("blue", "resi 139 & chain B")

cmd.select ("Outward", "resi 139 & chain B", merge=1)

cmd.color ("blue", "resi 140 & chain B")

cmd.select ("Outward", "resi 140 & chain B", merge=1)

cmd.color ("blue", "resi 141 & chain B")

cmd.select ("Outward", "resi 141 & chain B", merge=1)

cmd.color ("blue", "resi 142 & chain B")

cmd.select ("Outward", "resi 142 & chain B", merge=1)

cmd.color ("blue", "resi 143 & chain B")

cmd.select ("Outward", "resi 143 & chain B", merge=1)

cmd.color ("blue", "resi 144 & chain B")

cmd.select ("Outward", "resi 144 & chain B", merge=1)

cmd.color ("blue", "resi 145 & chain B")

cmd.select ("Outward", "resi 145 & chain B", merge=1)

cmd.color ("blue", "resi 146 & chain B")

cmd.select ("Outward", "resi 146 & chain B", merge=1)

cmd.color ("blue", "resi 147 & chain B")

cmd.select ("Outward", "resi 147 & chain B", merge=1)

cmd.color ("blue", "resi 111 & chain B")

cmd.select ("Outward", "resi 111 & chain B", merge=1)

cmd.color ("blue", "resi 112 & chain B")

cmd.select ("Outward", "resi 112 & chain B", merge=1)

cmd.color ("blue", "resi 113 & chain B")

cmd.select ("Outward", "resi 113 & chain B", merge=1)

cmd.color ("blue", "resi 114 & chain B")

cmd.select ("Outward", "resi 114 & chain B", merge=1)

cmd.color ("red", "resi 115 & chain B")

cmd.select ("Inward", "resi 115 & chain B", merge=1)

cmd.color ("blue", "resi 116 & chain B")

cmd.select ("Outward", "resi 116 & chain B", merge=1)

cmd.color ("blue", "resi 117 & chain B")

cmd.select ("Outward", "resi 117 & chain B", merge=1)

cmd.color ("blue", "resi 118 & chain B")

cmd.select ("Outward", "resi 118 & chain B", merge=1)

cmd.color ("blue", "resi 119 & chain B")

cmd.select ("Outward", "resi 119 & chain B", merge=1)

cmd.color ("blue", "resi 120 & chain B")

cmd.select ("Outward", "resi 120 & chain B", merge=1)

cmd.color ("blue", "resi 121 & chain B")

cmd.select ("Outward", "resi 121 & chain B", merge=1)

cmd.color ("blue", "resi 122 & chain B")

cmd.select ("Outward", "resi 122 & chain B", merge=1)

cmd.color ("blue", "resi 123 & chain B")

cmd.select ("Outward", "resi 123 & chain B", merge=1)

cmd.color ("blue", "resi 124 & chain B")

cmd.select ("Outward", "resi 124 & chain B", merge=1)

cmd.color ("blue", "resi 125 & chain B")

cmd.select ("Outward", "resi 125 & chain B", merge=1)

cmd.color ("blue", "resi 126 & chain B")

cmd.select ("Outward", "resi 126 & chain B", merge=1)

cmd.color ("blue", "resi 135 & chain C")

cmd.select ("Outward", "resi 135 & chain C", merge=1)

cmd.color ("blue", "resi 136 & chain C")

cmd.select ("Outward", "resi 136 & chain C", merge=1)

cmd.color ("blue", "resi 137 & chain C")

cmd.select ("Outward", "resi 137 & chain C", merge=1)

cmd.color ("blue", "resi 138 & chain C")

cmd.select ("Outward", "resi 138 & chain C", merge=1)

cmd.color ("blue", "resi 139 & chain C")

cmd.select ("Outward", "resi 139 & chain C", merge=1)

cmd.color ("blue", "resi 140 & chain C")

cmd.select ("Outward", "resi 140 & chain C", merge=1)

cmd.color ("blue", "resi 141 & chain C")

cmd.select ("Outward", "resi 141 & chain C", merge=1)

cmd.color ("blue", "resi 142 & chain C")

cmd.select ("Outward", "resi 142 & chain C", merge=1)

cmd.color ("blue", "resi 143 & chain C")

cmd.select ("Outward", "resi 143 & chain C", merge=1)

cmd.color ("blue", "resi 144 & chain C")

cmd.select ("Outward", "resi 144 & chain C", merge=1)

cmd.color ("blue", "resi 145 & chain C")

cmd.select ("Outward", "resi 145 & chain C", merge=1)

cmd.color ("blue", "resi 146 & chain C")

cmd.select ("Outward", "resi 146 & chain C", merge=1)

cmd.color ("blue", "resi 147 & chain C")

cmd.select ("Outward", "resi 147 & chain C", merge=1)

cmd.color ("blue", "resi 111 & chain C")

cmd.select ("Outward", "resi 111 & chain C", merge=1)

cmd.color ("blue", "resi 112 & chain C")

cmd.select ("Outward", "resi 112 & chain C", merge=1)

cmd.color ("blue", "resi 113 & chain C")

cmd.select ("Outward", "resi 113 & chain C", merge=1)

cmd.color ("blue", "resi 114 & chain C")

cmd.select ("Outward", "resi 114 & chain C", merge=1)

cmd.color ("blue", "resi 115 & chain C")

cmd.select ("Outward", "resi 115 & chain C", merge=1)

cmd.color ("blue", "resi 116 & chain C")

cmd.select ("Outward", "resi 116 & chain C", merge=1)

cmd.color ("blue", "resi 117 & chain C")

cmd.select ("Outward", "resi 117 & chain C", merge=1)

cmd.color ("blue", "resi 118 & chain C")

cmd.select ("Outward", "resi 118 & chain C", merge=1)

cmd.color ("blue", "resi 119 & chain C")

cmd.select ("Outward", "resi 119 & chain C", merge=1)

cmd.color ("blue", "resi 120 & chain C")

cmd.select ("Outward", "resi 120 & chain C", merge=1)

cmd.color ("blue", "resi 121 & chain C")

cmd.select ("Outward", "resi 121 & chain C", merge=1)

cmd.color ("blue", "resi 122 & chain C")

cmd.select ("Outward", "resi 122 & chain C", merge=1)

cmd.color ("blue", "resi 123 & chain C")

cmd.select ("Outward", "resi 123 & chain C", merge=1)

cmd.color ("blue", "resi 136 & chain D")

cmd.select ("Outward", "resi 136 & chain D", merge=1)

cmd.color ("blue", "resi 137 & chain D")

cmd.select ("Outward", "resi 137 & chain D", merge=1)

cmd.color ("blue", "resi 138 & chain D")

cmd.select ("Outward", "resi 138 & chain D", merge=1)

cmd.color ("blue", "resi 139 & chain D")

cmd.select ("Outward", "resi 139 & chain D", merge=1)

cmd.color ("blue", "resi 140 & chain D")

cmd.select ("Outward", "resi 140 & chain D", merge=1)

cmd.color ("blue", "resi 141 & chain D")

cmd.select ("Outward", "resi 141 & chain D", merge=1)

cmd.color ("blue", "resi 142 & chain D")

cmd.select ("Outward", "resi 142 & chain D", merge=1)

cmd.color ("blue", "resi 143 & chain D")

cmd.select ("Outward", "resi 143 & chain D", merge=1)

cmd.color ("blue", "resi 144 & chain D")

cmd.select ("Outward", "resi 144 & chain D", merge=1)

cmd.color ("blue", "resi 145 & chain D")

cmd.select ("Outward", "resi 145 & chain D", merge=1)

cmd.color ("blue", "resi 146 & chain D")

cmd.select ("Outward", "resi 146 & chain D", merge=1)

cmd.color ("blue", "resi 147 & chain D")

cmd.select ("Outward", "resi 147 & chain D", merge=1)

cmd.color ("red", "resi 111 & chain D")

cmd.select ("Inward", "resi 111 & chain D", merge=1)

cmd.color ("blue", "resi 112 & chain D")

cmd.select ("Outward", "resi 112 & chain D", merge=1)

cmd.color ("blue", "resi 113 & chain D")

cmd.select ("Outward", "resi 113 & chain D", merge=1)

cmd.color ("blue", "resi 114 & chain D")

cmd.select ("Outward", "resi 114 & chain D", merge=1)

cmd.color ("blue", "resi 115 & chain D")

cmd.select ("Outward", "resi 115 & chain D", merge=1)

cmd.color ("blue", "resi 116 & chain D")

cmd.select ("Outward", "resi 116 & chain D", merge=1)

cmd.color ("blue", "resi 117 & chain D")

cmd.select ("Outward", "resi 117 & chain D", merge=1)

cmd.color ("blue", "resi 118 & chain D")

cmd.select ("Outward", "resi 118 & chain D", merge=1)

cmd.color ("blue", "resi 119 & chain D")

cmd.select ("Outward", "resi 119 & chain D", merge=1)

cmd.color ("blue", "resi 120 & chain D")

cmd.select ("Outward", "resi 120 & chain D", merge=1)

cmd.color ("blue", "resi 121 & chain D")

cmd.select ("Outward", "resi 121 & chain D", merge=1)

cmd.color ("blue", "resi 122 & chain D")

cmd.select ("Outward", "resi 122 & chain D", merge=1)

cmd.color ("blue", "resi 136 & chain E")

cmd.select ("Outward", "resi 136 & chain E", merge=1)

cmd.color ("blue", "resi 137 & chain E")

cmd.select ("Outward", "resi 137 & chain E", merge=1)

cmd.color ("blue", "resi 138 & chain E")

cmd.select ("Outward", "resi 138 & chain E", merge=1)

cmd.color ("blue", "resi 139 & chain E")

cmd.select ("Outward", "resi 139 & chain E", merge=1)

cmd.color ("blue", "resi 140 & chain E")

cmd.select ("Outward", "resi 140 & chain E", merge=1)

cmd.color ("blue", "resi 141 & chain E")

cmd.select ("Outward", "resi 141 & chain E", merge=1)

cmd.color ("blue", "resi 142 & chain E")

cmd.select ("Outward", "resi 142 & chain E", merge=1)

cmd.color ("blue", "resi 143 & chain E")

cmd.select ("Outward", "resi 143 & chain E", merge=1)

cmd.color ("blue", "resi 144 & chain E")

cmd.select ("Outward", "resi 144 & chain E", merge=1)

cmd.color ("blue", "resi 145 & chain E")

cmd.select ("Outward", "resi 145 & chain E", merge=1)

cmd.color ("blue", "resi 146 & chain E")

cmd.select ("Outward", "resi 146 & chain E", merge=1)

cmd.color ("blue", "resi 147 & chain E")

cmd.select ("Outward", "resi 147 & chain E", merge=1)

cmd.color ("red", "resi 111 & chain E")

cmd.select ("Inward", "resi 111 & chain E", merge=1)

cmd.color ("blue", "resi 112 & chain E")

cmd.select ("Outward", "resi 112 & chain E", merge=1)

cmd.color ("blue", "resi 113 & chain E")

cmd.select ("Outward", "resi 113 & chain E", merge=1)

cmd.color ("blue", "resi 114 & chain E")

cmd.select ("Outward", "resi 114 & chain E", merge=1)

cmd.color ("blue", "resi 115 & chain E")

cmd.select ("Outward", "resi 115 & chain E", merge=1)

cmd.color ("blue", "resi 116 & chain E")

cmd.select ("Outward", "resi 116 & chain E", merge=1)

cmd.color ("blue", "resi 117 & chain E")

cmd.select ("Outward", "resi 117 & chain E", merge=1)

cmd.color ("blue", "resi 118 & chain E")

cmd.select ("Outward", "resi 118 & chain E", merge=1)

cmd.color ("blue", "resi 119 & chain E")

cmd.select ("Outward", "resi 119 & chain E", merge=1)

cmd.color ("blue", "resi 120 & chain E")

cmd.select ("Outward", "resi 120 & chain E", merge=1)

cmd.color ("blue", "resi 121 & chain E")

cmd.select ("Outward", "resi 121 & chain E", merge=1)

cmd.color ("blue", "resi 122 & chain E")

cmd.select ("Outward", "resi 122 & chain E", merge=1)

cmd.color ("blue", "resi 132 & chain F")

cmd.select ("Outward", "resi 132 & chain F", merge=1)

cmd.color ("blue", "resi 133 & chain F")

cmd.select ("Outward", "resi 133 & chain F", merge=1)

cmd.color ("blue", "resi 134 & chain F")

cmd.select ("Outward", "resi 134 & chain F", merge=1)

cmd.color ("blue", "resi 135 & chain F")

cmd.select ("Outward", "resi 135 & chain F", merge=1)

cmd.color ("blue", "resi 136 & chain F")

cmd.select ("Outward", "resi 136 & chain F", merge=1)

cmd.color ("blue", "resi 137 & chain F")

cmd.select ("Outward", "resi 137 & chain F", merge=1)

cmd.color ("blue", "resi 138 & chain F")

cmd.select ("Outward", "resi 138 & chain F", merge=1)

cmd.color ("blue", "resi 139 & chain F")

cmd.select ("Outward", "resi 139 & chain F", merge=1)

cmd.color ("blue", "resi 140 & chain F")

cmd.select ("Outward", "resi 140 & chain F", merge=1)

cmd.color ("blue", "resi 141 & chain F")

cmd.select ("Outward", "resi 141 & chain F", merge=1)

cmd.color ("blue", "resi 142 & chain F")

cmd.select ("Outward", "resi 142 & chain F", merge=1)

cmd.color ("blue", "resi 143 & chain F")

cmd.select ("Outward", "resi 143 & chain F", merge=1)

cmd.color ("blue", "resi 144 & chain F")

cmd.select ("Outward", "resi 144 & chain F", merge=1)

cmd.color ("blue", "resi 145 & chain F")

cmd.select ("Outward", "resi 145 & chain F", merge=1)

cmd.color ("blue", "resi 146 & chain F")

cmd.select ("Outward", "resi 146 & chain F", merge=1)

cmd.color ("blue", "resi 147 & chain F")

cmd.select ("Outward", "resi 147 & chain F", merge=1)

cmd.color ("blue", "resi 111 & chain F")

cmd.select ("Outward", "resi 111 & chain F", merge=1)

cmd.color ("blue", "resi 112 & chain F")

cmd.select ("Outward", "resi 112 & chain F", merge=1)

cmd.color ("blue", "resi 113 & chain F")

cmd.select ("Outward", "resi 113 & chain F", merge=1)

cmd.color ("blue", "resi 114 & chain F")

cmd.select ("Outward", "resi 114 & chain F", merge=1)

cmd.color ("blue", "resi 115 & chain F")

cmd.select ("Outward", "resi 115 & chain F", merge=1)

cmd.color ("blue", "resi 116 & chain F")

cmd.select ("Outward", "resi 116 & chain F", merge=1)

cmd.color ("blue", "resi 117 & chain F")

cmd.select ("Outward", "resi 117 & chain F", merge=1)

cmd.color ("blue", "resi 118 & chain F")

cmd.select ("Outward", "resi 118 & chain F", merge=1)

cmd.color ("blue", "resi 119 & chain F")

cmd.select ("Outward", "resi 119 & chain F", merge=1)

cmd.color ("blue", "resi 120 & chain F")

cmd.select ("Outward", "resi 120 & chain F", merge=1)

cmd.color ("blue", "resi 121 & chain F")

cmd.select ("Outward", "resi 121 & chain F", merge=1)

cmd.color ("blue", "resi 122 & chain F")

cmd.select ("Outward", "resi 122 & chain F", merge=1)

cmd.color ("blue", "resi 123 & chain F")

cmd.select ("Outward", "resi 123 & chain F", merge=1)

cmd.color ("blue", "resi 124 & chain F")

cmd.select ("Outward", "resi 124 & chain F", merge=1)

cmd.color ("blue", "resi 125 & chain F")

cmd.select ("Outward", "resi 125 & chain F", merge=1)

cmd.color ("blue", "resi 126 & chain F")

cmd.select ("Outward", "resi 126 & chain F", merge=1)

cmd.color ("blue", "resi 132 & chain G")

cmd.select ("Outward", "resi 132 & chain G", merge=1)

cmd.color ("blue", "resi 133 & chain G")

cmd.select ("Outward", "resi 133 & chain G", merge=1)

cmd.color ("blue", "resi 134 & chain G")

cmd.select ("Outward", "resi 134 & chain G", merge=1)

cmd.color ("blue", "resi 135 & chain G")

cmd.select ("Outward", "resi 135 & chain G", merge=1)

cmd.color ("blue", "resi 136 & chain G")

cmd.select ("Outward", "resi 136 & chain G", merge=1)

cmd.color ("blue", "resi 137 & chain G")

cmd.select ("Outward", "resi 137 & chain G", merge=1)

cmd.color ("blue", "resi 138 & chain G")

cmd.select ("Outward", "resi 138 & chain G", merge=1)

cmd.color ("blue", "resi 139 & chain G")

cmd.select ("Outward", "resi 139 & chain G", merge=1)

cmd.color ("blue", "resi 140 & chain G")

cmd.select ("Outward", "resi 140 & chain G", merge=1)

cmd.color ("blue", "resi 141 & chain G")

cmd.select ("Outward", "resi 141 & chain G", merge=1)

cmd.color ("blue", "resi 142 & chain G")

cmd.select ("Outward", "resi 142 & chain G", merge=1)

cmd.color ("blue", "resi 143 & chain G")

cmd.select ("Outward", "resi 143 & chain G", merge=1)

cmd.color ("blue", "resi 144 & chain G")

cmd.select ("Outward", "resi 144 & chain G", merge=1)

cmd.color ("blue", "resi 145 & chain G")

cmd.select ("Outward", "resi 145 & chain G", merge=1)

cmd.color ("blue", "resi 146 & chain G")

cmd.select ("Outward", "resi 146 & chain G", merge=1)

cmd.color ("blue", "resi 147 & chain G")

cmd.select ("Outward", "resi 147 & chain G", merge=1)

cmd.color ("blue", "resi 111 & chain G")

cmd.select ("Outward", "resi 111 & chain G", merge=1)

cmd.color ("blue", "resi 112 & chain G")

cmd.select ("Outward", "resi 112 & chain G", merge=1)

cmd.color ("blue", "resi 113 & chain G")

cmd.select ("Outward", "resi 113 & chain G", merge=1)

cmd.color ("blue", "resi 114 & chain G")

cmd.select ("Outward", "resi 114 & chain G", merge=1)

cmd.color ("blue", "resi 115 & chain G")

cmd.select ("Outward", "resi 115 & chain G", merge=1)

cmd.color ("blue", "resi 116 & chain G")

cmd.select ("Outward", "resi 116 & chain G", merge=1)

cmd.color ("blue", "resi 117 & chain G")

cmd.select ("Outward", "resi 117 & chain G", merge=1)

cmd.color ("blue", "resi 118 & chain G")

cmd.select ("Outward", "resi 118 & chain G", merge=1)

cmd.color ("blue", "resi 119 & chain G")

cmd.select ("Outward", "resi 119 & chain G", merge=1)

cmd.color ("blue", "resi 120 & chain G")

cmd.select ("Outward", "resi 120 & chain G", merge=1)

cmd.color ("blue", "resi 121 & chain G")

cmd.select ("Outward", "resi 121 & chain G", merge=1)

cmd.color ("blue", "resi 122 & chain G")

cmd.select ("Outward", "resi 122 & chain G", merge=1)

cmd.color ("blue", "resi 123 & chain G")

cmd.select ("Outward", "resi 123 & chain G", merge=1)

cmd.color ("blue", "resi 124 & chain G")

cmd.select ("Outward", "resi 124 & chain G", merge=1)

cmd.color ("blue", "resi 125 & chain G")

cmd.select ("Outward", "resi 125 & chain G", merge=1)

cmd.color ("blue", "resi 126 & chain G")

cmd.select ("Outward", "resi 126 & chain G", merge=1)

cmd.color ("blue", "resi 136 & chain A")

cmd.select ("Outward", "resi 136 & chain A", merge=1)

cmd.color ("blue", "resi 137 & chain A")

cmd.select ("Outward", "resi 137 & chain A", merge=1)

cmd.color ("blue", "resi 138 & chain A")

cmd.select ("Outward", "resi 138 & chain A", merge=1)

cmd.color ("blue", "resi 139 & chain A")

cmd.select ("Outward", "resi 139 & chain A", merge=1)

cmd.color ("blue", "resi 140 & chain A")

cmd.select ("Outward", "resi 140 & chain A", merge=1)

cmd.color ("blue", "resi 141 & chain A")

cmd.select ("Outward", "resi 141 & chain A", merge=1)

cmd.color ("blue", "resi 142 & chain A")

cmd.select ("Outward", "resi 142 & chain A", merge=1)

cmd.color ("blue", "resi 143 & chain A")

cmd.select ("Outward", "resi 143 & chain A", merge=1)

cmd.color ("blue", "resi 144 & chain A")

cmd.select ("Outward", "resi 144 & chain A", merge=1)

cmd.color ("blue", "resi 145 & chain A")

cmd.select ("Outward", "resi 145 & chain A", merge=1)

cmd.color ("blue", "resi 146 & chain A")

cmd.select ("Outward", "resi 146 & chain A", merge=1)

cmd.color ("blue", "resi 147 & chain A")

cmd.select ("Outward", "resi 147 & chain A", merge=1)

cmd.load_cgo( [9.0, 0,0,0, 0, 0, 0, 1, 1,1,0,0,0,1], "axis" )
