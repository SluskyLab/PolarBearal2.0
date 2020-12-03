from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5GAQ.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 34+35+36+37+38+39+40+41+42+43+44+45+46+47+48+49+50+51+52+53+54+55+56+57+58+59+60+61+62+63+64+65+66 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 74+75+76+77+78+79+80+81+82+83+84+85+86+87+88+89+90+91+92+93+94+95+96+97+98+99+100+101+102+103+104+105+106+107 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Bstrand2", "resi 34+35+36+37+38+39+40+41+42+43+44+45+46+47+48+49+50+51+52+53+54+55+56+57+58+59+60+61+62+63+64+65+66 & chain B ")
cmd.color ("orange", "Bstrand2")


cmd.select("Bstrand3", "resi 74+75+76+77+78+79+80+81+82+83+84+85+86+87+88+89+90+91+92+93+94+95+96+97+98+99+100+101+102+103+104+105+106+107 & chain B ")
cmd.color ("teal", "Bstrand3")


cmd.select("Cstrand4", "resi 34+35+36+37+38+39+40+41+42+43+44+45+46+47+48+49+50+51+52+53+54+55+56+57+58+59+60+61+62+63+64+65+66 & chain C ")
cmd.color ("yellow", "Cstrand4")


cmd.select("Cstrand5", "resi 74+75+76+77+78+79+80+81+82+83+84+85+86+87+88+89+90+91+92+93+94+95+96+97+98+99+100+101+102+103+104+105+106+107 & chain C ")
cmd.color ("blue", "Cstrand5")


cmd.select("Dstrand6", "resi 34+35+36+37+38+39+40+41+42+43+44+45+46+47+48+49+50+51+52+53+54+55+56+57+58+59+60+61+62+63+64+65+66 & chain D ")
cmd.color ("red", "Dstrand6")


cmd.select("Dstrand7", "resi 74+75+76+77+78+79+80+81+82+83+84+85+86+87+88+89+90+91+92+93+94+95+96+97+98+99+100+101+102+103+104+105+106+107 & chain D ")
cmd.color ("green", "Dstrand7")


cmd.select("Estrand8", "resi 34+35+36+37+38+39+40+41+42+43+44+45+46+47+48+49+50+51+52+53+54+55+56+57+58+59+60+61+62+63+64+65+66 & chain E ")
cmd.color ("orange", "Estrand8")


cmd.select("Estrand9", "resi 74+75+76+77+78+79+80+81+82+83+84+85+86+87+88+89+90+91+92+93+94+95+96+97+98+99+100+101+102+103+104+105+106+107 & chain E ")
cmd.color ("teal", "Estrand9")


cmd.select("Fstrand10", "resi 34+35+36+37+38+39+40+41+42+43+44+45+46+47+48+49+50+51+52+53+54+55+56+57+58+59+60+61+62+63+64+65+66 & chain F ")
cmd.color ("yellow", "Fstrand10")


cmd.select("Fstrand11", "resi 74+75+76+77+78+79+80+81+82+83+84+85+86+87+88+89+90+91+92+93+94+95+96+97+98+99+100+101+102+103+104+105+106+107 & chain F ")
cmd.color ("blue", "Fstrand11")


cmd.select("Gstrand12", "resi 34+35+36+37+38+39+40+41+42+43+44+45+46+47+48+49+50+51+52+53+54+55+56+57+58+59+60+61+62+63+64+65+66 & chain G ")
cmd.color ("red", "Gstrand12")


cmd.select("Gstrand13", "resi 74+75+76+77+78+79+80+81+82+83+84+85+86+87+88+89+90+91+92+93+94+95+96+97+98+99+100+101+102+103+104+105+106+107 & chain G ")
cmd.color ("green", "Gstrand13")


cmd.select("Hstrand14", "resi 34+35+36+37+38+39+40+41+42+43+44+45+46+47+48+49+50+51+52+53+54+55+56+57+58+59+60+61+62+63+64+65+66 & chain H ")
cmd.color ("orange", "Hstrand14")


cmd.select("Hstrand15", "resi 74+75+76+77+78+79+80+81+82+83+84+85+86+87+88+89+90+91+92+93+94+95+96+97+98+99+100+101+102+103+104+105+106+107 & chain H ")
cmd.color ("teal", "Hstrand15")


cmd.select("Istrand16", "resi 34+35+36+37+38+39+40+41+42+43+44+45+46+47+48+49+50+51+52+53+54+55+56+57+58+59+60+61+62+63+64+65+66 & chain I ")
cmd.color ("yellow", "Istrand16")


cmd.select("Istrand17", "resi 74+75+76+77+78+79+80+81+82+83+84+85+86+87+88+89+90+91+92+93+94+95+96+97+98+99+100+101+102+103+104+105+106+107 & chain I ")
cmd.color ("blue", "Istrand17")


cmd.select("barrel", "Astrand* or Bstrand* or Cstrand* or Dstrand* or Estrand* or Fstrand* or Gstrand* or Hstrand* or Istrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
