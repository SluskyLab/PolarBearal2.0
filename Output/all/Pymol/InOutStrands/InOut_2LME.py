from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2LME.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 52+53+54+55+56+57+58+59+60+61+62+63 & chain A ")


cmd.select("Astrand3", "resi 94+95+96+97+98+99+100+101+102+103+104 & chain A ")


cmd.select("Cstrand8", "resi 52+53+54+55+56+57+58+59+60+61+62+63 & chain C ")


cmd.select("Bstrand4", "resi 52+53+54+55+56+57+58+59+60+61+62+63 & chain B ")


cmd.select("Cstrand9", "resi 66+67+68+69+70+71+72+73+74+75+76+77 & chain C ")


cmd.select("Cstrand10", "resi 84+85+86+87+88+89+90 & chain C ")


cmd.select("Cstrand11", "resi 94+95+96+97+98+99+100+101+102+103+104 & chain C ")


cmd.select("Bstrand5", "resi 66+67+68+69+70+71+72+73+74+75+76+77 & chain B ")


cmd.select("Bstrand6", "resi 84+85+86+87+88+89+90 & chain B ")


cmd.select("Bstrand7", "resi 94+95+96+97+98+99+100+101+102+103+104 & chain B ")


cmd.select("Astrand2", "resi 84+85+86+87+88+89+90 & chain A ")


cmd.select("Astrand1", "resi 66+67+68+69+70+71+72+73+74+75+76+77 & chain A ")


cmd.select("barrel", "Astrand* or Cstrand* or Bstrand*")
cmd.show("sticks", "barrel")
cmd.show("cartoon", "barrel")
cmd.set("cartoon_side_chain_helper", "on")
cmd.zoom("barrel")
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

cmd.color ("blue", "resi 66 & chain C")

cmd.select ("Outward", "resi 66 & chain C", merge=1)

cmd.color ("blue", "resi 67 & chain C")

cmd.select ("Outward", "resi 67 & chain C", merge=1)

cmd.color ("blue", "resi 68 & chain C")

cmd.select ("Outward", "resi 68 & chain C", merge=1)

cmd.color ("blue", "resi 69 & chain C")

cmd.select ("Outward", "resi 69 & chain C", merge=1)

cmd.color ("blue", "resi 70 & chain C")

cmd.select ("Outward", "resi 70 & chain C", merge=1)

cmd.color ("blue", "resi 71 & chain C")

cmd.select ("Outward", "resi 71 & chain C", merge=1)

cmd.color ("blue", "resi 72 & chain C")

cmd.select ("Outward", "resi 72 & chain C", merge=1)

cmd.color ("blue", "resi 73 & chain C")

cmd.select ("Outward", "resi 73 & chain C", merge=1)

cmd.color ("blue", "resi 74 & chain C")

cmd.select ("Outward", "resi 74 & chain C", merge=1)

cmd.color ("blue", "resi 75 & chain C")

cmd.select ("Outward", "resi 75 & chain C", merge=1)

cmd.color ("blue", "resi 76 & chain C")

cmd.select ("Outward", "resi 76 & chain C", merge=1)

cmd.color ("blue", "resi 77 & chain C")

cmd.select ("Outward", "resi 77 & chain C", merge=1)

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

cmd.color ("blue", "resi 66 & chain B")

cmd.select ("Outward", "resi 66 & chain B", merge=1)

cmd.color ("blue", "resi 67 & chain B")

cmd.select ("Outward", "resi 67 & chain B", merge=1)

cmd.color ("blue", "resi 68 & chain B")

cmd.select ("Outward", "resi 68 & chain B", merge=1)

cmd.color ("blue", "resi 69 & chain B")

cmd.select ("Outward", "resi 69 & chain B", merge=1)

cmd.color ("blue", "resi 70 & chain B")

cmd.select ("Outward", "resi 70 & chain B", merge=1)

cmd.color ("blue", "resi 71 & chain B")

cmd.select ("Outward", "resi 71 & chain B", merge=1)

cmd.color ("blue", "resi 72 & chain B")

cmd.select ("Outward", "resi 72 & chain B", merge=1)

cmd.color ("blue", "resi 73 & chain B")

cmd.select ("Outward", "resi 73 & chain B", merge=1)

cmd.color ("blue", "resi 74 & chain B")

cmd.select ("Outward", "resi 74 & chain B", merge=1)

cmd.color ("blue", "resi 75 & chain B")

cmd.select ("Outward", "resi 75 & chain B", merge=1)

cmd.color ("blue", "resi 76 & chain B")

cmd.select ("Outward", "resi 76 & chain B", merge=1)

cmd.color ("blue", "resi 77 & chain B")

cmd.select ("Outward", "resi 77 & chain B", merge=1)

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

cmd.color ("blue", "resi 72 & chain A")

cmd.select ("Outward", "resi 72 & chain A", merge=1)

cmd.color ("blue", "resi 73 & chain A")

cmd.select ("Outward", "resi 73 & chain A", merge=1)

cmd.color ("blue", "resi 74 & chain A")

cmd.select ("Outward", "resi 74 & chain A", merge=1)

cmd.color ("blue", "resi 75 & chain A")

cmd.select ("Outward", "resi 75 & chain A", merge=1)

cmd.color ("blue", "resi 76 & chain A")

cmd.select ("Outward", "resi 76 & chain A", merge=1)

cmd.color ("blue", "resi 77 & chain A")

cmd.select ("Outward", "resi 77 & chain A", merge=1)

cmd.load_cgo( [9.0, 0,0,0, 0, 0, 0, 1, 1,1,0,0,0,1], "axis" )
