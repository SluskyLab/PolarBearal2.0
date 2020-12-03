from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/6RB9.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand3", "resi 97+98+99+100+101+102+103+104+105+106+107+108+109+110+111+112+113+114+115+116+117+118+119+120+121+122+123+124+125+126+127+128+129+130+131+132 & chain A ")


cmd.select("Astrand4", "resi 136+137+138+139+140+141+142+143+144+145+146+147+148+149+150+151+152+153+154+155+156+157+158+159+160+161+162+163+164+165+166+167+168+169+170+171 & chain A ")


cmd.select("Bstrand14", "resi 136+137+138+139+140+141+142+143+144+145+146+147+148+149+150+151+152+153+154+155+156+157+158+159+160+161+162+163+164+165+166+167+168+169+170+171 & chain B ")


cmd.select("Bstrand13", "resi 97+98+99+100+101+102+103+104+105+106+107+108+109+110+111+112+113+114+115+116+117+118+119+120+121+122+123+124+125+126+127+128+129+130+131+132 & chain B ")


cmd.select("Cstrand24", "resi 136+137+138+139+140+141+142+143+144+145+146+147+148+149+150+151+152+153+154+155+156+157+158+159+160+161+162+163+164+165+166+167+168+169+170+171 & chain C ")


cmd.select("Cstrand23", "resi 97+98+99+100+101+102+103+104+105+106+107+108+109+110+111+112+113+114+115+116+117+118+119+120+121+122+123+124+125+126+127+128+129+130+131+132 & chain C ")


cmd.select("Dstrand34", "resi 136+137+138+139+140+141+142+143+144+145+146+147+148+149+150+151+152+153+154+155+156+157+158+159+160+161+162+163+164+165+166+167+168+169+170+171 & chain D ")


cmd.select("Dstrand33", "resi 97+98+99+100+101+102+103+104+105+106+107+108+109+110+111+112+113+114+115+116+117+118+119+120+121+122+123+124+125+126+127+128+129+130+131+132 & chain D ")


cmd.select("Estrand44", "resi 136+137+138+139+140+141+142+143+144+145+146+147+148+149+150+151+152+153+154+155+156+157+158+159+160+161+162+163+164+165+166+167+168+169+170+171 & chain E ")


cmd.select("Estrand43", "resi 97+98+99+100+101+102+103+104+105+106+107+108+109+110+111+112+113+114+115+116+117+118+119+120+121+122+123+124+125+126+127+128+129+130+131+132 & chain E ")


cmd.select("Fstrand54", "resi 136+137+138+139+140+141+142+143+144+145+146+147+148+149+150+151+152+153+154+155+156+157+158+159+160+161+162+163+164+165+166+167+168+169+170+171 & chain F ")


cmd.select("Fstrand53", "resi 97+98+99+100+101+102+103+104+105+106+107+108+109+110+111+112+113+114+115+116+117+118+119+120+121+122+123+124+125+126+127+128+129+130+131+132 & chain F ")


cmd.select("Gstrand63", "resi 97+98+99+100+101+102+103+104+105+106+107+108+109+110+111+112+113+114+115+116+117+118+119+120+121+122+123+124+125+126+127+128+129+130+131+132 & chain G ")


cmd.select("Gstrand64", "resi 136+137+138+139+140+141+142+143+144+145+146+147+148+149+150+151+152+153+154+155+156+157+158+159+160+161+162+163+164+165+166+167+168+169+170+171 & chain G ")


cmd.select("barrel", "Astrand* or Bstrand* or Cstrand* or Dstrand* or Estrand* or Fstrand* or Gstrand*")
cmd.show("sticks", "barrel")
cmd.show("cartoon", "barrel")
cmd.set("cartoon_side_chain_helper", "on")
cmd.zoom("barrel")
cmd.color ("blue", "resi 97 & chain A")

cmd.select ("Outward", "resi 97 & chain A", merge=1)

cmd.color ("blue", "resi 98 & chain A")

cmd.select ("Outward", "resi 98 & chain A", merge=1)

cmd.color ("blue", "resi 99 & chain A")

cmd.select ("Outward", "resi 99 & chain A", merge=1)

cmd.color ("blue", "resi 100 & chain A")

cmd.select ("Outward", "resi 100 & chain A", merge=1)

cmd.color ("blue", "resi 101 & chain A")

cmd.select ("Outward", "resi 101 & chain A", merge=1)

cmd.color ("blue", "resi 102 & chain A")

cmd.select ("Outward", "resi 102 & chain A", merge=1)

cmd.color ("blue", "resi 103 & chain A")

cmd.select ("Outward", "resi 103 & chain A", merge=1)

cmd.color ("blue", "resi 104 & chain A")

cmd.select ("Outward", "resi 104 & chain A", merge=1)

cmd.color ("blue", "resi 105 & chain A")

cmd.select ("Outward", "resi 105 & chain A", merge=1)

cmd.color ("blue", "resi 106 & chain A")

cmd.select ("Outward", "resi 106 & chain A", merge=1)

cmd.color ("blue", "resi 107 & chain A")

cmd.select ("Outward", "resi 107 & chain A", merge=1)

cmd.color ("blue", "resi 108 & chain A")

cmd.select ("Outward", "resi 108 & chain A", merge=1)

cmd.color ("blue", "resi 109 & chain A")

cmd.select ("Outward", "resi 109 & chain A", merge=1)

cmd.color ("blue", "resi 110 & chain A")

cmd.select ("Outward", "resi 110 & chain A", merge=1)

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

cmd.color ("blue", "resi 123 & chain A")

cmd.select ("Outward", "resi 123 & chain A", merge=1)

cmd.color ("blue", "resi 124 & chain A")

cmd.select ("Outward", "resi 124 & chain A", merge=1)

cmd.color ("blue", "resi 125 & chain A")

cmd.select ("Outward", "resi 125 & chain A", merge=1)

cmd.color ("blue", "resi 126 & chain A")

cmd.select ("Outward", "resi 126 & chain A", merge=1)

cmd.color ("blue", "resi 127 & chain A")

cmd.select ("Outward", "resi 127 & chain A", merge=1)

cmd.color ("blue", "resi 128 & chain A")

cmd.select ("Outward", "resi 128 & chain A", merge=1)

cmd.color ("blue", "resi 129 & chain A")

cmd.select ("Outward", "resi 129 & chain A", merge=1)

cmd.color ("blue", "resi 130 & chain A")

cmd.select ("Outward", "resi 130 & chain A", merge=1)

cmd.color ("blue", "resi 131 & chain A")

cmd.select ("Outward", "resi 131 & chain A", merge=1)

cmd.color ("blue", "resi 132 & chain A")

cmd.select ("Outward", "resi 132 & chain A", merge=1)

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

cmd.color ("blue", "resi 148 & chain A")

cmd.select ("Outward", "resi 148 & chain A", merge=1)

cmd.color ("blue", "resi 149 & chain A")

cmd.select ("Outward", "resi 149 & chain A", merge=1)

cmd.color ("blue", "resi 150 & chain A")

cmd.select ("Outward", "resi 150 & chain A", merge=1)

cmd.color ("blue", "resi 151 & chain A")

cmd.select ("Outward", "resi 151 & chain A", merge=1)

cmd.color ("blue", "resi 152 & chain A")

cmd.select ("Outward", "resi 152 & chain A", merge=1)

cmd.color ("blue", "resi 153 & chain A")

cmd.select ("Outward", "resi 153 & chain A", merge=1)

cmd.color ("blue", "resi 154 & chain A")

cmd.select ("Outward", "resi 154 & chain A", merge=1)

cmd.color ("blue", "resi 155 & chain A")

cmd.select ("Outward", "resi 155 & chain A", merge=1)

cmd.color ("blue", "resi 156 & chain A")

cmd.select ("Outward", "resi 156 & chain A", merge=1)

cmd.color ("blue", "resi 157 & chain A")

cmd.select ("Outward", "resi 157 & chain A", merge=1)

cmd.color ("blue", "resi 158 & chain A")

cmd.select ("Outward", "resi 158 & chain A", merge=1)

cmd.color ("blue", "resi 159 & chain A")

cmd.select ("Outward", "resi 159 & chain A", merge=1)

cmd.color ("blue", "resi 160 & chain A")

cmd.select ("Outward", "resi 160 & chain A", merge=1)

cmd.color ("blue", "resi 161 & chain A")

cmd.select ("Outward", "resi 161 & chain A", merge=1)

cmd.color ("blue", "resi 162 & chain A")

cmd.select ("Outward", "resi 162 & chain A", merge=1)

cmd.color ("blue", "resi 163 & chain A")

cmd.select ("Outward", "resi 163 & chain A", merge=1)

cmd.color ("blue", "resi 164 & chain A")

cmd.select ("Outward", "resi 164 & chain A", merge=1)

cmd.color ("blue", "resi 165 & chain A")

cmd.select ("Outward", "resi 165 & chain A", merge=1)

cmd.color ("blue", "resi 166 & chain A")

cmd.select ("Outward", "resi 166 & chain A", merge=1)

cmd.color ("blue", "resi 167 & chain A")

cmd.select ("Outward", "resi 167 & chain A", merge=1)

cmd.color ("blue", "resi 168 & chain A")

cmd.select ("Outward", "resi 168 & chain A", merge=1)

cmd.color ("blue", "resi 169 & chain A")

cmd.select ("Outward", "resi 169 & chain A", merge=1)

cmd.color ("blue", "resi 170 & chain A")

cmd.select ("Outward", "resi 170 & chain A", merge=1)

cmd.color ("blue", "resi 171 & chain A")

cmd.select ("Outward", "resi 171 & chain A", merge=1)

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

cmd.color ("blue", "resi 148 & chain B")

cmd.select ("Outward", "resi 148 & chain B", merge=1)

cmd.color ("blue", "resi 149 & chain B")

cmd.select ("Outward", "resi 149 & chain B", merge=1)

cmd.color ("blue", "resi 150 & chain B")

cmd.select ("Outward", "resi 150 & chain B", merge=1)

cmd.color ("blue", "resi 151 & chain B")

cmd.select ("Outward", "resi 151 & chain B", merge=1)

cmd.color ("blue", "resi 152 & chain B")

cmd.select ("Outward", "resi 152 & chain B", merge=1)

cmd.color ("blue", "resi 153 & chain B")

cmd.select ("Outward", "resi 153 & chain B", merge=1)

cmd.color ("blue", "resi 154 & chain B")

cmd.select ("Outward", "resi 154 & chain B", merge=1)

cmd.color ("blue", "resi 155 & chain B")

cmd.select ("Outward", "resi 155 & chain B", merge=1)

cmd.color ("blue", "resi 156 & chain B")

cmd.select ("Outward", "resi 156 & chain B", merge=1)

cmd.color ("blue", "resi 157 & chain B")

cmd.select ("Outward", "resi 157 & chain B", merge=1)

cmd.color ("blue", "resi 158 & chain B")

cmd.select ("Outward", "resi 158 & chain B", merge=1)

cmd.color ("blue", "resi 159 & chain B")

cmd.select ("Outward", "resi 159 & chain B", merge=1)

cmd.color ("blue", "resi 160 & chain B")

cmd.select ("Outward", "resi 160 & chain B", merge=1)

cmd.color ("blue", "resi 161 & chain B")

cmd.select ("Outward", "resi 161 & chain B", merge=1)

cmd.color ("blue", "resi 162 & chain B")

cmd.select ("Outward", "resi 162 & chain B", merge=1)

cmd.color ("blue", "resi 163 & chain B")

cmd.select ("Outward", "resi 163 & chain B", merge=1)

cmd.color ("blue", "resi 164 & chain B")

cmd.select ("Outward", "resi 164 & chain B", merge=1)

cmd.color ("blue", "resi 165 & chain B")

cmd.select ("Outward", "resi 165 & chain B", merge=1)

cmd.color ("blue", "resi 166 & chain B")

cmd.select ("Outward", "resi 166 & chain B", merge=1)

cmd.color ("blue", "resi 167 & chain B")

cmd.select ("Outward", "resi 167 & chain B", merge=1)

cmd.color ("blue", "resi 168 & chain B")

cmd.select ("Outward", "resi 168 & chain B", merge=1)

cmd.color ("blue", "resi 169 & chain B")

cmd.select ("Outward", "resi 169 & chain B", merge=1)

cmd.color ("blue", "resi 170 & chain B")

cmd.select ("Outward", "resi 170 & chain B", merge=1)

cmd.color ("blue", "resi 171 & chain B")

cmd.select ("Outward", "resi 171 & chain B", merge=1)

cmd.color ("blue", "resi 97 & chain B")

cmd.select ("Outward", "resi 97 & chain B", merge=1)

cmd.color ("blue", "resi 98 & chain B")

cmd.select ("Outward", "resi 98 & chain B", merge=1)

cmd.color ("blue", "resi 99 & chain B")

cmd.select ("Outward", "resi 99 & chain B", merge=1)

cmd.color ("blue", "resi 100 & chain B")

cmd.select ("Outward", "resi 100 & chain B", merge=1)

cmd.color ("blue", "resi 101 & chain B")

cmd.select ("Outward", "resi 101 & chain B", merge=1)

cmd.color ("blue", "resi 102 & chain B")

cmd.select ("Outward", "resi 102 & chain B", merge=1)

cmd.color ("blue", "resi 103 & chain B")

cmd.select ("Outward", "resi 103 & chain B", merge=1)

cmd.color ("blue", "resi 104 & chain B")

cmd.select ("Outward", "resi 104 & chain B", merge=1)

cmd.color ("blue", "resi 105 & chain B")

cmd.select ("Outward", "resi 105 & chain B", merge=1)

cmd.color ("blue", "resi 106 & chain B")

cmd.select ("Outward", "resi 106 & chain B", merge=1)

cmd.color ("blue", "resi 107 & chain B")

cmd.select ("Outward", "resi 107 & chain B", merge=1)

cmd.color ("blue", "resi 108 & chain B")

cmd.select ("Outward", "resi 108 & chain B", merge=1)

cmd.color ("blue", "resi 109 & chain B")

cmd.select ("Outward", "resi 109 & chain B", merge=1)

cmd.color ("blue", "resi 110 & chain B")

cmd.select ("Outward", "resi 110 & chain B", merge=1)

cmd.color ("blue", "resi 111 & chain B")

cmd.select ("Outward", "resi 111 & chain B", merge=1)

cmd.color ("blue", "resi 112 & chain B")

cmd.select ("Outward", "resi 112 & chain B", merge=1)

cmd.color ("blue", "resi 113 & chain B")

cmd.select ("Outward", "resi 113 & chain B", merge=1)

cmd.color ("blue", "resi 114 & chain B")

cmd.select ("Outward", "resi 114 & chain B", merge=1)

cmd.color ("blue", "resi 115 & chain B")

cmd.select ("Outward", "resi 115 & chain B", merge=1)

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

cmd.color ("blue", "resi 127 & chain B")

cmd.select ("Outward", "resi 127 & chain B", merge=1)

cmd.color ("blue", "resi 128 & chain B")

cmd.select ("Outward", "resi 128 & chain B", merge=1)

cmd.color ("blue", "resi 129 & chain B")

cmd.select ("Outward", "resi 129 & chain B", merge=1)

cmd.color ("blue", "resi 130 & chain B")

cmd.select ("Outward", "resi 130 & chain B", merge=1)

cmd.color ("blue", "resi 131 & chain B")

cmd.select ("Outward", "resi 131 & chain B", merge=1)

cmd.color ("blue", "resi 132 & chain B")

cmd.select ("Outward", "resi 132 & chain B", merge=1)

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

cmd.color ("blue", "resi 148 & chain C")

cmd.select ("Outward", "resi 148 & chain C", merge=1)

cmd.color ("blue", "resi 149 & chain C")

cmd.select ("Outward", "resi 149 & chain C", merge=1)

cmd.color ("blue", "resi 150 & chain C")

cmd.select ("Outward", "resi 150 & chain C", merge=1)

cmd.color ("blue", "resi 151 & chain C")

cmd.select ("Outward", "resi 151 & chain C", merge=1)

cmd.color ("blue", "resi 152 & chain C")

cmd.select ("Outward", "resi 152 & chain C", merge=1)

cmd.color ("blue", "resi 153 & chain C")

cmd.select ("Outward", "resi 153 & chain C", merge=1)

cmd.color ("blue", "resi 154 & chain C")

cmd.select ("Outward", "resi 154 & chain C", merge=1)

cmd.color ("blue", "resi 155 & chain C")

cmd.select ("Outward", "resi 155 & chain C", merge=1)

cmd.color ("blue", "resi 156 & chain C")

cmd.select ("Outward", "resi 156 & chain C", merge=1)

cmd.color ("blue", "resi 157 & chain C")

cmd.select ("Outward", "resi 157 & chain C", merge=1)

cmd.color ("blue", "resi 158 & chain C")

cmd.select ("Outward", "resi 158 & chain C", merge=1)

cmd.color ("blue", "resi 159 & chain C")

cmd.select ("Outward", "resi 159 & chain C", merge=1)

cmd.color ("blue", "resi 160 & chain C")

cmd.select ("Outward", "resi 160 & chain C", merge=1)

cmd.color ("blue", "resi 161 & chain C")

cmd.select ("Outward", "resi 161 & chain C", merge=1)

cmd.color ("blue", "resi 162 & chain C")

cmd.select ("Outward", "resi 162 & chain C", merge=1)

cmd.color ("blue", "resi 163 & chain C")

cmd.select ("Outward", "resi 163 & chain C", merge=1)

cmd.color ("blue", "resi 164 & chain C")

cmd.select ("Outward", "resi 164 & chain C", merge=1)

cmd.color ("blue", "resi 165 & chain C")

cmd.select ("Outward", "resi 165 & chain C", merge=1)

cmd.color ("blue", "resi 166 & chain C")

cmd.select ("Outward", "resi 166 & chain C", merge=1)

cmd.color ("blue", "resi 167 & chain C")

cmd.select ("Outward", "resi 167 & chain C", merge=1)

cmd.color ("blue", "resi 168 & chain C")

cmd.select ("Outward", "resi 168 & chain C", merge=1)

cmd.color ("blue", "resi 169 & chain C")

cmd.select ("Outward", "resi 169 & chain C", merge=1)

cmd.color ("blue", "resi 170 & chain C")

cmd.select ("Outward", "resi 170 & chain C", merge=1)

cmd.color ("blue", "resi 171 & chain C")

cmd.select ("Outward", "resi 171 & chain C", merge=1)

cmd.color ("blue", "resi 97 & chain C")

cmd.select ("Outward", "resi 97 & chain C", merge=1)

cmd.color ("blue", "resi 98 & chain C")

cmd.select ("Outward", "resi 98 & chain C", merge=1)

cmd.color ("blue", "resi 99 & chain C")

cmd.select ("Outward", "resi 99 & chain C", merge=1)

cmd.color ("blue", "resi 100 & chain C")

cmd.select ("Outward", "resi 100 & chain C", merge=1)

cmd.color ("blue", "resi 101 & chain C")

cmd.select ("Outward", "resi 101 & chain C", merge=1)

cmd.color ("blue", "resi 102 & chain C")

cmd.select ("Outward", "resi 102 & chain C", merge=1)

cmd.color ("blue", "resi 103 & chain C")

cmd.select ("Outward", "resi 103 & chain C", merge=1)

cmd.color ("blue", "resi 104 & chain C")

cmd.select ("Outward", "resi 104 & chain C", merge=1)

cmd.color ("blue", "resi 105 & chain C")

cmd.select ("Outward", "resi 105 & chain C", merge=1)

cmd.color ("blue", "resi 106 & chain C")

cmd.select ("Outward", "resi 106 & chain C", merge=1)

cmd.color ("blue", "resi 107 & chain C")

cmd.select ("Outward", "resi 107 & chain C", merge=1)

cmd.color ("blue", "resi 108 & chain C")

cmd.select ("Outward", "resi 108 & chain C", merge=1)

cmd.color ("blue", "resi 109 & chain C")

cmd.select ("Outward", "resi 109 & chain C", merge=1)

cmd.color ("blue", "resi 110 & chain C")

cmd.select ("Outward", "resi 110 & chain C", merge=1)

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

cmd.color ("blue", "resi 124 & chain C")

cmd.select ("Outward", "resi 124 & chain C", merge=1)

cmd.color ("blue", "resi 125 & chain C")

cmd.select ("Outward", "resi 125 & chain C", merge=1)

cmd.color ("blue", "resi 126 & chain C")

cmd.select ("Outward", "resi 126 & chain C", merge=1)

cmd.color ("blue", "resi 127 & chain C")

cmd.select ("Outward", "resi 127 & chain C", merge=1)

cmd.color ("blue", "resi 128 & chain C")

cmd.select ("Outward", "resi 128 & chain C", merge=1)

cmd.color ("blue", "resi 129 & chain C")

cmd.select ("Outward", "resi 129 & chain C", merge=1)

cmd.color ("blue", "resi 130 & chain C")

cmd.select ("Outward", "resi 130 & chain C", merge=1)

cmd.color ("blue", "resi 131 & chain C")

cmd.select ("Outward", "resi 131 & chain C", merge=1)

cmd.color ("blue", "resi 132 & chain C")

cmd.select ("Outward", "resi 132 & chain C", merge=1)

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

cmd.color ("blue", "resi 148 & chain D")

cmd.select ("Outward", "resi 148 & chain D", merge=1)

cmd.color ("blue", "resi 149 & chain D")

cmd.select ("Outward", "resi 149 & chain D", merge=1)

cmd.color ("blue", "resi 150 & chain D")

cmd.select ("Outward", "resi 150 & chain D", merge=1)

cmd.color ("blue", "resi 151 & chain D")

cmd.select ("Outward", "resi 151 & chain D", merge=1)

cmd.color ("blue", "resi 152 & chain D")

cmd.select ("Outward", "resi 152 & chain D", merge=1)

cmd.color ("blue", "resi 153 & chain D")

cmd.select ("Outward", "resi 153 & chain D", merge=1)

cmd.color ("blue", "resi 154 & chain D")

cmd.select ("Outward", "resi 154 & chain D", merge=1)

cmd.color ("blue", "resi 155 & chain D")

cmd.select ("Outward", "resi 155 & chain D", merge=1)

cmd.color ("blue", "resi 156 & chain D")

cmd.select ("Outward", "resi 156 & chain D", merge=1)

cmd.color ("blue", "resi 157 & chain D")

cmd.select ("Outward", "resi 157 & chain D", merge=1)

cmd.color ("blue", "resi 158 & chain D")

cmd.select ("Outward", "resi 158 & chain D", merge=1)

cmd.color ("blue", "resi 159 & chain D")

cmd.select ("Outward", "resi 159 & chain D", merge=1)

cmd.color ("blue", "resi 160 & chain D")

cmd.select ("Outward", "resi 160 & chain D", merge=1)

cmd.color ("blue", "resi 161 & chain D")

cmd.select ("Outward", "resi 161 & chain D", merge=1)

cmd.color ("blue", "resi 162 & chain D")

cmd.select ("Outward", "resi 162 & chain D", merge=1)

cmd.color ("blue", "resi 163 & chain D")

cmd.select ("Outward", "resi 163 & chain D", merge=1)

cmd.color ("blue", "resi 164 & chain D")

cmd.select ("Outward", "resi 164 & chain D", merge=1)

cmd.color ("blue", "resi 165 & chain D")

cmd.select ("Outward", "resi 165 & chain D", merge=1)

cmd.color ("blue", "resi 166 & chain D")

cmd.select ("Outward", "resi 166 & chain D", merge=1)

cmd.color ("blue", "resi 167 & chain D")

cmd.select ("Outward", "resi 167 & chain D", merge=1)

cmd.color ("blue", "resi 168 & chain D")

cmd.select ("Outward", "resi 168 & chain D", merge=1)

cmd.color ("blue", "resi 169 & chain D")

cmd.select ("Outward", "resi 169 & chain D", merge=1)

cmd.color ("blue", "resi 170 & chain D")

cmd.select ("Outward", "resi 170 & chain D", merge=1)

cmd.color ("blue", "resi 171 & chain D")

cmd.select ("Outward", "resi 171 & chain D", merge=1)

cmd.color ("blue", "resi 97 & chain D")

cmd.select ("Outward", "resi 97 & chain D", merge=1)

cmd.color ("blue", "resi 98 & chain D")

cmd.select ("Outward", "resi 98 & chain D", merge=1)

cmd.color ("blue", "resi 99 & chain D")

cmd.select ("Outward", "resi 99 & chain D", merge=1)

cmd.color ("blue", "resi 100 & chain D")

cmd.select ("Outward", "resi 100 & chain D", merge=1)

cmd.color ("blue", "resi 101 & chain D")

cmd.select ("Outward", "resi 101 & chain D", merge=1)

cmd.color ("blue", "resi 102 & chain D")

cmd.select ("Outward", "resi 102 & chain D", merge=1)

cmd.color ("blue", "resi 103 & chain D")

cmd.select ("Outward", "resi 103 & chain D", merge=1)

cmd.color ("blue", "resi 104 & chain D")

cmd.select ("Outward", "resi 104 & chain D", merge=1)

cmd.color ("blue", "resi 105 & chain D")

cmd.select ("Outward", "resi 105 & chain D", merge=1)

cmd.color ("blue", "resi 106 & chain D")

cmd.select ("Outward", "resi 106 & chain D", merge=1)

cmd.color ("blue", "resi 107 & chain D")

cmd.select ("Outward", "resi 107 & chain D", merge=1)

cmd.color ("blue", "resi 108 & chain D")

cmd.select ("Outward", "resi 108 & chain D", merge=1)

cmd.color ("blue", "resi 109 & chain D")

cmd.select ("Outward", "resi 109 & chain D", merge=1)

cmd.color ("blue", "resi 110 & chain D")

cmd.select ("Outward", "resi 110 & chain D", merge=1)

cmd.color ("blue", "resi 111 & chain D")

cmd.select ("Outward", "resi 111 & chain D", merge=1)

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

cmd.color ("blue", "resi 123 & chain D")

cmd.select ("Outward", "resi 123 & chain D", merge=1)

cmd.color ("blue", "resi 124 & chain D")

cmd.select ("Outward", "resi 124 & chain D", merge=1)

cmd.color ("blue", "resi 125 & chain D")

cmd.select ("Outward", "resi 125 & chain D", merge=1)

cmd.color ("blue", "resi 126 & chain D")

cmd.select ("Outward", "resi 126 & chain D", merge=1)

cmd.color ("blue", "resi 127 & chain D")

cmd.select ("Outward", "resi 127 & chain D", merge=1)

cmd.color ("blue", "resi 128 & chain D")

cmd.select ("Outward", "resi 128 & chain D", merge=1)

cmd.color ("blue", "resi 129 & chain D")

cmd.select ("Outward", "resi 129 & chain D", merge=1)

cmd.color ("blue", "resi 130 & chain D")

cmd.select ("Outward", "resi 130 & chain D", merge=1)

cmd.color ("blue", "resi 131 & chain D")

cmd.select ("Outward", "resi 131 & chain D", merge=1)

cmd.color ("blue", "resi 132 & chain D")

cmd.select ("Outward", "resi 132 & chain D", merge=1)

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

cmd.color ("blue", "resi 148 & chain E")

cmd.select ("Outward", "resi 148 & chain E", merge=1)

cmd.color ("blue", "resi 149 & chain E")

cmd.select ("Outward", "resi 149 & chain E", merge=1)

cmd.color ("blue", "resi 150 & chain E")

cmd.select ("Outward", "resi 150 & chain E", merge=1)

cmd.color ("blue", "resi 151 & chain E")

cmd.select ("Outward", "resi 151 & chain E", merge=1)

cmd.color ("blue", "resi 152 & chain E")

cmd.select ("Outward", "resi 152 & chain E", merge=1)

cmd.color ("blue", "resi 153 & chain E")

cmd.select ("Outward", "resi 153 & chain E", merge=1)

cmd.color ("blue", "resi 154 & chain E")

cmd.select ("Outward", "resi 154 & chain E", merge=1)

cmd.color ("blue", "resi 155 & chain E")

cmd.select ("Outward", "resi 155 & chain E", merge=1)

cmd.color ("blue", "resi 156 & chain E")

cmd.select ("Outward", "resi 156 & chain E", merge=1)

cmd.color ("blue", "resi 157 & chain E")

cmd.select ("Outward", "resi 157 & chain E", merge=1)

cmd.color ("blue", "resi 158 & chain E")

cmd.select ("Outward", "resi 158 & chain E", merge=1)

cmd.color ("blue", "resi 159 & chain E")

cmd.select ("Outward", "resi 159 & chain E", merge=1)

cmd.color ("blue", "resi 160 & chain E")

cmd.select ("Outward", "resi 160 & chain E", merge=1)

cmd.color ("blue", "resi 161 & chain E")

cmd.select ("Outward", "resi 161 & chain E", merge=1)

cmd.color ("blue", "resi 162 & chain E")

cmd.select ("Outward", "resi 162 & chain E", merge=1)

cmd.color ("blue", "resi 163 & chain E")

cmd.select ("Outward", "resi 163 & chain E", merge=1)

cmd.color ("blue", "resi 164 & chain E")

cmd.select ("Outward", "resi 164 & chain E", merge=1)

cmd.color ("blue", "resi 165 & chain E")

cmd.select ("Outward", "resi 165 & chain E", merge=1)

cmd.color ("blue", "resi 166 & chain E")

cmd.select ("Outward", "resi 166 & chain E", merge=1)

cmd.color ("blue", "resi 167 & chain E")

cmd.select ("Outward", "resi 167 & chain E", merge=1)

cmd.color ("blue", "resi 168 & chain E")

cmd.select ("Outward", "resi 168 & chain E", merge=1)

cmd.color ("blue", "resi 169 & chain E")

cmd.select ("Outward", "resi 169 & chain E", merge=1)

cmd.color ("blue", "resi 170 & chain E")

cmd.select ("Outward", "resi 170 & chain E", merge=1)

cmd.color ("blue", "resi 171 & chain E")

cmd.select ("Outward", "resi 171 & chain E", merge=1)

cmd.color ("blue", "resi 97 & chain E")

cmd.select ("Outward", "resi 97 & chain E", merge=1)

cmd.color ("blue", "resi 98 & chain E")

cmd.select ("Outward", "resi 98 & chain E", merge=1)

cmd.color ("blue", "resi 99 & chain E")

cmd.select ("Outward", "resi 99 & chain E", merge=1)

cmd.color ("blue", "resi 100 & chain E")

cmd.select ("Outward", "resi 100 & chain E", merge=1)

cmd.color ("blue", "resi 101 & chain E")

cmd.select ("Outward", "resi 101 & chain E", merge=1)

cmd.color ("blue", "resi 102 & chain E")

cmd.select ("Outward", "resi 102 & chain E", merge=1)

cmd.color ("blue", "resi 103 & chain E")

cmd.select ("Outward", "resi 103 & chain E", merge=1)

cmd.color ("blue", "resi 104 & chain E")

cmd.select ("Outward", "resi 104 & chain E", merge=1)

cmd.color ("blue", "resi 105 & chain E")

cmd.select ("Outward", "resi 105 & chain E", merge=1)

cmd.color ("blue", "resi 106 & chain E")

cmd.select ("Outward", "resi 106 & chain E", merge=1)

cmd.color ("blue", "resi 107 & chain E")

cmd.select ("Outward", "resi 107 & chain E", merge=1)

cmd.color ("blue", "resi 108 & chain E")

cmd.select ("Outward", "resi 108 & chain E", merge=1)

cmd.color ("blue", "resi 109 & chain E")

cmd.select ("Outward", "resi 109 & chain E", merge=1)

cmd.color ("blue", "resi 110 & chain E")

cmd.select ("Outward", "resi 110 & chain E", merge=1)

cmd.color ("blue", "resi 111 & chain E")

cmd.select ("Outward", "resi 111 & chain E", merge=1)

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

cmd.color ("blue", "resi 123 & chain E")

cmd.select ("Outward", "resi 123 & chain E", merge=1)

cmd.color ("blue", "resi 124 & chain E")

cmd.select ("Outward", "resi 124 & chain E", merge=1)

cmd.color ("blue", "resi 125 & chain E")

cmd.select ("Outward", "resi 125 & chain E", merge=1)

cmd.color ("blue", "resi 126 & chain E")

cmd.select ("Outward", "resi 126 & chain E", merge=1)

cmd.color ("blue", "resi 127 & chain E")

cmd.select ("Outward", "resi 127 & chain E", merge=1)

cmd.color ("blue", "resi 128 & chain E")

cmd.select ("Outward", "resi 128 & chain E", merge=1)

cmd.color ("blue", "resi 129 & chain E")

cmd.select ("Outward", "resi 129 & chain E", merge=1)

cmd.color ("blue", "resi 130 & chain E")

cmd.select ("Outward", "resi 130 & chain E", merge=1)

cmd.color ("blue", "resi 131 & chain E")

cmd.select ("Outward", "resi 131 & chain E", merge=1)

cmd.color ("blue", "resi 132 & chain E")

cmd.select ("Outward", "resi 132 & chain E", merge=1)

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

cmd.color ("blue", "resi 148 & chain F")

cmd.select ("Outward", "resi 148 & chain F", merge=1)

cmd.color ("blue", "resi 149 & chain F")

cmd.select ("Outward", "resi 149 & chain F", merge=1)

cmd.color ("blue", "resi 150 & chain F")

cmd.select ("Outward", "resi 150 & chain F", merge=1)

cmd.color ("blue", "resi 151 & chain F")

cmd.select ("Outward", "resi 151 & chain F", merge=1)

cmd.color ("blue", "resi 152 & chain F")

cmd.select ("Outward", "resi 152 & chain F", merge=1)

cmd.color ("blue", "resi 153 & chain F")

cmd.select ("Outward", "resi 153 & chain F", merge=1)

cmd.color ("blue", "resi 154 & chain F")

cmd.select ("Outward", "resi 154 & chain F", merge=1)

cmd.color ("blue", "resi 155 & chain F")

cmd.select ("Outward", "resi 155 & chain F", merge=1)

cmd.color ("blue", "resi 156 & chain F")

cmd.select ("Outward", "resi 156 & chain F", merge=1)

cmd.color ("blue", "resi 157 & chain F")

cmd.select ("Outward", "resi 157 & chain F", merge=1)

cmd.color ("blue", "resi 158 & chain F")

cmd.select ("Outward", "resi 158 & chain F", merge=1)

cmd.color ("blue", "resi 159 & chain F")

cmd.select ("Outward", "resi 159 & chain F", merge=1)

cmd.color ("blue", "resi 160 & chain F")

cmd.select ("Outward", "resi 160 & chain F", merge=1)

cmd.color ("blue", "resi 161 & chain F")

cmd.select ("Outward", "resi 161 & chain F", merge=1)

cmd.color ("blue", "resi 162 & chain F")

cmd.select ("Outward", "resi 162 & chain F", merge=1)

cmd.color ("blue", "resi 163 & chain F")

cmd.select ("Outward", "resi 163 & chain F", merge=1)

cmd.color ("blue", "resi 164 & chain F")

cmd.select ("Outward", "resi 164 & chain F", merge=1)

cmd.color ("blue", "resi 165 & chain F")

cmd.select ("Outward", "resi 165 & chain F", merge=1)

cmd.color ("blue", "resi 166 & chain F")

cmd.select ("Outward", "resi 166 & chain F", merge=1)

cmd.color ("blue", "resi 167 & chain F")

cmd.select ("Outward", "resi 167 & chain F", merge=1)

cmd.color ("blue", "resi 168 & chain F")

cmd.select ("Outward", "resi 168 & chain F", merge=1)

cmd.color ("blue", "resi 169 & chain F")

cmd.select ("Outward", "resi 169 & chain F", merge=1)

cmd.color ("blue", "resi 170 & chain F")

cmd.select ("Outward", "resi 170 & chain F", merge=1)

cmd.color ("blue", "resi 171 & chain F")

cmd.select ("Outward", "resi 171 & chain F", merge=1)

cmd.color ("blue", "resi 97 & chain F")

cmd.select ("Outward", "resi 97 & chain F", merge=1)

cmd.color ("blue", "resi 98 & chain F")

cmd.select ("Outward", "resi 98 & chain F", merge=1)

cmd.color ("blue", "resi 99 & chain F")

cmd.select ("Outward", "resi 99 & chain F", merge=1)

cmd.color ("blue", "resi 100 & chain F")

cmd.select ("Outward", "resi 100 & chain F", merge=1)

cmd.color ("blue", "resi 101 & chain F")

cmd.select ("Outward", "resi 101 & chain F", merge=1)

cmd.color ("blue", "resi 102 & chain F")

cmd.select ("Outward", "resi 102 & chain F", merge=1)

cmd.color ("blue", "resi 103 & chain F")

cmd.select ("Outward", "resi 103 & chain F", merge=1)

cmd.color ("blue", "resi 104 & chain F")

cmd.select ("Outward", "resi 104 & chain F", merge=1)

cmd.color ("blue", "resi 105 & chain F")

cmd.select ("Outward", "resi 105 & chain F", merge=1)

cmd.color ("blue", "resi 106 & chain F")

cmd.select ("Outward", "resi 106 & chain F", merge=1)

cmd.color ("blue", "resi 107 & chain F")

cmd.select ("Outward", "resi 107 & chain F", merge=1)

cmd.color ("blue", "resi 108 & chain F")

cmd.select ("Outward", "resi 108 & chain F", merge=1)

cmd.color ("blue", "resi 109 & chain F")

cmd.select ("Outward", "resi 109 & chain F", merge=1)

cmd.color ("blue", "resi 110 & chain F")

cmd.select ("Outward", "resi 110 & chain F", merge=1)

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

cmd.color ("blue", "resi 127 & chain F")

cmd.select ("Outward", "resi 127 & chain F", merge=1)

cmd.color ("blue", "resi 128 & chain F")

cmd.select ("Outward", "resi 128 & chain F", merge=1)

cmd.color ("blue", "resi 129 & chain F")

cmd.select ("Outward", "resi 129 & chain F", merge=1)

cmd.color ("blue", "resi 130 & chain F")

cmd.select ("Outward", "resi 130 & chain F", merge=1)

cmd.color ("blue", "resi 131 & chain F")

cmd.select ("Outward", "resi 131 & chain F", merge=1)

cmd.color ("blue", "resi 132 & chain F")

cmd.select ("Outward", "resi 132 & chain F", merge=1)

cmd.color ("blue", "resi 97 & chain G")

cmd.select ("Outward", "resi 97 & chain G", merge=1)

cmd.color ("blue", "resi 98 & chain G")

cmd.select ("Outward", "resi 98 & chain G", merge=1)

cmd.color ("blue", "resi 99 & chain G")

cmd.select ("Outward", "resi 99 & chain G", merge=1)

cmd.color ("blue", "resi 100 & chain G")

cmd.select ("Outward", "resi 100 & chain G", merge=1)

cmd.color ("blue", "resi 101 & chain G")

cmd.select ("Outward", "resi 101 & chain G", merge=1)

cmd.color ("blue", "resi 102 & chain G")

cmd.select ("Outward", "resi 102 & chain G", merge=1)

cmd.color ("blue", "resi 103 & chain G")

cmd.select ("Outward", "resi 103 & chain G", merge=1)

cmd.color ("blue", "resi 104 & chain G")

cmd.select ("Outward", "resi 104 & chain G", merge=1)

cmd.color ("blue", "resi 105 & chain G")

cmd.select ("Outward", "resi 105 & chain G", merge=1)

cmd.color ("blue", "resi 106 & chain G")

cmd.select ("Outward", "resi 106 & chain G", merge=1)

cmd.color ("blue", "resi 107 & chain G")

cmd.select ("Outward", "resi 107 & chain G", merge=1)

cmd.color ("blue", "resi 108 & chain G")

cmd.select ("Outward", "resi 108 & chain G", merge=1)

cmd.color ("blue", "resi 109 & chain G")

cmd.select ("Outward", "resi 109 & chain G", merge=1)

cmd.color ("blue", "resi 110 & chain G")

cmd.select ("Outward", "resi 110 & chain G", merge=1)

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

cmd.color ("blue", "resi 127 & chain G")

cmd.select ("Outward", "resi 127 & chain G", merge=1)

cmd.color ("blue", "resi 128 & chain G")

cmd.select ("Outward", "resi 128 & chain G", merge=1)

cmd.color ("blue", "resi 129 & chain G")

cmd.select ("Outward", "resi 129 & chain G", merge=1)

cmd.color ("blue", "resi 130 & chain G")

cmd.select ("Outward", "resi 130 & chain G", merge=1)

cmd.color ("blue", "resi 131 & chain G")

cmd.select ("Outward", "resi 131 & chain G", merge=1)

cmd.color ("blue", "resi 132 & chain G")

cmd.select ("Outward", "resi 132 & chain G", merge=1)

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

cmd.color ("blue", "resi 148 & chain G")

cmd.select ("Outward", "resi 148 & chain G", merge=1)

cmd.color ("blue", "resi 149 & chain G")

cmd.select ("Outward", "resi 149 & chain G", merge=1)

cmd.color ("blue", "resi 150 & chain G")

cmd.select ("Outward", "resi 150 & chain G", merge=1)

cmd.color ("blue", "resi 151 & chain G")

cmd.select ("Outward", "resi 151 & chain G", merge=1)

cmd.color ("blue", "resi 152 & chain G")

cmd.select ("Outward", "resi 152 & chain G", merge=1)

cmd.color ("blue", "resi 153 & chain G")

cmd.select ("Outward", "resi 153 & chain G", merge=1)

cmd.color ("blue", "resi 154 & chain G")

cmd.select ("Outward", "resi 154 & chain G", merge=1)

cmd.color ("blue", "resi 155 & chain G")

cmd.select ("Outward", "resi 155 & chain G", merge=1)

cmd.color ("blue", "resi 156 & chain G")

cmd.select ("Outward", "resi 156 & chain G", merge=1)

cmd.color ("blue", "resi 157 & chain G")

cmd.select ("Outward", "resi 157 & chain G", merge=1)

cmd.color ("blue", "resi 158 & chain G")

cmd.select ("Outward", "resi 158 & chain G", merge=1)

cmd.color ("blue", "resi 159 & chain G")

cmd.select ("Outward", "resi 159 & chain G", merge=1)

cmd.color ("blue", "resi 160 & chain G")

cmd.select ("Outward", "resi 160 & chain G", merge=1)

cmd.color ("blue", "resi 161 & chain G")

cmd.select ("Outward", "resi 161 & chain G", merge=1)

cmd.color ("blue", "resi 162 & chain G")

cmd.select ("Outward", "resi 162 & chain G", merge=1)

cmd.color ("blue", "resi 163 & chain G")

cmd.select ("Outward", "resi 163 & chain G", merge=1)

cmd.color ("blue", "resi 164 & chain G")

cmd.select ("Outward", "resi 164 & chain G", merge=1)

cmd.color ("blue", "resi 165 & chain G")

cmd.select ("Outward", "resi 165 & chain G", merge=1)

cmd.color ("blue", "resi 166 & chain G")

cmd.select ("Outward", "resi 166 & chain G", merge=1)

cmd.color ("blue", "resi 167 & chain G")

cmd.select ("Outward", "resi 167 & chain G", merge=1)

cmd.color ("blue", "resi 168 & chain G")

cmd.select ("Outward", "resi 168 & chain G", merge=1)

cmd.color ("blue", "resi 169 & chain G")

cmd.select ("Outward", "resi 169 & chain G", merge=1)

cmd.color ("blue", "resi 170 & chain G")

cmd.select ("Outward", "resi 170 & chain G", merge=1)

cmd.color ("blue", "resi 171 & chain G")

cmd.select ("Outward", "resi 171 & chain G", merge=1)

cmd.load_cgo( [9.0, 117.699936,117.70007,81.957504, 117.69985, 117.700005, 176.82051, 1, 1,1,0,0,0,1], "axis" )
