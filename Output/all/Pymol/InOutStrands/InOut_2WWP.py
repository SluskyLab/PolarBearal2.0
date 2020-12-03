from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2WWP.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 41+42+43+44+45+46+47+48+49+50 & chain A ")


cmd.select("Astrand1", "resi 65+66+67+68+69+70+71 & chain A ")


cmd.select("Astrand2", "resi 77+78+79+80+81+82+83+84+85 & chain A ")


cmd.select("Astrand3", "resi 88+89+90+91+92+93+94+95+96+97+98 & chain A ")


cmd.select("Astrand4", "resi 104+105+106+107+108+109 & chain A ")


cmd.select("Astrand5", "resi 114+115+116+117+118+119+120+121+122+123 & chain A ")


cmd.select("Astrand6", "resi 128+129+130+131+132+133+134+135+136+137 & chain A ")


cmd.select("Astrand7", "resi 144+145+146+147+148+149+150 & chain A ")


cmd.select("barrel", "Astrand*")
cmd.show("sticks", "barrel")
cmd.show("cartoon", "barrel")
cmd.set("cartoon_side_chain_helper", "on")
cmd.zoom("barrel")
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

cmd.color ("blue", "resi 65 & chain A")

cmd.select ("Outward", "resi 65 & chain A", merge=1)

cmd.color ("blue", "resi 66 & chain A")

cmd.select ("Outward", "resi 66 & chain A", merge=1)

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

cmd.color ("blue", "resi 133 & chain A")

cmd.select ("Outward", "resi 133 & chain A", merge=1)

cmd.color ("blue", "resi 134 & chain A")

cmd.select ("Outward", "resi 134 & chain A", merge=1)

cmd.color ("blue", "resi 135 & chain A")

cmd.select ("Outward", "resi 135 & chain A", merge=1)

cmd.color ("blue", "resi 136 & chain A")

cmd.select ("Outward", "resi 136 & chain A", merge=1)

cmd.color ("blue", "resi 137 & chain A")

cmd.select ("Outward", "resi 137 & chain A", merge=1)

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

cmd.load_cgo( [9.0, 18.798124,-19.148876,6.3450003, 17.168875, -3.2581248, 2.964375, 1, 1,1,0,0,0,1], "axis" )
