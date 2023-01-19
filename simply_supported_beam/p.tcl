wipe
model BasicBuilder -ndm 3 -ndf 6
source parameter.tcl
#source initial_model.tcl
source updated_model.tcl
#source damaged_model.tcl
test NormDispIncr 0.01 200 2; 
algorithm KrylovNewton
constraints Transformation; 
numberer RCM;	
system BandGeneral;
integrator LoadControl 0.1;
analysis Static
analyze 10
loadConst -time 0.0;

set numModes 10
recorder Node -file mode1y.txt -nodeRange 1 16 -dof 2 eigen1
recorder Node -file mode2y.txt -nodeRange 1 16 -dof 2 eigen2
recorder Node -file mode3y.txt -nodeRange 1 16 -dof 2 eigen3
recorder Node -file mode4y.txt -nodeRange 1 16 -dof 2 eigen4
recorder Node -file mode5y.txt -nodeRange 1 16 -dof 2 eigen5
recorder Node -file mode6y.txt -nodeRange 1 16 -dof 2 eigen6
recorder Node -file mode7y.txt -nodeRange 1 16 -dof 2 eigen7
recorder Node -file mode8y.txt -nodeRange 1 16 -dof 2 eigen8
recorder Node -file mode9y.txt -nodeRange 1 16 -dof 2 eigen9
recorder Node -file mode10y.txt -nodeRange 1 16 -dof 2 eigen10
recorder Node -file mode1z.txt -nodeRange 1 16 -dof 3 eigen1
recorder Node -file mode2z.txt -nodeRange 1 16 -dof 3 eigen2
recorder Node -file mode3z.txt -nodeRange 1 16 -dof 3 eigen3
recorder Node -file mode4z.txt -nodeRange 1 16 -dof 3 eigen4
recorder Node -file mode5z.txt -nodeRange 1 16 -dof 3 eigen5
recorder Node -file mode6z.txt -nodeRange 1 16 -dof 3 eigen6
recorder Node -file mode7z.txt -nodeRange 1 16 -dof 3 eigen7
recorder Node -file mode8z.txt -nodeRange 1 16 -dof 3 eigen8
recorder Node -file mode9z.txt -nodeRange 1 16 -dof 3 eigen9
recorder Node -file mode10z.txt -nodeRange 1 16 -dof 3 eigen10
set pi [expr acos(-1.0)]
set eigFID [open EigenVal.txt w]
set lambda [eigen $numModes]
puts $eigFID " lambda          omega           period          frequency"
foreach lambda $lambda {
    set omega [expr sqrt($lambda)]
    set period [expr 2.0*$pi/$omega]
    set frequ [expr 1.0/$period]
    puts $eigFID [format " %+1.6e  %+1.6e  %+1.6e  %+1.6e" $lambda $omega $period $frequ]
}
close $eigFID
record





