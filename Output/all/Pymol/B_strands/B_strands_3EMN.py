from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3EMN.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Xstrand0", "resi 26+27+28+29+30+31+32 & chain X ")
cmd.color ("red", "Xstrand0")


cmd.select("Xstrand1", "resi 274+275+276+277+278+279+280+281+282 & chain X ")
cmd.color ("green", "Xstrand1")


cmd.select("Xstrand2", "resi 255+256+257+258+259+260+261+262+263+264 & chain X ")
cmd.color ("orange", "Xstrand2")


cmd.select("Xstrand3", "resi 242+243+244+245+246+247+248+249+250+251+252 & chain X ")
cmd.color ("teal", "Xstrand3")


cmd.select("Xstrand4", "resi 231+232+233+234+235+236+237+238 & chain X ")
cmd.color ("yellow", "Xstrand4")


cmd.select("Xstrand5", "resi 214+215+216+217+218+219+220+221+222+223+224+225 & chain X ")
cmd.color ("blue", "Xstrand5")


cmd.select("Xstrand6", "resi 202+203+204+205+206+207+208+209+210+211 & chain X ")
cmd.color ("red", "Xstrand6")


cmd.select("Xstrand7", "resi 189+190+191+192+193+194+195+196+197 & chain X ")
cmd.color ("green", "Xstrand7")


cmd.select("Xstrand8", "resi 178+179+180+181+182+183+184+185 & chain X ")
cmd.color ("orange", "Xstrand8")


cmd.select("Xstrand9", "resi 163+164+165+166+167+168+169+170+171+172+173+174 & chain X ")
cmd.color ("teal", "Xstrand9")


cmd.select("Xstrand10", "resi 149+150+151+152+153+154+155+156+157+158 & chain X ")
cmd.color ("yellow", "Xstrand10")


cmd.select("Xstrand11", "resi 137+138+139+140+141+142+143+144+145+146 & chain X ")
cmd.color ("blue", "Xstrand11")


cmd.select("Xstrand12", "resi 123+124+125+126+127+128+129+130+131 & chain X ")
cmd.color ("red", "Xstrand12")


cmd.select("Xstrand13", "resi 110+111+112+113+114+115+116+117+118+119+120 & chain X ")
cmd.color ("green", "Xstrand13")


cmd.select("Xstrand14", "resi 95+96+97+98+99+100+101+102+103 & chain X ")
cmd.color ("orange", "Xstrand14")


cmd.select("Xstrand15", "resi 81+82+83+84+85+86+87+88 & chain X ")
cmd.color ("teal", "Xstrand15")


cmd.select("Xstrand16", "resi 69+70+71+72+73+74+75+76 & chain X ")
cmd.color ("yellow", "Xstrand16")


cmd.select("Xstrand17", "resi 54+55+56+57+58+59+60+61+62+63+64 & chain X ")
cmd.color ("blue", "Xstrand17")


cmd.select("Xstrand18", "resi 38+39+40+41+42+43+44+45+46+47+48 & chain X ")
cmd.color ("red", "Xstrand18")


cmd.select("barrel", "Xstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
