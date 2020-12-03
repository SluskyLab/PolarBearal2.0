from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2C9J.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.remove("hydrogens")
cmd.h_add("(name CA)")
cmd.select("Astrand0", "resi 8+9+10+11+12+13+14+15+16+17+18 & chain A ")


cmd.select("Astrand1", "resi 113+114+115+116+117+118+119+120+121+122+123 & chain A ")


cmd.select("Astrand2", "resi 100+101+102+103+104+105+106+107+108+109+110 & chain A ")


cmd.select("Astrand3", "resi 87+88+89+90+91+92+93+94+95 & chain A ")


cmd.select("Astrand4", "resi 168+169+170+171+172+173+174+175+176+177+178+179 & chain A ")


cmd.select("Astrand5", "resi 152+153+154+155+156+157+158+159+160+161+162+163 & chain A ")


cmd.select("Astrand6", "resi 136+137+138+139+142+143+144+145+146+147+148+149 & chain A ")


cmd.select("Astrand7", "resi 190+191+192+193+194+195+196+197+198+199+200+201 & chain A ")


cmd.select("Astrand8", "resi 207+208+209+210+211+212+213+214+215+216+217 & chain A ")


cmd.select("Astrand9", "resi 37+38+39+40+41+42+43+44 & chain A ")


cmd.select("Astrand10", "resi 21+22+23+24+25+26+27+28+29+30+31+32 & chain A ")


cmd.group("Strands", "*strand*")
cmd.select("barrel", "Astrand*")
cmd.pseudoatom ("PseudoH113A", pos=[9.447713,-18.136414,31.023008])
cmd.pseudoatom ("PseudoH10A", pos=[6.884754,-17.699694,27.581606])
cmd.pseudoatom ("PseudoH115A", pos=[5.654546,-13.709839,28.238485])
cmd.pseudoatom ("PseudoH12A", pos=[2.1748955,-13.178139,26.506327])
cmd.pseudoatom ("PseudoH117A", pos=[1.668741,-8.598152,26.386446])
cmd.pseudoatom ("PseudoH14A", pos=[-2.2096517,-9.024748,23.764421])
cmd.pseudoatom ("PseudoH119A", pos=[-2.370347,-5.1887307,21.779007])
cmd.pseudoatom ("PseudoH16A", pos=[-6.1957726,-5.7861867,20.254286])
cmd.pseudoatom ("PseudoH121A", pos=[-6.4978585,-3.367904,16.70053])
cmd.pseudoatom ("PseudoH18A", pos=[-9.804082,-4.8305078,14.619884])
cmd.pseudoatom ("PseudoH109A", pos=[11.743275,-13.085918,30.066736])
cmd.pseudoatom ("PseudoH114A", pos=[9.964678,-14.371488,28.644173])
cmd.pseudoatom ("PseudoH107A", pos=[7.9907804,-9.709111,25.525553])
cmd.pseudoatom ("PseudoH116A", pos=[5.63239,-10.328357,25.304354])
cmd.pseudoatom ("PseudoH105A", pos=[3.8048208,-6.726195,22.025797])
cmd.pseudoatom ("PseudoH118A", pos=[1.6174703,-7.2386613,22.301155])
cmd.pseudoatom ("PseudoH103A", pos=[-0.4439583,-5.334871,16.947594])
cmd.pseudoatom ("PseudoH120A", pos=[-2.7744455,-5.6847005,17.381979])
cmd.pseudoatom ("PseudoH101A", pos=[-4.683301,-4.7328196,11.840073])
cmd.pseudoatom ("PseudoH122A", pos=[-6.4159656,-4.1933603,12.392502])
cmd.pseudoatom ("PseudoH100A", pos=[-4.2786655,-4.671275,7.493836])
cmd.pseudoatom ("PseudoH92A", pos=[0.61432946,-4.597728,10.791382])
cmd.pseudoatom ("PseudoH102A", pos=[-0.39329916,-3.9957168,12.690347])
cmd.pseudoatom ("PseudoH90A", pos=[4.982644,-4.2303185,16.377087])
cmd.pseudoatom ("PseudoH104A", pos=[3.8401775,-5.0696077,17.960455])
cmd.pseudoatom ("PseudoH88A", pos=[9.752545,-6.313022,21.704802])
cmd.pseudoatom ("PseudoH87A", pos=[13.933576,-6.704707,22.123245])
cmd.pseudoatom ("PseudoH177A", pos=[11.434316,-6.135243,16.264912])
cmd.pseudoatom ("PseudoH89A", pos=[9.266635,-5.4488773,17.118187])
cmd.pseudoatom ("PseudoH175A", pos=[6.8989725,-5.848419,11.608693])
cmd.pseudoatom ("PseudoH91A", pos=[4.840144,-5.137,12.101555])
cmd.pseudoatom ("PseudoH173A", pos=[2.6641457,-7.9200077,7.074894])
cmd.pseudoatom ("PseudoH93A", pos=[0.5551457,-7.283604,7.245737])
cmd.pseudoatom ("PseudoH171A", pos=[-1.992674,-9.214418,2.5520227])
cmd.pseudoatom ("PseudoH95A", pos=[-3.8090763,-8.431046,3.2935905])
cmd.pseudoatom ("PseudoH168A", pos=[-6.6229734,-18.3606,-0.11632228])
cmd.pseudoatom ("PseudoH160A", pos=[-2.079186,-15.872833,1.8175133])
cmd.pseudoatom ("PseudoH170A", pos=[-3.0270116,-13.599635,1.6334746])
cmd.pseudoatom ("PseudoH158A", pos=[3.3045082,-11.620379,2.2761464])
cmd.pseudoatom ("PseudoH156A", pos=[7.9881454,-8.259017,5.6041203])
cmd.pseudoatom ("PseudoH174A", pos=[6.9528227,-6.559435,7.2910433])
cmd.pseudoatom ("PseudoH154A", pos=[12.061612,-5.309343,10.009076])
cmd.pseudoatom ("PseudoH176A", pos=[11.092627,-4.345915,12.218025])
cmd.pseudoatom ("PseudoH152A", pos=[16.072683,-2.6463661,14.481342])
cmd.pseudoatom ("PseudoH148A", pos=[17.928871,-4.7387176,9.805685])
cmd.pseudoatom ("PseudoH153A", pos=[16.288677,-5.526165,11.0825205])
cmd.pseudoatom ("PseudoH146A", pos=[14.075993,-9.358121,7.1801524])
cmd.pseudoatom ("PseudoH155A", pos=[11.9203415,-8.932007,7.548107])
cmd.pseudoatom ("PseudoH144A", pos=[9.437381,-13.302061,5.343241])
cmd.pseudoatom ("PseudoH157A", pos=[7.2698417,-12.390341,4.2860374])
cmd.pseudoatom ("PseudoH139A", pos=[-2.9093876,-19.310886,6.0901837])
cmd.pseudoatom ("PseudoH161A", pos=[-4.200418,-18.36944,4.7305655])
cmd.pseudoatom ("PseudoH136A", pos=[-9.899117,-18.597403,5.859577])
cmd.pseudoatom ("PseudoH193A", pos=[10.169982,-19.436539,6.330572])
cmd.pseudoatom ("PseudoH143A", pos=[9.632863,-17.649971,4.7633047])
cmd.pseudoatom ("PseudoH191A", pos=[14.652776,-14.558971,5.766443])
cmd.pseudoatom ("PseudoH145A", pos=[13.665777,-12.614158,4.3130736])
cmd.pseudoatom ("PseudoH216A", pos=[15.748142,-18.393478,9.21101])
cmd.pseudoatom ("PseudoH192A", pos=[13.798821,-18.039045,8.459398])
cmd.pseudoatom ("PseudoH214A", pos=[10.194228,-21.26669,11.3861265])
cmd.pseudoatom ("PseudoH194A", pos=[8.149272,-20.763018,10.046225])
cmd.pseudoatom ("PseudoH212A", pos=[4.4659505,-22.444529,14.099168])
cmd.pseudoatom ("PseudoH196A", pos=[2.5604162,-22.335299,12.82726])
cmd.pseudoatom ("PseudoH210A", pos=[-1.5638568,-23.86474,17.105211])
cmd.pseudoatom ("PseudoH198A", pos=[-3.359706,-23.74079,15.706636])
cmd.pseudoatom ("PseudoH208A", pos=[-7.36415,-22.971561,19.968502])
cmd.pseudoatom ("PseudoH201A", pos=[-9.1675,-23.997913,18.546406])
cmd.pseudoatom ("PseudoH207A", pos=[-8.842992,-20.877577,23.58653])
cmd.pseudoatom ("PseudoH41A", pos=[-3.023313,-22.611856,23.17797])
cmd.pseudoatom ("PseudoH209A", pos=[-3.1243267,-23.59812,21.18665])
cmd.pseudoatom ("PseudoH39A", pos=[3.1103284,-23.697466,19.97661])
cmd.pseudoatom ("PseudoH211A", pos=[2.8124356,-24.02048,17.89246])
cmd.pseudoatom ("PseudoH37A", pos=[9.0166645,-24.333055,16.695402])
cmd.pseudoatom ("PseudoH38A", pos=[7.3764396,-24.856735,20.7886])
cmd.pseudoatom ("PseudoH40A", pos=[1.3930116,-22.649101,23.965212])
cmd.pseudoatom ("PseudoH27A", pos=[-2.3723893,-18.297426,26.251827])
cmd.pseudoatom ("PseudoH42A", pos=[-3.9870098,-18.681372,24.835306])
cmd.pseudoatom ("PseudoH25A", pos=[-7.185761,-13.979043,25.361116])
cmd.pseudoatom ("PseudoH44A", pos=[-9.50406,-14.913276,24.837059])
cmd.pseudoatom ("PseudoH17A", pos=[-10.50702,-4.808689,18.94464])
cmd.pseudoatom ("PseudoH22A", pos=[-11.586384,-5.3514056,20.96316])
cmd.pseudoatom ("PseudoH15A", pos=[-6.3882136,-7.569644,24.138899])
cmd.pseudoatom ("PseudoH24A", pos=[-7.5446663,-9.6424675,24.647795])
cmd.pseudoatom ("PseudoH13A", pos=[-2.1415012,-12.072957,26.91849])
cmd.pseudoatom ("PseudoH26A", pos=[-3.2906828,-14.226547,27.574732])
cmd.pseudoatom ("PseudoH11A", pos=[2.5465472,-17.134348,28.46645])
cmd.pseudoatom ("PseudoH28A", pos=[1.5930717,-19.382198,28.137632])
cmd.pseudoatom ("PseudoH9A", pos=[7.9065585,-21.931578,28.52795])
cmd.pseudoatom ("PseudoH30A", pos=[7.137224,-21.76474,24.863813])
cmd.group("Pseudo_Hydrogens", "PseudoH*")
cmd.pseudoatom ("PseudoR116A", pos=[4.62327,-11.570492,24.508614])
cmd.pseudoatom ("PseudoR122A", pos=[-7.723185,-5.25683,12.952868])
cmd.pseudoatom ("PseudoR171A", pos=[-1.8642182,-10.102958,4.0947056])
cmd.pseudoatom ("PseudoR155A", pos=[10.831832,-9.369227,8.8724])
cmd.pseudoatom ("PseudoR27A", pos=[-1.1550804,-17.34844,25.418535])
cmd.group("Pseudo_RGroups", "PseudoR*")
cmd.distance("StrongHBond", "resi 113 & chain A & name O", "resi 110 & chain A & name N")
cmd.distance("StrongHBond", "resi 113 & chain A & name N", "resi 110 & chain A & name O")
cmd.distance("StrongHBond", "resi 115 & chain A & name O", "resi 108 & chain A & name N")
cmd.distance("StrongHBond", "resi 115 & chain A & name N", "resi 108 & chain A & name O")
cmd.distance("StrongHBond", "resi 117 & chain A & name O", "resi 106 & chain A & name N")
cmd.distance("StrongHBond", "resi 117 & chain A & name N", "resi 106 & chain A & name O")
cmd.distance("StrongHBond", "resi 119 & chain A & name O", "resi 104 & chain A & name N")
cmd.distance("StrongHBond", "resi 119 & chain A & name N", "resi 104 & chain A & name O")
cmd.distance("StrongHBond", "resi 121 & chain A & name O", "resi 102 & chain A & name N")
cmd.distance("StrongHBond", "resi 121 & chain A & name N", "resi 102 & chain A & name O")
cmd.distance("StrongHBond", "resi 123 & chain A & name O", "resi 100 & chain A & name N")
cmd.distance("StrongHBond", "resi 123 & chain A & name N", "resi 100 & chain A & name O")
cmd.distance("StrongHBond", "resi 101 & chain A & name O", "resi 93 & chain A & name N")
cmd.distance("StrongHBond", "resi 101 & chain A & name N", "resi 93 & chain A & name O")
cmd.distance("StrongHBond", "resi 103 & chain A & name O", "resi 91 & chain A & name N")
cmd.distance("StrongHBond", "resi 103 & chain A & name N", "resi 91 & chain A & name O")
cmd.distance("StrongHBond", "resi 105 & chain A & name O", "resi 89 & chain A & name N")
cmd.distance("StrongHBond", "resi 105 & chain A & name N", "resi 89 & chain A & name O")
cmd.distance("StrongHBond", "resi 88 & chain A & name O", "resi 178 & chain A & name N")
cmd.distance("StrongHBond", "resi 88 & chain A & name N", "resi 178 & chain A & name O")
cmd.distance("StrongHBond", "resi 90 & chain A & name O", "resi 176 & chain A & name N")
cmd.distance("StrongHBond", "resi 90 & chain A & name N", "resi 176 & chain A & name O")
cmd.distance("StrongHBond", "resi 92 & chain A & name O", "resi 174 & chain A & name N")
cmd.distance("StrongHBond", "resi 92 & chain A & name N", "resi 174 & chain A & name O")
cmd.distance("StrongHBond", "resi 94 & chain A & name O", "resi 172 & chain A & name N")
cmd.distance("StrongHBond", "resi 94 & chain A & name N", "resi 172 & chain A & name O")
cmd.distance("StrongHBond", "resi 169 & chain A & name O", "resi 161 & chain A & name N")
cmd.distance("StrongHBond", "resi 169 & chain A & name N", "resi 161 & chain A & name O")
cmd.distance("StrongHBond", "resi 171 & chain A & name O", "resi 159 & chain A & name N")
cmd.distance("StrongHBond", "resi 171 & chain A & name N", "resi 159 & chain A & name O")
cmd.distance("StrongHBond", "resi 173 & chain A & name O", "resi 157 & chain A & name N")
cmd.distance("StrongHBond", "resi 173 & chain A & name N", "resi 157 & chain A & name O")
cmd.distance("StrongHBond", "resi 175 & chain A & name O", "resi 155 & chain A & name N")
cmd.distance("StrongHBond", "resi 175 & chain A & name N", "resi 155 & chain A & name O")
cmd.distance("StrongHBond", "resi 177 & chain A & name O", "resi 153 & chain A & name N")
cmd.distance("StrongHBond", "resi 177 & chain A & name N", "resi 153 & chain A & name O")
cmd.distance("StrongHBond", "resi 152 & chain A & name O", "resi 149 & chain A & name N")
cmd.distance("StrongHBond", "resi 152 & chain A & name N", "resi 149 & chain A & name O")
cmd.distance("StrongHBond", "resi 154 & chain A & name O", "resi 147 & chain A & name N")
cmd.distance("StrongHBond", "resi 154 & chain A & name N", "resi 147 & chain A & name O")
cmd.distance("StrongHBond", "resi 156 & chain A & name O", "resi 145 & chain A & name N")
cmd.distance("StrongHBond", "resi 156 & chain A & name N", "resi 145 & chain A & name O")
cmd.distance("StrongHBond", "resi 162 & chain A & name O", "resi 138 & chain A & name N")
cmd.distance("StrongHBond", "resi 162 & chain A & name N", "resi 138 & chain A & name O")
cmd.distance("StrongHBond", "resi 142 & chain A & name O", "resi 194 & chain A & name N")
cmd.distance("StrongHBond", "resi 142 & chain A & name N", "resi 194 & chain A & name O")
cmd.distance("StrongHBond", "resi 144 & chain A & name O", "resi 192 & chain A & name N")
cmd.distance("StrongHBond", "resi 144 & chain A & name N", "resi 192 & chain A & name O")
cmd.distance("StrongHBond", "resi 146 & chain A & name O", "resi 190 & chain A & name N")
cmd.distance("StrongHBond", "resi 146 & chain A & name N", "resi 190 & chain A & name O")
cmd.distance("StrongHBond", "resi 191 & chain A & name O", "resi 217 & chain A & name N")
cmd.distance("StrongHBond", "resi 191 & chain A & name N", "resi 217 & chain A & name O")
cmd.distance("StrongHBond", "resi 193 & chain A & name O", "resi 215 & chain A & name N")
cmd.distance("StrongHBond", "resi 193 & chain A & name N", "resi 215 & chain A & name O")
cmd.distance("StrongHBond", "resi 195 & chain A & name O", "resi 213 & chain A & name N")
cmd.distance("StrongHBond", "resi 195 & chain A & name N", "resi 213 & chain A & name O")
cmd.distance("StrongHBond", "resi 197 & chain A & name O", "resi 211 & chain A & name N")
cmd.distance("StrongHBond", "resi 197 & chain A & name N", "resi 211 & chain A & name O")
cmd.distance("StrongHBond", "resi 200 & chain A & name O", "resi 209 & chain A & name N")
cmd.distance("StrongHBond", "resi 200 & chain A & name N", "resi 209 & chain A & name O")
cmd.distance("StrongHBond", "resi 208 & chain A & name O", "resi 42 & chain A & name N")
cmd.distance("StrongHBond", "resi 208 & chain A & name N", "resi 42 & chain A & name O")
cmd.distance("StrongHBond", "resi 210 & chain A & name O", "resi 40 & chain A & name N")
cmd.distance("StrongHBond", "resi 210 & chain A & name N", "resi 40 & chain A & name O")
cmd.distance("StrongHBond", "resi 212 & chain A & name O", "resi 38 & chain A & name N")
cmd.distance("StrongHBond", "resi 212 & chain A & name N", "resi 38 & chain A & name O")
cmd.distance("StrongHBond", "resi 39 & chain A & name O", "resi 30 & chain A & name N")
cmd.distance("StrongHBond", "resi 39 & chain A & name N", "resi 30 & chain A & name O")
cmd.distance("StrongHBond", "resi 41 & chain A & name O", "resi 28 & chain A & name N")
cmd.distance("StrongHBond", "resi 41 & chain A & name N", "resi 28 & chain A & name O")
cmd.distance("StrongHBond", "resi 43 & chain A & name O", "resi 26 & chain A & name N")
cmd.distance("StrongHBond", "resi 43 & chain A & name N", "resi 26 & chain A & name O")
cmd.distance("StrongHBond", "resi 21 & chain A & name O", "resi 18 & chain A & name N")
cmd.distance("StrongHBond", "resi 21 & chain A & name N", "resi 18 & chain A & name O")
cmd.distance("StrongHBond", "resi 23 & chain A & name O", "resi 16 & chain A & name N")
cmd.distance("StrongHBond", "resi 23 & chain A & name N", "resi 16 & chain A & name O")
cmd.distance("StrongHBond", "resi 25 & chain A & name O", "resi 14 & chain A & name N")
cmd.distance("StrongHBond", "resi 25 & chain A & name N", "resi 14 & chain A & name O")
cmd.distance("StrongHBond", "resi 27 & chain A & name O", "resi 12 & chain A & name N")
cmd.distance("StrongHBond", "resi 27 & chain A & name N", "resi 12 & chain A & name O")
cmd.distance("StrongHBond", "resi 29 & chain A & name O", "resi 10 & chain A & name N")
cmd.distance("StrongHBond", "resi 29 & chain A & name N", "resi 10 & chain A & name O")
cmd.distance("StrongHBond", "resi 31 & chain A & name O", "resi 8 & chain A & name N")
cmd.distance("StrongHBond", "resi 31 & chain A & name N", "resi 8 & chain A & name O")
cmd.distance("WeakHBond", "resi 9 & chain A & name O", "PseudoH113A")
cmd.distance("WeakHBond", "resi 114 & chain A & name O", "PseudoH10A")
cmd.distance("WeakHBond", "resi 11 & chain A & name O", "PseudoH115A")
cmd.distance("WeakHBond", "resi 116 & chain A & name O", "PseudoH12A")
cmd.distance("WeakHBond", "resi 13 & chain A & name O", "PseudoH117A")
cmd.distance("WeakHBond", "resi 118 & chain A & name O", "PseudoH14A")
cmd.distance("WeakHBond", "resi 15 & chain A & name O", "PseudoH119A")
cmd.distance("WeakHBond", "resi 120 & chain A & name O", "PseudoH16A")
cmd.distance("WeakHBond", "resi 17 & chain A & name O", "PseudoH121A")
cmd.distance("WeakHBond", "resi 122 & chain A & name O", "PseudoH18A")
cmd.distance("WeakHBond", "resi 113 & chain A & name O", "PseudoH109A")
cmd.distance("WeakHBond", "resi 108 & chain A & name O", "PseudoH114A")
cmd.distance("WeakHBond", "resi 115 & chain A & name O", "PseudoH107A")
cmd.distance("WeakHBond", "resi 106 & chain A & name O", "PseudoH116A")
cmd.distance("WeakHBond", "resi 117 & chain A & name O", "PseudoH105A")
cmd.distance("WeakHBond", "resi 104 & chain A & name O", "PseudoH118A")
cmd.distance("WeakHBond", "resi 119 & chain A & name O", "PseudoH103A")
cmd.distance("WeakHBond", "resi 102 & chain A & name O", "PseudoH120A")
cmd.distance("WeakHBond", "resi 121 & chain A & name O", "PseudoH101A")
cmd.distance("WeakHBond", "resi 100 & chain A & name O", "PseudoH122A")
cmd.distance("WeakHBond", "resi 93 & chain A & name O", "PseudoH100A")
cmd.distance("WeakHBond", "resi 101 & chain A & name O", "PseudoH92A")
cmd.distance("WeakHBond", "resi 91 & chain A & name O", "PseudoH102A")
cmd.distance("WeakHBond", "resi 103 & chain A & name O", "PseudoH90A")
cmd.distance("WeakHBond", "resi 89 & chain A & name O", "PseudoH104A")
cmd.distance("WeakHBond", "resi 105 & chain A & name O", "PseudoH88A")
cmd.distance("WeakHBond", "resi 178 & chain A & name O", "PseudoH87A")
cmd.distance("WeakHBond", "resi 88 & chain A & name O", "PseudoH177A")
cmd.distance("WeakHBond", "resi 176 & chain A & name O", "PseudoH89A")
cmd.distance("WeakHBond", "resi 90 & chain A & name O", "PseudoH175A")
cmd.distance("WeakHBond", "resi 174 & chain A & name O", "PseudoH91A")
cmd.distance("WeakHBond", "resi 92 & chain A & name O", "PseudoH173A")
cmd.distance("WeakHBond", "resi 172 & chain A & name O", "PseudoH93A")
cmd.distance("WeakHBond", "resi 94 & chain A & name O", "PseudoH171A")
cmd.distance("WeakHBond", "resi 170 & chain A & name O", "PseudoH95A")
cmd.distance("WeakHBond", "resi 161 & chain A & name O", "PseudoH168A")
cmd.distance("WeakHBond", "resi 169 & chain A & name O", "PseudoH160A")
cmd.distance("WeakHBond", "resi 159 & chain A & name O", "PseudoH170A")
cmd.distance("WeakHBond", "resi 171 & chain A & name O", "PseudoH158A")
cmd.distance("WeakHBond", "resi 173 & chain A & name O", "PseudoH156A")
cmd.distance("WeakHBond", "resi 155 & chain A & name O", "PseudoH174A")
cmd.distance("WeakHBond", "resi 175 & chain A & name O", "PseudoH154A")
cmd.distance("WeakHBond", "resi 153 & chain A & name O", "PseudoH176A")
cmd.distance("WeakHBond", "resi 177 & chain A & name O", "PseudoH152A")
cmd.distance("WeakHBond", "resi 152 & chain A & name O", "PseudoH148A")
cmd.distance("WeakHBond", "resi 147 & chain A & name O", "PseudoH153A")
cmd.distance("WeakHBond", "resi 154 & chain A & name O", "PseudoH146A")
cmd.distance("WeakHBond", "resi 145 & chain A & name O", "PseudoH155A")
cmd.distance("WeakHBond", "resi 156 & chain A & name O", "PseudoH144A")
cmd.distance("WeakHBond", "resi 143 & chain A & name O", "PseudoH157A")
cmd.distance("WeakHBond", "resi 160 & chain A & name O", "PseudoH139A")
cmd.distance("WeakHBond", "resi 138 & chain A & name O", "PseudoH161A")
cmd.distance("WeakHBond", "resi 162 & chain A & name O", "PseudoH136A")
cmd.distance("WeakHBond", "resi 142 & chain A & name O", "PseudoH193A")
cmd.distance("WeakHBond", "resi 192 & chain A & name O", "PseudoH143A")
cmd.distance("WeakHBond", "resi 144 & chain A & name O", "PseudoH191A")
cmd.distance("WeakHBond", "resi 190 & chain A & name O", "PseudoH145A")
cmd.distance("WeakHBond", "resi 191 & chain A & name O", "PseudoH216A")
cmd.distance("WeakHBond", "resi 215 & chain A & name O", "PseudoH192A")
cmd.distance("WeakHBond", "resi 193 & chain A & name O", "PseudoH214A")
cmd.distance("WeakHBond", "resi 213 & chain A & name O", "PseudoH194A")
cmd.distance("WeakHBond", "resi 195 & chain A & name O", "PseudoH212A")
cmd.distance("WeakHBond", "resi 211 & chain A & name O", "PseudoH196A")
cmd.distance("WeakHBond", "resi 197 & chain A & name O", "PseudoH210A")
cmd.distance("WeakHBond", "resi 209 & chain A & name O", "PseudoH198A")
cmd.distance("WeakHBond", "resi 200 & chain A & name O", "PseudoH208A")
cmd.distance("WeakHBond", "resi 207 & chain A & name O", "PseudoH201A")
cmd.distance("WeakHBond", "resi 42 & chain A & name O", "PseudoH207A")
cmd.distance("WeakHBond", "resi 208 & chain A & name O", "PseudoH41A")
cmd.distance("WeakHBond", "resi 40 & chain A & name O", "PseudoH209A")
cmd.distance("WeakHBond", "resi 210 & chain A & name O", "PseudoH39A")
cmd.distance("WeakHBond", "resi 38 & chain A & name O", "PseudoH211A")
cmd.distance("WeakHBond", "resi 212 & chain A & name O", "PseudoH37A")
cmd.distance("WeakHBond", "resi 30 & chain A & name O", "PseudoH38A")
cmd.distance("WeakHBond", "resi 28 & chain A & name O", "PseudoH40A")
cmd.distance("WeakHBond", "resi 41 & chain A & name O", "PseudoH27A")
cmd.distance("WeakHBond", "resi 26 & chain A & name O", "PseudoH42A")
cmd.distance("WeakHBond", "resi 43 & chain A & name O", "PseudoH25A")
cmd.distance("WeakHBond", "resi 24 & chain A & name O", "PseudoH44A")
cmd.distance("WeakHBond", "resi 21 & chain A & name O", "PseudoH17A")
cmd.distance("WeakHBond", "resi 16 & chain A & name O", "PseudoH22A")
cmd.distance("WeakHBond", "resi 23 & chain A & name O", "PseudoH15A")
cmd.distance("WeakHBond", "resi 14 & chain A & name O", "PseudoH24A")
cmd.distance("WeakHBond", "resi 25 & chain A & name O", "PseudoH13A")
cmd.distance("WeakHBond", "resi 12 & chain A & name O", "PseudoH26A")
cmd.distance("WeakHBond", "resi 27 & chain A & name O", "PseudoH11A")
cmd.distance("WeakHBond", "resi 10 & chain A & name O", "PseudoH28A")
cmd.distance("WeakHBond", "resi 29 & chain A & name O", "PseudoH9A")
cmd.distance("WeakHBond", "resi 8 & chain A & name O", "PseudoH30A")
cmd.distance("NonHBond", "resi 114 & chain A & name CB", "resi 109 & chain A & name CB")
cmd.distance("NonHBond", "PseudoR116A", "resi 107 & chain A & name CB")
cmd.distance("NonHBond", "resi 118 & chain A & name CB", "resi 105 & chain A & name CB")
cmd.distance("NonHBond", "resi 120 & chain A & name CB", "resi 103 & chain A & name CB")
cmd.distance("NonHBond", "PseudoR122A", "resi 101 & chain A & name CB")
cmd.distance("NonHBond", "resi 100 & chain A & name CB", "resi 94 & chain A & name CB")
cmd.distance("NonHBond", "resi 102 & chain A & name CB", "resi 92 & chain A & name CB")
cmd.distance("NonHBond", "resi 104 & chain A & name CB", "resi 90 & chain A & name CB")
cmd.distance("NonHBond", "resi 106 & chain A & name CB", "resi 88 & chain A & name CB")
cmd.distance("NonHBond", "resi 87 & chain A & name CB", "resi 179 & chain A & name CB")
cmd.distance("NonHBond", "resi 89 & chain A & name CB", "resi 177 & chain A & name CB")
cmd.distance("NonHBond", "resi 91 & chain A & name CB", "resi 175 & chain A & name CB")
cmd.distance("NonHBond", "resi 93 & chain A & name CB", "resi 173 & chain A & name CB")
cmd.distance("NonHBond", "resi 95 & chain A & name CB", "PseudoR171A")
cmd.distance("NonHBond", "resi 168 & chain A & name CB", "resi 162 & chain A & name CB")
cmd.distance("NonHBond", "resi 170 & chain A & name CB", "resi 160 & chain A & name CB")
cmd.distance("NonHBond", "resi 172 & chain A & name CB", "resi 158 & chain A & name CB")
cmd.distance("NonHBond", "resi 174 & chain A & name CB", "resi 156 & chain A & name CB")
cmd.distance("NonHBond", "resi 176 & chain A & name CB", "resi 154 & chain A & name CB")
cmd.distance("NonHBond", "resi 153 & chain A & name CB", "resi 148 & chain A & name CB")
cmd.distance("NonHBond", "PseudoR155A", "resi 146 & chain A & name CB")
cmd.distance("NonHBond", "resi 157 & chain A & name CB", "resi 144 & chain A & name CB")
cmd.distance("NonHBond", "resi 161 & chain A & name CB", "resi 139 & chain A & name CB")
cmd.distance("NonHBond", "resi 163 & chain A & name CB", "resi 136 & chain A & name CB")
cmd.distance("NonHBond", "resi 143 & chain A & name CB", "resi 193 & chain A & name CB")
cmd.distance("NonHBond", "resi 145 & chain A & name CB", "resi 191 & chain A & name CB")
cmd.distance("NonHBond", "resi 192 & chain A & name CB", "resi 216 & chain A & name CB")
cmd.distance("NonHBond", "resi 194 & chain A & name CB", "resi 214 & chain A & name CB")
cmd.distance("NonHBond", "resi 196 & chain A & name CB", "resi 212 & chain A & name CB")
cmd.distance("NonHBond", "resi 198 & chain A & name CB", "resi 210 & chain A & name CB")
cmd.distance("NonHBond", "resi 201 & chain A & name CB", "resi 208 & chain A & name CB")
cmd.distance("NonHBond", "resi 207 & chain A & name CB", "resi 43 & chain A & name CB")
cmd.distance("NonHBond", "resi 209 & chain A & name CB", "resi 41 & chain A & name CB")
cmd.distance("NonHBond", "resi 211 & chain A & name CB", "resi 39 & chain A & name CB")
cmd.distance("NonHBond", "resi 213 & chain A & name CB", "resi 37 & chain A & name CB")
cmd.distance("NonHBond", "resi 42 & chain A & name CB", "PseudoR27A")
cmd.distance("NonHBond", "resi 44 & chain A & name CB", "resi 25 & chain A & name CB")
cmd.distance("NonHBond", "resi 22 & chain A & name CB", "resi 17 & chain A & name CB")
cmd.distance("NonHBond", "resi 24 & chain A & name CB", "resi 15 & chain A & name CB")
cmd.distance("NonHBond", "resi 26 & chain A & name CB", "resi 13 & chain A & name CB")
cmd.distance("NonHBond", "resi 28 & chain A & name CB", "resi 11 & chain A & name CB")
cmd.show("stick", "barrel")
cmd.color("red","StrongHBond")
cmd.color("green","WeakHBond")
cmd.color("purpleblue","NonHBond")
cmd.color("magenta","PseudoR*")
cmd.color("green","name CA & barrel")
cmd.color("red","name O & barrel")
cmd.color("blue","name N & barrel")
cmd.hide("labels")
cmd.zoom("barrel")
