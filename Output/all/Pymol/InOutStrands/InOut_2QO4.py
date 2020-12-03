from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2QO4.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 4+5+6+7+8+9+10+11+12 & chain A ")


cmd.select("Astrand1", "resi 37+38+39+40+41+42+43 & chain A ")


cmd.select("Astrand2", "resi 46+47+48+49+50+51+52+53 & chain A ")


cmd.select("Astrand3", "resi 56+57+58+59+60+61+62+63 & chain A ")


cmd.select("Astrand9", "resi 116+117+118+119+120+121+122+123+124 & chain A ")


cmd.select("Astrand8", "resi 106+107+108+109+110+111+112+113 & chain A ")


cmd.select("Astrand7", "resi 97+98+99+100+101+102+103 & chain A ")


cmd.select("Astrand6", "resi 88+89+90+91+92 & chain A ")


cmd.select("Astrand5", "resi 77+78+79+80+81+82+83+84+85 & chain A ")


cmd.select("Astrand4", "resi 67+68+69+70+71 & chain A ")


cmd.select("barrel", "Astrand*")
cmd.show("sticks", "barrel")
cmd.show("cartoon", "barrel")
cmd.set("cartoon_side_chain_helper", "on")
cmd.zoom("barrel")
cmd.color ("blue", "resi 4 & chain A")

cmd.select ("Outward", "resi 4 & chain A", merge=1)

cmd.color ("blue", "resi 5 & chain A")

cmd.select ("Outward", "resi 5 & chain A", merge=1)

cmd.color ("blue", "resi 6 & chain A")

cmd.select ("Outward", "resi 6 & chain A", merge=1)

cmd.color ("blue", "resi 7 & chain A")

cmd.select ("Outward", "resi 7 & chain A", merge=1)

cmd.color ("blue", "resi 8 & chain A")

cmd.select ("Outward", "resi 8 & chain A", merge=1)

cmd.color ("blue", "resi 9 & chain A")

cmd.select ("Outward", "resi 9 & chain A", merge=1)

cmd.color ("blue", "resi 10 & chain A")

cmd.select ("Outward", "resi 10 & chain A", merge=1)

cmd.color ("blue", "resi 11 & chain A")

cmd.select ("Outward", "resi 11 & chain A", merge=1)

cmd.color ("blue", "resi 12 & chain A")

cmd.select ("Outward", "resi 12 & chain A", merge=1)

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

cmd.color ("blue", "resi 67 & chain A")

cmd.select ("Outward", "resi 67 & chain A", merge=1)

cmd.color ("blue", "resi 68 & chain A")

cmd.select ("Outward", "resi 68 & chain A", merge=1)

cmd.color ("blue", "resi 69 & chain A")

cmd.select ("Outward", "resi 69 & chain A", merge=1)

cmd.color ("blue", "resi 70 & chain A")

cmd.select ("Outward", "resi 70 & chain A", merge=1)

cmd.color ("blue", "resi 71 & chain A")

cmd.select ("Outward", "resi 71 & chain A", merge=1)

cmd.load_cgo( [9.0, -16.83925,23.549623,-2.1883755, -5.9155, 13.588249, 3.8763747, 1, 1,1,0,0,0,1], "axis" )
