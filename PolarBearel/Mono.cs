﻿/*
**  File: Mono.cs
**  Started: 
**  Contributors: Joanna Slusky, Meghan Franklin, Ryan Feehan
**  Overview: 
**
**  About: 
**
**  Last Edited: 
*/

using System;
using System.Collections.Generic;
using System.Linq;
using System.Numerics;
using betaBarrelProgram.BarrelStructures;
using System.Collections;
using System.IO;

namespace betaBarrelProgram
{
    namespace Mono
    {
        public class MonoProtein : Protein
        {
            public List<Chain> Chains { get; set; }
            /* public List<Chain> Chains = new List<BarrelStructures.Chain>(); */
            public int ChainCount { get; set; }
            public int totalResNum { get; set; }
            public string PdbName { get; set; }


            public MonoProtein(ref AtomParser.AtomCategory _myAtomCat, string PdbName)
            {
                /*this.Chains = new List<BarrelStructures.Chain>();*/
                this.ChainCount = 0;
                this.totalResNum = 0;
                this.PdbName = PdbName;
                this.Chains = new List<BarrelStructures.Chain>();

                for (int chainNum = 0; chainNum < _myAtomCat.chainAtomsList.Count; chainNum++)
                {
                    bool IsItProtein = false;
                    for (int atomNum = 0; atomNum < _myAtomCat.ChainAtomList[chainNum].cartnAtoms.Count; atomNum++)
                    {
                        if (_myAtomCat.ChainAtomList[chainNum].CartnAtoms[atomNum].atomName == "CA") IsItProtein = true;
                    }
                    if (IsItProtein == true)
                    {
                        Chain myChain = new Chain(ref _myAtomCat, chainNum, PdbName, true, Global.DB_DIR, false);
                        //Chain myChain = new Chain(ref _myAtomCat, chainNum, PdbName, false, Global.MONO_DB_DIR); //changed mono status for SS for solubles
                        this.Chains.Add(myChain);
                        this.ChainCount++;
                    }
                }
            }

            public MonoProtein(ref AtomParser.AtomCategory _myAtomCat, int chainNum, string PdbName)
            {
                this.ChainCount = 0;
                this.totalResNum = 0;
                this.PdbName = PdbName;
                this.Chains = new List<BarrelStructures.Chain>();
                BarrelStructures.Chain myChain = new BarrelStructures.Chain(ref _myAtomCat, chainNum, PdbName, true, Global.DB_DIR, false);
                this.Chains.Add(myChain);
            }

            public void translate(Vector3 translationCoords)
            {
                for (int chainCtr = 0; chainCtr < this.Chains.Count; chainCtr++)
                {
                    this.Chains[chainCtr].translate(translationCoords);
                }
            }
        }

        public class MonoBarrel : Barrel

        {
            public List<Strand> Strands { get; set; }
            public List<Vector3> NellipseCoords { get; set; }
            public List<Vector3> CellipseCoords { get; set; }
            public Vector3 Ncentroid { get; set; }
            public Vector3 Ccentroid { get; set; }
            public Vector3 Axis { get; set; }
            public bool Direction { get; set; }
            public double AvgTilt { get; set; }
            public double AvgTilt_even { get; set; }
            public double AvgTilt_odd { get; set; }
            public List<List<int>> protoBarrel { get; set; }
            public double AvgRadius { get; set; }
            public List<Res> LoopResies { get; set; }
            public string PdbName { get; set; }
            public string ChainName { get; set; }
            public List<double> StrandLength { get; set; }
            public Vector3 OriginalNcentroid { get; set; }
            public Vector3 OriginalCcentroid { get; set; }
            public Vector3 AxisVector { get; set; }
            public Vector3 NewCaxisPt { get; set; }
            public Vector3 OldCaxisPt { get; set; }
            public int ShearNum { get; set; }
            public List<double> PrevTwists { get; set; }
            public bool Success { get; set; }
            //public static string path = Global.OUTPUT_DIR;

            //barrel constructor 
            public MonoBarrel(Chain _myChain, Protein _myProtein)
            {
                this.Strands = new List<Strand>();
                this.ChainName = _myChain.ChainName;
                this.protoBarrel = new List<List<int>>();
                this.PdbName = _myChain.PdbName;
                this.Success = true;//need to actually check this at some point, but variable is currently only for all method
                string path = Global.OUTPUT_DIR;
                

                #region makeBarrel
                //Current method of defining strands
                createStrands(ref _myChain);
				//If DSSP definitions are important
	            /*foreach (Res Res1 in _myChain){
	                checkDSSPNeighs(Res1, ref _myChain);
				}*/
				/* commented out to work on 6H3I_A*/
                makeBarrelCircular(ref _myChain); // keeps out the beta strands that occlude the barrel
                removeNonBarrelRes(ref _myChain);

                if (PdbName.ToUpper() != "6H3I_A" && PdbName.ToUpper() != "6H3J")// the big guy (SprA) loses too much if passed threw the following code
                {
                    //twice for 2VQI
                    makeBarrelCircular(ref _myChain);
                    removeNonBarrelRes(ref _myChain);

                    //check the ends for inserting loops
                    setCEllipseCoords(ref _myChain);
                    setNEllipseCoords(ref _myChain);

                    this.Axis = this.Ccentroid - this.Ncentroid;

                    for (int strandCtr = 0; strandCtr < this.protoBarrel.Count; strandCtr++)
                    {// gets rid of loops that can bond with each other but go into the middle
                        double angle = (SharedFunctions.AngleBetween(_myChain.Residues[this.protoBarrel[strandCtr][0]].BackboneCoords["CA"] - _myChain.Residues[this.protoBarrel[strandCtr][1]].BackboneCoords["CA"], this.Axis));
                        double direction = SharedFunctions.AngleBetween(_myChain.Residues[this.protoBarrel[strandCtr][0]].BackboneCoords["CA"] - _myChain.Residues[this.protoBarrel[strandCtr][this.protoBarrel[strandCtr].Count - 1]].BackboneCoords["CA"], this.Axis);

                        while ((direction > 90 && angle < 105) || (angle > 75 && direction < 90))
                        {
                            this.protoBarrel[strandCtr].RemoveAt(0);
                            angle = (SharedFunctions.AngleBetween(_myChain.Residues[this.protoBarrel[strandCtr][0]].BackboneCoords["CA"] - _myChain.Residues[this.protoBarrel[strandCtr][1]].BackboneCoords["CA"], this.Axis));
                        }

                        double angle2 = (SharedFunctions.AngleBetween(_myChain.Residues[this.protoBarrel[strandCtr][this.protoBarrel[strandCtr].Count - 1]].BackboneCoords["CA"] - _myChain.Residues[this.protoBarrel[strandCtr][this.protoBarrel[strandCtr].Count - 2]].BackboneCoords["CA"], this.Axis));

                        while ((angle2 < 105 && direction < 90) || (angle2 > 75 && direction > 90))
                        {
                            this.protoBarrel[strandCtr].RemoveAt(this.protoBarrel[strandCtr].Count - 1);
                            angle2 = (SharedFunctions.AngleBetween(_myChain.Residues[this.protoBarrel[strandCtr][this.protoBarrel[strandCtr].Count - 1]].BackboneCoords["CA"] - _myChain.Residues[this.protoBarrel[strandCtr][this.protoBarrel[strandCtr].Count - 2]].BackboneCoords["CA"], this.Axis));
                        }
                    }
                }
           		//checkStrands is written to use protobarrel list before the strand list is created. 
				//checkStrandDefnsDSSP(ref _myChain);
                
				//redefine axis
                setCEllipseCoords(ref _myChain);
                setNEllipseCoords(ref _myChain);
                this.Axis = this.Ncentroid - this.Ccentroid;
                /*end of 6H3I_A commented out*/

                for (int strandCtr = 0; strandCtr < protoBarrel.Count; strandCtr++)
                {
                    Strand newStrand = new Strand(_myChain, protoBarrel[strandCtr][0], protoBarrel[strandCtr][protoBarrel[strandCtr].Count - 1], strandCtr);
                    this.Strands.Add(newStrand);
                }

                #endregion
                SharedFunctions.writePymolScriptForStrands(this.Strands, Global.OUTPUT_DIR, Global.DB_DIR, this.PdbName);// added to look at SprA

                #region Amino Acid Pair
                try
                {
                    SharedFunctions.AminoAcidPairs(this.Strands, Global.OUTPUT_DIR, Global.DB_DIR, this.PdbName);
                }
                catch (Exception exception)
                {
                    Console.WriteLine("Failed to make pairs");
                    string fileLocation = Global.OUTPUT_DIR + "AAPairErrorLog.txt";
                    using (StreamWriter file = new StreamWriter(fileLocation, append: true))
                    {
                        string newLine = this.PdbName + "\t" + exception.InnerException + exception.Message + "\t" + exception.StackTrace + "\t" + exception.Source + "\t" + exception.Data + "\n";
                        file.WriteLine(newLine);
                    }
                }
                #endregion


                #region Rotate barrel to z-axis
                this.AvgRadius = SharedFunctions.setRadius(this.Strands, this.Axis, this.Ccentroid, this.Ncentroid);
                setCEllipseCoords(ref _myChain);
                setNEllipseCoords(ref _myChain);

                this.AxisVector = SharedFunctions.getNormal(this.NellipseCoords, this.Ncentroid);

                this.OriginalCcentroid = this.Ccentroid;
                this.OriginalNcentroid = this.Ncentroid;
                this.NewCaxisPt = ((this.Ncentroid - this.Ccentroid).Length() * this.AxisVector) + this.Ncentroid;
                int axisDirection = 1;
                if ((this.NewCaxisPt - this.OriginalCcentroid).Length() > ((((this.Ncentroid - this.Ccentroid).Length() * -1 * this.AxisVector) + this.Ncentroid) - this.OriginalCcentroid).Length())
                {
                    axisDirection = -1;
                    this.NewCaxisPt = (((this.Ncentroid - this.Ccentroid).Length() * -1 * this.AxisVector) + this.Ncentroid);
                }

                this.Axis = this.NewCaxisPt - this.Ncentroid;
                this.OldCaxisPt = this.NewCaxisPt;
                this.rotateToZ(ref _myChain);

                if (this.Axis.Length() > 22.5) setBottom(ref _myChain);
                else centerZ(ref _myChain);

                rotate180(ref _myChain);

                setCEllipseCoords(ref _myChain);
                setNEllipseCoords(ref _myChain);

                this.AxisVector = SharedFunctions.getNormal(this.NellipseCoords, this.Ncentroid);
                this.NewCaxisPt = (axisDirection * (this.Ncentroid - this.Ccentroid).Length() * this.AxisVector) + this.Ncentroid;
                this.Axis = this.NewCaxisPt - this.Ncentroid;

                for (int strandCtr = 0; strandCtr < this.Strands.Count; strandCtr++)
                {
                    for (int resCtr = 0; resCtr < this.Strands[strandCtr].Residues.Count; resCtr++)
                    {
                        this.Strands[strandCtr].Residues[resCtr].Z = this.Strands[strandCtr].Residues[resCtr].BackboneCoords["CA"].Z;
                    }
                }
                #endregion

                SharedFunctions.setInOut(this.Strands, path, this.PdbName, this.Axis, this.Ccentroid, this.Ncentroid);

                /* ---------output information--------- */
	            this.StrandLength = SharedFunctions.getStrandLengths(this.Strands, path, this.PdbName);
                this.PrevTwists = SharedFunctions.writeTwists(this.Strands, Global.MONO_OUTPUT_DIR, this.PdbName);

                /*string fileLocation6 = path + "\\ZCoords\\XYZCoords_" + this.PdbName + ".txt";
	            using (System.IO.StreamWriter file = new System.IO.StreamWriter(fileLocation6))
	            {
	                string newLine = "Res" + "\t" + "Num" + "\t" + "Chain" + "\t" + "XYZcoords";
	                file.WriteLine(newLine);
	                foreach (Res res in _myChain)
	                {
	                    foreach (Atom atom in res)
	                    {
	                        if (atom.AtomName == "CA") file.WriteLine("{0}\t{1}\t{2}\t{3}\t{4}\t{5}", res.ThreeLetCode, res.SeqID, res.ChainName, atom.Coords.X, atom.Coords.Y, atom.Coords.Z);
	                    }
	                }
	            }*/
                string use_dir = path + "ZCoords";
                if (!System.IO.Directory.Exists(use_dir))
                {
                    System.IO.Directory.CreateDirectory(use_dir);
                }

                string fileLocation15 = path + "ZCoords/AllZCoords_" + this.PdbName + ".txt";
	            using (System.IO.StreamWriter file = new System.IO.StreamWriter(fileLocation15))
	            {
	                string newLine = "Res" + "\t" + "Num" + "\t" + "Strand" + "\t" + "Z-coord";
	                file.WriteLine(newLine);
	                foreach (Strand strand in this.Strands)
	                {
	                    foreach (Res res in strand)
	                    {
	                        foreach (Atom atom in res)
	                        {
	                            if (atom.AtomName == "CA") file.WriteLine("{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}", res.ThreeLetCode, res.SeqID, strand.StrandNum, strand.ChainName, atom.Coords.X, atom.Coords.Y, atom.Coords.Z);
	                        }
	                    }
	                }
	            }

	            //DSSP has to be used to define strands before the strands are created; although I could clear and recreate them if necessary...
	            //Dictionary<string, string> Loops = SharedFunctions.getLoopTurns(this.Strands, ref _myChain, path, this.PdbName);
                //SharedFunctions.writePymolScriptForLoops(Loops, Global.OUTPUT_DIR, Global.MACMONODBDIR, ref _myChain, this.PdbName);
                //SharedFunctions.findLoopsHBondingPartnersGeomOnly(Loops, Global.OUTPUT_DIR, ref _myChain, this.PdbName, false);

                //REMPVE// SharedFunctions.writePymolScriptForStrands(this.Strands, Global.OUTPUT_DIR, Global.DB_DIR, this.PdbName);
	            //writeAminoAcidsTypesToFile(ref _myChain, path);

	            SharedFunctions.setInOut(this.Strands, path, this.PdbName, this.Axis, this.Ccentroid, this.Ncentroid);

	            /*string fileLocation6 = path + "\\Renumb\\XYZCoords_" + this.PdbName + ".txt";
	            using (System.IO.StreamWriter file = new System.IO.StreamWriter(fileLocation6))
	            {
	                string newLine = "Res" + "\t" + "Num" + "\t" + "Chain" + "\t" + "XYZcoords";
	                file.WriteLine(newLine);
	                foreach (Res res in _myChain)
	                {
	                    foreach (Atom atom in res)
	                    {
	                        if (atom.AtomName == "CA") file.WriteLine("{0}\t{1}\t{2}\t{3}\t{4}\t{5}", res.ThreeLetCode, res.ResNum + 1, res.ChainName, atom.Coords.X, atom.Coords.Y, atom.Coords.Z);
	                    }
	                }
	            }*/

	            // make list of loop residues
	            //listLoopRes(ref _myChain);

	            //find shear number July 22, 2014
	            //int ShearNum = shearNum(ref _myChain);

	            //SharedFunctions.findNearestNeighbors(this.Strands, path, this.PdbName); //based on CA distances; this is needed for shear number determination now.
	            //getShearNum();
            
	            //SharedFunctions.findHBondingPartnersEnergy(this.Strands, path, this.PdbName); //SQRWL-like implementation of hydrogen bonding
	            //SharedFunctions.findNearNeighDistOnly(this.Strands, path, this.PdbName);
           
	            //Energy adds neighbors to res; geom and dist both add to atom; this section clears both sets of lists to be reformed by a different function.
	            /*foreach (Strand strand in this.Strands)
	            {
	                foreach (Res res in strand)
	                {
	                    res.SideChainNeighbors = new List<Res>();
	                    res.BackboneNeighbors = new List<Res>();
	                    foreach (Atom atom in res)
	                    {
	                        atom.SCSCNeighAtoms = new List<Atom>();
	                        atom.SCBBNeighAtoms = new List<Atom>();
	                        atom.BBNeighAtoms = new List<Atom>();
	                    }
	                }
	            }*/

	            //SharedFunctions.findHBondingPartnersGeomOnly(this.Strands, path, this.PdbName, false); //Modelling program-like implementation of hydrogen bonding
	            //SharedFunctions.findAllNearNeighDistOnly(this.Strands, path, this.PdbName, ref _myChain);
	            //this.Axis = this.Ccentroid - this.Ncentroid; //july3
	            this.AvgTilt = SharedFunctions.getTiltsByAA(this.Strands, path, this.PdbName, this.Axis, ref Global.AADict);
                this.Success = true;
	            //getTyrVector(path, ref _myChain);
            
            }

            public void createStrands(ref Chain _myChain)
            {

                List<int> myStrand1 = new List<int>();
                List<int> myStrand2 = new List<int>();
                List<int> myStrand3 = new List<int>();
                bool strandStart = false;
                int usually0 = 0;
                if (PdbName.ToUpper() == "3KVN") usually0 = 330;
                if (PdbName.ToUpper() == "3RFZ") usually0 = 110;
                if (PdbName.ToUpper() == "4EPA") usually0 = 120;
                if (PdbName.ToUpper() == "4QKY") usually0 = 180;
                if (PdbName.ToUpper() == "4K3B") usually0 = 400;
                if (PdbName.ToUpper() == "4K3C") usually0 = 150;
                if (PdbName.ToUpper() == "6SLJ") usually0 = 120;
                if (PdbName.ToUpper() == "6FOK") usually0 = 120;
                if (PdbName.Substring(0, 4).ToUpper() == "6WUT") usually0 = 70;
                //if (PdbName.ToUpper() == "6UCU") usually0 = 30;
                int usuallyEnd = _myChain.ResidueCount;
                if (PdbName.ToUpper() == "3RFZ") usuallyEnd = 603;
                if (PdbName.ToUpper() == "6UCU") usuallyEnd = _myChain.Residues.Count-10;//small helix at the end is added as strand, breaking check first w/ last

                for (int res1ctr = usually0; res1ctr < usuallyEnd; res1ctr++)
                {
                    Res Residue1 = _myChain.Residues[res1ctr];
                    for (int atomCtr1 = 0; atomCtr1 < Residue1.Atoms.Count; atomCtr1++)
                    {

                        if (Residue1.Atoms[atomCtr1].AtomName == "N" && Residue1.ThreeLetCode != "PRO")
                        {
                            Atom N = Residue1.Atoms[atomCtr1];
                            for (int res2ctr = usually0; res2ctr < usuallyEnd; res2ctr++)
                            {

                                if (Math.Abs(res2ctr - res1ctr) > 3)
                                {
                                    Res Residue2 = _myChain.Residues[res2ctr];
                                    for (int atomCtr2 = 0; atomCtr2 < Residue2.Atoms.Count; atomCtr2++)
                                    {
                                        if (Residue2.Atoms[atomCtr2].AtomName == "O")
                                        {
                                            Atom O = Residue2.Atoms[atomCtr2];
                                            double d = (O.Coords - N.Hydrogen).Length();
                                            //just using a distance cuttoff for now, not actually calculating hbond angles
                                            //if (d < 2.75)  
                                            //{
                                            //    double w = calculateHydrogenBond(N, O, d);
                                            //}
                                            // establish first two strands

                                            double minD = 2.75; //was 2.75 for 2013 bioinf paper;

                                            if (d < minD && (Residue1.SSType == "B" || Residue2.SSType == "B"))
                                            {
                                                //if (strandStart == false) firstRes = Residue1.SeqID;
                                                if (Residue1.Neighbors.Contains(Residue2.ResNum) == false) Residue1.Neighbors.Add(Residue2.ResNum);
                                                if (Residue2.Neighbors.Contains(Residue1.ResNum) == false) Residue2.Neighbors.Add(Residue1.ResNum);

                                                if (Math.Abs(Residue1.ResNum - Residue2.ResNum) < 75)
                                                {
                                                    if (myStrand1.Count > 0)
                                                    {
                                                        myStrand1.Sort();

                                                        for (int i = myStrand1[0]; i < myStrand1[myStrand1.Count - 1]; i++)
                                                        {
                                                            if (myStrand1.Contains(i) == false) myStrand1.Add(i);
                                                            myStrand1.Sort();
                                                        }
                                                    }
                                                    if (myStrand2.Count > 0)
                                                    {
                                                        myStrand2.Sort();


                                                        for (int i = myStrand2[0]; i < myStrand2[myStrand2.Count - 1]; i++)
                                                        {
                                                            if (myStrand2.Contains(i) == false) myStrand2.Add(i);
                                                            myStrand2.Sort();
                                                        }
                                                    }
                                                    if (myStrand3.Count > 0)
                                                    {
                                                        myStrand3.Sort();

                                                        for (int i = myStrand3[0]; i < myStrand3[myStrand3.Count - 1]; i++)
                                                        {
                                                            if (myStrand3.Contains(i) == false) myStrand3.Add(i);
                                                            myStrand3.Sort();
                                                        }
                                                    }
                                                    int lowerRes;
                                                    int higherRes;
                                                    if (Residue1.ResNum - Residue2.ResNum > 0)
                                                    {
                                                        lowerRes = Residue2.ResNum;
                                                        higherRes = Residue1.ResNum;
                                                    }
                                                    else
                                                    {
                                                        lowerRes = Residue1.ResNum;
                                                        higherRes = Residue2.ResNum;
                                                    }
                                                    if (strandStart == false)
                                                    {
                                                        if ((myStrand2.Contains(lowerRes) == true || myStrand2.Contains(lowerRes + 1) == true) || ((myStrand1.Count > 4 && myStrand2.Count > 4) && (lowerRes > myStrand1[myStrand1.Count - 1] && higherRes > myStrand2[myStrand2.Count - 1])))
                                                        {
                                                            strandStart = true;

                                                        }
                                                    }
                                                    if (strandStart == false)
                                                    {
                                                        //damage control
                                                        if (myStrand1.Count > 0 && (lowerRes > myStrand1[myStrand1.Count - 1] + 6 || lowerRes < myStrand1[0])) // less than 6 misses a bit of strand 1 in 3BS0
                                                        {
                                                            if (myStrand1.Count < 4) myStrand1.Clear();
                                                            else lowerRes = myStrand1[myStrand1.Count - 1];
                                                        }

                                                        if (myStrand2.Count > 0 && (higherRes > myStrand2[myStrand2.Count - 1] + 5 || higherRes < myStrand2[0] - 9)) // 8 is here because of a loop in 1E54
                                                        {
                                                            if (myStrand2.Count < 4) myStrand2.Clear();
                                                            else higherRes = myStrand2[myStrand2.Count - 1];
                                                        }

                                                        //

                                                        if (myStrand1.Contains(lowerRes) == false && myStrand2.Contains(lowerRes) == false) myStrand1.Add(lowerRes);
                                                        if (myStrand2.Contains(higherRes) == false && myStrand1.Contains(higherRes) == false) myStrand2.Add(higherRes);


                                                    }


                                                    if (strandStart == true)
                                                    {
                                                        if (lowerRes > myStrand2[myStrand2.Count - 1] && (myStrand3.Count == 0 || higherRes > myStrand3[myStrand3.Count - 1]))
                                                        {
                                                            if (myStrand3.Count > 0 && lowerRes < myStrand3[0] - 5) break; //some loop getting in the ways
                                                            List<int> newList = new List<int>();

                                                            for (int ctr = 0; ctr < myStrand1.Count; ctr++)
                                                            {
                                                                newList.Add(myStrand1[ctr]);
                                                            }

                                                            protoBarrel.Add(newList);
                                                            myStrand1.Clear();
                                                            for (int ctr = 0; ctr < myStrand2.Count; ctr++)
                                                            {
                                                                myStrand1.Add(myStrand2[ctr]);
                                                            }
                                                            myStrand2.Clear();
                                                            for (int ctr = 0; ctr < myStrand3.Count; ctr++)
                                                            {
                                                                myStrand2.Add(myStrand3[ctr]);
                                                            }
                                                            myStrand3.Clear();

                                                        }

                                                        if (lowerRes > myStrand1[myStrand1.Count - 1] || myStrand3.Count == 0 || higherRes > myStrand3[myStrand3.Count - 1])
                                                        {
                                                            if (myStrand2.Contains(lowerRes) == false && myStrand1.Contains(lowerRes) == false && myStrand3.Contains(lowerRes) == false) myStrand2.Add(lowerRes);
                                                            if (myStrand3.Contains(higherRes) == false && myStrand2.Contains(higherRes) == false && myStrand1.Contains(higherRes) == false) myStrand3.Add(higherRes);
                                                        }
                                                        else
                                                        {

                                                            if (protoBarrel.Count > 0 && lowerRes > protoBarrel[protoBarrel.Count - 1][protoBarrel[protoBarrel.Count - 1].Count - 1])
                                                            {
                                                                if (myStrand1.Contains(lowerRes) == false && myStrand2.Contains(lowerRes) == false && myStrand3.Contains(lowerRes) == false) myStrand1.Add(lowerRes);
                                                                if (myStrand2.Contains(higherRes) == false && myStrand1.Contains(higherRes) == false && myStrand3.Contains(higherRes) == false) myStrand2.Add(higherRes);
                                                            }
                                                        }
                                                    }

                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                } //end of going through each res and adding to barrel. 

                if (protoBarrel.Count > 4)

                {// go back through from the start of the final strand and make sure we got all of strand 1 and final strand
                    myStrand3.Sort();
                    for (int lastStrndResCtr = myStrand3[0]; lastStrndResCtr < usuallyEnd; lastStrndResCtr++)
                    {
                        if (_myChain.Residues[lastStrndResCtr].Neighbors.Count != 0)
                        {
                            for (int nCtr = 0; nCtr < _myChain.Residues[lastStrndResCtr].Neighbors.Count; nCtr++)
                            {
                                int neighbor = _myChain.Residues[lastStrndResCtr].Neighbors[nCtr];
                                if (neighbor < protoBarrel[1][0])
                                {
                                    if (protoBarrel[0].Contains(neighbor) == false) protoBarrel[0].Add(neighbor);
                                    if (myStrand3.Contains(lastStrndResCtr) == false) myStrand3.Add(lastStrndResCtr);
                                }
                            }
                        }
                    }
                    protoBarrel[0].Sort();


                    // now finish everything       
                    myStrand2.Sort();
                    myStrand1.Sort();
                    myStrand3.Sort();
                    protoBarrel.Add(myStrand1);
                    protoBarrel.Add(myStrand2);
                    protoBarrel.Add(myStrand3);

                }
                for (int x = 0; x < this.protoBarrel.Count; x++) { Console.WriteLine(x + "\t" + _myChain.Residues[this.protoBarrel[x][0]].SeqID + "\t" + _myChain.Residues[this.protoBarrel[x].Last()].SeqID); }

	            if (PdbName.ToUpper() == "3RBH" || PdbName.ToUpper() == "4AFK") //Added 4afk 6-22-17 as replacement in v4 for 3rbh
	            {
	                List<int> myStrand4 = new List<int>();
	                List<int> myStrand5 = new List<int>();
	                List<int> myStrand6 = new List<int>();
	                myStrand4.AddRange(Enumerable.Range(protoBarrel[4][0]-2, 7));
	                myStrand5.AddRange(Enumerable.Range(protoBarrel[4][20], 8));
	                myStrand6.AddRange(Enumerable.Range(protoBarrel[4][31], 9));
	                protoBarrel.RemoveRange(4, 1);
	                protoBarrel.Insert(4, myStrand6);
	                protoBarrel.Insert(4, myStrand5);
	                protoBarrel.Insert(4, myStrand4);
	            }

	            if (PdbName.ToUpper() == "2YNK")
	            {
	                myStrand1 = new List<int>();
	                myStrand1.AddRange(Enumerable.Range(protoBarrel[1][0], 10));
	                protoBarrel.Insert(1, myStrand1);
	                protoBarrel[2].RemoveRange(0, 10);
	            }
	            if (PdbName.ToUpper() == "4AIP")
	            {
	                myStrand1 = new List<int>();
	                myStrand1.AddRange(Enumerable.Range(protoBarrel[20][0], 12));
	                protoBarrel.Insert(20, myStrand1);
	                protoBarrel[21].RemoveRange(0, 12);
	            }
	            if (PdbName.ToUpper() == "2O4V")
	            {
	                protoBarrel[14].RemoveRange(0, 13);
	            }
	            if (PdbName.ToUpper() == "2X55") //added 6-22-17 for v4
	            {
	                protoBarrel[9].InsertRange(0, Enumerable.Range(protoBarrel[9][0]-4, 4));
	            }
	            if (PdbName.ToUpper() == "4FT6") //added 6-22-17 for v4
	            {
	                protoBarrel[2].RemoveRange(15, 5);
	            }
	            if (PdbName.ToUpper() == "4ZGV") //added 6-22-17 for v4
	            {
	                protoBarrel.RemoveRange(0, 2);
	                protoBarrel[8].RemoveRange(25, 23);
	                protoBarrel[9].RemoveRange(0, 5);

	                myStrand1 = new List<int>();
	                myStrand1.AddRange(Enumerable.Range(protoBarrel[15][0], 17));
	                protoBarrel.Insert(15, myStrand1);
	                protoBarrel[16].RemoveRange(0, 20);
	            }
	            if (PdbName.ToUpper() == "5FP1") //added 6-22-17 for v4
	            {
	                protoBarrel[7].RemoveRange(14, 9);
	                protoBarrel[8].RemoveRange(0, 22);
	            }
	            if (PdbName.Substring(0, 4).ToUpper() == "5FQ8") //added 6-22-17 for v4
	            {
                    //RYAN check why this failed later
	                protoBarrel[3].RemoveRange(27, 13);
	                protoBarrel[4].RemoveRange(0, 41);
                    protoBarrel[16].RemoveRange(0, protoBarrel[16].Count - 15);
                    protoBarrel[19].RemoveRange(13, 15);
	                protoBarrel.RemoveRange(20, 2);
	            }
	            if (PdbName.ToUpper() == "5FR8") //added 6-22-17 for v4
	            {
	                protoBarrel[19].RemoveRange(17, 32);
	            }
	            if (PdbName.ToUpper() == "3SY7") //added 6-22-17 for v4
	            {
	                protoBarrel[6].RemoveRange(9, 4);
	            }
	            if (PdbName.ToUpper() == "4FSP") //added 6-22-17 for v4
	            {
	                protoBarrel[6].RemoveRange(10, 4);
	            }
	            if (PdbName.ToUpper() == "5LDV") //added 6-22-17 for v4
	            {
	                protoBarrel[6].RemoveRange(11, 16);
	            }
	            if (PdbName.Substring(0, 4).ToUpper() == "5T3R") //added 6-22-17 for v4
	            {
	                protoBarrel.RemoveRange(19, 1);
	            }
	            if (PdbName.ToUpper() == "2MAF") //Added 2-17-17 for creating design scaffolds
	            {
	                protoBarrel[4].RemoveRange(12, 19);
	                protoBarrel[5].RemoveRange(0, 19);
	            }
	            if (PdbName.ToUpper() == "3DZM") //Added 2-17-17 for creating design scaffolds
	            {
	                protoBarrel[7].RemoveRange(0, 23);
               
	            }
	            if (PdbName.ToUpper() == "1FEP") //Added 6-5-17 for loop definitions
	            {
	                protoBarrel[16].RemoveRange(22, 10);
	            }
	            if (PdbName.ToUpper() == "3FIP") //Added 5-25-18 - this should have been fixed YEARS ago.
	            {
	                protoBarrel[5].RemoveRange(13, protoBarrel[5].Count-13);
	                protoBarrel[7].RemoveRange(0, 28);
	                protoBarrel.RemoveRange(6, 1);
	            }
	            if (PdbName.ToUpper() == "5M9B") //Added 5-25-18 for v5DB
	            {
	                protoBarrel[16].RemoveRange(22, 16);
	            }
	            if (PdbName.ToUpper() == "5MDO") //Added 5-25-18 for v5DB
	            {
	                protoBarrel[12].InsertRange(0, Enumerable.Range(protoBarrel[12][0]-3, 3));
	                protoBarrel[13].AddRange(Enumerable.Range(protoBarrel[13].Last(), 4));
	            }
                if (PdbName.ToUpper() == "6SLJ") //Added 12/17/20 for v6DB
                {
                    //TODO: clean up the strand edges before any loop analysis
                    protoBarrel[12].RemoveRange(0, protoBarrel[12].Count - 14);
                    protoBarrel[13].RemoveRange(12, protoBarrel[13].Count - 12);
                    protoBarrel[15].RemoveRange(15, protoBarrel[15].Count - 15);
                    protoBarrel[19].RemoveRange(9, protoBarrel[19].Count - 9);
                    protoBarrel.RemoveRange(16, 2);

                    myStrand1 = new List<int>();
                    myStrand1.AddRange(Enumerable.Range(protoBarrel[1][0], 11));
                    protoBarrel.Insert(1, myStrand1);
                }
                if (PdbName.ToUpper() == "6H3I_A")
                {
                    protoBarrel.RemoveRange(7, 10);
                    protoBarrel.RemoveRange(11, 9);
                    protoBarrel[26].RemoveRange(protoBarrel[26].Count - 3, 3);
                }
                if (PdbName.ToUpper() == "6H3J")
                {
                    protoBarrel.RemoveRange(7, 9);
                    protoBarrel.RemoveRange(11, 7);
                    protoBarrel[6].RemoveRange(8, protoBarrel[6].Count - 8);
                }


                // re print strands to check changes
                for (int x = 0; x < this.protoBarrel.Count; x++) { Console.WriteLine(x + "\t" + _myChain.Residues[this.protoBarrel[x][0]].SeqID + "\t" + _myChain.Residues[this.protoBarrel[x].Last()].SeqID); }

            }//End of CreateStrands

            public void checkStrandDefnsDSSP(ref Chain _myChain) //Added 6-5-17 for loops
	        {
	            for (int strandNum = 0; strandNum < this.protoBarrel.Count; strandNum ++)
	            {
	                //Remove turn residues
	                while (_myChain.Residues[this.protoBarrel[strandNum][0]].DSSP == "T")
	                {
	                    int removed_res = _myChain.Residues[this.protoBarrel[strandNum][0]].ResNum;
	                    this.protoBarrel[strandNum].RemoveAt(0);
	                    Console.WriteLine("Removed res{1} from beg of strand {0}", strandNum, removed_res);
	                }

	                while (_myChain.Residues[this.protoBarrel[strandNum].Last()].DSSP == "T")
	                {
	                    int removed_res = _myChain.Residues[this.protoBarrel[strandNum].Last()].ResNum;
	                    this.protoBarrel[strandNum].RemoveAt(this.protoBarrel[strandNum].Count - 1);
	                    Console.WriteLine("Removed res{1} from end of strand {0}", strandNum, removed_res);
	                }


	                //Add to the beginning of strands
	                try
	                {
	                    while (_myChain.Residues[this.protoBarrel[strandNum][0] - 1].DSSP == "E")
	                    {
	                        try
	                        {
	                            if (this.protoBarrel[strandNum][0] - 1 > this.protoBarrel[strandNum - 1].Last() + 1)
	                            {
	                                this.protoBarrel[strandNum].Add(_myChain.Residues[this.protoBarrel[strandNum][0] - 1].ResNum);
	                                //checkDSSPNeighs(_myChain.Residues[this.protoBarrel[strandNum][0] - 1], ref _myChain);
	                                Console.WriteLine("added res{1} to beg of strand {0}", strandNum, _myChain.Residues[this.protoBarrel[strandNum][0] - 1].ResNum);
	                                this.protoBarrel[strandNum].Sort();
	                            }
	                            else { break;  }
	                        }
	                        catch (ArgumentOutOfRangeException) { Console.WriteLine("Ran into prev strand"); break; }
                        
	                    }
	                }
	                catch (ArgumentOutOfRangeException) { continue; }

	                //For adding to the ends of strands
	                try
	                {
	                    while (_myChain.Residues[this.protoBarrel[strandNum].Last() + 1].DSSP == "E")
	                    {
	                        try
	                        {
	                            if (this.protoBarrel[strandNum].Last() + 1 < this.protoBarrel[strandNum + 1][0] - 1)
	                            {
	                                this.protoBarrel[strandNum].Add(_myChain.Residues[this.protoBarrel[strandNum].Last() + 1].ResNum);
	                                //checkDSSPNeighs(_myChain.Residues[this.protoBarrel[strandNum].Last() + 1], ref _myChain);
	                                Console.WriteLine("added res{1} to end of strand {0}", strandNum, _myChain.Residues[this.protoBarrel[strandNum].Last() + 1].ResNum);
	                                this.protoBarrel[strandNum].Sort();
	                            }
	                            else { break;  }
	                        }
	                        catch (ArgumentOutOfRangeException) { Console.WriteLine("Ran into next strand"); break; }
	                    }
	                }
	                catch (ArgumentOutOfRangeException) { continue; }
	            }

	        }

	        public void checkDSSPNeighs(Res Res1, ref Chain _myChain) //Added 6-5-17 for loops
	        {
	            double minD = 2.75;

	            foreach (Res Res2 in _myChain)
	            {
	                if (Math.Abs(Res1.SeqID - Res2.SeqID) > 2)
	                {
	                    double d = (Res1.Atoms[0].Hydrogen - Res2.BackboneCoords["O"]).Length();
	                    if (d < minD && (Res2.SSType == "B" || Res2.DSSP == "E"))
	                    {
	                        if (Res1.Neighbors.Contains(Res2.ResNum) == false) Res1.Neighbors.Add(Res2.ResNum);
	                        if (Res2.Neighbors.Contains(Res1.ResNum) == false) Res2.Neighbors.Add(Res1.ResNum);
	                    }
	                }
	            }                       
	        }

            // this will calculate the shear number of the beta barrel.  see murzin lesk and chothia 1994 http://www.mrc-lmb.cam.ac.uk/tcb/pdf/chc/97_jmb_236_1369_94.pdf
            public int shearNum(ref Chain _myChain)
            {
                string filelocation = Global.OUTPUT_DIR + "ShearNum_" + PdbName + ".txt";
                using (System.IO.StreamWriter file = new System.IO.StreamWriter(filelocation))
                {
                    // first determine nearest hbonding neighbor with N coming from N-term  (arbitrary)           
                    for (int strandCtr = 0; strandCtr < this.Strands.Count(); strandCtr++)
                    {
                        int strand2 = strandCtr + 1;
                        if (strandCtr == this.Strands.Count() - 1) strand2 = 0;

                        for (int resCtr = 0; resCtr < this.Strands[strandCtr].Residues.Count(); resCtr++)
                        {

                            Res firstRes = this.Strands[strandCtr].Residues[resCtr];
                            double minD = 3.4;
                            if (firstRes.Atoms[0].AtomName == "N" && firstRes.ThreeLetCode != "PRO")
                            {
                                Atom firstAtom = firstRes.Atoms[0];

                                for (int resCtr2 = 0; resCtr2 < this.Strands[strand2].Residues.Count(); resCtr2++)
                                {
                                    Atom secondAtom = this.Strands[strand2].Residues[resCtr2].Atoms[3];
                                    if (secondAtom.AtomName == "O")
                                    {
                                        double d = (secondAtom.Coords - firstAtom.Coords).Length();
                                        if (d < minD)
                                        {
                                            minD = d;
                                            firstRes.h_bonder = this.Strands[strand2].Residues[resCtr2].ResNum;
                                            firstRes.h_bonderID = this.Strands[strand2].Residues[resCtr2].SeqID;
                                            firstRes.bDist = (this.Strands[strand2].Residues[resCtr2].Atoms[1].Coords - firstRes.Atoms[1].Coords).Length();
                                        }

                                    }

                                }


                            }
                            // looking at o=n as well just to be safe... 
                            if (firstRes.h_bonder == 0 && firstRes.Atoms[3].AtomName == "O")
                            {
                                Atom firstAtom = firstRes.Atoms[3];

                                for (int resCtr2 = 0; resCtr2 < this.Strands[strand2].Residues.Count(); resCtr2++)
                                {
                                    Atom secondAtom = this.Strands[strand2].Residues[resCtr2].Atoms[0];
                                    if (secondAtom.AtomName == "N")
                                    {
                                        double d = (secondAtom.Coords - firstAtom.Coords).Length();

                                        if (d < minD)
                                        {
                                            minD = d;
                                            firstRes.h_bonder = this.Strands[strand2].Residues[resCtr2].ResNum;
                                            firstRes.h_bonderID = this.Strands[strand2].Residues[resCtr2].SeqID;
                                            firstRes.bDist = (this.Strands[strand2].Residues[resCtr2].Atoms[1].Coords - firstRes.Atoms[1].Coords).Length();
                                        }
                                    }
                                }
                            }
                            if (firstRes.h_bonder == 0) file.WriteLine("strand {0} res {1} has no partner!", strandCtr, firstRes.SeqID);
                            else file.WriteLine("strand {0} res {1}s partner is {2}; k = {3}", strandCtr, firstRes.SeqID, firstRes.h_bonderID, firstRes.ResStrandNum);
                        }
                    }
                    return 1;
                }
            }

            public void getShearNum() //7-11-16 MWF; produces an integer for shear number.
            {
                int shearNum = 0;
                int k = 0; int l = 0; int j = 0; int m = 0;
                int StrandNum1; int StrandNum2; int StrandNum0 = 0;
                string filelocation = Global.OUTPUT_DIR + "ShearNum/ShearNum_" + PdbName + ".txt";
                using (System.IO.StreamWriter file = new System.IO.StreamWriter(filelocation))
                {
                    int res_num = 0;
                    Res first_res = this.Strands[0].Residues[res_num];
                    Res next_res = this.Strands[0].Residues[res_num];
                    Res prev_res = this.Strands[0].Residues[res_num];
                    StrandNum1 = first_res.StrandNum;
                    if (this.Strands[StrandNum1].Residues.Last().Z < this.Strands[StrandNum1].Residues[0].Z) k = this.Strands[StrandNum1].Count() - first_res.ResStrandNum;
                    else k = first_res.ResStrandNum;
                    while (StrandNum1 < this.Strands.Count - 1)
                    {
                        if (first_res.ShearNumNeigh == null)
                        {
                            file.WriteLine("End of seq, restarting");
                            prev_res = first_res;
                            m = l;

                            //If a residue with no neighbors is reached - strand sticks up and need a new residue to restart; go to opposite end of strand and work back towards this residue
                            bool dir = false;
                            if (first_res.ResStrandNum > this.Strands[StrandNum1].Count() / 2)
                            {
                                res_num = 0;
                                dir = true;
                            }
                            else res_num = this.Strands[StrandNum1].Residues.Count() - 1;

                            while (first_res.ShearNumNeigh == null)
                            {
                                if (dir == true)
                                {
                                    res_num += 1;
                                    first_res = this.Strands[StrandNum1].Residues[res_num];
                                }
                                else
                                {
                                    res_num -= 1;
                                    first_res = this.Strands[StrandNum1].Residues[res_num];
                                }
                            }

                            StrandNum1 = first_res.StrandNum;
                            if (this.Strands[StrandNum1].Residues.Last().Z < this.Strands[StrandNum1].Residues[0].Z) j = this.Strands[StrandNum1].Count() - first_res.ResStrandNum;
                            else j = first_res.ResStrandNum;

                            file.WriteLine("{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}", prev_res.SeqID, prev_res.StrandNum, m, first_res.SeqID, first_res.StrandNum, j, m - j);
                            shearNum += j - m;
                        }

                        if (this.Strands[StrandNum1].Residues.Last().Z < this.Strands[StrandNum1].Residues[0].Z) j = this.Strands[StrandNum1].Count() - first_res.ResStrandNum;
                        else j = first_res.ResStrandNum;

                        next_res = first_res.ShearNumNeigh;
                        StrandNum2 = next_res.StrandNum;
                        if (this.Strands[StrandNum2].Residues.Last().Z < this.Strands[StrandNum2].Residues[0].Z) l = this.Strands[StrandNum2].Count() - next_res.ResStrandNum;
                        else l = next_res.ResStrandNum;

                        file.WriteLine("{0}\t{1}\t{2}\t{3}\t{4}\t{5}", first_res.SeqID, first_res.StrandNum, j, next_res.SeqID, next_res.StrandNum, l);
                        prev_res = first_res;
                        StrandNum0 = prev_res.StrandNum;
                        m = j;
                        first_res = next_res;
                        StrandNum1 = first_res.StrandNum;

                    }
                    if (StrandNum1 == this.Strands.Count - 1)
                    {
                        if (first_res.ShearNumNeigh == null)
                        {
                            file.WriteLine("End of seq, restarting");
                            prev_res = first_res;
                            m = l;

                            //If a residue with no neighbors is reached - strand sticks up and need a new residue to restart; go to opposite end of strand and work back towards this residue
                            bool dir = false;
                            if (first_res.ResStrandNum > this.Strands[StrandNum1].Count() / 2)
                            {
                                res_num = 0;
                                dir = true;
                            }
                            else res_num = this.Strands[StrandNum1].Residues.Count() - 1;

                            while (first_res.ShearNumNeigh == null)
                            {
                                if (dir == true)
                                {
                                    res_num += 1;
                                    first_res = this.Strands[StrandNum1].Residues[res_num];
                                }
                                else
                                {
                                    res_num -= 1;
                                    first_res = this.Strands[StrandNum1].Residues[res_num];
                                }
                            }

                            StrandNum1 = first_res.StrandNum;
                            if (this.Strands[StrandNum1].Residues.Last().Z < this.Strands[StrandNum1].Residues[0].Z) j = this.Strands[StrandNum1].Count() - first_res.ResStrandNum;
                            else j = first_res.ResStrandNum;

                            file.WriteLine("{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}", prev_res.SeqID, prev_res.StrandNum, m, first_res.SeqID, first_res.StrandNum, j, m - j);
                            shearNum += j - m;
                        }

                        if (this.Strands[StrandNum1].Residues.Last().Z < this.Strands[StrandNum1].Residues[0].Z) j = this.Strands[StrandNum1].Count() - first_res.ResStrandNum;
                        else j = first_res.ResStrandNum;

                        next_res = first_res.ShearNumNeigh;
                        StrandNum2 = next_res.StrandNum;
                        if (this.Strands[StrandNum2].Residues.Last().Z < this.Strands[StrandNum2].Residues[0].Z) l = this.Strands[StrandNum2].Count() - next_res.ResStrandNum;
                        else l = next_res.ResStrandNum;

                        file.WriteLine("End of seq");
                        file.WriteLine("{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}", first_res.SeqID, first_res.StrandNum, j, next_res.SeqID, next_res.StrandNum, l, Math.Abs(l - k));
                        shearNum += Math.Abs(l - k);
                        this.ShearNum = shearNum;
                    }


                }
            }

            public void rotate180(ref Chain _myChain)
            {
                double phi = Math.PI;
                Matrix4x4 rotationMatrixY2 = new Matrix4x4((float)Math.Cos(phi), 0, (float)Math.Sin(phi), 0,
                                                         0, 1, 0, 0,
                                                           (float)(-1 * Math.Sin(phi)), 0, (float)Math.Cos(phi),
                                                         0, 0, 0, 0, 0);

                for (int resCtr = 0; resCtr < _myChain.Residues.Count; resCtr++)
                {
                    for (int atomCtr = 0; atomCtr < _myChain.Residues[resCtr].Atoms.Count; atomCtr++)
                    {
                        _myChain.Residues[resCtr].Atoms[atomCtr].Coords = Vector3.Transform(_myChain.Residues[resCtr].Atoms[atomCtr].Coords, rotationMatrixY2);
                        if (_myChain.Residues[resCtr].Atoms[atomCtr].AtomName == "CA" || _myChain.Residues[resCtr].Atoms[atomCtr].AtomName == "C" || _myChain.Residues[resCtr].Atoms[atomCtr].AtomName == "N" || _myChain.Residues[resCtr].Atoms[atomCtr].AtomName == "O")
                        {

                            _myChain.Residues[resCtr].BackboneCoords[_myChain.Residues[resCtr].Atoms[atomCtr].AtomName] = _myChain.Residues[resCtr].Atoms[atomCtr].Coords;
                        }
                    }
                }
            }

            public void setBottom(ref Chain _myChain)
            {
                double adjuster = 12.5;
                //double adjuster = .0962 * this.Axis.Length() + 8.3358;
                //double adjuster = 11.75;
                // if (this.Axis.Length() < 30) adjuster = 11;
                // if (this.Axis.Length() > 40) adjuster = 12.75;
                double adjustment = adjuster - this.Ncentroid.Z;

                for (int resCtr = 0; resCtr < _myChain.Residues.Count; resCtr++)
                {
                    for (int atomCtr = 0; atomCtr < _myChain.Residues[resCtr].Atoms.Count; atomCtr++)
                    {

                        Vector3 newCoords = new Vector3(_myChain.Residues[resCtr].Atoms[atomCtr].Coords.X, _myChain.Residues[resCtr].Atoms[atomCtr].Coords.Y, (float)(_myChain.Residues[resCtr].Atoms[atomCtr].Coords.Z + (adjustment)));
                        _myChain.Residues[resCtr].Atoms[atomCtr].Coords = newCoords;


                        if (_myChain.Residues[resCtr].Atoms[atomCtr].AtomName == "CA" || _myChain.Residues[resCtr].Atoms[atomCtr].AtomName == "C" || _myChain.Residues[resCtr].Atoms[atomCtr].AtomName == "N" || _myChain.Residues[resCtr].Atoms[atomCtr].AtomName == "O")
                        {

                            _myChain.Residues[resCtr].BackboneCoords[_myChain.Residues[resCtr].Atoms[atomCtr].AtomName] = _myChain.Residues[resCtr].Atoms[atomCtr].Coords;
                        }
                    }
                }
            }

            public void centerZ(ref Chain _myChain)
            {
                /* double avgZ = 0;
                 int totalRes = 0;
                 for (int strandCtr = 0; strandCtr < this.Strands.Count; strandCtr++)
                 {
                     for (int resCtr = 0; resCtr < this.Strands[strandCtr].Residues.Count; resCtr++)
                     {
                         avgZ = avgZ + this.Strands[strandCtr].Residues[resCtr].BackboneCoords["CA"].Z;
                         totalRes++;
                     }
                 }
                 avgZ = avgZ / totalRes;
                 */
                double avgZ = (this.Ncentroid.Z + this.Ccentroid.Z) / 2;

                for (int resCtr = 0; resCtr < _myChain.Residues.Count; resCtr++)
                {
                    for (int atomCtr = 0; atomCtr < _myChain.Residues[resCtr].Atoms.Count; atomCtr++)
                    {

                        Vector3 newCoords = new Vector3(_myChain.Residues[resCtr].Atoms[atomCtr].Coords.X, _myChain.Residues[resCtr].Atoms[atomCtr].Coords.Y, (float)(_myChain.Residues[resCtr].Atoms[atomCtr].Coords.Z - (avgZ)));
                        _myChain.Residues[resCtr].Atoms[atomCtr].Coords = newCoords;


                        if (_myChain.Residues[resCtr].Atoms[atomCtr].AtomName == "CA" || _myChain.Residues[resCtr].Atoms[atomCtr].AtomName == "C" || _myChain.Residues[resCtr].Atoms[atomCtr].AtomName == "N" || _myChain.Residues[resCtr].Atoms[atomCtr].AtomName == "O")
                        {

                            _myChain.Residues[resCtr].BackboneCoords[_myChain.Residues[resCtr].Atoms[atomCtr].AtomName] = _myChain.Residues[resCtr].Atoms[atomCtr].Coords;
                        }
                    }
                }


            }

            public void listLoopRes(ref Chain _myChain)
            {

                string fileLocation = Global.OUTPUT_DIR + "\\Loop_out_" + this.PdbName + ".py";
                using (System.IO.StreamWriter file = new System.IO.StreamWriter(fileLocation))
                {

                    file.WriteLine("from pymol import cmd, stored");
                    this.LoopResies = new List<Res>();
                    if (this.Strands.Count > 0 && this.Strands[0].Residues[0].ResNum < 18)
                    {
                        file.WriteLine("cmd.select(\"loopFirst\", \"resi {0}-{1} & chain{2}\")", _myChain.Residues[0].SeqID, this.Strands[0].Residues[0].SeqID, this.ChainName);
                        file.WriteLine("cmd.color ( \"salmon\", \"loopFirst\")");
                        for (int resCtr = _myChain.Residues[0].ResNum; resCtr < this.Strands[0].Residues[0].ResNum; resCtr++)
                        {
                            _myChain.Residues[resCtr].Z = _myChain.Residues[resCtr].BackboneCoords["CA"].Z;
                            _myChain.Residues[resCtr].Inward = false;
                            this.LoopResies.Add(_myChain.Residues[resCtr]);
                        }
                    }

                    if (_myChain.Residues[_myChain.Residues.Count - 1].ResNum - this.Strands[this.Strands.Count - 1].Residues[this.Strands[this.Strands.Count - 1].Residues.Count - 1].ResNum < 18)
                    {
                        file.WriteLine("cmd.select(\"loopLast\", \"resi {0}-{1} & chain{2}\")", this.Strands[this.Strands.Count - 1].Residues[this.Strands[this.Strands.Count - 1].Residues.Count - 1].SeqID, _myChain.Residues[_myChain.Residues.Count - 1].SeqID, this.ChainName);
                        file.WriteLine("cmd.color ( \"salmon\", \"loopLast\")");
                        for (int resCtr = _myChain.Residues[0].ResNum; resCtr < this.Strands[0].Residues[0].ResNum; resCtr++)
                        {
                            _myChain.Residues[resCtr].Z = _myChain.Residues[resCtr].BackboneCoords["CA"].Z;
                            _myChain.Residues[resCtr].Inward = false;
                            this.LoopResies.Add(_myChain.Residues[resCtr]);
                        }
                    }
                    for (int strandCtr = 0; strandCtr < this.Strands.Count - 1; strandCtr++)
                    {

                        int loopLength = this.Strands[strandCtr + 1].Residues[0].ResNum - this.Strands[strandCtr].Residues[this.Strands[strandCtr].Residues.Count - 1].ResNum;
                        //Console.WriteLine("LoopLength = {0}", loopLength);
                        if (loopLength < 18)
                        {

                            file.WriteLine("cmd.select(\"loop{0}\", \"resi {1}-{2} & chain{3}\")", strandCtr, this.Strands[strandCtr].Residues[this.Strands[strandCtr].Residues.Count - 1].SeqID, this.Strands[strandCtr + 1].Residues[0].SeqID, this.ChainName);
                            file.WriteLine("cmd.color ( \"salmon\", \"loop{0}\")", strandCtr);
                            for (int resCtr = this.Strands[strandCtr].Residues[this.Strands[strandCtr].Residues.Count - 1].ResNum + 1; resCtr < this.Strands[strandCtr + 1].Residues[0].ResNum; resCtr++)
                            {
                                _myChain.Residues[resCtr].Z = _myChain.Residues[resCtr].BackboneCoords["CA"].Z;
                                //double direction = SharedFunctions.AngleBetween(_myChain.Residues[resCtr].Direction, this.Axis);
                                //Res myRes = _myChain.Residues[resCtr];
                                //double angle = SharedFunctions.AngleBetween(myRes.BackboneCoords["CA"] - ((myRes.BackboneCoords["N"] + myRes.BackboneCoords["C"]) / 2), this.Axis);
                                //if (direction > 150)
                                //{
                                //    if (angle > 90)
                                //    {
                                //        myRes.Inward = true;
                                //        Console.WriteLine("resi {0} is inward", myRes.SeqID);
                                //    }
                                //    else myRes.Inward = false;
                                //}
                                //else if (direction < 30)
                                //{
                                //    if (angle < 90)
                                //    {
                                //        myRes.Inward = true;
                                //        Console.WriteLine("resi {0} is inward", myRes.SeqID);
                                //    }
                                //    else myRes.Inward = false;
                                //}
                                //else myRes.Inward = false;
                                _myChain.Residues[resCtr].Inward = false;
                                this.LoopResies.Add(_myChain.Residues[resCtr]);

                            }
                        }
                        else if (loopLength < 50)
                        {
                            bool enteringBarrel = false;

                            Vector3 direction = new Vector3();
                            direction = this.Strands[strandCtr].Residues[this.Strands[strandCtr].Residues.Count - 1].BackboneCoords["CA"] - this.Strands[strandCtr].Residues[0].BackboneCoords["CA"];
                            double angle = SharedFunctions.AngleBetween(this.Axis, direction);


                            if (angle < 90 && this.Ccentroid.Z > 0)
                            {
                                for (int resCtr = this.Strands[strandCtr].Residues[this.Strands[strandCtr].Residues.Count - 1].ResNum + 1; resCtr < this.Strands[strandCtr + 1].Residues[0].ResNum; resCtr++)
                                {
                                    double lowestZ = this.Ccentroid.Z;
                                    if (_myChain.Residues[resCtr].BackboneCoords["CA"].Z < lowestZ - 6)
                                    {
                                        enteringBarrel = true;
                                        break;
                                    }
                                }
                            }
                            else if (angle < 90 && this.Ccentroid.Z < 0)
                            {
                                for (int resCtr = this.Strands[strandCtr].Residues[this.Strands[strandCtr].Residues.Count - 1].ResNum + 1; resCtr < this.Strands[strandCtr + 1].Residues[0].ResNum; resCtr++)
                                {
                                    double highestZ = this.Ccentroid.Z;
                                    if (_myChain.Residues[resCtr].BackboneCoords["CA"].Z > highestZ + 6)
                                    {
                                        enteringBarrel = true;
                                        break;
                                    }
                                }
                            }
                            else if (angle > 90 && this.Ncentroid.Z < 0)
                            {
                                for (int resCtr = this.Strands[strandCtr].Residues[this.Strands[strandCtr].Residues.Count - 1].ResNum + 1; resCtr < this.Strands[strandCtr + 1].Residues[0].ResNum; resCtr++)
                                {
                                    double highestZ = this.Ncentroid.Z;
                                    if (_myChain.Residues[resCtr].BackboneCoords["CA"].Z > highestZ + 3)
                                    {
                                        enteringBarrel = true;
                                        break;
                                    }
                                }
                            }
                            else if (angle > 90 && this.Ncentroid.Z > 0)
                            {
                                for (int resCtr = this.Strands[strandCtr].Residues[this.Strands[strandCtr].Residues.Count - 1].ResNum + 1; resCtr < this.Strands[strandCtr + 1].Residues[0].ResNum; resCtr++)
                                {
                                    double lowestZ = this.Ncentroid.Z;
                                    if (_myChain.Residues[resCtr].BackboneCoords["CA"].Z < lowestZ - 6)
                                    {
                                        enteringBarrel = true;
                                        break;
                                    }
                                }
                            }

                            if (enteringBarrel == false)
                            {
                                file.WriteLine("cmd.select(\"loop{0}\", \"resi {1}-{2} & chain{3}\")", strandCtr, this.Strands[strandCtr].Residues[this.Strands[strandCtr].Residues.Count - 1].SeqID, this.Strands[strandCtr + 1].Residues[0].SeqID, this.ChainName);
                                file.WriteLine("cmd.color ( \"salmon\", \"loop{0}\")", strandCtr);
                                for (int resCtr = this.Strands[strandCtr].Residues[this.Strands[strandCtr].Residues.Count - 1].ResNum + 1; resCtr < this.Strands[strandCtr + 1].Residues[0].ResNum; resCtr++)
                                {
                                    _myChain.Residues[resCtr].Z = _myChain.Residues[resCtr].BackboneCoords["CA"].Z;

                                    _myChain.Residues[resCtr].Inward = false;
                                    this.LoopResies.Add(_myChain.Residues[resCtr]);
                                }
                            }
                        }

                    }
                }
            }

            public void rotateToZ(ref Chain _myChain)
            {
                double length = this.Axis.Length();

                double psi = Math.Atan(this.Axis.Y / this.Axis.X);
                if (0 == this.Axis.X) { psi = 0; }
                Matrix4x4 rotationMatrixZT = new Matrix4x4((float)Math.Cos(psi), (float)Math.Sin(psi), 0, 0, -1 * (float)Math.Sin(psi), (float)Math.Cos(psi), 0, 0, 0, 0, 1, 0, 0, 0, 0, 0);
                Matrix4x4 rotationMatrixZ = new Matrix4x4((float)Math.Cos(psi), -1 * (float)Math.Sin(psi), 0, 0, (float)Math.Sin(psi), (float)Math.Cos(psi), 0, 0, 0, 0, 1, 0, 0, 0, 0, 0);
                Vector3 axis1 = new Vector3();
                axis1 = Vector3.Transform(this.Axis, rotationMatrixZ);

                double theta = Math.Atan(axis1.X / axis1.Z);
                if (0 == this.Axis.Z) { theta = 0; }
                Matrix4x4 rotationMatrixYT = new Matrix4x4((float)Math.Cos(theta), 0, -1 * (float)Math.Sin(theta), 0, 0, 1, 0, 0, (float)Math.Sin(theta), 0, (float)Math.Cos(theta), 0, 0, 0, 0, 0);
                Matrix4x4 rotationMatrixY = new Matrix4x4((float)Math.Cos(theta), 0, (float)Math.Sin(theta), 0, 0, 1, 0, 0, -1 * (float)Math.Sin(theta), 0, (float)Math.Cos(theta), 0, 0, 0, 0, 0);

                Vector3 axis2 = new Vector3();
                axis2 = Vector3.Transform(axis1, rotationMatrixY);


                for (int resCtr = 0; resCtr < _myChain.Residues.Count; resCtr++)
                {
                    for (int atomCtr = 0; atomCtr < _myChain.Residues[resCtr].Atoms.Count; atomCtr++)
                    {
                        _myChain.Residues[resCtr].Atoms[atomCtr].Coords = Vector3.Transform(_myChain.Residues[resCtr].Atoms[atomCtr].Coords, rotationMatrixZ);
                        _myChain.Residues[resCtr].Atoms[atomCtr].Coords = Vector3.Transform(_myChain.Residues[resCtr].Atoms[atomCtr].Coords, rotationMatrixY);



                        if (_myChain.Residues[resCtr].Atoms[atomCtr].AtomName == "CA" || _myChain.Residues[resCtr].Atoms[atomCtr].AtomName == "C" || _myChain.Residues[resCtr].Atoms[atomCtr].AtomName == "N" || _myChain.Residues[resCtr].Atoms[atomCtr].AtomName == "O")
                        {

                            _myChain.Residues[resCtr].BackboneCoords[_myChain.Residues[resCtr].Atoms[atomCtr].AtomName] = _myChain.Residues[resCtr].Atoms[atomCtr].Coords;
                        }
                    }
                }

                if (this.Strands[1].Residues[0].BackboneCoords["CA"].Z > this.Strands[0].Residues[0].BackboneCoords["CA"].Z)
                {
                    double phi = Math.PI;
                    Matrix4x4 rotationMatrixY2 = new Matrix4x4((float)Math.Cos(phi), 0, (float)Math.Sin(phi), 0, 0, 1, 0, 0, -1 * (float)Math.Sin(phi), 0, (float)Math.Cos(phi), 0, 0, 0, 0, 0);
                    Vector3 axis3 = new Vector3();
                    axis3 = Vector3.Transform(axis2, rotationMatrixY2);


                    for (int resCtr = 0; resCtr < _myChain.Residues.Count; resCtr++)
                    {
                        for (int atomCtr = 0; atomCtr < _myChain.Residues[resCtr].Atoms.Count; atomCtr++)
                        {
                            _myChain.Residues[resCtr].Atoms[atomCtr].Coords = Vector3.Transform(_myChain.Residues[resCtr].Atoms[atomCtr].Coords, rotationMatrixY2);
                            if (_myChain.Residues[resCtr].Atoms[atomCtr].AtomName == "CA" || _myChain.Residues[resCtr].Atoms[atomCtr].AtomName == "C" || _myChain.Residues[resCtr].Atoms[atomCtr].AtomName == "N" || _myChain.Residues[resCtr].Atoms[atomCtr].AtomName == "O")
                            {

                                _myChain.Residues[resCtr].BackboneCoords[_myChain.Residues[resCtr].Atoms[atomCtr].AtomName] = _myChain.Residues[resCtr].Atoms[atomCtr].Coords;
                            }
                        }
                    }
                }
                setCEllipseCoords(ref _myChain);
                setNEllipseCoords(ref _myChain);

                Vector3 translate = new Vector3(this.Ccentroid.X, this.Ccentroid.Y, 0);

                for (int resCtr = 0; resCtr < _myChain.Residues.Count; resCtr++)
                {
                    for (int atomCtr = 0; atomCtr < _myChain.Residues[resCtr].Atoms.Count; atomCtr++)
                    {
                        _myChain.Residues[resCtr].Atoms[atomCtr].Coords -= translate;

                        if (_myChain.Residues[resCtr].Atoms[atomCtr].AtomName == "CA" || _myChain.Residues[resCtr].Atoms[atomCtr].AtomName == "C" || _myChain.Residues[resCtr].Atoms[atomCtr].AtomName == "N" || _myChain.Residues[resCtr].Atoms[atomCtr].AtomName == "O")
                        {

                            _myChain.Residues[resCtr].BackboneCoords[_myChain.Residues[resCtr].Atoms[atomCtr].AtomName] = _myChain.Residues[resCtr].Atoms[atomCtr].Coords;
                        }
                    }
                }
                setCEllipseCoords(ref _myChain);
                setNEllipseCoords(ref _myChain);
            }

            public void rotateToZmem(ref Chain _myChain)
            {
                double halfLength = this.Axis.Length() * .5;

                double theta = Math.Acos(14.5 / halfLength);
                Matrix4x4 rotationMatrixY = new Matrix4x4((float)Math.Cos(theta), 0, (float)Math.Sin(theta), 0, 0, 1, 0, 0, (float)(-1 * Math.Sin(theta)), 0, (float)Math.Cos(theta), 0, 0, 0, 0, 0);
                //Console.WriteLine("theta ={0}", theta * 180 / Math.PI);

                for (int resCtr = 0; resCtr < _myChain.Residues.Count; resCtr++)
                {
                    for (int atomCtr = 0; atomCtr < _myChain.Residues[resCtr].Atoms.Count; atomCtr++)
                    {

                        _myChain.Residues[resCtr].Atoms[atomCtr].Coords = Vector3.Transform(_myChain.Residues[resCtr].Atoms[atomCtr].Coords, rotationMatrixY);



                        if (_myChain.Residues[resCtr].Atoms[atomCtr].AtomName == "CA" || _myChain.Residues[resCtr].Atoms[atomCtr].AtomName == "C" || _myChain.Residues[resCtr].Atoms[atomCtr].AtomName == "N" || _myChain.Residues[resCtr].Atoms[atomCtr].AtomName == "O")
                        {

                            _myChain.Residues[resCtr].BackboneCoords[_myChain.Residues[resCtr].Atoms[atomCtr].AtomName] = _myChain.Residues[resCtr].Atoms[atomCtr].Coords;
                        }
                    }
                }
            }

            public void makeBarrelCircular(ref Chain _myChain)
            {

                for (int strndCtr2 = 0; strndCtr2 < this.protoBarrel.Count; strndCtr2++)
                {
                    if (this.protoBarrel[strndCtr2].Count == 0) this.protoBarrel.RemoveAt(strndCtr2);
                    for (int i = this.protoBarrel[strndCtr2][0]; i < this.protoBarrel[strndCtr2][this.protoBarrel[strndCtr2].Count - 1]; i++)
                    {
                        if (this.protoBarrel[strndCtr2].Contains(i) == false)
                        {
                            this.protoBarrel[strndCtr2].Add(i);
                            //Console.WriteLine("added res to strand {0}", strndCtr2);
                            this.protoBarrel[strndCtr2].Sort();
                        }


                    }
                }


                for (int strndCtr = 0; strndCtr < this.protoBarrel.Count;)
                {
                    bool HbondedPrev = false;
                    bool HbondedNext = false;


                    for (int resCtr = 0; resCtr < this.protoBarrel[strndCtr].Count; resCtr++)
                    { // for each residue
                        for (int nCtr = 0; nCtr < _myChain.Residues[this.protoBarrel[strndCtr][resCtr]].Neighbors.Count; nCtr++)
                        {// for each neighbor
                            if (strndCtr == 0)
                            {
                                if (this.protoBarrel[this.protoBarrel.Count - 1].Contains(_myChain.Residues[this.protoBarrel[strndCtr][resCtr]].Neighbors[nCtr])) HbondedPrev = true;
                                if (this.PdbName.Substring(0,4).ToUpper()=="6WUT") HbondedPrev = true;//SAM barrel is too open for this to be detected
                                if (this.protoBarrel[1].Contains(_myChain.Residues[this.protoBarrel[strndCtr][resCtr]].Neighbors[nCtr])) HbondedNext = true;
                            }
                            else if (strndCtr == this.protoBarrel.Count - 1)
                            {
                                if (this.protoBarrel[strndCtr - 1].Contains(_myChain.Residues[this.protoBarrel[strndCtr][resCtr]].Neighbors[nCtr])) HbondedPrev = true;
                                if (this.protoBarrel[0].Contains(_myChain.Residues[this.protoBarrel[strndCtr][resCtr]].Neighbors[nCtr])) HbondedNext = true;
                                if (this.PdbName.Substring(0, 4).ToUpper() == "6WUT") HbondedNext = true;//SAM barrel is too open for this to be detected
                            }
                            else
                            {
                                if (this.protoBarrel[strndCtr - 1].Contains(_myChain.Residues[this.protoBarrel[strndCtr][resCtr]].Neighbors[nCtr])) HbondedPrev = true;
                                if (this.protoBarrel[strndCtr + 1].Contains(_myChain.Residues[this.protoBarrel[strndCtr][resCtr]].Neighbors[nCtr])) HbondedNext = true;
                            }


                        }


                    }
                    if (HbondedPrev == false || HbondedNext == false)
                    {
                        this.protoBarrel.Remove(this.protoBarrel[strndCtr]);
                        //Console.WriteLine("removing strand {0}", strndCtr);
                    }
                    else strndCtr++;

                }

            }

            public void makeBarrelCircularPatt(ref Chain chain) //This is based on the premise that H-bonding between beta sheets in chains only occurs in the barrel
            {
                //fill in the barrel
                int nextchain;
                int prevchain;
                double d; double minD = 3.00;
                int i; //strand count
                Vector3 strand1vec;
                Vector3 strand2vec;

                #region Combine sequential strands, i.e. upper and lower
                for (i = 1; i < protoBarrel.Count;)//for each strand
                {
                    strand1vec = chain.Residues[protoBarrel[i - 1].Last()].BackboneCoords["CA"] - chain.Residues[protoBarrel[i - 1][0]].BackboneCoords["CA"];
                    strand2vec = chain.Residues[protoBarrel[i].Last()].BackboneCoords["CA"] - chain.Residues[protoBarrel[i][0]].BackboneCoords["CA"];
                    //Console.WriteLine("{0} {1} {2} {3} {4}", strand1vec, strand1vec.Length(), strand2vec, strand2vec.Length(), (strand1vec + strand2vec).Length());
                    double longest = strand1vec.Length();
                    if (strand2vec.Length() > longest) longest = strand2vec.Length();

                    if ((strand1vec + strand2vec).Length() > longest)
                    {
                        protoBarrel[i - 1].AddRange(protoBarrel[i]);
                        protoBarrel.RemoveRange(i, 1);
                        //Console.WriteLine("Combined two strands");
                    }
                    else if (protoBarrel[i - 1].Count <= 3) protoBarrel.RemoveRange(i - 1, 1);
                    else i++;
                }
                #endregion

                for (i = 0; i < protoBarrel.Count;)//for each strand
                {
                    int HbondedPrev = 0;
                    int HbondedNext = 0;

                    if (i == 0)
                    {
                        prevchain = protoBarrel.Count - 1;
                        nextchain = i + 1;
                    }
                    else if (i == protoBarrel.Count - 1)
                    {
                        prevchain = i - 1;
                        nextchain = 0;
                    }
                    else
                    {
                        prevchain = i - 1;
                        nextchain = i + 1;
                    }

                    #region Check for any neighbors in other chains
                    for (int res1ctr = 0; res1ctr < protoBarrel[i].Count - 1; res1ctr++)//for each res in strand
                    {
                        Res Residue1 = chain.Residues[protoBarrel[i][res1ctr]];

                        for (int atomCtr1 = 0; atomCtr1 < Residue1.Atoms.Count; atomCtr1++)
                        {
                            if (Residue1.Atoms[atomCtr1].AtomName == "N" && Residue1.ThreeLetCode != "PRO")
                            {
                                Atom N = Residue1.Atoms[atomCtr1];

                                for (int res3ctr = 0; res3ctr < protoBarrel[prevchain].Count; res3ctr++) //Check previous strand for neighbors
                                {
                                    Res Residue2 = chain.Residues[protoBarrel[prevchain][res3ctr]];

                                    for (int atomCtr2 = 0; atomCtr2 < Residue2.Atoms.Count; atomCtr2++)
                                    {
                                        if (Residue2.Atoms[atomCtr2].AtomName == "O")
                                        {
                                            Atom O = Residue2.Atoms[atomCtr2];
                                            atomCtr2 = Residue2.Atoms.Count;  // to skip the loop once "O" atom is found, and thus go to next residue number

                                            d = (O.Coords - N.Hydrogen).Length();
                                            if (d < minD && (Residue1.SSType == "B" && Residue2.SSType == "B"))
                                            {
                                                HbondedPrev += 1;
                                                if (Residue1.Neighbors.Contains(Residue2.ResNum) == false) Residue1.Neighbors.Add(Residue2.ResNum);
                                                if (Residue2.Neighbors.Contains(Residue1.ResNum) == false) Residue2.Neighbors.Add(Residue1.ResNum);

                                            }
                                        }
                                    }
                                }
                            CheckNextChain:
                                for (int res3ctr = 0; res3ctr < protoBarrel[nextchain].Count; res3ctr++) //Check next strand for neighbors
                                {
                                    Res Residue2 = chain.Residues[protoBarrel[nextchain][res3ctr]];
                                    for (int atomCtr2 = 0; atomCtr2 < Residue2.Atoms.Count; atomCtr2++)
                                    {
                                        if (Residue2.Atoms[atomCtr2].AtomName == "O")
                                        {

                                            Atom O = Residue2.Atoms[atomCtr2];
                                            atomCtr2 = Residue2.Atoms.Count;  // to skip the loop once "O" atom is found, and thus go to next residue number

                                            d = (O.Coords - N.Hydrogen).Length();
                                            if (d < minD && (Residue1.SSType == "B" && Residue2.SSType == "B"))
                                            {
                                                HbondedNext += 1;
                                                if (Residue1.Neighbors.Contains(Residue2.ResNum) == false) Residue1.Neighbors.Add(Residue2.ResNum);
                                                if (Residue2.Neighbors.Contains(Residue1.ResNum) == false) Residue2.Neighbors.Add(Residue1.ResNum);
                                            }
                                        }
                                    }
                                }
                            }
                        }


                    }
                    #endregion

                    if ((HbondedPrev == 0 && HbondedNext == 0) || protoBarrel[i].Count == 0)
                    {
                        protoBarrel.RemoveRange(i, 1);
                        //Console.WriteLine("removing strand {0}", i);
                    }
                    else if (protoBarrel[i].Count <= 4 && (HbondedPrev == 0 || HbondedNext == 0))
                    {
                        protoBarrel.RemoveRange(i, 1);
                        //Console.WriteLine("removing strand {0}", i);
                    }
                    else i++;

                    HbondedNext = 0;
                    HbondedPrev = 0;

                } //End of checking each chain
            }

            public void removeNonBarrelRes(ref Chain _myChain)
            {// removes residues that are not h-bonded to the next or the previous strand.
             //bool deletedSomething = false;
                for (int strndCtr = 0; strndCtr < this.protoBarrel.Count; strndCtr++)
                {
                    for (int resCtr = 0; resCtr < this.protoBarrel[strndCtr].Count;)
                    {
                        bool markForDeletion = true;

                        if (_myChain.Residues[this.protoBarrel[strndCtr][resCtr]].Neighbors.Count != 0)

                        {
                            for (int nCtr = 0; nCtr < _myChain.Residues[this.protoBarrel[strndCtr][resCtr]].Neighbors.Count; nCtr++)
                            {
                                if (strndCtr == 0)
                                {
                                    if (this.protoBarrel[this.protoBarrel.Count - 1].Contains(_myChain.Residues[this.protoBarrel[strndCtr][resCtr]].Neighbors[nCtr]) == true || this.protoBarrel[strndCtr + 1].Contains(_myChain.Residues[this.protoBarrel[strndCtr][resCtr]].Neighbors[nCtr]) == true) markForDeletion = false;

                                }
                                else if (strndCtr == this.protoBarrel.Count - 1)
                                {
                                    if (this.protoBarrel[strndCtr - 1].Contains(_myChain.Residues[this.protoBarrel[strndCtr][resCtr]].Neighbors[nCtr]) == true || this.protoBarrel[0].Contains(_myChain.Residues[this.protoBarrel[strndCtr][resCtr]].Neighbors[nCtr]) == true) markForDeletion = false;

                                }
                                else
                                {
                                    if (this.protoBarrel[strndCtr - 1].Contains(_myChain.Residues[this.protoBarrel[strndCtr][resCtr]].Neighbors[nCtr]) == true || this.protoBarrel[strndCtr + 1].Contains(_myChain.Residues[this.protoBarrel[strndCtr][resCtr]].Neighbors[nCtr]) == true) markForDeletion = false;

                                }
                            }
                        }

                        if (markForDeletion == true)
                        {
                            this.protoBarrel[strndCtr].RemoveAt(resCtr);
                            //Console.WriteLine("removed a residue from Strand {0})", strndCtr);
                        }
                        else resCtr++;
                        //resCtr--;

                    }

                    this.protoBarrel[strndCtr].Sort();

                    for (int resCtr = 0; resCtr < this.protoBarrel[strndCtr].Count;)
                    {// if there are no residues before or after 5 that are part of the sheet delete that residue too.
                        bool markForDeletion = true;
                        for (int ctr2 = this.protoBarrel[strndCtr][resCtr] - 5; ctr2 < this.protoBarrel[strndCtr][resCtr] + 5; ctr2++)
                        {
                            if (ctr2 > -1 && ctr2 != this.protoBarrel[strndCtr][resCtr])
                            {
                                if (this.protoBarrel[strndCtr].Contains(ctr2) == true)
                                {
                                    markForDeletion = false;
                                }

                            }
                        }
                        if (markForDeletion == true)
                        {
                            this.protoBarrel[strndCtr].RemoveAt(resCtr);
                            Console.WriteLine("removed a residue from Strand {0} because no nearby residues", strndCtr);
                            //deletedSomething = true;
                        }
                        else resCtr++;
                    }

                    if (this.protoBarrel[strndCtr].Count == 0) protoBarrel.RemoveAt(strndCtr);
                }
            }

	        public bool check_neighbors(int strand_num, Res Res1)
	        {
	            bool markForDeletion = true;
	            for (int nCtr = 0; nCtr < Res1.Neighbors.Count; nCtr++)
	            {
	                if (strand_num == 0)
	                {
	                    if (this.protoBarrel[this.protoBarrel.Count - 1].Contains(Res1.Neighbors[nCtr]) == true || this.protoBarrel[strand_num + 1].Contains(Res1.Neighbors[nCtr]) == true) markForDeletion = false;

	                }
	                else if (strand_num == this.protoBarrel.Count - 1)
	                {
	                    if (this.protoBarrel[strand_num - 1].Contains(Res1.Neighbors[nCtr]) == true || this.protoBarrel[0].Contains(Res1.Neighbors[nCtr]) == true) markForDeletion = false;

	                }
	                else
	                {
	                    if (this.protoBarrel[strand_num - 1].Contains(Res1.Neighbors[nCtr]) == true || this.protoBarrel[strand_num + 1].Contains(Res1.Neighbors[nCtr]) == true) markForDeletion = false;

	                }
	            }
	            return markForDeletion;
	        }
			

            public void getTilts()
            {
                for (int strandCtr = 0; strandCtr < Strands.Count; strandCtr++)
                {
                    this.Strands[strandCtr].getTilts(this.Axis, strandCtr);
                }
            }

            public void setCEllipseCoords(ref Chain _myChain)
            {
                //this is the top (extracellular) ellipse
                List<Vector3> myEllipse = new List<Vector3>();
                Vector3 centroid = new Vector3();

                for (int strandCtr = 0; strandCtr < this.protoBarrel.Count; strandCtr++)
                {
                    Vector3 firstCA = new Vector3();
                    firstCA = _myChain.Residues[this.protoBarrel[strandCtr][0]].BackboneCoords["CA"];
                    Vector3 lastCA = new Vector3();
                    lastCA = _myChain.Residues[this.protoBarrel[strandCtr][this.protoBarrel[strandCtr].Count - 1]].BackboneCoords["CA"];



                    if (strandCtr % 2 == 0)
                    {
                        myEllipse.Add(lastCA);
                        centroid += lastCA;

                    }
                    else
                    {
                        myEllipse.Add(firstCA);
                        centroid += firstCA;

                    }

                }
                this.CellipseCoords = myEllipse;
                centroid = centroid / this.protoBarrel.Count;
                this.Ccentroid = centroid;


            }

            public void setNEllipseCoords(ref Chain _myChain)
            {
                //this is the bottom (periplasmic) ellipse
                List<Vector3> myEllipse = new List<Vector3>();
                Vector3 centroid = new Vector3();

                for (int strandCtr = 0; strandCtr < this.protoBarrel.Count; strandCtr++)
                {
                    Vector3 firstCA = new Vector3();
                    firstCA = _myChain.Residues[this.protoBarrel[strandCtr][0]].BackboneCoords["CA"];
                    Vector3 lastCA = new Vector3();
                    lastCA = _myChain.Residues[this.protoBarrel[strandCtr][this.protoBarrel[strandCtr].Count - 1]].BackboneCoords["CA"];


                    if (strandCtr % 2 == 0)
                    {
                        myEllipse.Add(firstCA);
                        centroid += firstCA;

                    }
                    else
                    {
                        myEllipse.Add(lastCA);
                        centroid += lastCA;
                    }

                }
                this.NellipseCoords = myEllipse;
                centroid = centroid / this.protoBarrel.Count;
                this.Ncentroid = centroid;


            }

            public void checkStrands()
            {
                int direction = 0;
                for (int strandCtr = 0; strandCtr < this.Strands.Count; strandCtr++)
                {
                    if (strandCtr % 2 == 0)
                    {
                        if (SharedFunctions.AngleBetween((this.Strands[strandCtr].Residues[0].BackboneCoords["CA"] - this.Strands[strandCtr].Residues[2].BackboneCoords["CA"]), this.Axis) < SharedFunctions.AngleBetween(this.Strands[strandCtr].Residues[2].BackboneCoords["CA"] - this.Strands[strandCtr].Residues[0].BackboneCoords["CA"], this.Axis)) direction--;
                        else direction++;
                    }
                    else
                    {
                        if (SharedFunctions.AngleBetween((this.Strands[strandCtr].Residues[0].BackboneCoords["CA"] - this.Strands[strandCtr].Residues[2].BackboneCoords["CA"]), this.Axis) < SharedFunctions.AngleBetween(this.Strands[strandCtr].Residues[2].BackboneCoords["CA"] - this.Strands[strandCtr].Residues[0].BackboneCoords["CA"], this.Axis)) direction++;
                        else direction--;
                    }
                }
                if (direction < 0)
                {
                    this.Direction = false;
                }
                else this.Direction = true;

                for (int strandCtr = 0; strandCtr < this.Strands.Count; strandCtr++)
                {
                    if (this.Direction == false)
                    {
                        int markForDeletion = 0;

                        if (strandCtr % 2 == 0)
                        {
                            for (int residueCtr = 1; residueCtr < this.Strands[strandCtr].Residues.Count - 1; residueCtr++)
                            {
                                if (SharedFunctions.AngleBetween((this.Strands[strandCtr].Residues[residueCtr - 1].BackboneCoords["CA"] - this.Strands[strandCtr].Residues[residueCtr + 1].BackboneCoords["CA"]), this.Axis) > SharedFunctions.AngleBetween(this.Strands[strandCtr].Residues[residueCtr + 1].BackboneCoords["CA"] - this.Strands[strandCtr].Residues[residueCtr - 1].BackboneCoords["CA"], this.Axis)) markForDeletion++;
                                else markForDeletion--;
                            }

                        }
                        else
                        {
                            for (int residueCtr = 1; residueCtr < this.Strands[strandCtr].Residues.Count - 1; residueCtr++)
                            {
                                if (SharedFunctions.AngleBetween((this.Strands[strandCtr].Residues[residueCtr - 1].BackboneCoords["CA"] - this.Strands[strandCtr].Residues[residueCtr + 1].BackboneCoords["CA"]), this.Axis) < SharedFunctions.AngleBetween(this.Strands[strandCtr].Residues[residueCtr + 1].BackboneCoords["CA"] - this.Strands[strandCtr].Residues[residueCtr - 1].BackboneCoords["CA"], this.Axis)) markForDeletion++;
                                else markForDeletion--;
                            }
                        }
                        if (markForDeletion > 0)
                        {
                            //Console.WriteLine("Removed Strand {0} !!!!!!", strandCtr);
                            this.Strands.Remove(this.Strands[strandCtr]);


                            if (strandCtr == 0) this.Direction = true;
                            else strandCtr--;

                            //break;
                        }
                    }


                    if (this.Direction == true)
                    {

                        int markForDeletion = 0;

                        if (strandCtr % 2 == 0)
                        {
                            for (int residueCtr = 1; residueCtr < this.Strands[strandCtr].Residues.Count - 1; residueCtr++)
                            {
                                double forwardAngle = SharedFunctions.AngleBetween((this.Strands[strandCtr].Residues[residueCtr - 1].BackboneCoords["CA"] - this.Strands[strandCtr].Residues[residueCtr + 1].BackboneCoords["CA"]), this.Axis);
                                double backwardAngle = SharedFunctions.AngleBetween((this.Strands[strandCtr].Residues[residueCtr + 1].BackboneCoords["CA"] - this.Strands[strandCtr].Residues[residueCtr - 1].BackboneCoords["CA"]), this.Axis);
                                if (forwardAngle < backwardAngle) markForDeletion++;
                                //if (SharedFunctions.AngleBetween((this.Strands[strandCtr].Residues[residueCtr - 1].BackboneCoords["CA"] - this.Strands[strandCtr].Residues[residueCtr + 1].BackboneCoords["CA"]), this.Axis) < SharedFunctions.AngleBetween(this.Strands[strandCtr].Residues[residueCtr + 1].BackboneCoords["CA"] - this.Strands[strandCtr].Residues[residueCtr - 1].BackboneCoords["CA"], this.Axis)) markForDeletion++;
                                else markForDeletion--;
                            }

                        }
                        else
                        {
                            for (int residueCtr = 1; residueCtr < this.Strands[strandCtr].Residues.Count - 1; residueCtr++)
                            {
                                if (SharedFunctions.AngleBetween((this.Strands[strandCtr].Residues[residueCtr - 1].BackboneCoords["CA"] - this.Strands[strandCtr].Residues[residueCtr + 1].BackboneCoords["CA"]), this.Axis) > SharedFunctions.AngleBetween(this.Strands[strandCtr].Residues[residueCtr + 1].BackboneCoords["CA"] - this.Strands[strandCtr].Residues[residueCtr - 1].BackboneCoords["CA"], this.Axis)) markForDeletion++;
                                else markForDeletion--;
                            }
                        }
                        if (markForDeletion > 0)
                        {

                            //Console.WriteLine("Removed Strand {0} !!!!!!", strandCtr);
                            this.Strands.Remove(this.Strands[strandCtr]);

                            strandCtr--;
                            if (strandCtr == 0) this.Direction = false;
                            //break;
                        }

                    }
                }
                //make sure strandNum is correct. 
                for (int strandCtr = 0; strandCtr < this.Strands.Count; strandCtr++)
                {
                    this.Strands[strandCtr].StrandNum = strandCtr;
                    for (int resCtr = 0; resCtr < this.Strands[strandCtr].Residues.Count; resCtr++)
                    {
                        this.Strands[strandCtr].Residues[resCtr].StrandNum = strandCtr;
                    }
                }

            }

            public void writeAminoAcidsTypesToFile(ref Chain _myChain, string outputDirectory)
            {
                string fileLocation3 = outputDirectory + "AminoAcids\\AminoAcidTypes" + this.PdbName + ".txt";
                using (System.IO.StreamWriter file = new System.IO.StreamWriter(fileLocation3))
                {
                    file.WriteLine("Sl.No\t*PDB ID*\t*Strands Per Chain*\t*Chains Per Protein*\t*Residue Number*\t*AminoAcid*\t*Chain*\t*Strand Number*\t*Interface*");

                    int sl_no = 1;
                    bool interface_value;
                    for (int strandCtr = 0; strandCtr < protoBarrel.Count; strandCtr++)
                    {
                        if (strandCtr == 0 || strandCtr == protoBarrel.Count - 1) // to check the residues that are at interface of the different chains
                        {
                            interface_value = true;
                        }
                        else interface_value = false;

                        for (int residues = protoBarrel[strandCtr][0]; residues <= protoBarrel[strandCtr].Last(); residues++)
                        {
                            file.WriteLine("{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}", sl_no, this.PdbName, protoBarrel.Count, protoBarrel.Count, _myChain.Residues[residues].SeqID, _myChain.Residues[residues].ThreeLetCode, _myChain.ChainName, strandCtr, interface_value);
                            sl_no++;
                        }
                    }
                }
            }

            public void getTyrVector(string outputDirectory, ref Chain myChain)
            {
                string newLine;
                Vector3 strandVect;
                Vector3 ringVect;
                Vector3 Cg;
                Vector3 OH;

                string fileLocation = outputDirectory + "FoldingPatterns/TyrVect" + this.PdbName + ".txt";
                using (System.IO.StreamWriter file = new System.IO.StreamWriter(fileLocation))
                {
                    newLine = "Res" + "\t" + "ResNum" + "\t" + "Strand" + "\t" + "Chain" + "\t" + "Angle Btwn Ring/Strand" + "\t" + "Dihedral";
                    file.WriteLine(newLine);

                    foreach (Strand strand in this.Strands)
                    {
                        for (int resIndex = 0; resIndex < strand.Residues.Count; resIndex++)
                        {
                            Res res1 = strand.Residues[resIndex];
                            if (res1.ThreeLetCode == "TYR")
                            {
                                //Use CA coords of neighboring residues to determine strand vector
                                if (resIndex == strand.Residues.Count - 1) strandVect = strand.Residues[resIndex].BackboneCoords["CA"] - strand.Residues[resIndex - 2].BackboneCoords["CA"];
                                else if (resIndex == 0) strandVect = strand.Residues[resIndex + 2].BackboneCoords["CA"] - strand.Residues[resIndex].BackboneCoords["CA"];
                                else strandVect = strand.Residues[resIndex + 1].BackboneCoords["CA"] - strand.Residues[resIndex - 1].BackboneCoords["CA"];

                                Cg = res1.Atoms[0].Coords;
                                OH = res1.Atoms[0].Coords;
                                foreach (Atom atom1 in res1)
                                {
                                    if (atom1.AtomName == "CG") Cg = atom1.Coords;
                                    if (atom1.AtomName == "OH") OH = atom1.Coords;
                                }
                                ringVect = OH - Cg;
                                double dihedral = SharedFunctions.CalculateTorsion(myChain.Residues[res1.ResNum - 2].BackboneCoords["CA"], res1.BackboneCoords["CA"], Cg, OH);
                                file.WriteLine("{0}\t{1}\t{2}\t{3}\t{4}\t{5}", res1.ThreeLetCode, res1.SeqID, strand.StrandNum, res1.ChainName, SharedFunctions.AngleBetween(ringVect, strandVect), dihedral);
                            }

                        }
                    }
                }
            }

            public IEnumerator<Strand> GetEnumerator()
            {
                return Strands.GetEnumerator();
            }

            IEnumerator IEnumerable.GetEnumerator()
            {
                return this.GetEnumerator();
            }
        }
	
    }

 }
