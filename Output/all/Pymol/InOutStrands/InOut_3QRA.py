from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3QRA.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 30+31+32+33+34+35+36+37+38+39+40+41+42+43 & chain A ")


cmd.select("Astrand7", "resi 169+170+171+172+173+174+175+176+177+178+179+180+181 & chain A ")


cmd.select("Astrand6", "resi 155+156+157+158+159+160+161+162+163+164+165+166 & chain A ")


cmd.select("Astrand1", "resi 53+54+55+56+57+58+59+60+61+62 & chain A ")


cmd.select("Astrand2", "resi 67+68+69+70+71+72+73+74+75+76+77+78 & chain A ")


cmd.select("Astrand3", "resi 91+92+93+94+95+96+97+98+99+100+101+102+103+104+105+106 & chain A ")


cmd.select("Astrand4", "resi 111+112+113+114+115+116+117+118+119+120+121+122+123+124+125+126+127 & chain A ")


cmd.select("Astrand5", "resi 133+134+135+136+137+138+139+140+141+142+143+144+145+146+147+148+149 & chain A ")


cmd.select("barrel", "Astrand*")
cmd.show("sticks", "barrel")
cmd.show("cartoon", "barrel")
cmd.set("cartoon_side_chain_helper", "on")
cmd.zoom("barrel")
cmd.color ("blue", "resi 30 & chain A")

cmd.select ("Outward", "resi 30 & chain A", merge=1)

cmd.color ("red", "resi 31 & chain A")

cmd.select ("Inward", "resi 31 & chain A", merge=1)

cmd.color ("blue", "resi 32 & chain A")

cmd.select ("Outward", "resi 32 & chain A", merge=1)

cmd.color ("red", "resi 33 & chain A")

cmd.select ("Inward", "resi 33 & chain A", merge=1)

cmd.color ("blue", "resi 34 & chain A")

cmd.select ("Outward", "resi 34 & chain A", merge=1)

cmd.color ("red", "resi 35 & chain A")

cmd.select ("Inward", "resi 35 & chain A", merge=1)

cmd.color ("blue", "resi 36 & chain A")

cmd.select ("Outward", "resi 36 & chain A", merge=1)

cmd.color ("red", "resi 37 & chain A")

cmd.select ("Inward", "resi 37 & chain A", merge=1)

cmd.color ("blue", "resi 38 & chain A")

cmd.select ("Outward", "resi 38 & chain A", merge=1)

cmd.color ("red", "resi 39 & chain A")

cmd.select ("Inward", "resi 39 & chain A", merge=1)

cmd.color ("blue", "resi 40 & chain A")

cmd.select ("Outward", "resi 40 & chain A", merge=1)

cmd.color ("red", "resi 41 & chain A")

cmd.select ("Inward", "resi 41 & chain A", merge=1)

cmd.color ("blue", "resi 42 & chain A")

cmd.select ("Outward", "resi 42 & chain A", merge=1)

cmd.color ("red", "resi 43 & chain A")

cmd.select ("Inward", "resi 43 & chain A", merge=1)

cmd.color ("red", "resi 169 & chain A")

cmd.select ("Inward", "resi 169 & chain A", merge=1)

cmd.color ("blue", "resi 170 & chain A")

cmd.select ("Outward", "resi 170 & chain A", merge=1)

cmd.color ("red", "resi 171 & chain A")

cmd.select ("Inward", "resi 171 & chain A", merge=1)

cmd.color ("blue", "resi 172 & chain A")

cmd.select ("Outward", "resi 172 & chain A", merge=1)

cmd.color ("red", "resi 173 & chain A")

cmd.select ("Inward", "resi 173 & chain A", merge=1)

cmd.color ("blue", "resi 174 & chain A")

cmd.select ("Outward", "resi 174 & chain A", merge=1)

cmd.color ("red", "resi 175 & chain A")

cmd.select ("Inward", "resi 175 & chain A", merge=1)

cmd.color ("blue", "resi 176 & chain A")

cmd.select ("Outward", "resi 176 & chain A", merge=1)

cmd.color ("red", "resi 177 & chain A")

cmd.select ("Inward", "resi 177 & chain A", merge=1)

cmd.color ("blue", "resi 178 & chain A")

cmd.select ("Outward", "resi 178 & chain A", merge=1)

cmd.color ("red", "resi 179 & chain A")

cmd.select ("Inward", "resi 179 & chain A", merge=1)

cmd.color ("blue", "resi 180 & chain A")

cmd.select ("Outward", "resi 180 & chain A", merge=1)

cmd.color ("red", "resi 181 & chain A")

cmd.select ("Inward", "resi 181 & chain A", merge=1)

cmd.color ("blue", "resi 155 & chain A")

cmd.select ("Outward", "resi 155 & chain A", merge=1)

cmd.color ("red", "resi 156 & chain A")

cmd.select ("Inward", "resi 156 & chain A", merge=1)

cmd.color ("blue", "resi 157 & chain A")

cmd.select ("Outward", "resi 157 & chain A", merge=1)

cmd.color ("red", "resi 158 & chain A")

cmd.select ("Inward", "resi 158 & chain A", merge=1)

cmd.color ("blue", "resi 159 & chain A")

cmd.select ("Outward", "resi 159 & chain A", merge=1)

cmd.color ("red", "resi 160 & chain A")

cmd.select ("Inward", "resi 160 & chain A", merge=1)

cmd.color ("blue", "resi 161 & chain A")

cmd.select ("Outward", "resi 161 & chain A", merge=1)

cmd.color ("red", "resi 162 & chain A")

cmd.select ("Inward", "resi 162 & chain A", merge=1)

cmd.color ("blue", "resi 163 & chain A")

cmd.select ("Outward", "resi 163 & chain A", merge=1)

cmd.color ("red", "resi 164 & chain A")

cmd.select ("Inward", "resi 164 & chain A", merge=1)

cmd.color ("blue", "resi 165 & chain A")

cmd.select ("Outward", "resi 165 & chain A", merge=1)

cmd.color ("red", "resi 166 & chain A")

cmd.select ("Inward", "resi 166 & chain A", merge=1)

cmd.color ("blue", "resi 53 & chain A")

cmd.select ("Outward", "resi 53 & chain A", merge=1)

cmd.color ("red", "resi 54 & chain A")

cmd.select ("Inward", "resi 54 & chain A", merge=1)

cmd.color ("blue", "resi 55 & chain A")

cmd.select ("Outward", "resi 55 & chain A", merge=1)

cmd.color ("red", "resi 56 & chain A")

cmd.select ("Inward", "resi 56 & chain A", merge=1)

cmd.color ("blue", "resi 57 & chain A")

cmd.select ("Outward", "resi 57 & chain A", merge=1)

cmd.color ("red", "resi 58 & chain A")

cmd.select ("Inward", "resi 58 & chain A", merge=1)

cmd.color ("blue", "resi 59 & chain A")

cmd.select ("Outward", "resi 59 & chain A", merge=1)

cmd.color ("red", "resi 60 & chain A")

cmd.select ("Inward", "resi 60 & chain A", merge=1)

cmd.color ("blue", "resi 61 & chain A")

cmd.select ("Outward", "resi 61 & chain A", merge=1)

cmd.color ("blue", "resi 62 & chain A")

cmd.select ("Outward", "resi 62 & chain A", merge=1)

cmd.color ("blue", "resi 67 & chain A")

cmd.select ("Outward", "resi 67 & chain A", merge=1)

cmd.color ("red", "resi 68 & chain A")

cmd.select ("Inward", "resi 68 & chain A", merge=1)

cmd.color ("blue", "resi 69 & chain A")

cmd.select ("Outward", "resi 69 & chain A", merge=1)

cmd.color ("red", "resi 70 & chain A")

cmd.select ("Inward", "resi 70 & chain A", merge=1)

cmd.color ("blue", "resi 71 & chain A")

cmd.select ("Outward", "resi 71 & chain A", merge=1)

cmd.color ("red", "resi 72 & chain A")

cmd.select ("Inward", "resi 72 & chain A", merge=1)

cmd.color ("blue", "resi 73 & chain A")

cmd.select ("Outward", "resi 73 & chain A", merge=1)

cmd.color ("red", "resi 74 & chain A")

cmd.select ("Inward", "resi 74 & chain A", merge=1)

cmd.color ("blue", "resi 75 & chain A")

cmd.select ("Outward", "resi 75 & chain A", merge=1)

cmd.color ("red", "resi 76 & chain A")

cmd.select ("Inward", "resi 76 & chain A", merge=1)

cmd.color ("blue", "resi 77 & chain A")

cmd.select ("Outward", "resi 77 & chain A", merge=1)

cmd.color ("red", "resi 78 & chain A")

cmd.select ("Inward", "resi 78 & chain A", merge=1)

cmd.color ("blue", "resi 91 & chain A")

cmd.select ("Outward", "resi 91 & chain A", merge=1)

cmd.color ("red", "resi 92 & chain A")

cmd.select ("Inward", "resi 92 & chain A", merge=1)

cmd.color ("blue", "resi 93 & chain A")

cmd.select ("Outward", "resi 93 & chain A", merge=1)

cmd.color ("red", "resi 94 & chain A")

cmd.select ("Inward", "resi 94 & chain A", merge=1)

cmd.color ("blue", "resi 95 & chain A")

cmd.select ("Outward", "resi 95 & chain A", merge=1)

cmd.color ("red", "resi 96 & chain A")

cmd.select ("Inward", "resi 96 & chain A", merge=1)

cmd.color ("blue", "resi 97 & chain A")

cmd.select ("Outward", "resi 97 & chain A", merge=1)

cmd.color ("red", "resi 98 & chain A")

cmd.select ("Inward", "resi 98 & chain A", merge=1)

cmd.color ("blue", "resi 99 & chain A")

cmd.select ("Outward", "resi 99 & chain A", merge=1)

cmd.color ("red", "resi 100 & chain A")

cmd.select ("Inward", "resi 100 & chain A", merge=1)

cmd.color ("blue", "resi 101 & chain A")

cmd.select ("Outward", "resi 101 & chain A", merge=1)

cmd.color ("red", "resi 102 & chain A")

cmd.select ("Inward", "resi 102 & chain A", merge=1)

cmd.color ("blue", "resi 103 & chain A")

cmd.select ("Outward", "resi 103 & chain A", merge=1)

cmd.color ("red", "resi 104 & chain A")

cmd.select ("Inward", "resi 104 & chain A", merge=1)

cmd.color ("blue", "resi 105 & chain A")

cmd.select ("Outward", "resi 105 & chain A", merge=1)

cmd.color ("blue", "resi 106 & chain A")

cmd.select ("Outward", "resi 106 & chain A", merge=1)

cmd.color ("blue", "resi 111 & chain A")

cmd.select ("Outward", "resi 111 & chain A", merge=1)

cmd.color ("red", "resi 112 & chain A")

cmd.select ("Inward", "resi 112 & chain A", merge=1)

cmd.color ("blue", "resi 113 & chain A")

cmd.select ("Outward", "resi 113 & chain A", merge=1)

cmd.color ("red", "resi 114 & chain A")

cmd.select ("Inward", "resi 114 & chain A", merge=1)

cmd.color ("blue", "resi 115 & chain A")

cmd.select ("Outward", "resi 115 & chain A", merge=1)

cmd.color ("red", "resi 116 & chain A")

cmd.select ("Inward", "resi 116 & chain A", merge=1)

cmd.color ("blue", "resi 117 & chain A")

cmd.select ("Outward", "resi 117 & chain A", merge=1)

cmd.color ("red", "resi 118 & chain A")

cmd.select ("Inward", "resi 118 & chain A", merge=1)

cmd.color ("blue", "resi 119 & chain A")

cmd.select ("Outward", "resi 119 & chain A", merge=1)

cmd.color ("red", "resi 120 & chain A")

cmd.select ("Inward", "resi 120 & chain A", merge=1)

cmd.color ("blue", "resi 121 & chain A")

cmd.select ("Outward", "resi 121 & chain A", merge=1)

cmd.color ("red", "resi 122 & chain A")

cmd.select ("Inward", "resi 122 & chain A", merge=1)

cmd.color ("blue", "resi 123 & chain A")

cmd.select ("Outward", "resi 123 & chain A", merge=1)

cmd.color ("red", "resi 124 & chain A")

cmd.select ("Inward", "resi 124 & chain A", merge=1)

cmd.color ("blue", "resi 125 & chain A")

cmd.select ("Outward", "resi 125 & chain A", merge=1)

cmd.color ("red", "resi 126 & chain A")

cmd.select ("Inward", "resi 126 & chain A", merge=1)

cmd.color ("blue", "resi 127 & chain A")

cmd.select ("Outward", "resi 127 & chain A", merge=1)

cmd.color ("blue", "resi 133 & chain A")

cmd.select ("Outward", "resi 133 & chain A", merge=1)

cmd.color ("red", "resi 134 & chain A")

cmd.select ("Inward", "resi 134 & chain A", merge=1)

cmd.color ("blue", "resi 135 & chain A")

cmd.select ("Outward", "resi 135 & chain A", merge=1)

cmd.color ("red", "resi 136 & chain A")

cmd.select ("Inward", "resi 136 & chain A", merge=1)

cmd.color ("blue", "resi 137 & chain A")

cmd.select ("Outward", "resi 137 & chain A", merge=1)

cmd.color ("red", "resi 138 & chain A")

cmd.select ("Inward", "resi 138 & chain A", merge=1)

cmd.color ("blue", "resi 139 & chain A")

cmd.select ("Outward", "resi 139 & chain A", merge=1)

cmd.color ("red", "resi 140 & chain A")

cmd.select ("Inward", "resi 140 & chain A", merge=1)

cmd.color ("blue", "resi 141 & chain A")

cmd.select ("Outward", "resi 141 & chain A", merge=1)

cmd.color ("red", "resi 142 & chain A")

cmd.select ("Inward", "resi 142 & chain A", merge=1)

cmd.color ("blue", "resi 143 & chain A")

cmd.select ("Outward", "resi 143 & chain A", merge=1)

cmd.color ("red", "resi 144 & chain A")

cmd.select ("Inward", "resi 144 & chain A", merge=1)

cmd.color ("blue", "resi 145 & chain A")

cmd.select ("Outward", "resi 145 & chain A", merge=1)

cmd.color ("red", "resi 146 & chain A")

cmd.select ("Inward", "resi 146 & chain A", merge=1)

cmd.color ("blue", "resi 147 & chain A")

cmd.select ("Outward", "resi 147 & chain A", merge=1)

cmd.color ("red", "resi 148 & chain A")

cmd.select ("Inward", "resi 148 & chain A", merge=1)

cmd.color ("red", "resi 149 & chain A")

cmd.select ("Inward", "resi 149 & chain A", merge=1)

cmd.load_cgo( [9.0, 12.690125,35.84125,31.821, 12.690125, 35.84125, 31.821, 1, 1,1,0,0,0,1], "axis" )
