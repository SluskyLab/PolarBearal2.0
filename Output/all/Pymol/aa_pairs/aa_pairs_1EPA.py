from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1EPA.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.remove("hydrogens")
cmd.h_add("(name CA)")
cmd.select("Astrand0", "resi 13+14+15+16+17+18+19+20+21 & chain A ")


cmd.select("Astrand1", "resi 37+38+39+40+41+42+43+44 & chain A ")


cmd.select("Astrand2", "resi 47+48+49+50+51+52+53+54+55+56 & chain A ")


cmd.select("Astrand3", "resi 59+60+61+62+63+64+65+66+67+68+69 & chain A ")


cmd.select("Astrand4", "resi 75+76+77+78+79 & chain A ")


cmd.select("Astrand5", "resi 84+85+86+87+88+89+90+91+92 & chain A ")


cmd.select("Astrand6", "resi 97+98+99+100+101+102+103+104 & chain A ")


cmd.select("Astrand7", "resi 111+112+113+114+115+116+117+118 & chain A ")


cmd.group("Strands", "*strand*")
cmd.select("barrel", "Astrand*")
cmd.pseudoatom ("PseudoH40A", pos=[-3.117722,20.510225,8.877326])
cmd.pseudoatom ("PseudoH14A", pos=[-3.9515648,21.634848,11.057685])
cmd.pseudoatom ("PseudoH38A", pos=[-1.4750017,17.410646,15.135112])
cmd.pseudoatom ("PseudoH16A", pos=[-2.9396234,18.47885,16.665344])
cmd.pseudoatom ("PseudoH37A", pos=[2.3389993,15.731513,17.029696])
cmd.pseudoatom ("PseudoH52A", pos=[1.2449359,16.097824,10.606737])
cmd.pseudoatom ("PseudoH39A", pos=[-0.66918766,17.1637,10.839019])
cmd.pseudoatom ("PseudoH50A", pos=[-1.7509859,16.53564,4.8558])
cmd.pseudoatom ("PseudoH41A", pos=[-4.0733566,18.009686,5.3836837])
cmd.pseudoatom ("PseudoH48A", pos=[-5.2762337,16.295559,-0.16315138])
cmd.pseudoatom ("PseudoH43A", pos=[-5.8523173,18.785828,-1.0704577])
cmd.pseudoatom ("PseudoH66A", pos=[-0.6492494,13.556799,-0.050066918])
cmd.pseudoatom ("PseudoH49A", pos=[-0.9462617,15.969742,0.6566067])
cmd.pseudoatom ("PseudoH64A", pos=[3.6493258,15.618819,4.645751])
cmd.pseudoatom ("PseudoH51A", pos=[2.5666742,16.571138,6.2948885])
cmd.pseudoatom ("PseudoH62A", pos=[6.7643514,16.361307,10.535317])
cmd.pseudoatom ("PseudoH53A", pos=[5.3069725,15.484457,12.663216])
cmd.pseudoatom ("PseudoH60A", pos=[9.093655,15.328264,16.492556])
cmd.pseudoatom ("PseudoH55A", pos=[8.620581,13.466011,18.121843])
cmd.pseudoatom ("PseudoH78A", pos=[-0.9598081,7.5726495,-0.0881204])
cmd.pseudoatom ("PseudoH67A", pos=[-2.6524315,9.719315,-0.48971808])
cmd.pseudoatom ("PseudoH76A", pos=[-7.876271,7.490277,0.2678641])
cmd.pseudoatom ("PseudoH69A", pos=[-9.351675,8.88206,-1.4565518])
cmd.pseudoatom ("PseudoH75A", pos=[-10.514893,6.1893373,3.6047702])
cmd.pseudoatom ("PseudoH86A", pos=[-5.08876,3.6649103,3.3233688])
cmd.pseudoatom ("PseudoH77A", pos=[-4.299851,5.0171356,1.214776])
cmd.pseudoatom ("PseudoH84A", pos=[1.0562549,2.0656672,0.8021808])
cmd.pseudoatom ("PseudoH104A", pos=[-0.1131174,0.94312334,6.1544843])
cmd.pseudoatom ("PseudoH85A", pos=[-1.0907483,2.4131293,4.9975505])
cmd.pseudoatom ("PseudoH102A", pos=[-4.8974676,3.879204,8.625051])
cmd.pseudoatom ("PseudoH87A", pos=[-6.3799596,5.1963844,7.1951056])
cmd.pseudoatom ("PseudoH100A", pos=[-9.6656885,7.8112864,11.1267])
cmd.pseudoatom ("PseudoH89A", pos=[-11.537614,8.335098,9.646289])
cmd.pseudoatom ("PseudoH98A", pos=[-13.095596,12.614634,13.542445])
cmd.pseudoatom ("PseudoH92A", pos=[-15.675764,12.668383,14.172845])
cmd.pseudoatom ("PseudoH97A", pos=[-11.776504,16.210472,16.152756])
cmd.pseudoatom ("PseudoH116A", pos=[-8.771437,10.799162,16.925777])
cmd.pseudoatom ("PseudoH99A", pos=[-10.206473,9.613659,15.100588])
cmd.pseudoatom ("PseudoH114A", pos=[-6.1607685,4.7999353,14.285722])
cmd.pseudoatom ("PseudoH101A", pos=[-7.5641465,3.9902828,12.265404])
cmd.pseudoatom ("PseudoH112A", pos=[-3.1726277,-0.083681226,11.8537035])
cmd.pseudoatom ("PseudoH103A", pos=[-2.817588,-0.10673687,9.299618])
cmd.pseudoatom ("PseudoH113A", pos=[-2.9577427,2.1875648,15.572146])
cmd.pseudoatom ("PseudoH20A", pos=[-4.339101,7.270469,18.731577])
cmd.pseudoatom ("PseudoH115A", pos=[-5.2098145,8.164444,17.039429])
cmd.pseudoatom ("PseudoH17A", pos=[-4.3908424,14.305468,17.32914])
cmd.pseudoatom ("PseudoH117A", pos=[-6.60257,14.626554,16.467667])
cmd.pseudoatom ("PseudoH15A", pos=[-6.4762373,19.845562,14.316875])
cmd.group("Pseudo_Hydrogens", "PseudoH*")
cmd.pseudoatom ("PseudoR37A", pos=[1.1015507,14.415619,17.14297])
cmd.group("Pseudo_RGroups", "PseudoR*")
cmd.distance("StrongHBond", "resi 13 & chain A & name O", "resi 41 & chain A & name N")
cmd.distance("StrongHBond", "resi 13 & chain A & name N", "resi 41 & chain A & name O")
cmd.distance("StrongHBond", "resi 15 & chain A & name O", "resi 39 & chain A & name N")
cmd.distance("StrongHBond", "resi 15 & chain A & name N", "resi 39 & chain A & name O")
cmd.distance("StrongHBond", "resi 38 & chain A & name O", "resi 53 & chain A & name N")
cmd.distance("StrongHBond", "resi 38 & chain A & name N", "resi 53 & chain A & name O")
cmd.distance("StrongHBond", "resi 40 & chain A & name O", "resi 51 & chain A & name N")
cmd.distance("StrongHBond", "resi 40 & chain A & name N", "resi 51 & chain A & name O")
cmd.distance("StrongHBond", "resi 42 & chain A & name O", "resi 49 & chain A & name N")
cmd.distance("StrongHBond", "resi 42 & chain A & name N", "resi 49 & chain A & name O")
cmd.distance("StrongHBond", "resi 44 & chain A & name O", "resi 47 & chain A & name N")
cmd.distance("StrongHBond", "resi 44 & chain A & name N", "resi 47 & chain A & name O")
cmd.distance("StrongHBond", "resi 48 & chain A & name O", "resi 67 & chain A & name N")
cmd.distance("StrongHBond", "resi 48 & chain A & name N", "resi 67 & chain A & name O")
cmd.distance("StrongHBond", "resi 50 & chain A & name O", "resi 65 & chain A & name N")
cmd.distance("StrongHBond", "resi 50 & chain A & name N", "resi 65 & chain A & name O")
cmd.distance("StrongHBond", "resi 52 & chain A & name O", "resi 63 & chain A & name N")
cmd.distance("StrongHBond", "resi 52 & chain A & name N", "resi 63 & chain A & name O")
cmd.distance("StrongHBond", "resi 54 & chain A & name O", "resi 61 & chain A & name N")
cmd.distance("StrongHBond", "resi 54 & chain A & name N", "resi 61 & chain A & name O")
cmd.distance("StrongHBond", "resi 56 & chain A & name O", "resi 59 & chain A & name N")
cmd.distance("StrongHBond", "resi 56 & chain A & name N", "resi 59 & chain A & name O")
cmd.distance("StrongHBond", "resi 68 & chain A & name O", "resi 77 & chain A & name N")
cmd.distance("StrongHBond", "resi 68 & chain A & name N", "resi 77 & chain A & name O")
cmd.distance("StrongHBond", "resi 76 & chain A & name O", "resi 87 & chain A & name N")
cmd.distance("StrongHBond", "resi 76 & chain A & name N", "resi 87 & chain A & name O")
cmd.distance("StrongHBond", "resi 78 & chain A & name O", "resi 85 & chain A & name N")
cmd.distance("StrongHBond", "resi 78 & chain A & name N", "resi 85 & chain A & name O")
cmd.distance("StrongHBond", "resi 86 & chain A & name O", "resi 103 & chain A & name N")
cmd.distance("StrongHBond", "resi 86 & chain A & name N", "resi 103 & chain A & name O")
cmd.distance("StrongHBond", "resi 88 & chain A & name O", "resi 101 & chain A & name N")
cmd.distance("StrongHBond", "resi 88 & chain A & name N", "resi 101 & chain A & name O")
cmd.distance("StrongHBond", "resi 98 & chain A & name O", "resi 117 & chain A & name N")
cmd.distance("StrongHBond", "resi 98 & chain A & name N", "resi 117 & chain A & name O")
cmd.distance("StrongHBond", "resi 100 & chain A & name O", "resi 115 & chain A & name N")
cmd.distance("StrongHBond", "resi 100 & chain A & name N", "resi 115 & chain A & name O")
cmd.distance("StrongHBond", "resi 102 & chain A & name O", "resi 113 & chain A & name N")
cmd.distance("StrongHBond", "resi 102 & chain A & name N", "resi 113 & chain A & name O")
cmd.distance("StrongHBond", "resi 104 & chain A & name O", "resi 111 & chain A & name N")
cmd.distance("StrongHBond", "resi 104 & chain A & name N", "resi 111 & chain A & name O")
cmd.distance("StrongHBond", "resi 114 & chain A & name O", "resi 21 & chain A & name N")
cmd.distance("StrongHBond", "resi 114 & chain A & name N", "resi 21 & chain A & name O")
cmd.distance("StrongHBond", "resi 116 & chain A & name O", "resi 19 & chain A & name N")
cmd.distance("StrongHBond", "resi 116 & chain A & name N", "resi 19 & chain A & name O")
cmd.distance("StrongHBond", "resi 118 & chain A & name O", "resi 16 & chain A & name N")
cmd.distance("StrongHBond", "resi 118 & chain A & name N", "resi 16 & chain A & name O")
cmd.distance("WeakHBond", "resi 13 & chain A & name O", "PseudoH40A")
cmd.distance("WeakHBond", "resi 39 & chain A & name O", "PseudoH14A")
cmd.distance("WeakHBond", "resi 15 & chain A & name O", "PseudoH38A")
cmd.distance("WeakHBond", "resi 37 & chain A & name O", "PseudoH16A")
cmd.distance("WeakHBond", "resi 53 & chain A & name O", "PseudoH37A")
cmd.distance("WeakHBond", "resi 38 & chain A & name O", "PseudoH52A")
cmd.distance("WeakHBond", "resi 51 & chain A & name O", "PseudoH39A")
cmd.distance("WeakHBond", "resi 40 & chain A & name O", "PseudoH50A")
cmd.distance("WeakHBond", "resi 49 & chain A & name O", "PseudoH41A")
cmd.distance("WeakHBond", "resi 42 & chain A & name O", "PseudoH48A")
cmd.distance("WeakHBond", "resi 47 & chain A & name O", "PseudoH43A")
cmd.distance("WeakHBond", "resi 48 & chain A & name O", "PseudoH66A")
cmd.distance("WeakHBond", "resi 65 & chain A & name O", "PseudoH49A")
cmd.distance("WeakHBond", "resi 50 & chain A & name O", "PseudoH64A")
cmd.distance("WeakHBond", "resi 63 & chain A & name O", "PseudoH51A")
cmd.distance("WeakHBond", "resi 52 & chain A & name O", "PseudoH62A")
cmd.distance("WeakHBond", "resi 61 & chain A & name O", "PseudoH53A")
cmd.distance("WeakHBond", "resi 54 & chain A & name O", "PseudoH60A")
cmd.distance("WeakHBond", "resi 59 & chain A & name O", "PseudoH55A")
cmd.distance("WeakHBond", "resi 66 & chain A & name O", "PseudoH78A")
cmd.distance("WeakHBond", "resi 77 & chain A & name O", "PseudoH67A")
cmd.distance("WeakHBond", "resi 68 & chain A & name O", "PseudoH76A")
cmd.distance("WeakHBond", "resi 75 & chain A & name O", "PseudoH69A")
cmd.distance("WeakHBond", "resi 87 & chain A & name O", "PseudoH75A")
cmd.distance("WeakHBond", "resi 76 & chain A & name O", "PseudoH86A")
cmd.distance("WeakHBond", "resi 85 & chain A & name O", "PseudoH77A")
cmd.distance("WeakHBond", "resi 78 & chain A & name O", "PseudoH84A")
cmd.distance("WeakHBond", "resi 84 & chain A & name O", "PseudoH104A")
cmd.distance("WeakHBond", "resi 103 & chain A & name O", "PseudoH85A")
cmd.distance("WeakHBond", "resi 86 & chain A & name O", "PseudoH102A")
cmd.distance("WeakHBond", "resi 101 & chain A & name O", "PseudoH87A")
cmd.distance("WeakHBond", "resi 88 & chain A & name O", "PseudoH100A")
cmd.distance("WeakHBond", "resi 99 & chain A & name O", "PseudoH89A")
cmd.distance("WeakHBond", "resi 91 & chain A & name O", "PseudoH98A")
cmd.distance("WeakHBond", "resi 97 & chain A & name O", "PseudoH92A")
cmd.distance("WeakHBond", "resi 117 & chain A & name O", "PseudoH97A")
cmd.distance("WeakHBond", "resi 98 & chain A & name O", "PseudoH116A")
cmd.distance("WeakHBond", "resi 115 & chain A & name O", "PseudoH99A")
cmd.distance("WeakHBond", "resi 100 & chain A & name O", "PseudoH114A")
cmd.distance("WeakHBond", "resi 113 & chain A & name O", "PseudoH101A")
cmd.distance("WeakHBond", "resi 102 & chain A & name O", "PseudoH112A")
cmd.distance("WeakHBond", "resi 111 & chain A & name O", "PseudoH103A")
cmd.distance("WeakHBond", "resi 21 & chain A & name O", "PseudoH113A")
cmd.distance("WeakHBond", "resi 114 & chain A & name O", "PseudoH20A")
cmd.distance("WeakHBond", "resi 19 & chain A & name O", "PseudoH115A")
cmd.distance("WeakHBond", "resi 116 & chain A & name O", "PseudoH17A")
cmd.distance("WeakHBond", "resi 16 & chain A & name O", "PseudoH117A")
cmd.distance("WeakHBond", "resi 118 & chain A & name O", "PseudoH15A")
cmd.distance("NonHBond", "resi 14 & chain A & name CB", "resi 40 & chain A & name CB")
cmd.distance("NonHBond", "resi 16 & chain A & name CB", "resi 38 & chain A & name CB")
cmd.distance("NonHBond", "PseudoR37A", "resi 54 & chain A & name CB")
cmd.distance("NonHBond", "resi 39 & chain A & name CB", "resi 52 & chain A & name CB")
cmd.distance("NonHBond", "resi 41 & chain A & name CB", "resi 50 & chain A & name CB")
cmd.distance("NonHBond", "resi 43 & chain A & name CB", "resi 48 & chain A & name CB")
cmd.distance("NonHBond", "resi 49 & chain A & name CB", "resi 66 & chain A & name CB")
cmd.distance("NonHBond", "resi 51 & chain A & name CB", "resi 64 & chain A & name CB")
cmd.distance("NonHBond", "resi 53 & chain A & name CB", "resi 62 & chain A & name CB")
cmd.distance("NonHBond", "resi 55 & chain A & name CB", "resi 60 & chain A & name CB")
cmd.distance("NonHBond", "resi 67 & chain A & name CB", "resi 78 & chain A & name CB")
cmd.distance("NonHBond", "resi 69 & chain A & name CB", "resi 76 & chain A & name CB")
cmd.distance("NonHBond", "resi 75 & chain A & name CB", "resi 88 & chain A & name CB")
cmd.distance("NonHBond", "resi 77 & chain A & name CB", "resi 86 & chain A & name CB")
cmd.distance("NonHBond", "resi 79 & chain A & name CB", "resi 84 & chain A & name CB")
cmd.distance("NonHBond", "resi 85 & chain A & name CB", "resi 104 & chain A & name CB")
cmd.distance("NonHBond", "resi 87 & chain A & name CB", "resi 102 & chain A & name CB")
cmd.distance("NonHBond", "resi 89 & chain A & name CB", "resi 100 & chain A & name CB")
cmd.distance("NonHBond", "resi 92 & chain A & name CB", "resi 98 & chain A & name CB")
cmd.distance("NonHBond", "resi 97 & chain A & name CB", "resi 118 & chain A & name CB")
cmd.distance("NonHBond", "resi 99 & chain A & name CB", "resi 116 & chain A & name CB")
cmd.distance("NonHBond", "resi 101 & chain A & name CB", "resi 114 & chain A & name CB")
cmd.distance("NonHBond", "resi 103 & chain A & name CB", "resi 112 & chain A & name CB")
cmd.distance("NonHBond", "resi 115 & chain A & name CB", "resi 20 & chain A & name CB")
cmd.distance("NonHBond", "resi 117 & chain A & name CB", "resi 17 & chain A & name CB")
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
