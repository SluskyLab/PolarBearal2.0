from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5GAQ.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand1", "resi 34+35+36+37+38+39+40+41+42+43+44+45+46+47+48+49+50+51+52+53+54+55+56+57+58+59+60+61+62+63+64+65+66 & chain A ")


cmd.select("Astrand2", "resi 74+75+76+77+78+79+80+81+82+83+84+85+86+87+88+89+90+91+92+93+94+95+96+97+98+99+100+101+102+103+104+105+106+107 & chain A ")


cmd.select("Bstrand18", "resi 34+35+36+37+38+39+40+41+42+43+44+45+46+47+48+49+50+51+52+53+54+55+56+57+58+59+60+61+62+63+64+65+66 & chain B ")


cmd.select("Bstrand19", "resi 74+75+76+77+78+79+80+81+82+83+84+85+86+87+88+89+90+91+92+93+94+95+96+97+98+99+100+101+102+103+104+105+106+107 & chain B ")


cmd.select("Cstrand35", "resi 34+35+36+37+38+39+40+41+42+43+44+45+46+47+48+49+50+51+52+53+54+55+56+57+58+59+60+61+62+63+64+65+66 & chain C ")


cmd.select("Cstrand36", "resi 74+75+76+77+78+79+80+81+82+83+84+85+86+87+88+89+90+91+92+93+94+95+96+97+98+99+100+101+102+103+104+105+106+107 & chain C ")


cmd.select("Dstrand52", "resi 34+35+36+37+38+39+40+41+42+43+44+45+46+47+48+49+50+51+52+53+54+55+56+57+58+59+60+61+62+63+64+65+66 & chain D ")


cmd.select("Dstrand53", "resi 74+75+76+77+78+79+80+81+82+83+84+85+86+87+88+89+90+91+92+93+94+95+96+97+98+99+100+101+102+103+104+105+106+107 & chain D ")


cmd.select("Estrand69", "resi 34+35+36+37+38+39+40+41+42+43+44+45+46+47+48+49+50+51+52+53+54+55+56+57+58+59+60+61+62+63+64+65+66 & chain E ")


cmd.select("Estrand70", "resi 74+75+76+77+78+79+80+81+82+83+84+85+86+87+88+89+90+91+92+93+94+95+96+97+98+99+100+101+102+103+104+105+106+107 & chain E ")


cmd.select("Fstrand86", "resi 34+35+36+37+38+39+40+41+42+43+44+45+46+47+48+49+50+51+52+53+54+55+56+57+58+59+60+61+62+63+64+65+66 & chain F ")


cmd.select("Fstrand87", "resi 74+75+76+77+78+79+80+81+82+83+84+85+86+87+88+89+90+91+92+93+94+95+96+97+98+99+100+101+102+103+104+105+106+107 & chain F ")


cmd.select("Gstrand103", "resi 34+35+36+37+38+39+40+41+42+43+44+45+46+47+48+49+50+51+52+53+54+55+56+57+58+59+60+61+62+63+64+65+66 & chain G ")


cmd.select("Gstrand104", "resi 74+75+76+77+78+79+80+81+82+83+84+85+86+87+88+89+90+91+92+93+94+95+96+97+98+99+100+101+102+103+104+105+106+107 & chain G ")


cmd.select("Hstrand120", "resi 34+35+36+37+38+39+40+41+42+43+44+45+46+47+48+49+50+51+52+53+54+55+56+57+58+59+60+61+62+63+64+65+66 & chain H ")


cmd.select("Hstrand121", "resi 74+75+76+77+78+79+80+81+82+83+84+85+86+87+88+89+90+91+92+93+94+95+96+97+98+99+100+101+102+103+104+105+106+107 & chain H ")


cmd.select("Istrand137", "resi 34+35+36+37+38+39+40+41+42+43+44+45+46+47+48+49+50+51+52+53+54+55+56+57+58+59+60+61+62+63+64+65+66 & chain I ")


cmd.select("Istrand138", "resi 74+75+76+77+78+79+80+81+82+83+84+85+86+87+88+89+90+91+92+93+94+95+96+97+98+99+100+101+102+103+104+105+106+107 & chain I ")


cmd.select("barrel", "Astrand* or Bstrand* or Cstrand* or Dstrand* or Estrand* or Fstrand* or Gstrand* or Hstrand* or Istrand*")
cmd.show("sticks", "barrel")
cmd.show("cartoon", "barrel")
cmd.set("cartoon_side_chain_helper", "on")
cmd.zoom("barrel")
cmd.color ("blue", "resi 34 & chain A")

cmd.select ("Outward", "resi 34 & chain A", merge=1)

cmd.color ("blue", "resi 35 & chain A")

cmd.select ("Outward", "resi 35 & chain A", merge=1)

cmd.color ("blue", "resi 36 & chain A")

cmd.select ("Outward", "resi 36 & chain A", merge=1)

cmd.color ("blue", "resi 37 & chain A")

cmd.select ("Outward", "resi 37 & chain A", merge=1)

cmd.color ("blue", "resi 38 & chain A")

cmd.select ("Outward", "resi 38 & chain A", merge=1)

cmd.color ("blue", "resi 39 & chain A")

cmd.select ("Outward", "resi 39 & chain A", merge=1)

cmd.color ("blue", "resi 40 & chain A")

cmd.select ("Outward", "resi 40 & chain A", merge=1)

cmd.color ("blue", "resi 41 & chain A")

cmd.select ("Outward", "resi 41 & chain A", merge=1)

cmd.color ("blue", "resi 42 & chain A")

cmd.select ("Outward", "resi 42 & chain A", merge=1)

cmd.color ("blue", "resi 43 & chain A")

cmd.select ("Outward", "resi 43 & chain A", merge=1)

cmd.color ("blue", "resi 44 & chain A")

cmd.select ("Outward", "resi 44 & chain A", merge=1)

cmd.color ("blue", "resi 45 & chain A")

cmd.select ("Outward", "resi 45 & chain A", merge=1)

cmd.color ("blue", "resi 46 & chain A")

cmd.select ("Outward", "resi 46 & chain A", merge=1)

cmd.color ("blue", "resi 47 & chain A")

cmd.select ("Outward", "resi 47 & chain A", merge=1)

cmd.color ("blue", "resi 48 & chain A")

cmd.select ("Outward", "resi 48 & chain A", merge=1)

cmd.color ("blue", "resi 49 & chain A")

cmd.select ("Outward", "resi 49 & chain A", merge=1)

cmd.color ("blue", "resi 50 & chain A")

cmd.select ("Outward", "resi 50 & chain A", merge=1)

cmd.color ("blue", "resi 51 & chain A")

cmd.select ("Outward", "resi 51 & chain A", merge=1)

cmd.color ("blue", "resi 52 & chain A")

cmd.select ("Outward", "resi 52 & chain A", merge=1)

cmd.color ("blue", "resi 53 & chain A")

cmd.select ("Outward", "resi 53 & chain A", merge=1)

cmd.color ("blue", "resi 54 & chain A")

cmd.select ("Outward", "resi 54 & chain A", merge=1)

cmd.color ("blue", "resi 55 & chain A")

cmd.select ("Outward", "resi 55 & chain A", merge=1)

cmd.color ("blue", "resi 56 & chain A")

cmd.select ("Outward", "resi 56 & chain A", merge=1)

cmd.color ("blue", "resi 57 & chain A")

cmd.select ("Outward", "resi 57 & chain A", merge=1)

cmd.color ("blue", "resi 58 & chain A")

cmd.select ("Outward", "resi 58 & chain A", merge=1)

cmd.color ("blue", "resi 59 & chain A")

cmd.select ("Outward", "resi 59 & chain A", merge=1)

cmd.color ("blue", "resi 60 & chain A")

cmd.select ("Outward", "resi 60 & chain A", merge=1)

cmd.color ("blue", "resi 61 & chain A")

cmd.select ("Outward", "resi 61 & chain A", merge=1)

cmd.color ("blue", "resi 62 & chain A")

cmd.select ("Outward", "resi 62 & chain A", merge=1)

cmd.color ("blue", "resi 63 & chain A")

cmd.select ("Outward", "resi 63 & chain A", merge=1)

cmd.color ("blue", "resi 64 & chain A")

cmd.select ("Outward", "resi 64 & chain A", merge=1)

cmd.color ("blue", "resi 65 & chain A")

cmd.select ("Outward", "resi 65 & chain A", merge=1)

cmd.color ("blue", "resi 66 & chain A")

cmd.select ("Outward", "resi 66 & chain A", merge=1)

cmd.color ("blue", "resi 74 & chain A")

cmd.select ("Outward", "resi 74 & chain A", merge=1)

cmd.color ("blue", "resi 75 & chain A")

cmd.select ("Outward", "resi 75 & chain A", merge=1)

cmd.color ("blue", "resi 76 & chain A")

cmd.select ("Outward", "resi 76 & chain A", merge=1)

cmd.color ("blue", "resi 77 & chain A")

cmd.select ("Outward", "resi 77 & chain A", merge=1)

cmd.color ("blue", "resi 78 & chain A")

cmd.select ("Outward", "resi 78 & chain A", merge=1)

cmd.color ("blue", "resi 79 & chain A")

cmd.select ("Outward", "resi 79 & chain A", merge=1)

cmd.color ("blue", "resi 80 & chain A")

cmd.select ("Outward", "resi 80 & chain A", merge=1)

cmd.color ("blue", "resi 81 & chain A")

cmd.select ("Outward", "resi 81 & chain A", merge=1)

cmd.color ("blue", "resi 82 & chain A")

cmd.select ("Outward", "resi 82 & chain A", merge=1)

cmd.color ("blue", "resi 83 & chain A")

cmd.select ("Outward", "resi 83 & chain A", merge=1)

cmd.color ("blue", "resi 84 & chain A")

cmd.select ("Outward", "resi 84 & chain A", merge=1)

cmd.color ("blue", "resi 85 & chain A")

cmd.select ("Outward", "resi 85 & chain A", merge=1)

cmd.color ("blue", "resi 86 & chain A")

cmd.select ("Outward", "resi 86 & chain A", merge=1)

cmd.color ("blue", "resi 87 & chain A")

cmd.select ("Outward", "resi 87 & chain A", merge=1)

cmd.color ("blue", "resi 88 & chain A")

cmd.select ("Outward", "resi 88 & chain A", merge=1)

cmd.color ("blue", "resi 89 & chain A")

cmd.select ("Outward", "resi 89 & chain A", merge=1)

cmd.color ("blue", "resi 90 & chain A")

cmd.select ("Outward", "resi 90 & chain A", merge=1)

cmd.color ("blue", "resi 91 & chain A")

cmd.select ("Outward", "resi 91 & chain A", merge=1)

cmd.color ("blue", "resi 92 & chain A")

cmd.select ("Outward", "resi 92 & chain A", merge=1)

cmd.color ("blue", "resi 93 & chain A")

cmd.select ("Outward", "resi 93 & chain A", merge=1)

cmd.color ("blue", "resi 94 & chain A")

cmd.select ("Outward", "resi 94 & chain A", merge=1)

cmd.color ("blue", "resi 95 & chain A")

cmd.select ("Outward", "resi 95 & chain A", merge=1)

cmd.color ("blue", "resi 96 & chain A")

cmd.select ("Outward", "resi 96 & chain A", merge=1)

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

cmd.color ("blue", "resi 34 & chain B")

cmd.select ("Outward", "resi 34 & chain B", merge=1)

cmd.color ("blue", "resi 35 & chain B")

cmd.select ("Outward", "resi 35 & chain B", merge=1)

cmd.color ("blue", "resi 36 & chain B")

cmd.select ("Outward", "resi 36 & chain B", merge=1)

cmd.color ("blue", "resi 37 & chain B")

cmd.select ("Outward", "resi 37 & chain B", merge=1)

cmd.color ("blue", "resi 38 & chain B")

cmd.select ("Outward", "resi 38 & chain B", merge=1)

cmd.color ("blue", "resi 39 & chain B")

cmd.select ("Outward", "resi 39 & chain B", merge=1)

cmd.color ("blue", "resi 40 & chain B")

cmd.select ("Outward", "resi 40 & chain B", merge=1)

cmd.color ("blue", "resi 41 & chain B")

cmd.select ("Outward", "resi 41 & chain B", merge=1)

cmd.color ("blue", "resi 42 & chain B")

cmd.select ("Outward", "resi 42 & chain B", merge=1)

cmd.color ("blue", "resi 43 & chain B")

cmd.select ("Outward", "resi 43 & chain B", merge=1)

cmd.color ("blue", "resi 44 & chain B")

cmd.select ("Outward", "resi 44 & chain B", merge=1)

cmd.color ("blue", "resi 45 & chain B")

cmd.select ("Outward", "resi 45 & chain B", merge=1)

cmd.color ("blue", "resi 46 & chain B")

cmd.select ("Outward", "resi 46 & chain B", merge=1)

cmd.color ("blue", "resi 47 & chain B")

cmd.select ("Outward", "resi 47 & chain B", merge=1)

cmd.color ("blue", "resi 48 & chain B")

cmd.select ("Outward", "resi 48 & chain B", merge=1)

cmd.color ("blue", "resi 49 & chain B")

cmd.select ("Outward", "resi 49 & chain B", merge=1)

cmd.color ("blue", "resi 50 & chain B")

cmd.select ("Outward", "resi 50 & chain B", merge=1)

cmd.color ("blue", "resi 51 & chain B")

cmd.select ("Outward", "resi 51 & chain B", merge=1)

cmd.color ("blue", "resi 52 & chain B")

cmd.select ("Outward", "resi 52 & chain B", merge=1)

cmd.color ("blue", "resi 53 & chain B")

cmd.select ("Outward", "resi 53 & chain B", merge=1)

cmd.color ("blue", "resi 54 & chain B")

cmd.select ("Outward", "resi 54 & chain B", merge=1)

cmd.color ("blue", "resi 55 & chain B")

cmd.select ("Outward", "resi 55 & chain B", merge=1)

cmd.color ("blue", "resi 56 & chain B")

cmd.select ("Outward", "resi 56 & chain B", merge=1)

cmd.color ("blue", "resi 57 & chain B")

cmd.select ("Outward", "resi 57 & chain B", merge=1)

cmd.color ("blue", "resi 58 & chain B")

cmd.select ("Outward", "resi 58 & chain B", merge=1)

cmd.color ("blue", "resi 59 & chain B")

cmd.select ("Outward", "resi 59 & chain B", merge=1)

cmd.color ("blue", "resi 60 & chain B")

cmd.select ("Outward", "resi 60 & chain B", merge=1)

cmd.color ("blue", "resi 61 & chain B")

cmd.select ("Outward", "resi 61 & chain B", merge=1)

cmd.color ("blue", "resi 62 & chain B")

cmd.select ("Outward", "resi 62 & chain B", merge=1)

cmd.color ("blue", "resi 63 & chain B")

cmd.select ("Outward", "resi 63 & chain B", merge=1)

cmd.color ("blue", "resi 64 & chain B")

cmd.select ("Outward", "resi 64 & chain B", merge=1)

cmd.color ("blue", "resi 65 & chain B")

cmd.select ("Outward", "resi 65 & chain B", merge=1)

cmd.color ("blue", "resi 66 & chain B")

cmd.select ("Outward", "resi 66 & chain B", merge=1)

cmd.color ("blue", "resi 74 & chain B")

cmd.select ("Outward", "resi 74 & chain B", merge=1)

cmd.color ("blue", "resi 75 & chain B")

cmd.select ("Outward", "resi 75 & chain B", merge=1)

cmd.color ("blue", "resi 76 & chain B")

cmd.select ("Outward", "resi 76 & chain B", merge=1)

cmd.color ("blue", "resi 77 & chain B")

cmd.select ("Outward", "resi 77 & chain B", merge=1)

cmd.color ("blue", "resi 78 & chain B")

cmd.select ("Outward", "resi 78 & chain B", merge=1)

cmd.color ("blue", "resi 79 & chain B")

cmd.select ("Outward", "resi 79 & chain B", merge=1)

cmd.color ("blue", "resi 80 & chain B")

cmd.select ("Outward", "resi 80 & chain B", merge=1)

cmd.color ("blue", "resi 81 & chain B")

cmd.select ("Outward", "resi 81 & chain B", merge=1)

cmd.color ("blue", "resi 82 & chain B")

cmd.select ("Outward", "resi 82 & chain B", merge=1)

cmd.color ("blue", "resi 83 & chain B")

cmd.select ("Outward", "resi 83 & chain B", merge=1)

cmd.color ("blue", "resi 84 & chain B")

cmd.select ("Outward", "resi 84 & chain B", merge=1)

cmd.color ("blue", "resi 85 & chain B")

cmd.select ("Outward", "resi 85 & chain B", merge=1)

cmd.color ("blue", "resi 86 & chain B")

cmd.select ("Outward", "resi 86 & chain B", merge=1)

cmd.color ("blue", "resi 87 & chain B")

cmd.select ("Outward", "resi 87 & chain B", merge=1)

cmd.color ("blue", "resi 88 & chain B")

cmd.select ("Outward", "resi 88 & chain B", merge=1)

cmd.color ("blue", "resi 89 & chain B")

cmd.select ("Outward", "resi 89 & chain B", merge=1)

cmd.color ("blue", "resi 90 & chain B")

cmd.select ("Outward", "resi 90 & chain B", merge=1)

cmd.color ("blue", "resi 91 & chain B")

cmd.select ("Outward", "resi 91 & chain B", merge=1)

cmd.color ("blue", "resi 92 & chain B")

cmd.select ("Outward", "resi 92 & chain B", merge=1)

cmd.color ("blue", "resi 93 & chain B")

cmd.select ("Outward", "resi 93 & chain B", merge=1)

cmd.color ("blue", "resi 94 & chain B")

cmd.select ("Outward", "resi 94 & chain B", merge=1)

cmd.color ("blue", "resi 95 & chain B")

cmd.select ("Outward", "resi 95 & chain B", merge=1)

cmd.color ("blue", "resi 96 & chain B")

cmd.select ("Outward", "resi 96 & chain B", merge=1)

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

cmd.color ("blue", "resi 34 & chain C")

cmd.select ("Outward", "resi 34 & chain C", merge=1)

cmd.color ("blue", "resi 35 & chain C")

cmd.select ("Outward", "resi 35 & chain C", merge=1)

cmd.color ("blue", "resi 36 & chain C")

cmd.select ("Outward", "resi 36 & chain C", merge=1)

cmd.color ("blue", "resi 37 & chain C")

cmd.select ("Outward", "resi 37 & chain C", merge=1)

cmd.color ("blue", "resi 38 & chain C")

cmd.select ("Outward", "resi 38 & chain C", merge=1)

cmd.color ("blue", "resi 39 & chain C")

cmd.select ("Outward", "resi 39 & chain C", merge=1)

cmd.color ("blue", "resi 40 & chain C")

cmd.select ("Outward", "resi 40 & chain C", merge=1)

cmd.color ("blue", "resi 41 & chain C")

cmd.select ("Outward", "resi 41 & chain C", merge=1)

cmd.color ("blue", "resi 42 & chain C")

cmd.select ("Outward", "resi 42 & chain C", merge=1)

cmd.color ("blue", "resi 43 & chain C")

cmd.select ("Outward", "resi 43 & chain C", merge=1)

cmd.color ("blue", "resi 44 & chain C")

cmd.select ("Outward", "resi 44 & chain C", merge=1)

cmd.color ("blue", "resi 45 & chain C")

cmd.select ("Outward", "resi 45 & chain C", merge=1)

cmd.color ("blue", "resi 46 & chain C")

cmd.select ("Outward", "resi 46 & chain C", merge=1)

cmd.color ("blue", "resi 47 & chain C")

cmd.select ("Outward", "resi 47 & chain C", merge=1)

cmd.color ("blue", "resi 48 & chain C")

cmd.select ("Outward", "resi 48 & chain C", merge=1)

cmd.color ("blue", "resi 49 & chain C")

cmd.select ("Outward", "resi 49 & chain C", merge=1)

cmd.color ("blue", "resi 50 & chain C")

cmd.select ("Outward", "resi 50 & chain C", merge=1)

cmd.color ("blue", "resi 51 & chain C")

cmd.select ("Outward", "resi 51 & chain C", merge=1)

cmd.color ("blue", "resi 52 & chain C")

cmd.select ("Outward", "resi 52 & chain C", merge=1)

cmd.color ("blue", "resi 53 & chain C")

cmd.select ("Outward", "resi 53 & chain C", merge=1)

cmd.color ("blue", "resi 54 & chain C")

cmd.select ("Outward", "resi 54 & chain C", merge=1)

cmd.color ("blue", "resi 55 & chain C")

cmd.select ("Outward", "resi 55 & chain C", merge=1)

cmd.color ("blue", "resi 56 & chain C")

cmd.select ("Outward", "resi 56 & chain C", merge=1)

cmd.color ("blue", "resi 57 & chain C")

cmd.select ("Outward", "resi 57 & chain C", merge=1)

cmd.color ("blue", "resi 58 & chain C")

cmd.select ("Outward", "resi 58 & chain C", merge=1)

cmd.color ("blue", "resi 59 & chain C")

cmd.select ("Outward", "resi 59 & chain C", merge=1)

cmd.color ("blue", "resi 60 & chain C")

cmd.select ("Outward", "resi 60 & chain C", merge=1)

cmd.color ("blue", "resi 61 & chain C")

cmd.select ("Outward", "resi 61 & chain C", merge=1)

cmd.color ("blue", "resi 62 & chain C")

cmd.select ("Outward", "resi 62 & chain C", merge=1)

cmd.color ("blue", "resi 63 & chain C")

cmd.select ("Outward", "resi 63 & chain C", merge=1)

cmd.color ("blue", "resi 64 & chain C")

cmd.select ("Outward", "resi 64 & chain C", merge=1)

cmd.color ("blue", "resi 65 & chain C")

cmd.select ("Outward", "resi 65 & chain C", merge=1)

cmd.color ("blue", "resi 66 & chain C")

cmd.select ("Outward", "resi 66 & chain C", merge=1)

cmd.color ("blue", "resi 74 & chain C")

cmd.select ("Outward", "resi 74 & chain C", merge=1)

cmd.color ("blue", "resi 75 & chain C")

cmd.select ("Outward", "resi 75 & chain C", merge=1)

cmd.color ("blue", "resi 76 & chain C")

cmd.select ("Outward", "resi 76 & chain C", merge=1)

cmd.color ("blue", "resi 77 & chain C")

cmd.select ("Outward", "resi 77 & chain C", merge=1)

cmd.color ("blue", "resi 78 & chain C")

cmd.select ("Outward", "resi 78 & chain C", merge=1)

cmd.color ("blue", "resi 79 & chain C")

cmd.select ("Outward", "resi 79 & chain C", merge=1)

cmd.color ("blue", "resi 80 & chain C")

cmd.select ("Outward", "resi 80 & chain C", merge=1)

cmd.color ("blue", "resi 81 & chain C")

cmd.select ("Outward", "resi 81 & chain C", merge=1)

cmd.color ("blue", "resi 82 & chain C")

cmd.select ("Outward", "resi 82 & chain C", merge=1)

cmd.color ("blue", "resi 83 & chain C")

cmd.select ("Outward", "resi 83 & chain C", merge=1)

cmd.color ("blue", "resi 84 & chain C")

cmd.select ("Outward", "resi 84 & chain C", merge=1)

cmd.color ("blue", "resi 85 & chain C")

cmd.select ("Outward", "resi 85 & chain C", merge=1)

cmd.color ("blue", "resi 86 & chain C")

cmd.select ("Outward", "resi 86 & chain C", merge=1)

cmd.color ("blue", "resi 87 & chain C")

cmd.select ("Outward", "resi 87 & chain C", merge=1)

cmd.color ("blue", "resi 88 & chain C")

cmd.select ("Outward", "resi 88 & chain C", merge=1)

cmd.color ("blue", "resi 89 & chain C")

cmd.select ("Outward", "resi 89 & chain C", merge=1)

cmd.color ("blue", "resi 90 & chain C")

cmd.select ("Outward", "resi 90 & chain C", merge=1)

cmd.color ("blue", "resi 91 & chain C")

cmd.select ("Outward", "resi 91 & chain C", merge=1)

cmd.color ("blue", "resi 92 & chain C")

cmd.select ("Outward", "resi 92 & chain C", merge=1)

cmd.color ("blue", "resi 93 & chain C")

cmd.select ("Outward", "resi 93 & chain C", merge=1)

cmd.color ("blue", "resi 94 & chain C")

cmd.select ("Outward", "resi 94 & chain C", merge=1)

cmd.color ("blue", "resi 95 & chain C")

cmd.select ("Outward", "resi 95 & chain C", merge=1)

cmd.color ("blue", "resi 96 & chain C")

cmd.select ("Outward", "resi 96 & chain C", merge=1)

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

cmd.color ("blue", "resi 34 & chain D")

cmd.select ("Outward", "resi 34 & chain D", merge=1)

cmd.color ("blue", "resi 35 & chain D")

cmd.select ("Outward", "resi 35 & chain D", merge=1)

cmd.color ("blue", "resi 36 & chain D")

cmd.select ("Outward", "resi 36 & chain D", merge=1)

cmd.color ("blue", "resi 37 & chain D")

cmd.select ("Outward", "resi 37 & chain D", merge=1)

cmd.color ("blue", "resi 38 & chain D")

cmd.select ("Outward", "resi 38 & chain D", merge=1)

cmd.color ("blue", "resi 39 & chain D")

cmd.select ("Outward", "resi 39 & chain D", merge=1)

cmd.color ("blue", "resi 40 & chain D")

cmd.select ("Outward", "resi 40 & chain D", merge=1)

cmd.color ("blue", "resi 41 & chain D")

cmd.select ("Outward", "resi 41 & chain D", merge=1)

cmd.color ("blue", "resi 42 & chain D")

cmd.select ("Outward", "resi 42 & chain D", merge=1)

cmd.color ("blue", "resi 43 & chain D")

cmd.select ("Outward", "resi 43 & chain D", merge=1)

cmd.color ("blue", "resi 44 & chain D")

cmd.select ("Outward", "resi 44 & chain D", merge=1)

cmd.color ("blue", "resi 45 & chain D")

cmd.select ("Outward", "resi 45 & chain D", merge=1)

cmd.color ("blue", "resi 46 & chain D")

cmd.select ("Outward", "resi 46 & chain D", merge=1)

cmd.color ("blue", "resi 47 & chain D")

cmd.select ("Outward", "resi 47 & chain D", merge=1)

cmd.color ("blue", "resi 48 & chain D")

cmd.select ("Outward", "resi 48 & chain D", merge=1)

cmd.color ("blue", "resi 49 & chain D")

cmd.select ("Outward", "resi 49 & chain D", merge=1)

cmd.color ("blue", "resi 50 & chain D")

cmd.select ("Outward", "resi 50 & chain D", merge=1)

cmd.color ("blue", "resi 51 & chain D")

cmd.select ("Outward", "resi 51 & chain D", merge=1)

cmd.color ("blue", "resi 52 & chain D")

cmd.select ("Outward", "resi 52 & chain D", merge=1)

cmd.color ("blue", "resi 53 & chain D")

cmd.select ("Outward", "resi 53 & chain D", merge=1)

cmd.color ("blue", "resi 54 & chain D")

cmd.select ("Outward", "resi 54 & chain D", merge=1)

cmd.color ("blue", "resi 55 & chain D")

cmd.select ("Outward", "resi 55 & chain D", merge=1)

cmd.color ("blue", "resi 56 & chain D")

cmd.select ("Outward", "resi 56 & chain D", merge=1)

cmd.color ("blue", "resi 57 & chain D")

cmd.select ("Outward", "resi 57 & chain D", merge=1)

cmd.color ("blue", "resi 58 & chain D")

cmd.select ("Outward", "resi 58 & chain D", merge=1)

cmd.color ("blue", "resi 59 & chain D")

cmd.select ("Outward", "resi 59 & chain D", merge=1)

cmd.color ("blue", "resi 60 & chain D")

cmd.select ("Outward", "resi 60 & chain D", merge=1)

cmd.color ("blue", "resi 61 & chain D")

cmd.select ("Outward", "resi 61 & chain D", merge=1)

cmd.color ("blue", "resi 62 & chain D")

cmd.select ("Outward", "resi 62 & chain D", merge=1)

cmd.color ("blue", "resi 63 & chain D")

cmd.select ("Outward", "resi 63 & chain D", merge=1)

cmd.color ("blue", "resi 64 & chain D")

cmd.select ("Outward", "resi 64 & chain D", merge=1)

cmd.color ("blue", "resi 65 & chain D")

cmd.select ("Outward", "resi 65 & chain D", merge=1)

cmd.color ("blue", "resi 66 & chain D")

cmd.select ("Outward", "resi 66 & chain D", merge=1)

cmd.color ("blue", "resi 74 & chain D")

cmd.select ("Outward", "resi 74 & chain D", merge=1)

cmd.color ("blue", "resi 75 & chain D")

cmd.select ("Outward", "resi 75 & chain D", merge=1)

cmd.color ("blue", "resi 76 & chain D")

cmd.select ("Outward", "resi 76 & chain D", merge=1)

cmd.color ("blue", "resi 77 & chain D")

cmd.select ("Outward", "resi 77 & chain D", merge=1)

cmd.color ("blue", "resi 78 & chain D")

cmd.select ("Outward", "resi 78 & chain D", merge=1)

cmd.color ("blue", "resi 79 & chain D")

cmd.select ("Outward", "resi 79 & chain D", merge=1)

cmd.color ("blue", "resi 80 & chain D")

cmd.select ("Outward", "resi 80 & chain D", merge=1)

cmd.color ("blue", "resi 81 & chain D")

cmd.select ("Outward", "resi 81 & chain D", merge=1)

cmd.color ("blue", "resi 82 & chain D")

cmd.select ("Outward", "resi 82 & chain D", merge=1)

cmd.color ("blue", "resi 83 & chain D")

cmd.select ("Outward", "resi 83 & chain D", merge=1)

cmd.color ("blue", "resi 84 & chain D")

cmd.select ("Outward", "resi 84 & chain D", merge=1)

cmd.color ("blue", "resi 85 & chain D")

cmd.select ("Outward", "resi 85 & chain D", merge=1)

cmd.color ("blue", "resi 86 & chain D")

cmd.select ("Outward", "resi 86 & chain D", merge=1)

cmd.color ("blue", "resi 87 & chain D")

cmd.select ("Outward", "resi 87 & chain D", merge=1)

cmd.color ("blue", "resi 88 & chain D")

cmd.select ("Outward", "resi 88 & chain D", merge=1)

cmd.color ("blue", "resi 89 & chain D")

cmd.select ("Outward", "resi 89 & chain D", merge=1)

cmd.color ("blue", "resi 90 & chain D")

cmd.select ("Outward", "resi 90 & chain D", merge=1)

cmd.color ("blue", "resi 91 & chain D")

cmd.select ("Outward", "resi 91 & chain D", merge=1)

cmd.color ("blue", "resi 92 & chain D")

cmd.select ("Outward", "resi 92 & chain D", merge=1)

cmd.color ("blue", "resi 93 & chain D")

cmd.select ("Outward", "resi 93 & chain D", merge=1)

cmd.color ("blue", "resi 94 & chain D")

cmd.select ("Outward", "resi 94 & chain D", merge=1)

cmd.color ("blue", "resi 95 & chain D")

cmd.select ("Outward", "resi 95 & chain D", merge=1)

cmd.color ("blue", "resi 96 & chain D")

cmd.select ("Outward", "resi 96 & chain D", merge=1)

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

cmd.color ("blue", "resi 34 & chain E")

cmd.select ("Outward", "resi 34 & chain E", merge=1)

cmd.color ("blue", "resi 35 & chain E")

cmd.select ("Outward", "resi 35 & chain E", merge=1)

cmd.color ("blue", "resi 36 & chain E")

cmd.select ("Outward", "resi 36 & chain E", merge=1)

cmd.color ("blue", "resi 37 & chain E")

cmd.select ("Outward", "resi 37 & chain E", merge=1)

cmd.color ("blue", "resi 38 & chain E")

cmd.select ("Outward", "resi 38 & chain E", merge=1)

cmd.color ("blue", "resi 39 & chain E")

cmd.select ("Outward", "resi 39 & chain E", merge=1)

cmd.color ("blue", "resi 40 & chain E")

cmd.select ("Outward", "resi 40 & chain E", merge=1)

cmd.color ("blue", "resi 41 & chain E")

cmd.select ("Outward", "resi 41 & chain E", merge=1)

cmd.color ("blue", "resi 42 & chain E")

cmd.select ("Outward", "resi 42 & chain E", merge=1)

cmd.color ("blue", "resi 43 & chain E")

cmd.select ("Outward", "resi 43 & chain E", merge=1)

cmd.color ("blue", "resi 44 & chain E")

cmd.select ("Outward", "resi 44 & chain E", merge=1)

cmd.color ("blue", "resi 45 & chain E")

cmd.select ("Outward", "resi 45 & chain E", merge=1)

cmd.color ("blue", "resi 46 & chain E")

cmd.select ("Outward", "resi 46 & chain E", merge=1)

cmd.color ("blue", "resi 47 & chain E")

cmd.select ("Outward", "resi 47 & chain E", merge=1)

cmd.color ("blue", "resi 48 & chain E")

cmd.select ("Outward", "resi 48 & chain E", merge=1)

cmd.color ("blue", "resi 49 & chain E")

cmd.select ("Outward", "resi 49 & chain E", merge=1)

cmd.color ("blue", "resi 50 & chain E")

cmd.select ("Outward", "resi 50 & chain E", merge=1)

cmd.color ("blue", "resi 51 & chain E")

cmd.select ("Outward", "resi 51 & chain E", merge=1)

cmd.color ("blue", "resi 52 & chain E")

cmd.select ("Outward", "resi 52 & chain E", merge=1)

cmd.color ("blue", "resi 53 & chain E")

cmd.select ("Outward", "resi 53 & chain E", merge=1)

cmd.color ("blue", "resi 54 & chain E")

cmd.select ("Outward", "resi 54 & chain E", merge=1)

cmd.color ("blue", "resi 55 & chain E")

cmd.select ("Outward", "resi 55 & chain E", merge=1)

cmd.color ("blue", "resi 56 & chain E")

cmd.select ("Outward", "resi 56 & chain E", merge=1)

cmd.color ("blue", "resi 57 & chain E")

cmd.select ("Outward", "resi 57 & chain E", merge=1)

cmd.color ("blue", "resi 58 & chain E")

cmd.select ("Outward", "resi 58 & chain E", merge=1)

cmd.color ("blue", "resi 59 & chain E")

cmd.select ("Outward", "resi 59 & chain E", merge=1)

cmd.color ("blue", "resi 60 & chain E")

cmd.select ("Outward", "resi 60 & chain E", merge=1)

cmd.color ("blue", "resi 61 & chain E")

cmd.select ("Outward", "resi 61 & chain E", merge=1)

cmd.color ("blue", "resi 62 & chain E")

cmd.select ("Outward", "resi 62 & chain E", merge=1)

cmd.color ("blue", "resi 63 & chain E")

cmd.select ("Outward", "resi 63 & chain E", merge=1)

cmd.color ("blue", "resi 64 & chain E")

cmd.select ("Outward", "resi 64 & chain E", merge=1)

cmd.color ("blue", "resi 65 & chain E")

cmd.select ("Outward", "resi 65 & chain E", merge=1)

cmd.color ("blue", "resi 66 & chain E")

cmd.select ("Outward", "resi 66 & chain E", merge=1)

cmd.color ("blue", "resi 74 & chain E")

cmd.select ("Outward", "resi 74 & chain E", merge=1)

cmd.color ("blue", "resi 75 & chain E")

cmd.select ("Outward", "resi 75 & chain E", merge=1)

cmd.color ("blue", "resi 76 & chain E")

cmd.select ("Outward", "resi 76 & chain E", merge=1)

cmd.color ("blue", "resi 77 & chain E")

cmd.select ("Outward", "resi 77 & chain E", merge=1)

cmd.color ("blue", "resi 78 & chain E")

cmd.select ("Outward", "resi 78 & chain E", merge=1)

cmd.color ("blue", "resi 79 & chain E")

cmd.select ("Outward", "resi 79 & chain E", merge=1)

cmd.color ("blue", "resi 80 & chain E")

cmd.select ("Outward", "resi 80 & chain E", merge=1)

cmd.color ("blue", "resi 81 & chain E")

cmd.select ("Outward", "resi 81 & chain E", merge=1)

cmd.color ("blue", "resi 82 & chain E")

cmd.select ("Outward", "resi 82 & chain E", merge=1)

cmd.color ("blue", "resi 83 & chain E")

cmd.select ("Outward", "resi 83 & chain E", merge=1)

cmd.color ("blue", "resi 84 & chain E")

cmd.select ("Outward", "resi 84 & chain E", merge=1)

cmd.color ("blue", "resi 85 & chain E")

cmd.select ("Outward", "resi 85 & chain E", merge=1)

cmd.color ("blue", "resi 86 & chain E")

cmd.select ("Outward", "resi 86 & chain E", merge=1)

cmd.color ("blue", "resi 87 & chain E")

cmd.select ("Outward", "resi 87 & chain E", merge=1)

cmd.color ("blue", "resi 88 & chain E")

cmd.select ("Outward", "resi 88 & chain E", merge=1)

cmd.color ("blue", "resi 89 & chain E")

cmd.select ("Outward", "resi 89 & chain E", merge=1)

cmd.color ("blue", "resi 90 & chain E")

cmd.select ("Outward", "resi 90 & chain E", merge=1)

cmd.color ("blue", "resi 91 & chain E")

cmd.select ("Outward", "resi 91 & chain E", merge=1)

cmd.color ("blue", "resi 92 & chain E")

cmd.select ("Outward", "resi 92 & chain E", merge=1)

cmd.color ("blue", "resi 93 & chain E")

cmd.select ("Outward", "resi 93 & chain E", merge=1)

cmd.color ("blue", "resi 94 & chain E")

cmd.select ("Outward", "resi 94 & chain E", merge=1)

cmd.color ("blue", "resi 95 & chain E")

cmd.select ("Outward", "resi 95 & chain E", merge=1)

cmd.color ("blue", "resi 96 & chain E")

cmd.select ("Outward", "resi 96 & chain E", merge=1)

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

cmd.color ("blue", "resi 34 & chain F")

cmd.select ("Outward", "resi 34 & chain F", merge=1)

cmd.color ("blue", "resi 35 & chain F")

cmd.select ("Outward", "resi 35 & chain F", merge=1)

cmd.color ("blue", "resi 36 & chain F")

cmd.select ("Outward", "resi 36 & chain F", merge=1)

cmd.color ("blue", "resi 37 & chain F")

cmd.select ("Outward", "resi 37 & chain F", merge=1)

cmd.color ("blue", "resi 38 & chain F")

cmd.select ("Outward", "resi 38 & chain F", merge=1)

cmd.color ("blue", "resi 39 & chain F")

cmd.select ("Outward", "resi 39 & chain F", merge=1)

cmd.color ("blue", "resi 40 & chain F")

cmd.select ("Outward", "resi 40 & chain F", merge=1)

cmd.color ("blue", "resi 41 & chain F")

cmd.select ("Outward", "resi 41 & chain F", merge=1)

cmd.color ("blue", "resi 42 & chain F")

cmd.select ("Outward", "resi 42 & chain F", merge=1)

cmd.color ("blue", "resi 43 & chain F")

cmd.select ("Outward", "resi 43 & chain F", merge=1)

cmd.color ("blue", "resi 44 & chain F")

cmd.select ("Outward", "resi 44 & chain F", merge=1)

cmd.color ("blue", "resi 45 & chain F")

cmd.select ("Outward", "resi 45 & chain F", merge=1)

cmd.color ("blue", "resi 46 & chain F")

cmd.select ("Outward", "resi 46 & chain F", merge=1)

cmd.color ("blue", "resi 47 & chain F")

cmd.select ("Outward", "resi 47 & chain F", merge=1)

cmd.color ("blue", "resi 48 & chain F")

cmd.select ("Outward", "resi 48 & chain F", merge=1)

cmd.color ("blue", "resi 49 & chain F")

cmd.select ("Outward", "resi 49 & chain F", merge=1)

cmd.color ("blue", "resi 50 & chain F")

cmd.select ("Outward", "resi 50 & chain F", merge=1)

cmd.color ("blue", "resi 51 & chain F")

cmd.select ("Outward", "resi 51 & chain F", merge=1)

cmd.color ("blue", "resi 52 & chain F")

cmd.select ("Outward", "resi 52 & chain F", merge=1)

cmd.color ("blue", "resi 53 & chain F")

cmd.select ("Outward", "resi 53 & chain F", merge=1)

cmd.color ("blue", "resi 54 & chain F")

cmd.select ("Outward", "resi 54 & chain F", merge=1)

cmd.color ("blue", "resi 55 & chain F")

cmd.select ("Outward", "resi 55 & chain F", merge=1)

cmd.color ("blue", "resi 56 & chain F")

cmd.select ("Outward", "resi 56 & chain F", merge=1)

cmd.color ("blue", "resi 57 & chain F")

cmd.select ("Outward", "resi 57 & chain F", merge=1)

cmd.color ("blue", "resi 58 & chain F")

cmd.select ("Outward", "resi 58 & chain F", merge=1)

cmd.color ("blue", "resi 59 & chain F")

cmd.select ("Outward", "resi 59 & chain F", merge=1)

cmd.color ("blue", "resi 60 & chain F")

cmd.select ("Outward", "resi 60 & chain F", merge=1)

cmd.color ("blue", "resi 61 & chain F")

cmd.select ("Outward", "resi 61 & chain F", merge=1)

cmd.color ("blue", "resi 62 & chain F")

cmd.select ("Outward", "resi 62 & chain F", merge=1)

cmd.color ("blue", "resi 63 & chain F")

cmd.select ("Outward", "resi 63 & chain F", merge=1)

cmd.color ("blue", "resi 64 & chain F")

cmd.select ("Outward", "resi 64 & chain F", merge=1)

cmd.color ("blue", "resi 65 & chain F")

cmd.select ("Outward", "resi 65 & chain F", merge=1)

cmd.color ("blue", "resi 66 & chain F")

cmd.select ("Outward", "resi 66 & chain F", merge=1)

cmd.color ("blue", "resi 74 & chain F")

cmd.select ("Outward", "resi 74 & chain F", merge=1)

cmd.color ("blue", "resi 75 & chain F")

cmd.select ("Outward", "resi 75 & chain F", merge=1)

cmd.color ("blue", "resi 76 & chain F")

cmd.select ("Outward", "resi 76 & chain F", merge=1)

cmd.color ("blue", "resi 77 & chain F")

cmd.select ("Outward", "resi 77 & chain F", merge=1)

cmd.color ("blue", "resi 78 & chain F")

cmd.select ("Outward", "resi 78 & chain F", merge=1)

cmd.color ("blue", "resi 79 & chain F")

cmd.select ("Outward", "resi 79 & chain F", merge=1)

cmd.color ("blue", "resi 80 & chain F")

cmd.select ("Outward", "resi 80 & chain F", merge=1)

cmd.color ("blue", "resi 81 & chain F")

cmd.select ("Outward", "resi 81 & chain F", merge=1)

cmd.color ("blue", "resi 82 & chain F")

cmd.select ("Outward", "resi 82 & chain F", merge=1)

cmd.color ("blue", "resi 83 & chain F")

cmd.select ("Outward", "resi 83 & chain F", merge=1)

cmd.color ("blue", "resi 84 & chain F")

cmd.select ("Outward", "resi 84 & chain F", merge=1)

cmd.color ("blue", "resi 85 & chain F")

cmd.select ("Outward", "resi 85 & chain F", merge=1)

cmd.color ("blue", "resi 86 & chain F")

cmd.select ("Outward", "resi 86 & chain F", merge=1)

cmd.color ("blue", "resi 87 & chain F")

cmd.select ("Outward", "resi 87 & chain F", merge=1)

cmd.color ("blue", "resi 88 & chain F")

cmd.select ("Outward", "resi 88 & chain F", merge=1)

cmd.color ("blue", "resi 89 & chain F")

cmd.select ("Outward", "resi 89 & chain F", merge=1)

cmd.color ("blue", "resi 90 & chain F")

cmd.select ("Outward", "resi 90 & chain F", merge=1)

cmd.color ("blue", "resi 91 & chain F")

cmd.select ("Outward", "resi 91 & chain F", merge=1)

cmd.color ("blue", "resi 92 & chain F")

cmd.select ("Outward", "resi 92 & chain F", merge=1)

cmd.color ("blue", "resi 93 & chain F")

cmd.select ("Outward", "resi 93 & chain F", merge=1)

cmd.color ("blue", "resi 94 & chain F")

cmd.select ("Outward", "resi 94 & chain F", merge=1)

cmd.color ("blue", "resi 95 & chain F")

cmd.select ("Outward", "resi 95 & chain F", merge=1)

cmd.color ("blue", "resi 96 & chain F")

cmd.select ("Outward", "resi 96 & chain F", merge=1)

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

cmd.color ("blue", "resi 34 & chain G")

cmd.select ("Outward", "resi 34 & chain G", merge=1)

cmd.color ("blue", "resi 35 & chain G")

cmd.select ("Outward", "resi 35 & chain G", merge=1)

cmd.color ("blue", "resi 36 & chain G")

cmd.select ("Outward", "resi 36 & chain G", merge=1)

cmd.color ("blue", "resi 37 & chain G")

cmd.select ("Outward", "resi 37 & chain G", merge=1)

cmd.color ("blue", "resi 38 & chain G")

cmd.select ("Outward", "resi 38 & chain G", merge=1)

cmd.color ("blue", "resi 39 & chain G")

cmd.select ("Outward", "resi 39 & chain G", merge=1)

cmd.color ("blue", "resi 40 & chain G")

cmd.select ("Outward", "resi 40 & chain G", merge=1)

cmd.color ("blue", "resi 41 & chain G")

cmd.select ("Outward", "resi 41 & chain G", merge=1)

cmd.color ("blue", "resi 42 & chain G")

cmd.select ("Outward", "resi 42 & chain G", merge=1)

cmd.color ("blue", "resi 43 & chain G")

cmd.select ("Outward", "resi 43 & chain G", merge=1)

cmd.color ("blue", "resi 44 & chain G")

cmd.select ("Outward", "resi 44 & chain G", merge=1)

cmd.color ("blue", "resi 45 & chain G")

cmd.select ("Outward", "resi 45 & chain G", merge=1)

cmd.color ("blue", "resi 46 & chain G")

cmd.select ("Outward", "resi 46 & chain G", merge=1)

cmd.color ("blue", "resi 47 & chain G")

cmd.select ("Outward", "resi 47 & chain G", merge=1)

cmd.color ("blue", "resi 48 & chain G")

cmd.select ("Outward", "resi 48 & chain G", merge=1)

cmd.color ("blue", "resi 49 & chain G")

cmd.select ("Outward", "resi 49 & chain G", merge=1)

cmd.color ("blue", "resi 50 & chain G")

cmd.select ("Outward", "resi 50 & chain G", merge=1)

cmd.color ("blue", "resi 51 & chain G")

cmd.select ("Outward", "resi 51 & chain G", merge=1)

cmd.color ("blue", "resi 52 & chain G")

cmd.select ("Outward", "resi 52 & chain G", merge=1)

cmd.color ("blue", "resi 53 & chain G")

cmd.select ("Outward", "resi 53 & chain G", merge=1)

cmd.color ("blue", "resi 54 & chain G")

cmd.select ("Outward", "resi 54 & chain G", merge=1)

cmd.color ("blue", "resi 55 & chain G")

cmd.select ("Outward", "resi 55 & chain G", merge=1)

cmd.color ("blue", "resi 56 & chain G")

cmd.select ("Outward", "resi 56 & chain G", merge=1)

cmd.color ("blue", "resi 57 & chain G")

cmd.select ("Outward", "resi 57 & chain G", merge=1)

cmd.color ("blue", "resi 58 & chain G")

cmd.select ("Outward", "resi 58 & chain G", merge=1)

cmd.color ("blue", "resi 59 & chain G")

cmd.select ("Outward", "resi 59 & chain G", merge=1)

cmd.color ("blue", "resi 60 & chain G")

cmd.select ("Outward", "resi 60 & chain G", merge=1)

cmd.color ("blue", "resi 61 & chain G")

cmd.select ("Outward", "resi 61 & chain G", merge=1)

cmd.color ("blue", "resi 62 & chain G")

cmd.select ("Outward", "resi 62 & chain G", merge=1)

cmd.color ("blue", "resi 63 & chain G")

cmd.select ("Outward", "resi 63 & chain G", merge=1)

cmd.color ("blue", "resi 64 & chain G")

cmd.select ("Outward", "resi 64 & chain G", merge=1)

cmd.color ("blue", "resi 65 & chain G")

cmd.select ("Outward", "resi 65 & chain G", merge=1)

cmd.color ("blue", "resi 66 & chain G")

cmd.select ("Outward", "resi 66 & chain G", merge=1)

cmd.color ("blue", "resi 74 & chain G")

cmd.select ("Outward", "resi 74 & chain G", merge=1)

cmd.color ("blue", "resi 75 & chain G")

cmd.select ("Outward", "resi 75 & chain G", merge=1)

cmd.color ("blue", "resi 76 & chain G")

cmd.select ("Outward", "resi 76 & chain G", merge=1)

cmd.color ("blue", "resi 77 & chain G")

cmd.select ("Outward", "resi 77 & chain G", merge=1)

cmd.color ("blue", "resi 78 & chain G")

cmd.select ("Outward", "resi 78 & chain G", merge=1)

cmd.color ("blue", "resi 79 & chain G")

cmd.select ("Outward", "resi 79 & chain G", merge=1)

cmd.color ("blue", "resi 80 & chain G")

cmd.select ("Outward", "resi 80 & chain G", merge=1)

cmd.color ("blue", "resi 81 & chain G")

cmd.select ("Outward", "resi 81 & chain G", merge=1)

cmd.color ("blue", "resi 82 & chain G")

cmd.select ("Outward", "resi 82 & chain G", merge=1)

cmd.color ("blue", "resi 83 & chain G")

cmd.select ("Outward", "resi 83 & chain G", merge=1)

cmd.color ("blue", "resi 84 & chain G")

cmd.select ("Outward", "resi 84 & chain G", merge=1)

cmd.color ("blue", "resi 85 & chain G")

cmd.select ("Outward", "resi 85 & chain G", merge=1)

cmd.color ("blue", "resi 86 & chain G")

cmd.select ("Outward", "resi 86 & chain G", merge=1)

cmd.color ("blue", "resi 87 & chain G")

cmd.select ("Outward", "resi 87 & chain G", merge=1)

cmd.color ("blue", "resi 88 & chain G")

cmd.select ("Outward", "resi 88 & chain G", merge=1)

cmd.color ("blue", "resi 89 & chain G")

cmd.select ("Outward", "resi 89 & chain G", merge=1)

cmd.color ("blue", "resi 90 & chain G")

cmd.select ("Outward", "resi 90 & chain G", merge=1)

cmd.color ("blue", "resi 91 & chain G")

cmd.select ("Outward", "resi 91 & chain G", merge=1)

cmd.color ("blue", "resi 92 & chain G")

cmd.select ("Outward", "resi 92 & chain G", merge=1)

cmd.color ("blue", "resi 93 & chain G")

cmd.select ("Outward", "resi 93 & chain G", merge=1)

cmd.color ("blue", "resi 94 & chain G")

cmd.select ("Outward", "resi 94 & chain G", merge=1)

cmd.color ("blue", "resi 95 & chain G")

cmd.select ("Outward", "resi 95 & chain G", merge=1)

cmd.color ("blue", "resi 96 & chain G")

cmd.select ("Outward", "resi 96 & chain G", merge=1)

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

cmd.color ("blue", "resi 34 & chain H")

cmd.select ("Outward", "resi 34 & chain H", merge=1)

cmd.color ("blue", "resi 35 & chain H")

cmd.select ("Outward", "resi 35 & chain H", merge=1)

cmd.color ("blue", "resi 36 & chain H")

cmd.select ("Outward", "resi 36 & chain H", merge=1)

cmd.color ("blue", "resi 37 & chain H")

cmd.select ("Outward", "resi 37 & chain H", merge=1)

cmd.color ("blue", "resi 38 & chain H")

cmd.select ("Outward", "resi 38 & chain H", merge=1)

cmd.color ("blue", "resi 39 & chain H")

cmd.select ("Outward", "resi 39 & chain H", merge=1)

cmd.color ("blue", "resi 40 & chain H")

cmd.select ("Outward", "resi 40 & chain H", merge=1)

cmd.color ("blue", "resi 41 & chain H")

cmd.select ("Outward", "resi 41 & chain H", merge=1)

cmd.color ("blue", "resi 42 & chain H")

cmd.select ("Outward", "resi 42 & chain H", merge=1)

cmd.color ("blue", "resi 43 & chain H")

cmd.select ("Outward", "resi 43 & chain H", merge=1)

cmd.color ("blue", "resi 44 & chain H")

cmd.select ("Outward", "resi 44 & chain H", merge=1)

cmd.color ("blue", "resi 45 & chain H")

cmd.select ("Outward", "resi 45 & chain H", merge=1)

cmd.color ("blue", "resi 46 & chain H")

cmd.select ("Outward", "resi 46 & chain H", merge=1)

cmd.color ("blue", "resi 47 & chain H")

cmd.select ("Outward", "resi 47 & chain H", merge=1)

cmd.color ("blue", "resi 48 & chain H")

cmd.select ("Outward", "resi 48 & chain H", merge=1)

cmd.color ("blue", "resi 49 & chain H")

cmd.select ("Outward", "resi 49 & chain H", merge=1)

cmd.color ("blue", "resi 50 & chain H")

cmd.select ("Outward", "resi 50 & chain H", merge=1)

cmd.color ("blue", "resi 51 & chain H")

cmd.select ("Outward", "resi 51 & chain H", merge=1)

cmd.color ("blue", "resi 52 & chain H")

cmd.select ("Outward", "resi 52 & chain H", merge=1)

cmd.color ("blue", "resi 53 & chain H")

cmd.select ("Outward", "resi 53 & chain H", merge=1)

cmd.color ("blue", "resi 54 & chain H")

cmd.select ("Outward", "resi 54 & chain H", merge=1)

cmd.color ("blue", "resi 55 & chain H")

cmd.select ("Outward", "resi 55 & chain H", merge=1)

cmd.color ("blue", "resi 56 & chain H")

cmd.select ("Outward", "resi 56 & chain H", merge=1)

cmd.color ("blue", "resi 57 & chain H")

cmd.select ("Outward", "resi 57 & chain H", merge=1)

cmd.color ("blue", "resi 58 & chain H")

cmd.select ("Outward", "resi 58 & chain H", merge=1)

cmd.color ("blue", "resi 59 & chain H")

cmd.select ("Outward", "resi 59 & chain H", merge=1)

cmd.color ("blue", "resi 60 & chain H")

cmd.select ("Outward", "resi 60 & chain H", merge=1)

cmd.color ("blue", "resi 61 & chain H")

cmd.select ("Outward", "resi 61 & chain H", merge=1)

cmd.color ("blue", "resi 62 & chain H")

cmd.select ("Outward", "resi 62 & chain H", merge=1)

cmd.color ("blue", "resi 63 & chain H")

cmd.select ("Outward", "resi 63 & chain H", merge=1)

cmd.color ("blue", "resi 64 & chain H")

cmd.select ("Outward", "resi 64 & chain H", merge=1)

cmd.color ("blue", "resi 65 & chain H")

cmd.select ("Outward", "resi 65 & chain H", merge=1)

cmd.color ("blue", "resi 66 & chain H")

cmd.select ("Outward", "resi 66 & chain H", merge=1)

cmd.color ("blue", "resi 74 & chain H")

cmd.select ("Outward", "resi 74 & chain H", merge=1)

cmd.color ("blue", "resi 75 & chain H")

cmd.select ("Outward", "resi 75 & chain H", merge=1)

cmd.color ("blue", "resi 76 & chain H")

cmd.select ("Outward", "resi 76 & chain H", merge=1)

cmd.color ("blue", "resi 77 & chain H")

cmd.select ("Outward", "resi 77 & chain H", merge=1)

cmd.color ("blue", "resi 78 & chain H")

cmd.select ("Outward", "resi 78 & chain H", merge=1)

cmd.color ("blue", "resi 79 & chain H")

cmd.select ("Outward", "resi 79 & chain H", merge=1)

cmd.color ("blue", "resi 80 & chain H")

cmd.select ("Outward", "resi 80 & chain H", merge=1)

cmd.color ("blue", "resi 81 & chain H")

cmd.select ("Outward", "resi 81 & chain H", merge=1)

cmd.color ("blue", "resi 82 & chain H")

cmd.select ("Outward", "resi 82 & chain H", merge=1)

cmd.color ("blue", "resi 83 & chain H")

cmd.select ("Outward", "resi 83 & chain H", merge=1)

cmd.color ("blue", "resi 84 & chain H")

cmd.select ("Outward", "resi 84 & chain H", merge=1)

cmd.color ("blue", "resi 85 & chain H")

cmd.select ("Outward", "resi 85 & chain H", merge=1)

cmd.color ("blue", "resi 86 & chain H")

cmd.select ("Outward", "resi 86 & chain H", merge=1)

cmd.color ("blue", "resi 87 & chain H")

cmd.select ("Outward", "resi 87 & chain H", merge=1)

cmd.color ("blue", "resi 88 & chain H")

cmd.select ("Outward", "resi 88 & chain H", merge=1)

cmd.color ("blue", "resi 89 & chain H")

cmd.select ("Outward", "resi 89 & chain H", merge=1)

cmd.color ("blue", "resi 90 & chain H")

cmd.select ("Outward", "resi 90 & chain H", merge=1)

cmd.color ("blue", "resi 91 & chain H")

cmd.select ("Outward", "resi 91 & chain H", merge=1)

cmd.color ("blue", "resi 92 & chain H")

cmd.select ("Outward", "resi 92 & chain H", merge=1)

cmd.color ("blue", "resi 93 & chain H")

cmd.select ("Outward", "resi 93 & chain H", merge=1)

cmd.color ("blue", "resi 94 & chain H")

cmd.select ("Outward", "resi 94 & chain H", merge=1)

cmd.color ("blue", "resi 95 & chain H")

cmd.select ("Outward", "resi 95 & chain H", merge=1)

cmd.color ("blue", "resi 96 & chain H")

cmd.select ("Outward", "resi 96 & chain H", merge=1)

cmd.color ("blue", "resi 97 & chain H")

cmd.select ("Outward", "resi 97 & chain H", merge=1)

cmd.color ("blue", "resi 98 & chain H")

cmd.select ("Outward", "resi 98 & chain H", merge=1)

cmd.color ("blue", "resi 99 & chain H")

cmd.select ("Outward", "resi 99 & chain H", merge=1)

cmd.color ("blue", "resi 100 & chain H")

cmd.select ("Outward", "resi 100 & chain H", merge=1)

cmd.color ("blue", "resi 101 & chain H")

cmd.select ("Outward", "resi 101 & chain H", merge=1)

cmd.color ("blue", "resi 102 & chain H")

cmd.select ("Outward", "resi 102 & chain H", merge=1)

cmd.color ("blue", "resi 103 & chain H")

cmd.select ("Outward", "resi 103 & chain H", merge=1)

cmd.color ("blue", "resi 104 & chain H")

cmd.select ("Outward", "resi 104 & chain H", merge=1)

cmd.color ("blue", "resi 105 & chain H")

cmd.select ("Outward", "resi 105 & chain H", merge=1)

cmd.color ("blue", "resi 106 & chain H")

cmd.select ("Outward", "resi 106 & chain H", merge=1)

cmd.color ("blue", "resi 107 & chain H")

cmd.select ("Outward", "resi 107 & chain H", merge=1)

cmd.color ("blue", "resi 34 & chain I")

cmd.select ("Outward", "resi 34 & chain I", merge=1)

cmd.color ("blue", "resi 35 & chain I")

cmd.select ("Outward", "resi 35 & chain I", merge=1)

cmd.color ("blue", "resi 36 & chain I")

cmd.select ("Outward", "resi 36 & chain I", merge=1)

cmd.color ("blue", "resi 37 & chain I")

cmd.select ("Outward", "resi 37 & chain I", merge=1)

cmd.color ("blue", "resi 38 & chain I")

cmd.select ("Outward", "resi 38 & chain I", merge=1)

cmd.color ("blue", "resi 39 & chain I")

cmd.select ("Outward", "resi 39 & chain I", merge=1)

cmd.color ("blue", "resi 40 & chain I")

cmd.select ("Outward", "resi 40 & chain I", merge=1)

cmd.color ("blue", "resi 41 & chain I")

cmd.select ("Outward", "resi 41 & chain I", merge=1)

cmd.color ("blue", "resi 42 & chain I")

cmd.select ("Outward", "resi 42 & chain I", merge=1)

cmd.color ("blue", "resi 43 & chain I")

cmd.select ("Outward", "resi 43 & chain I", merge=1)

cmd.color ("blue", "resi 44 & chain I")

cmd.select ("Outward", "resi 44 & chain I", merge=1)

cmd.color ("blue", "resi 45 & chain I")

cmd.select ("Outward", "resi 45 & chain I", merge=1)

cmd.color ("blue", "resi 46 & chain I")

cmd.select ("Outward", "resi 46 & chain I", merge=1)

cmd.color ("blue", "resi 47 & chain I")

cmd.select ("Outward", "resi 47 & chain I", merge=1)

cmd.color ("blue", "resi 48 & chain I")

cmd.select ("Outward", "resi 48 & chain I", merge=1)

cmd.color ("blue", "resi 49 & chain I")

cmd.select ("Outward", "resi 49 & chain I", merge=1)

cmd.color ("blue", "resi 50 & chain I")

cmd.select ("Outward", "resi 50 & chain I", merge=1)

cmd.color ("blue", "resi 51 & chain I")

cmd.select ("Outward", "resi 51 & chain I", merge=1)

cmd.color ("blue", "resi 52 & chain I")

cmd.select ("Outward", "resi 52 & chain I", merge=1)

cmd.color ("blue", "resi 53 & chain I")

cmd.select ("Outward", "resi 53 & chain I", merge=1)

cmd.color ("blue", "resi 54 & chain I")

cmd.select ("Outward", "resi 54 & chain I", merge=1)

cmd.color ("blue", "resi 55 & chain I")

cmd.select ("Outward", "resi 55 & chain I", merge=1)

cmd.color ("blue", "resi 56 & chain I")

cmd.select ("Outward", "resi 56 & chain I", merge=1)

cmd.color ("blue", "resi 57 & chain I")

cmd.select ("Outward", "resi 57 & chain I", merge=1)

cmd.color ("blue", "resi 58 & chain I")

cmd.select ("Outward", "resi 58 & chain I", merge=1)

cmd.color ("blue", "resi 59 & chain I")

cmd.select ("Outward", "resi 59 & chain I", merge=1)

cmd.color ("blue", "resi 60 & chain I")

cmd.select ("Outward", "resi 60 & chain I", merge=1)

cmd.color ("blue", "resi 61 & chain I")

cmd.select ("Outward", "resi 61 & chain I", merge=1)

cmd.color ("blue", "resi 62 & chain I")

cmd.select ("Outward", "resi 62 & chain I", merge=1)

cmd.color ("blue", "resi 63 & chain I")

cmd.select ("Outward", "resi 63 & chain I", merge=1)

cmd.color ("blue", "resi 64 & chain I")

cmd.select ("Outward", "resi 64 & chain I", merge=1)

cmd.color ("blue", "resi 65 & chain I")

cmd.select ("Outward", "resi 65 & chain I", merge=1)

cmd.color ("blue", "resi 66 & chain I")

cmd.select ("Outward", "resi 66 & chain I", merge=1)

cmd.color ("blue", "resi 74 & chain I")

cmd.select ("Outward", "resi 74 & chain I", merge=1)

cmd.color ("blue", "resi 75 & chain I")

cmd.select ("Outward", "resi 75 & chain I", merge=1)

cmd.color ("blue", "resi 76 & chain I")

cmd.select ("Outward", "resi 76 & chain I", merge=1)

cmd.color ("blue", "resi 77 & chain I")

cmd.select ("Outward", "resi 77 & chain I", merge=1)

cmd.color ("blue", "resi 78 & chain I")

cmd.select ("Outward", "resi 78 & chain I", merge=1)

cmd.color ("blue", "resi 79 & chain I")

cmd.select ("Outward", "resi 79 & chain I", merge=1)

cmd.color ("blue", "resi 80 & chain I")

cmd.select ("Outward", "resi 80 & chain I", merge=1)

cmd.color ("blue", "resi 81 & chain I")

cmd.select ("Outward", "resi 81 & chain I", merge=1)

cmd.color ("blue", "resi 82 & chain I")

cmd.select ("Outward", "resi 82 & chain I", merge=1)

cmd.color ("blue", "resi 83 & chain I")

cmd.select ("Outward", "resi 83 & chain I", merge=1)

cmd.color ("blue", "resi 84 & chain I")

cmd.select ("Outward", "resi 84 & chain I", merge=1)

cmd.color ("blue", "resi 85 & chain I")

cmd.select ("Outward", "resi 85 & chain I", merge=1)

cmd.color ("blue", "resi 86 & chain I")

cmd.select ("Outward", "resi 86 & chain I", merge=1)

cmd.color ("blue", "resi 87 & chain I")

cmd.select ("Outward", "resi 87 & chain I", merge=1)

cmd.color ("blue", "resi 88 & chain I")

cmd.select ("Outward", "resi 88 & chain I", merge=1)

cmd.color ("blue", "resi 89 & chain I")

cmd.select ("Outward", "resi 89 & chain I", merge=1)

cmd.color ("blue", "resi 90 & chain I")

cmd.select ("Outward", "resi 90 & chain I", merge=1)

cmd.color ("blue", "resi 91 & chain I")

cmd.select ("Outward", "resi 91 & chain I", merge=1)

cmd.color ("blue", "resi 92 & chain I")

cmd.select ("Outward", "resi 92 & chain I", merge=1)

cmd.color ("blue", "resi 93 & chain I")

cmd.select ("Outward", "resi 93 & chain I", merge=1)

cmd.color ("blue", "resi 94 & chain I")

cmd.select ("Outward", "resi 94 & chain I", merge=1)

cmd.color ("blue", "resi 95 & chain I")

cmd.select ("Outward", "resi 95 & chain I", merge=1)

cmd.color ("blue", "resi 96 & chain I")

cmd.select ("Outward", "resi 96 & chain I", merge=1)

cmd.color ("blue", "resi 97 & chain I")

cmd.select ("Outward", "resi 97 & chain I", merge=1)

cmd.color ("blue", "resi 98 & chain I")

cmd.select ("Outward", "resi 98 & chain I", merge=1)

cmd.color ("blue", "resi 99 & chain I")

cmd.select ("Outward", "resi 99 & chain I", merge=1)

cmd.color ("blue", "resi 100 & chain I")

cmd.select ("Outward", "resi 100 & chain I", merge=1)

cmd.color ("blue", "resi 101 & chain I")

cmd.select ("Outward", "resi 101 & chain I", merge=1)

cmd.color ("blue", "resi 102 & chain I")

cmd.select ("Outward", "resi 102 & chain I", merge=1)

cmd.color ("blue", "resi 103 & chain I")

cmd.select ("Outward", "resi 103 & chain I", merge=1)

cmd.color ("blue", "resi 104 & chain I")

cmd.select ("Outward", "resi 104 & chain I", merge=1)

cmd.color ("blue", "resi 105 & chain I")

cmd.select ("Outward", "resi 105 & chain I", merge=1)

cmd.color ("blue", "resi 106 & chain I")

cmd.select ("Outward", "resi 106 & chain I", merge=1)

cmd.color ("blue", "resi 107 & chain I")

cmd.select ("Outward", "resi 107 & chain I", merge=1)

cmd.load_cgo( [9.0, 160.15927,160.15962,200.3246, 160.1595, 160.15936, 115.547104, 1, 1,1,0,0,0,1], "axis" )
