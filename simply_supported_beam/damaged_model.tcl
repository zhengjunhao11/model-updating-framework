wipe
model BasicBuilder -ndm 3 -ndf 6
#set units
#N m pa
#----------------------
#node information
node 1 0 0 0
node 2 1 0 0
node 3 2 0 0 
node 4 3 0 0
node 5 4 0 0
node 6 5 0 0 
node 7 6 0 0
node 8 7 0 0
node 9 8 0 0
node 10 9 0 0
node 11 10 0 0
node 12 11 0 0
node 13 12 0 0
node 14 13 0 0
node 15 14 0 0
node 16 15 0 0
puts "nodes"
#----
set E 3.45e+10
set po 0.3
set ly 0.15
set lz 0.3
set A [expr $ly*$lz]
set Iy [expr $ly*$lz**3/12]
set Iz [expr $lz*$ly**3/12]
set J [expr $Iz+$Iy]
set G [expr $E/(2*(1+$po))]
set den 2500
puts "section"
set Iy1 [expr 0.3*$ly*$lz**3/12]
set Iz1 [expr 0.3*$lz*$ly**3/12]
set J1 [expr $Iz1+$Iy1]
#set Geometric Transformation
geomTransf PDelta 1 0 0 1
element elasticBeamColumn 1 1 2 $A $E $G $J $Iy $Iz 1 -mass [expr $den*$A]
element elasticBeamColumn 2 2 3 $A $E $G $J $Iy $Iz 1 -mass [expr $den*$A]
element elasticBeamColumn 3 3 4 $A $E $G $J $Iy $Iz 1 -mass [expr $den*$A]
element elasticBeamColumn 4 4 5 $A $E $G $J $Iy $Iz 1 -mass [expr $den*$A]
element elasticBeamColumn 5 5 6 $A $E $G $J1 $Iy1 $Iz1 1 -mass [expr $den*$A]
element elasticBeamColumn 6 6 7 $A $E $G $J $Iy $Iz 1 -mass [expr $den*$A]
element elasticBeamColumn 7 7 8 $A $E $G $J $Iy $Iz 1 -mass [expr $den*$A]
element elasticBeamColumn 8 8 9 $A $E $G $J $Iy $Iz 1 -mass [expr $den*$A]
element elasticBeamColumn 9 9 10 $A $E $G $J $Iy $Iz 1 -mass [expr $den*$A]
element elasticBeamColumn 10 10 11 $A $E $G $J1 $Iy1 $Iz1 1 -mass [expr $den*$A]
element elasticBeamColumn 11 11 12 $A $E $G $J $Iy $Iz 1 -mass [expr $den*$A]
element elasticBeamColumn 12 12 13 $A $E $G $J $Iy $Iz 1 -mass [expr $den*$A]
element elasticBeamColumn 13 13 14 $A $E $G $J1 $Iy1 $Iz1 1 -mass [expr $den*$A]
element elasticBeamColumn 14 14 15 $A $E $G $J $Iy $Iz 1 -mass [expr $den*$A]
element elasticBeamColumn 15 15 16 $A $E $G $J $Iy $Iz 1 -mass [expr $den*$A]
puts "element"
#set fix
fix 1 1 1 1 1 1 0
fix 16 0 1 1 1 1 0
puts "fix"
#eleload
pattern Plain 7 Linear {
eleLoad -range 1 15 -type -beamUniform [expr -9.8*$den*$A] 0
}
puts "eleload"

