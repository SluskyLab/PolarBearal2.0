from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3DWO.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Xstrand0", "resi 44+45+46+47+48+49+50+51+52+53+54+55+56+57+58+59+60+61+62+63 & chain X ")


cmd.select("Xstrand18", "resi 423+424+425+426+427+428+429+430+431+432+433+434+435+436+437+438+439+440+441 & chain X ")


cmd.select("Xstrand12", "resi 324+325+326+327+328+329+330+336+337+338+339+340+341+342+343+344+345+346 & chain X ")


cmd.select("Xstrand6", "resi 226+227+228+229+230+231+232+233+239+240+241+242+243+244+245+246+247+248 & chain X ")


cmd.select("Xstrand10", "resi 300+301+302+303+304+305+306+307+308+309+316+317+318+319+320+321 & chain X ")


cmd.select("Xstrand5", "resi 201+202+203+204+205+206+207+208+209+210+211+212+213+214+215+216+217+218+219+220 & chain X ")


cmd.select("Xstrand4", "resi 158+159+160+161+162+163+164+165+166+167+168+169+170+171+172+173+174+175+176+177 & chain X ")


cmd.select("Xstrand8", "resi 275+276+277+278+279+280+281+287+288+289+290+291+292+293+294+295 & chain X ")


cmd.select("Xstrand3", "resi 138+139+140+141+142+143+144+145+146+147+148+149+150+151+152+153 & chain X ")


cmd.select("Xstrand2", "resi 110+111+112+113+114+115+116+117+118+119+120+121+122+123+124+125 & chain X ")


cmd.select("Xstrand1", "resi 93+94+95+96+97+98+99+100+101+102+103+104+105 & chain X ")


cmd.select("Xstrand14", "resi 351+352+353+354+355+356+357+358+359+360 & chain X ")


cmd.select("Xstrand15", "resi 378+379+380+381+382+383+384+385+386+387+388 & chain X ")


cmd.select("Xstrand16", "resi 395+396+397+398+399+400+401+402+403+404+405+406 & chain X ")


cmd.select("barrel", "Xstrand*")
cmd.show("sticks", "barrel")
cmd.show("cartoon", "barrel")
cmd.set("cartoon_side_chain_helper", "on")
cmd.zoom("barrel")
cmd.color ("red", "resi 44 & chain X")

cmd.select ("Inward", "resi 44 & chain X", merge=1)

cmd.color ("blue", "resi 45 & chain X")

cmd.select ("Outward", "resi 45 & chain X", merge=1)

cmd.color ("red", "resi 46 & chain X")

cmd.select ("Inward", "resi 46 & chain X", merge=1)

cmd.color ("blue", "resi 47 & chain X")

cmd.select ("Outward", "resi 47 & chain X", merge=1)

cmd.color ("red", "resi 48 & chain X")

cmd.select ("Inward", "resi 48 & chain X", merge=1)

cmd.color ("blue", "resi 49 & chain X")

cmd.select ("Outward", "resi 49 & chain X", merge=1)

cmd.color ("red", "resi 50 & chain X")

cmd.select ("Inward", "resi 50 & chain X", merge=1)

cmd.color ("blue", "resi 51 & chain X")

cmd.select ("Outward", "resi 51 & chain X", merge=1)

cmd.color ("red", "resi 52 & chain X")

cmd.select ("Inward", "resi 52 & chain X", merge=1)

cmd.color ("blue", "resi 53 & chain X")

cmd.select ("Outward", "resi 53 & chain X", merge=1)

cmd.color ("red", "resi 54 & chain X")

cmd.select ("Inward", "resi 54 & chain X", merge=1)

cmd.color ("blue", "resi 55 & chain X")

cmd.select ("Outward", "resi 55 & chain X", merge=1)

cmd.color ("red", "resi 56 & chain X")

cmd.select ("Inward", "resi 56 & chain X", merge=1)

cmd.color ("blue", "resi 57 & chain X")

cmd.select ("Outward", "resi 57 & chain X", merge=1)

cmd.color ("red", "resi 58 & chain X")

cmd.select ("Inward", "resi 58 & chain X", merge=1)

cmd.color ("blue", "resi 59 & chain X")

cmd.select ("Outward", "resi 59 & chain X", merge=1)

cmd.color ("red", "resi 60 & chain X")

cmd.select ("Inward", "resi 60 & chain X", merge=1)

cmd.color ("blue", "resi 61 & chain X")

cmd.select ("Outward", "resi 61 & chain X", merge=1)

cmd.color ("red", "resi 62 & chain X")

cmd.select ("Inward", "resi 62 & chain X", merge=1)

cmd.color ("blue", "resi 63 & chain X")

cmd.select ("Outward", "resi 63 & chain X", merge=1)

cmd.color ("blue", "resi 423 & chain X")

cmd.select ("Outward", "resi 423 & chain X", merge=1)

cmd.color ("red", "resi 424 & chain X")

cmd.select ("Inward", "resi 424 & chain X", merge=1)

cmd.color ("red", "resi 425 & chain X")

cmd.select ("Inward", "resi 425 & chain X", merge=1)

cmd.color ("red", "resi 426 & chain X")

cmd.select ("Inward", "resi 426 & chain X", merge=1)

cmd.color ("blue", "resi 427 & chain X")

cmd.select ("Outward", "resi 427 & chain X", merge=1)

cmd.color ("red", "resi 428 & chain X")

cmd.select ("Inward", "resi 428 & chain X", merge=1)

cmd.color ("blue", "resi 429 & chain X")

cmd.select ("Outward", "resi 429 & chain X", merge=1)

cmd.color ("red", "resi 430 & chain X")

cmd.select ("Inward", "resi 430 & chain X", merge=1)

cmd.color ("blue", "resi 431 & chain X")

cmd.select ("Outward", "resi 431 & chain X", merge=1)

cmd.color ("red", "resi 432 & chain X")

cmd.select ("Inward", "resi 432 & chain X", merge=1)

cmd.color ("blue", "resi 433 & chain X")

cmd.select ("Outward", "resi 433 & chain X", merge=1)

cmd.color ("red", "resi 434 & chain X")

cmd.select ("Inward", "resi 434 & chain X", merge=1)

cmd.color ("blue", "resi 435 & chain X")

cmd.select ("Outward", "resi 435 & chain X", merge=1)

cmd.color ("red", "resi 436 & chain X")

cmd.select ("Inward", "resi 436 & chain X", merge=1)

cmd.color ("blue", "resi 437 & chain X")

cmd.select ("Outward", "resi 437 & chain X", merge=1)

cmd.color ("red", "resi 438 & chain X")

cmd.select ("Inward", "resi 438 & chain X", merge=1)

cmd.color ("blue", "resi 439 & chain X")

cmd.select ("Outward", "resi 439 & chain X", merge=1)

cmd.color ("red", "resi 440 & chain X")

cmd.select ("Inward", "resi 440 & chain X", merge=1)

cmd.color ("red", "resi 441 & chain X")

cmd.select ("Inward", "resi 441 & chain X", merge=1)

cmd.color ("red", "resi 324 & chain X")

cmd.select ("Inward", "resi 324 & chain X", merge=1)

cmd.color ("blue", "resi 325 & chain X")

cmd.select ("Outward", "resi 325 & chain X", merge=1)

cmd.color ("red", "resi 326 & chain X")

cmd.select ("Inward", "resi 326 & chain X", merge=1)

cmd.color ("red", "resi 327 & chain X")

cmd.select ("Inward", "resi 327 & chain X", merge=1)

cmd.color ("blue", "resi 328 & chain X")

cmd.select ("Outward", "resi 328 & chain X", merge=1)

cmd.color ("red", "resi 329 & chain X")

cmd.select ("Inward", "resi 329 & chain X", merge=1)

cmd.color ("blue", "resi 330 & chain X")

cmd.select ("Outward", "resi 330 & chain X", merge=1)

cmd.color ("red", "resi 336 & chain X")

cmd.select ("Inward", "resi 336 & chain X", merge=1)

cmd.color ("blue", "resi 337 & chain X")

cmd.select ("Outward", "resi 337 & chain X", merge=1)

cmd.color ("red", "resi 338 & chain X")

cmd.select ("Inward", "resi 338 & chain X", merge=1)

cmd.color ("blue", "resi 339 & chain X")

cmd.select ("Outward", "resi 339 & chain X", merge=1)

cmd.color ("red", "resi 340 & chain X")

cmd.select ("Inward", "resi 340 & chain X", merge=1)

cmd.color ("blue", "resi 341 & chain X")

cmd.select ("Outward", "resi 341 & chain X", merge=1)

cmd.color ("red", "resi 342 & chain X")

cmd.select ("Inward", "resi 342 & chain X", merge=1)

cmd.color ("blue", "resi 343 & chain X")

cmd.select ("Outward", "resi 343 & chain X", merge=1)

cmd.color ("red", "resi 344 & chain X")

cmd.select ("Inward", "resi 344 & chain X", merge=1)

cmd.color ("blue", "resi 345 & chain X")

cmd.select ("Outward", "resi 345 & chain X", merge=1)

cmd.color ("blue", "resi 346 & chain X")

cmd.select ("Outward", "resi 346 & chain X", merge=1)

cmd.color ("blue", "resi 226 & chain X")

cmd.select ("Outward", "resi 226 & chain X", merge=1)

cmd.color ("red", "resi 227 & chain X")

cmd.select ("Inward", "resi 227 & chain X", merge=1)

cmd.color ("blue", "resi 228 & chain X")

cmd.select ("Outward", "resi 228 & chain X", merge=1)

cmd.color ("red", "resi 229 & chain X")

cmd.select ("Inward", "resi 229 & chain X", merge=1)

cmd.color ("blue", "resi 230 & chain X")

cmd.select ("Outward", "resi 230 & chain X", merge=1)

cmd.color ("red", "resi 231 & chain X")

cmd.select ("Inward", "resi 231 & chain X", merge=1)

cmd.color ("blue", "resi 232 & chain X")

cmd.select ("Outward", "resi 232 & chain X", merge=1)

cmd.color ("red", "resi 233 & chain X")

cmd.select ("Inward", "resi 233 & chain X", merge=1)

cmd.color ("blue", "resi 239 & chain X")

cmd.select ("Outward", "resi 239 & chain X", merge=1)

cmd.color ("red", "resi 240 & chain X")

cmd.select ("Inward", "resi 240 & chain X", merge=1)

cmd.color ("blue", "resi 241 & chain X")

cmd.select ("Outward", "resi 241 & chain X", merge=1)

cmd.color ("red", "resi 242 & chain X")

cmd.select ("Inward", "resi 242 & chain X", merge=1)

cmd.color ("blue", "resi 243 & chain X")

cmd.select ("Outward", "resi 243 & chain X", merge=1)

cmd.color ("red", "resi 244 & chain X")

cmd.select ("Inward", "resi 244 & chain X", merge=1)

cmd.color ("blue", "resi 245 & chain X")

cmd.select ("Outward", "resi 245 & chain X", merge=1)

cmd.color ("blue", "resi 246 & chain X")

cmd.select ("Outward", "resi 246 & chain X", merge=1)

cmd.color ("red", "resi 247 & chain X")

cmd.select ("Inward", "resi 247 & chain X", merge=1)

cmd.color ("blue", "resi 248 & chain X")

cmd.select ("Outward", "resi 248 & chain X", merge=1)

cmd.color ("blue", "resi 300 & chain X")

cmd.select ("Outward", "resi 300 & chain X", merge=1)

cmd.color ("red", "resi 301 & chain X")

cmd.select ("Inward", "resi 301 & chain X", merge=1)

cmd.color ("blue", "resi 302 & chain X")

cmd.select ("Outward", "resi 302 & chain X", merge=1)

cmd.color ("red", "resi 303 & chain X")

cmd.select ("Inward", "resi 303 & chain X", merge=1)

cmd.color ("blue", "resi 304 & chain X")

cmd.select ("Outward", "resi 304 & chain X", merge=1)

cmd.color ("red", "resi 305 & chain X")

cmd.select ("Inward", "resi 305 & chain X", merge=1)

cmd.color ("blue", "resi 306 & chain X")

cmd.select ("Outward", "resi 306 & chain X", merge=1)

cmd.color ("red", "resi 307 & chain X")

cmd.select ("Inward", "resi 307 & chain X", merge=1)

cmd.color ("blue", "resi 308 & chain X")

cmd.select ("Outward", "resi 308 & chain X", merge=1)

cmd.color ("red", "resi 309 & chain X")

cmd.select ("Inward", "resi 309 & chain X", merge=1)

cmd.color ("blue", "resi 316 & chain X")

cmd.select ("Outward", "resi 316 & chain X", merge=1)

cmd.color ("red", "resi 317 & chain X")

cmd.select ("Inward", "resi 317 & chain X", merge=1)

cmd.color ("blue", "resi 318 & chain X")

cmd.select ("Outward", "resi 318 & chain X", merge=1)

cmd.color ("red", "resi 319 & chain X")

cmd.select ("Inward", "resi 319 & chain X", merge=1)

cmd.color ("blue", "resi 320 & chain X")

cmd.select ("Outward", "resi 320 & chain X", merge=1)

cmd.color ("red", "resi 321 & chain X")

cmd.select ("Inward", "resi 321 & chain X", merge=1)

cmd.color ("red", "resi 201 & chain X")

cmd.select ("Inward", "resi 201 & chain X", merge=1)

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

cmd.color ("red", "resi 211 & chain X")

cmd.select ("Inward", "resi 211 & chain X", merge=1)

cmd.color ("blue", "resi 212 & chain X")

cmd.select ("Outward", "resi 212 & chain X", merge=1)

cmd.color ("red", "resi 213 & chain X")

cmd.select ("Inward", "resi 213 & chain X", merge=1)

cmd.color ("blue", "resi 214 & chain X")

cmd.select ("Outward", "resi 214 & chain X", merge=1)

cmd.color ("red", "resi 215 & chain X")

cmd.select ("Inward", "resi 215 & chain X", merge=1)

cmd.color ("blue", "resi 216 & chain X")

cmd.select ("Outward", "resi 216 & chain X", merge=1)

cmd.color ("red", "resi 217 & chain X")

cmd.select ("Inward", "resi 217 & chain X", merge=1)

cmd.color ("blue", "resi 218 & chain X")

cmd.select ("Outward", "resi 218 & chain X", merge=1)

cmd.color ("red", "resi 219 & chain X")

cmd.select ("Inward", "resi 219 & chain X", merge=1)

cmd.color ("blue", "resi 220 & chain X")

cmd.select ("Outward", "resi 220 & chain X", merge=1)

cmd.color ("blue", "resi 158 & chain X")

cmd.select ("Outward", "resi 158 & chain X", merge=1)

cmd.color ("red", "resi 159 & chain X")

cmd.select ("Inward", "resi 159 & chain X", merge=1)

cmd.color ("blue", "resi 160 & chain X")

cmd.select ("Outward", "resi 160 & chain X", merge=1)

cmd.color ("red", "resi 161 & chain X")

cmd.select ("Inward", "resi 161 & chain X", merge=1)

cmd.color ("blue", "resi 162 & chain X")

cmd.select ("Outward", "resi 162 & chain X", merge=1)

cmd.color ("red", "resi 163 & chain X")

cmd.select ("Inward", "resi 163 & chain X", merge=1)

cmd.color ("blue", "resi 164 & chain X")

cmd.select ("Outward", "resi 164 & chain X", merge=1)

cmd.color ("red", "resi 165 & chain X")

cmd.select ("Inward", "resi 165 & chain X", merge=1)

cmd.color ("blue", "resi 166 & chain X")

cmd.select ("Outward", "resi 166 & chain X", merge=1)

cmd.color ("red", "resi 167 & chain X")

cmd.select ("Inward", "resi 167 & chain X", merge=1)

cmd.color ("blue", "resi 168 & chain X")

cmd.select ("Outward", "resi 168 & chain X", merge=1)

cmd.color ("red", "resi 169 & chain X")

cmd.select ("Inward", "resi 169 & chain X", merge=1)

cmd.color ("blue", "resi 170 & chain X")

cmd.select ("Outward", "resi 170 & chain X", merge=1)

cmd.color ("red", "resi 171 & chain X")

cmd.select ("Inward", "resi 171 & chain X", merge=1)

cmd.color ("blue", "resi 172 & chain X")

cmd.select ("Outward", "resi 172 & chain X", merge=1)

cmd.color ("red", "resi 173 & chain X")

cmd.select ("Inward", "resi 173 & chain X", merge=1)

cmd.color ("blue", "resi 174 & chain X")

cmd.select ("Outward", "resi 174 & chain X", merge=1)

cmd.color ("red", "resi 175 & chain X")

cmd.select ("Inward", "resi 175 & chain X", merge=1)

cmd.color ("blue", "resi 176 & chain X")

cmd.select ("Outward", "resi 176 & chain X", merge=1)

cmd.color ("red", "resi 177 & chain X")

cmd.select ("Inward", "resi 177 & chain X", merge=1)

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

cmd.color ("red", "resi 287 & chain X")

cmd.select ("Inward", "resi 287 & chain X", merge=1)

cmd.color ("blue", "resi 288 & chain X")

cmd.select ("Outward", "resi 288 & chain X", merge=1)

cmd.color ("red", "resi 289 & chain X")

cmd.select ("Inward", "resi 289 & chain X", merge=1)

cmd.color ("blue", "resi 290 & chain X")

cmd.select ("Outward", "resi 290 & chain X", merge=1)

cmd.color ("red", "resi 291 & chain X")

cmd.select ("Inward", "resi 291 & chain X", merge=1)

cmd.color ("blue", "resi 292 & chain X")

cmd.select ("Outward", "resi 292 & chain X", merge=1)

cmd.color ("red", "resi 293 & chain X")

cmd.select ("Inward", "resi 293 & chain X", merge=1)

cmd.color ("blue", "resi 294 & chain X")

cmd.select ("Outward", "resi 294 & chain X", merge=1)

cmd.color ("blue", "resi 295 & chain X")

cmd.select ("Outward", "resi 295 & chain X", merge=1)

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

cmd.color ("red", "resi 147 & chain X")

cmd.select ("Inward", "resi 147 & chain X", merge=1)

cmd.color ("blue", "resi 148 & chain X")

cmd.select ("Outward", "resi 148 & chain X", merge=1)

cmd.color ("red", "resi 149 & chain X")

cmd.select ("Inward", "resi 149 & chain X", merge=1)

cmd.color ("blue", "resi 150 & chain X")

cmd.select ("Outward", "resi 150 & chain X", merge=1)

cmd.color ("red", "resi 151 & chain X")

cmd.select ("Inward", "resi 151 & chain X", merge=1)

cmd.color ("blue", "resi 152 & chain X")

cmd.select ("Outward", "resi 152 & chain X", merge=1)

cmd.color ("blue", "resi 153 & chain X")

cmd.select ("Outward", "resi 153 & chain X", merge=1)

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

cmd.color ("red", "resi 121 & chain X")

cmd.select ("Inward", "resi 121 & chain X", merge=1)

cmd.color ("red", "resi 122 & chain X")

cmd.select ("Inward", "resi 122 & chain X", merge=1)

cmd.color ("blue", "resi 123 & chain X")

cmd.select ("Outward", "resi 123 & chain X", merge=1)

cmd.color ("red", "resi 124 & chain X")

cmd.select ("Inward", "resi 124 & chain X", merge=1)

cmd.color ("blue", "resi 125 & chain X")

cmd.select ("Outward", "resi 125 & chain X", merge=1)

cmd.color ("red", "resi 93 & chain X")

cmd.select ("Inward", "resi 93 & chain X", merge=1)

cmd.color ("blue", "resi 94 & chain X")

cmd.select ("Outward", "resi 94 & chain X", merge=1)

cmd.color ("red", "resi 95 & chain X")

cmd.select ("Inward", "resi 95 & chain X", merge=1)

cmd.color ("blue", "resi 96 & chain X")

cmd.select ("Outward", "resi 96 & chain X", merge=1)

cmd.color ("red", "resi 97 & chain X")

cmd.select ("Inward", "resi 97 & chain X", merge=1)

cmd.color ("blue", "resi 98 & chain X")

cmd.select ("Outward", "resi 98 & chain X", merge=1)

cmd.color ("red", "resi 99 & chain X")

cmd.select ("Inward", "resi 99 & chain X", merge=1)

cmd.color ("blue", "resi 100 & chain X")

cmd.select ("Outward", "resi 100 & chain X", merge=1)

cmd.color ("red", "resi 101 & chain X")

cmd.select ("Inward", "resi 101 & chain X", merge=1)

cmd.color ("blue", "resi 102 & chain X")

cmd.select ("Outward", "resi 102 & chain X", merge=1)

cmd.color ("red", "resi 103 & chain X")

cmd.select ("Inward", "resi 103 & chain X", merge=1)

cmd.color ("blue", "resi 104 & chain X")

cmd.select ("Outward", "resi 104 & chain X", merge=1)

cmd.color ("blue", "resi 105 & chain X")

cmd.select ("Outward", "resi 105 & chain X", merge=1)

cmd.color ("blue", "resi 351 & chain X")

cmd.select ("Outward", "resi 351 & chain X", merge=1)

cmd.color ("red", "resi 352 & chain X")

cmd.select ("Inward", "resi 352 & chain X", merge=1)

cmd.color ("blue", "resi 353 & chain X")

cmd.select ("Outward", "resi 353 & chain X", merge=1)

cmd.color ("red", "resi 354 & chain X")

cmd.select ("Inward", "resi 354 & chain X", merge=1)

cmd.color ("blue", "resi 355 & chain X")

cmd.select ("Outward", "resi 355 & chain X", merge=1)

cmd.color ("red", "resi 356 & chain X")

cmd.select ("Inward", "resi 356 & chain X", merge=1)

cmd.color ("blue", "resi 357 & chain X")

cmd.select ("Outward", "resi 357 & chain X", merge=1)

cmd.color ("red", "resi 358 & chain X")

cmd.select ("Inward", "resi 358 & chain X", merge=1)

cmd.color ("blue", "resi 359 & chain X")

cmd.select ("Outward", "resi 359 & chain X", merge=1)

cmd.color ("red", "resi 360 & chain X")

cmd.select ("Inward", "resi 360 & chain X", merge=1)

cmd.color ("red", "resi 378 & chain X")

cmd.select ("Inward", "resi 378 & chain X", merge=1)

cmd.color ("blue", "resi 379 & chain X")

cmd.select ("Outward", "resi 379 & chain X", merge=1)

cmd.color ("red", "resi 380 & chain X")

cmd.select ("Inward", "resi 380 & chain X", merge=1)

cmd.color ("blue", "resi 381 & chain X")

cmd.select ("Outward", "resi 381 & chain X", merge=1)

cmd.color ("red", "resi 382 & chain X")

cmd.select ("Inward", "resi 382 & chain X", merge=1)

cmd.color ("blue", "resi 383 & chain X")

cmd.select ("Outward", "resi 383 & chain X", merge=1)

cmd.color ("red", "resi 384 & chain X")

cmd.select ("Inward", "resi 384 & chain X", merge=1)

cmd.color ("blue", "resi 385 & chain X")

cmd.select ("Outward", "resi 385 & chain X", merge=1)

cmd.color ("red", "resi 386 & chain X")

cmd.select ("Inward", "resi 386 & chain X", merge=1)

cmd.color ("blue", "resi 387 & chain X")

cmd.select ("Outward", "resi 387 & chain X", merge=1)

cmd.color ("blue", "resi 388 & chain X")

cmd.select ("Outward", "resi 388 & chain X", merge=1)

cmd.color ("blue", "resi 395 & chain X")

cmd.select ("Outward", "resi 395 & chain X", merge=1)

cmd.color ("red", "resi 396 & chain X")

cmd.select ("Inward", "resi 396 & chain X", merge=1)

cmd.color ("blue", "resi 397 & chain X")

cmd.select ("Outward", "resi 397 & chain X", merge=1)

cmd.color ("red", "resi 398 & chain X")

cmd.select ("Inward", "resi 398 & chain X", merge=1)

cmd.color ("blue", "resi 399 & chain X")

cmd.select ("Outward", "resi 399 & chain X", merge=1)

cmd.color ("red", "resi 400 & chain X")

cmd.select ("Inward", "resi 400 & chain X", merge=1)

cmd.color ("blue", "resi 401 & chain X")

cmd.select ("Outward", "resi 401 & chain X", merge=1)

cmd.color ("red", "resi 402 & chain X")

cmd.select ("Inward", "resi 402 & chain X", merge=1)

cmd.color ("blue", "resi 403 & chain X")

cmd.select ("Outward", "resi 403 & chain X", merge=1)

cmd.color ("red", "resi 404 & chain X")

cmd.select ("Inward", "resi 404 & chain X", merge=1)

cmd.color ("blue", "resi 405 & chain X")

cmd.select ("Outward", "resi 405 & chain X", merge=1)

cmd.color ("red", "resi 406 & chain X")

cmd.select ("Inward", "resi 406 & chain X", merge=1)

cmd.load_cgo( [9.0, 45.10793,62.770355,42.872997, 45.10793, 62.770355, 42.872997, 1, 1,1,0,0,0,1], "axis" )
