from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3EMN.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Xstrand0", "resi 26+27+28+29+30+31+32 & chain X ")


cmd.select("Xstrand18", "resi 274+275+276+277+278+279+280+281+282 & chain X ")


cmd.select("Xstrand17", "resi 255+256+257+258+259+260+261+262+263+264 & chain X ")


cmd.select("Xstrand16", "resi 242+243+244+245+246+247+248+249+250+251+252 & chain X ")


cmd.select("Xstrand15", "resi 231+232+233+234+235+236+237+238 & chain X ")


cmd.select("Xstrand14", "resi 214+215+216+217+218+219+220+221+222+223+224+225 & chain X ")


cmd.select("Xstrand13", "resi 202+203+204+205+206+207+208+209+210+211 & chain X ")


cmd.select("Xstrand12", "resi 189+190+191+192+193+194+195+196+197 & chain X ")


cmd.select("Xstrand11", "resi 178+179+180+181+182+183+184+185 & chain X ")


cmd.select("Xstrand10", "resi 163+164+165+166+167+168+169+170+171+172+173+174 & chain X ")


cmd.select("Xstrand9", "resi 149+150+151+152+153+154+155+156+157+158 & chain X ")


cmd.select("Xstrand8", "resi 137+138+139+140+141+142+143+144+145+146 & chain X ")


cmd.select("Xstrand7", "resi 123+124+125+126+127+128+129+130+131 & chain X ")


cmd.select("Xstrand6", "resi 110+111+112+113+114+115+116+117+118+119+120 & chain X ")


cmd.select("Xstrand5", "resi 95+96+97+98+99+100+101+102+103 & chain X ")


cmd.select("Xstrand4", "resi 81+82+83+84+85+86+87+88 & chain X ")


cmd.select("Xstrand3", "resi 69+70+71+72+73+74+75+76 & chain X ")


cmd.select("Xstrand2", "resi 54+55+56+57+58+59+60+61+62+63+64 & chain X ")


cmd.select("Xstrand1", "resi 38+39+40+41+42+43+44+45+46+47+48 & chain X ")


cmd.select("barrel", "Xstrand*")
cmd.show("sticks", "barrel")
cmd.show("cartoon", "barrel")
cmd.set("cartoon_side_chain_helper", "on")
cmd.zoom("barrel")
cmd.color ("red", "resi 26 & chain X")

cmd.select ("Inward", "resi 26 & chain X", merge=1)

cmd.color ("blue", "resi 27 & chain X")

cmd.select ("Outward", "resi 27 & chain X", merge=1)

cmd.color ("red", "resi 28 & chain X")

cmd.select ("Inward", "resi 28 & chain X", merge=1)

cmd.color ("blue", "resi 29 & chain X")

cmd.select ("Outward", "resi 29 & chain X", merge=1)

cmd.color ("red", "resi 30 & chain X")

cmd.select ("Inward", "resi 30 & chain X", merge=1)

cmd.color ("blue", "resi 31 & chain X")

cmd.select ("Outward", "resi 31 & chain X", merge=1)

cmd.color ("red", "resi 32 & chain X")

cmd.select ("Inward", "resi 32 & chain X", merge=1)

cmd.color ("red", "resi 274 & chain X")

cmd.select ("Inward", "resi 274 & chain X", merge=1)

cmd.color ("blue", "resi 275 & chain X")

cmd.select ("Outward", "resi 275 & chain X", merge=1)

cmd.color ("red", "resi 276 & chain X")

cmd.select ("Inward", "resi 276 & chain X", merge=1)

cmd.color ("blue", "resi 277 & chain X")

cmd.select ("Outward", "resi 277 & chain X", merge=1)

cmd.color ("red", "resi 278 & chain X")

cmd.select ("Inward", "resi 278 & chain X", merge=1)

cmd.color ("blue", "resi 279 & chain X")

cmd.select ("Outward", "resi 279 & chain X", merge=1)

cmd.color ("red", "resi 280 & chain X")

cmd.select ("Inward", "resi 280 & chain X", merge=1)

cmd.color ("blue", "resi 281 & chain X")

cmd.select ("Outward", "resi 281 & chain X", merge=1)

cmd.color ("red", "resi 282 & chain X")

cmd.select ("Inward", "resi 282 & chain X", merge=1)

cmd.color ("blue", "resi 255 & chain X")

cmd.select ("Outward", "resi 255 & chain X", merge=1)

cmd.color ("red", "resi 256 & chain X")

cmd.select ("Inward", "resi 256 & chain X", merge=1)

cmd.color ("blue", "resi 257 & chain X")

cmd.select ("Outward", "resi 257 & chain X", merge=1)

cmd.color ("red", "resi 258 & chain X")

cmd.select ("Inward", "resi 258 & chain X", merge=1)

cmd.color ("blue", "resi 259 & chain X")

cmd.select ("Outward", "resi 259 & chain X", merge=1)

cmd.color ("red", "resi 260 & chain X")

cmd.select ("Inward", "resi 260 & chain X", merge=1)

cmd.color ("blue", "resi 261 & chain X")

cmd.select ("Outward", "resi 261 & chain X", merge=1)

cmd.color ("red", "resi 262 & chain X")

cmd.select ("Inward", "resi 262 & chain X", merge=1)

cmd.color ("blue", "resi 263 & chain X")

cmd.select ("Outward", "resi 263 & chain X", merge=1)

cmd.color ("blue", "resi 264 & chain X")

cmd.select ("Outward", "resi 264 & chain X", merge=1)

cmd.color ("red", "resi 242 & chain X")

cmd.select ("Inward", "resi 242 & chain X", merge=1)

cmd.color ("blue", "resi 243 & chain X")

cmd.select ("Outward", "resi 243 & chain X", merge=1)

cmd.color ("red", "resi 244 & chain X")

cmd.select ("Inward", "resi 244 & chain X", merge=1)

cmd.color ("blue", "resi 245 & chain X")

cmd.select ("Outward", "resi 245 & chain X", merge=1)

cmd.color ("red", "resi 246 & chain X")

cmd.select ("Inward", "resi 246 & chain X", merge=1)

cmd.color ("blue", "resi 247 & chain X")

cmd.select ("Outward", "resi 247 & chain X", merge=1)

cmd.color ("red", "resi 248 & chain X")

cmd.select ("Inward", "resi 248 & chain X", merge=1)

cmd.color ("blue", "resi 249 & chain X")

cmd.select ("Outward", "resi 249 & chain X", merge=1)

cmd.color ("blue", "resi 250 & chain X")

cmd.select ("Outward", "resi 250 & chain X", merge=1)

cmd.color ("red", "resi 251 & chain X")

cmd.select ("Inward", "resi 251 & chain X", merge=1)

cmd.color ("blue", "resi 252 & chain X")

cmd.select ("Outward", "resi 252 & chain X", merge=1)

cmd.color ("blue", "resi 231 & chain X")

cmd.select ("Outward", "resi 231 & chain X", merge=1)

cmd.color ("red", "resi 232 & chain X")

cmd.select ("Inward", "resi 232 & chain X", merge=1)

cmd.color ("blue", "resi 233 & chain X")

cmd.select ("Outward", "resi 233 & chain X", merge=1)

cmd.color ("red", "resi 234 & chain X")

cmd.select ("Inward", "resi 234 & chain X", merge=1)

cmd.color ("blue", "resi 235 & chain X")

cmd.select ("Outward", "resi 235 & chain X", merge=1)

cmd.color ("red", "resi 236 & chain X")

cmd.select ("Inward", "resi 236 & chain X", merge=1)

cmd.color ("blue", "resi 237 & chain X")

cmd.select ("Outward", "resi 237 & chain X", merge=1)

cmd.color ("red", "resi 238 & chain X")

cmd.select ("Inward", "resi 238 & chain X", merge=1)

cmd.color ("red", "resi 214 & chain X")

cmd.select ("Inward", "resi 214 & chain X", merge=1)

cmd.color ("blue", "resi 215 & chain X")

cmd.select ("Outward", "resi 215 & chain X", merge=1)

cmd.color ("red", "resi 216 & chain X")

cmd.select ("Inward", "resi 216 & chain X", merge=1)

cmd.color ("blue", "resi 217 & chain X")

cmd.select ("Outward", "resi 217 & chain X", merge=1)

cmd.color ("red", "resi 218 & chain X")

cmd.select ("Inward", "resi 218 & chain X", merge=1)

cmd.color ("blue", "resi 219 & chain X")

cmd.select ("Outward", "resi 219 & chain X", merge=1)

cmd.color ("red", "resi 220 & chain X")

cmd.select ("Inward", "resi 220 & chain X", merge=1)

cmd.color ("blue", "resi 221 & chain X")

cmd.select ("Outward", "resi 221 & chain X", merge=1)

cmd.color ("red", "resi 222 & chain X")

cmd.select ("Inward", "resi 222 & chain X", merge=1)

cmd.color ("blue", "resi 223 & chain X")

cmd.select ("Outward", "resi 223 & chain X", merge=1)

cmd.color ("red", "resi 224 & chain X")

cmd.select ("Inward", "resi 224 & chain X", merge=1)

cmd.color ("blue", "resi 225 & chain X")

cmd.select ("Outward", "resi 225 & chain X", merge=1)

cmd.color ("blue", "resi 202 & chain X")

cmd.select ("Outward", "resi 202 & chain X", merge=1)

cmd.color ("red", "resi 203 & chain X")

cmd.select ("Inward", "resi 203 & chain X", merge=1)

cmd.color ("blue", "resi 204 & chain X")

cmd.select ("Outward", "resi 204 & chain X", merge=1)

cmd.color ("red", "resi 205 & chain X")

cmd.select ("Inward", "resi 205 & chain X", merge=1)

cmd.color ("blue", "resi 206 & chain X")

cmd.select ("Outward", "resi 206 & chain X", merge=1)

cmd.color ("red", "resi 207 & chain X")

cmd.select ("Inward", "resi 207 & chain X", merge=1)

cmd.color ("blue", "resi 208 & chain X")

cmd.select ("Outward", "resi 208 & chain X", merge=1)

cmd.color ("red", "resi 209 & chain X")

cmd.select ("Inward", "resi 209 & chain X", merge=1)

cmd.color ("blue", "resi 210 & chain X")

cmd.select ("Outward", "resi 210 & chain X", merge=1)

cmd.color ("blue", "resi 211 & chain X")

cmd.select ("Outward", "resi 211 & chain X", merge=1)

cmd.color ("red", "resi 189 & chain X")

cmd.select ("Inward", "resi 189 & chain X", merge=1)

cmd.color ("blue", "resi 190 & chain X")

cmd.select ("Outward", "resi 190 & chain X", merge=1)

cmd.color ("red", "resi 191 & chain X")

cmd.select ("Inward", "resi 191 & chain X", merge=1)

cmd.color ("blue", "resi 192 & chain X")

cmd.select ("Outward", "resi 192 & chain X", merge=1)

cmd.color ("red", "resi 193 & chain X")

cmd.select ("Inward", "resi 193 & chain X", merge=1)

cmd.color ("blue", "resi 194 & chain X")

cmd.select ("Outward", "resi 194 & chain X", merge=1)

cmd.color ("red", "resi 195 & chain X")

cmd.select ("Inward", "resi 195 & chain X", merge=1)

cmd.color ("blue", "resi 196 & chain X")

cmd.select ("Outward", "resi 196 & chain X", merge=1)

cmd.color ("red", "resi 197 & chain X")

cmd.select ("Inward", "resi 197 & chain X", merge=1)

cmd.color ("blue", "resi 178 & chain X")

cmd.select ("Outward", "resi 178 & chain X", merge=1)

cmd.color ("red", "resi 179 & chain X")

cmd.select ("Inward", "resi 179 & chain X", merge=1)

cmd.color ("blue", "resi 180 & chain X")

cmd.select ("Outward", "resi 180 & chain X", merge=1)

cmd.color ("red", "resi 181 & chain X")

cmd.select ("Inward", "resi 181 & chain X", merge=1)

cmd.color ("blue", "resi 182 & chain X")

cmd.select ("Outward", "resi 182 & chain X", merge=1)

cmd.color ("red", "resi 183 & chain X")

cmd.select ("Inward", "resi 183 & chain X", merge=1)

cmd.color ("blue", "resi 184 & chain X")

cmd.select ("Outward", "resi 184 & chain X", merge=1)

cmd.color ("red", "resi 185 & chain X")

cmd.select ("Inward", "resi 185 & chain X", merge=1)

cmd.color ("red", "resi 163 & chain X")

cmd.select ("Inward", "resi 163 & chain X", merge=1)

cmd.color ("blue", "resi 164 & chain X")

cmd.select ("Outward", "resi 164 & chain X", merge=1)

cmd.color ("red", "resi 165 & chain X")

cmd.select ("Inward", "resi 165 & chain X", merge=1)

cmd.color ("red", "resi 166 & chain X")

cmd.select ("Inward", "resi 166 & chain X", merge=1)

cmd.color ("blue", "resi 167 & chain X")

cmd.select ("Outward", "resi 167 & chain X", merge=1)

cmd.color ("red", "resi 168 & chain X")

cmd.select ("Inward", "resi 168 & chain X", merge=1)

cmd.color ("blue", "resi 169 & chain X")

cmd.select ("Outward", "resi 169 & chain X", merge=1)

cmd.color ("red", "resi 170 & chain X")

cmd.select ("Inward", "resi 170 & chain X", merge=1)

cmd.color ("blue", "resi 171 & chain X")

cmd.select ("Outward", "resi 171 & chain X", merge=1)

cmd.color ("red", "resi 172 & chain X")

cmd.select ("Inward", "resi 172 & chain X", merge=1)

cmd.color ("blue", "resi 173 & chain X")

cmd.select ("Outward", "resi 173 & chain X", merge=1)

cmd.color ("red", "resi 174 & chain X")

cmd.select ("Inward", "resi 174 & chain X", merge=1)

cmd.color ("blue", "resi 149 & chain X")

cmd.select ("Outward", "resi 149 & chain X", merge=1)

cmd.color ("red", "resi 150 & chain X")

cmd.select ("Inward", "resi 150 & chain X", merge=1)

cmd.color ("blue", "resi 151 & chain X")

cmd.select ("Outward", "resi 151 & chain X", merge=1)

cmd.color ("red", "resi 152 & chain X")

cmd.select ("Inward", "resi 152 & chain X", merge=1)

cmd.color ("blue", "resi 153 & chain X")

cmd.select ("Outward", "resi 153 & chain X", merge=1)

cmd.color ("red", "resi 154 & chain X")

cmd.select ("Inward", "resi 154 & chain X", merge=1)

cmd.color ("blue", "resi 155 & chain X")

cmd.select ("Outward", "resi 155 & chain X", merge=1)

cmd.color ("red", "resi 156 & chain X")

cmd.select ("Inward", "resi 156 & chain X", merge=1)

cmd.color ("blue", "resi 157 & chain X")

cmd.select ("Outward", "resi 157 & chain X", merge=1)

cmd.color ("blue", "resi 158 & chain X")

cmd.select ("Outward", "resi 158 & chain X", merge=1)

cmd.color ("red", "resi 137 & chain X")

cmd.select ("Inward", "resi 137 & chain X", merge=1)

cmd.color ("blue", "resi 138 & chain X")

cmd.select ("Outward", "resi 138 & chain X", merge=1)

cmd.color ("red", "resi 139 & chain X")

cmd.select ("Inward", "resi 139 & chain X", merge=1)

cmd.color ("blue", "resi 140 & chain X")

cmd.select ("Outward", "resi 140 & chain X", merge=1)

cmd.color ("red", "resi 141 & chain X")

cmd.select ("Inward", "resi 141 & chain X", merge=1)

cmd.color ("blue", "resi 142 & chain X")

cmd.select ("Outward", "resi 142 & chain X", merge=1)

cmd.color ("red", "resi 143 & chain X")

cmd.select ("Inward", "resi 143 & chain X", merge=1)

cmd.color ("blue", "resi 144 & chain X")

cmd.select ("Outward", "resi 144 & chain X", merge=1)

cmd.color ("red", "resi 145 & chain X")

cmd.select ("Inward", "resi 145 & chain X", merge=1)

cmd.color ("blue", "resi 146 & chain X")

cmd.select ("Outward", "resi 146 & chain X", merge=1)

cmd.color ("blue", "resi 123 & chain X")

cmd.select ("Outward", "resi 123 & chain X", merge=1)

cmd.color ("red", "resi 124 & chain X")

cmd.select ("Inward", "resi 124 & chain X", merge=1)

cmd.color ("blue", "resi 125 & chain X")

cmd.select ("Outward", "resi 125 & chain X", merge=1)

cmd.color ("red", "resi 126 & chain X")

cmd.select ("Inward", "resi 126 & chain X", merge=1)

cmd.color ("blue", "resi 127 & chain X")

cmd.select ("Outward", "resi 127 & chain X", merge=1)

cmd.color ("red", "resi 128 & chain X")

cmd.select ("Inward", "resi 128 & chain X", merge=1)

cmd.color ("blue", "resi 129 & chain X")

cmd.select ("Outward", "resi 129 & chain X", merge=1)

cmd.color ("red", "resi 130 & chain X")

cmd.select ("Inward", "resi 130 & chain X", merge=1)

cmd.color ("blue", "resi 131 & chain X")

cmd.select ("Outward", "resi 131 & chain X", merge=1)

cmd.color ("blue", "resi 110 & chain X")

cmd.select ("Outward", "resi 110 & chain X", merge=1)

cmd.color ("red", "resi 111 & chain X")

cmd.select ("Inward", "resi 111 & chain X", merge=1)

cmd.color ("blue", "resi 112 & chain X")

cmd.select ("Outward", "resi 112 & chain X", merge=1)

cmd.color ("red", "resi 113 & chain X")

cmd.select ("Inward", "resi 113 & chain X", merge=1)

cmd.color ("blue", "resi 114 & chain X")

cmd.select ("Outward", "resi 114 & chain X", merge=1)

cmd.color ("red", "resi 115 & chain X")

cmd.select ("Inward", "resi 115 & chain X", merge=1)

cmd.color ("blue", "resi 116 & chain X")

cmd.select ("Outward", "resi 116 & chain X", merge=1)

cmd.color ("red", "resi 117 & chain X")

cmd.select ("Inward", "resi 117 & chain X", merge=1)

cmd.color ("blue", "resi 118 & chain X")

cmd.select ("Outward", "resi 118 & chain X", merge=1)

cmd.color ("red", "resi 119 & chain X")

cmd.select ("Inward", "resi 119 & chain X", merge=1)

cmd.color ("blue", "resi 120 & chain X")

cmd.select ("Outward", "resi 120 & chain X", merge=1)

cmd.color ("blue", "resi 95 & chain X")

cmd.select ("Outward", "resi 95 & chain X", merge=1)

cmd.color ("red", "resi 96 & chain X")

cmd.select ("Inward", "resi 96 & chain X", merge=1)

cmd.color ("blue", "resi 97 & chain X")

cmd.select ("Outward", "resi 97 & chain X", merge=1)

cmd.color ("red", "resi 98 & chain X")

cmd.select ("Inward", "resi 98 & chain X", merge=1)

cmd.color ("blue", "resi 99 & chain X")

cmd.select ("Outward", "resi 99 & chain X", merge=1)

cmd.color ("red", "resi 100 & chain X")

cmd.select ("Inward", "resi 100 & chain X", merge=1)

cmd.color ("blue", "resi 101 & chain X")

cmd.select ("Outward", "resi 101 & chain X", merge=1)

cmd.color ("red", "resi 102 & chain X")

cmd.select ("Inward", "resi 102 & chain X", merge=1)

cmd.color ("blue", "resi 103 & chain X")

cmd.select ("Outward", "resi 103 & chain X", merge=1)

cmd.color ("blue", "resi 81 & chain X")

cmd.select ("Outward", "resi 81 & chain X", merge=1)

cmd.color ("red", "resi 82 & chain X")

cmd.select ("Inward", "resi 82 & chain X", merge=1)

cmd.color ("blue", "resi 83 & chain X")

cmd.select ("Outward", "resi 83 & chain X", merge=1)

cmd.color ("red", "resi 84 & chain X")

cmd.select ("Inward", "resi 84 & chain X", merge=1)

cmd.color ("blue", "resi 85 & chain X")

cmd.select ("Outward", "resi 85 & chain X", merge=1)

cmd.color ("red", "resi 86 & chain X")

cmd.select ("Inward", "resi 86 & chain X", merge=1)

cmd.color ("blue", "resi 87 & chain X")

cmd.select ("Outward", "resi 87 & chain X", merge=1)

cmd.color ("red", "resi 88 & chain X")

cmd.select ("Inward", "resi 88 & chain X", merge=1)

cmd.color ("blue", "resi 69 & chain X")

cmd.select ("Outward", "resi 69 & chain X", merge=1)

cmd.color ("red", "resi 70 & chain X")

cmd.select ("Inward", "resi 70 & chain X", merge=1)

cmd.color ("blue", "resi 71 & chain X")

cmd.select ("Outward", "resi 71 & chain X", merge=1)

cmd.color ("red", "resi 72 & chain X")

cmd.select ("Inward", "resi 72 & chain X", merge=1)

cmd.color ("blue", "resi 73 & chain X")

cmd.select ("Outward", "resi 73 & chain X", merge=1)

cmd.color ("red", "resi 74 & chain X")

cmd.select ("Inward", "resi 74 & chain X", merge=1)

cmd.color ("blue", "resi 75 & chain X")

cmd.select ("Outward", "resi 75 & chain X", merge=1)

cmd.color ("red", "resi 76 & chain X")

cmd.select ("Inward", "resi 76 & chain X", merge=1)

cmd.color ("blue", "resi 54 & chain X")

cmd.select ("Outward", "resi 54 & chain X", merge=1)

cmd.color ("red", "resi 55 & chain X")

cmd.select ("Inward", "resi 55 & chain X", merge=1)

cmd.color ("blue", "resi 56 & chain X")

cmd.select ("Outward", "resi 56 & chain X", merge=1)

cmd.color ("red", "resi 57 & chain X")

cmd.select ("Inward", "resi 57 & chain X", merge=1)

cmd.color ("blue", "resi 58 & chain X")

cmd.select ("Outward", "resi 58 & chain X", merge=1)

cmd.color ("red", "resi 59 & chain X")

cmd.select ("Inward", "resi 59 & chain X", merge=1)

cmd.color ("blue", "resi 60 & chain X")

cmd.select ("Outward", "resi 60 & chain X", merge=1)

cmd.color ("red", "resi 61 & chain X")

cmd.select ("Inward", "resi 61 & chain X", merge=1)

cmd.color ("blue", "resi 62 & chain X")

cmd.select ("Outward", "resi 62 & chain X", merge=1)

cmd.color ("red", "resi 63 & chain X")

cmd.select ("Inward", "resi 63 & chain X", merge=1)

cmd.color ("blue", "resi 64 & chain X")

cmd.select ("Outward", "resi 64 & chain X", merge=1)

cmd.color ("red", "resi 38 & chain X")

cmd.select ("Inward", "resi 38 & chain X", merge=1)

cmd.color ("blue", "resi 39 & chain X")

cmd.select ("Outward", "resi 39 & chain X", merge=1)

cmd.color ("red", "resi 40 & chain X")

cmd.select ("Inward", "resi 40 & chain X", merge=1)

cmd.color ("blue", "resi 41 & chain X")

cmd.select ("Outward", "resi 41 & chain X", merge=1)

cmd.color ("red", "resi 42 & chain X")

cmd.select ("Inward", "resi 42 & chain X", merge=1)

cmd.color ("blue", "resi 43 & chain X")

cmd.select ("Outward", "resi 43 & chain X", merge=1)

cmd.color ("red", "resi 44 & chain X")

cmd.select ("Inward", "resi 44 & chain X", merge=1)

cmd.color ("blue", "resi 45 & chain X")

cmd.select ("Outward", "resi 45 & chain X", merge=1)

cmd.color ("red", "resi 46 & chain X")

cmd.select ("Inward", "resi 46 & chain X", merge=1)

cmd.color ("blue", "resi 47 & chain X")

cmd.select ("Outward", "resi 47 & chain X", merge=1)

cmd.color ("blue", "resi 48 & chain X")

cmd.select ("Outward", "resi 48 & chain X", merge=1)

cmd.load_cgo( [9.0, 2.746947,30.663424,22.828161, 2.746947, 30.663424, 22.828161, 1, 1,1,0,0,0,1], "axis" )
